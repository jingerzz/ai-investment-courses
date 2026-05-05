#!/usr/bin/env bash
# bootstrap.sh — One-shot setup for the AI Investing (Zo-professional) course.
#
# Idempotent. Safe to re-run. Each step prints what it's doing and either
# performs the action or skips it because the desired state already exists.
#
# Steps:
#   1. Locate the course repo
#   2. Install uv if missing
#   3. uv sync both course MCP servers
#   4. Install Ollama if missing
#   5. Ensure ollama daemon is running
#   6. Pull gemma4:e2b
#   7. Patch page-index-rag-course/config.json to use gemma4:e2b
#   8. Install consumer skills into /home/workspace/Skills/
#   9. Run verify.sh

set -euo pipefail

# ─────────────────────────────────────────────────────────────────────────────
# Pretty output
# ─────────────────────────────────────────────────────────────────────────────
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
BOLD='\033[1m'
DIM='\033[2m'
RESET='\033[0m'

step()  { printf "\n${BOLD}▸ %s${RESET}\n" "$*"; }
ok()    { printf "  ${GREEN}✓${RESET} %s\n" "$*"; }
skip()  { printf "  ${DIM}↷ %s${RESET}\n" "$*"; }
warn()  { printf "  ${YELLOW}⚠ %s${RESET}\n" "$*"; }
fail()  { printf "  ${RED}✗ %s${RESET}\n" "$*"; exit 1; }

# ─────────────────────────────────────────────────────────────────────────────
# 1. Locate the course repo
# ─────────────────────────────────────────────────────────────────────────────
step "Locating course repo"

if [[ -n "${ZO_COURSE_REPO:-}" ]] && [[ -d "$ZO_COURSE_REPO" ]]; then
  REPO="$ZO_COURSE_REPO"
elif [[ -d "/home/workspace/AI-Investing-Course/repo" ]]; then
  REPO="/home/workspace/AI-Investing-Course/repo"
elif [[ -d "/home/workspace/ai-investment-courses" ]]; then
  REPO="/home/workspace/ai-investment-courses"
else
  fail "Course repo not found. Set ZO_COURSE_REPO or clone https://github.com/jingerzz/ai-investment-courses to /home/workspace/ai-investment-courses"
fi

SPY_TLT_DIR="$REPO/professional/servers/spy-tlt-course"
RAG_DIR="$REPO/professional/servers/page-index-rag-course"
SKILLS_SRC="$REPO/zo-professional/skills"
SKILLS_DST="${ZO_SKILLS_DIR:-/home/workspace/Skills}"

[[ -d "$SPY_TLT_DIR" ]] || fail "Missing $SPY_TLT_DIR"
[[ -d "$RAG_DIR" ]]     || fail "Missing $RAG_DIR"
[[ -d "$SKILLS_SRC" ]]  || fail "Missing $SKILLS_SRC"

ok "Repo: $REPO"

# ─────────────────────────────────────────────────────────────────────────────
# 2. Install uv if missing
# ─────────────────────────────────────────────────────────────────────────────
step "Checking uv"

if command -v uv >/dev/null 2>&1; then
  skip "uv already installed ($(uv --version))"
else
  warn "uv not found — installing from astral.sh"
  curl -LsSf https://astral.sh/uv/install.sh | sh
  # Make uv available in this shell
  export PATH="$HOME/.local/bin:$PATH"
  command -v uv >/dev/null 2>&1 || fail "uv install failed — see https://docs.astral.sh/uv/getting-started/installation/"
  ok "uv installed ($(uv --version))"
fi

# ─────────────────────────────────────────────────────────────────────────────
# 3. uv sync both servers
# ─────────────────────────────────────────────────────────────────────────────
step "Syncing spy-tlt-course"
( cd "$SPY_TLT_DIR" && uv sync --quiet )
ok "spy-tlt-course dependencies installed"

step "Syncing page-index-rag-course"
( cd "$RAG_DIR" && uv sync --quiet )
ok "page-index-rag-course dependencies installed"

# ─────────────────────────────────────────────────────────────────────────────
# 4. Install Ollama if missing
# ─────────────────────────────────────────────────────────────────────────────
step "Checking Ollama"

if command -v ollama >/dev/null 2>&1; then
  skip "ollama already installed ($(ollama --version 2>&1 | head -n1))"
else
  warn "ollama not found — installing from ollama.com"
  # Ollama's installer extracts a zstd-compressed tarball; ensure zstd is available first
  if ! command -v zstd >/dev/null 2>&1; then
    warn "  zstd not found — required by Ollama installer; installing"
    if command -v apt-get >/dev/null 2>&1; then
      sudo apt-get install -y zstd >/dev/null 2>&1 || \
        fail "failed to install zstd. Run 'sudo apt-get install -y zstd' manually and retry."
    else
      fail "zstd is required to install Ollama but cannot be auto-installed on this system. Install zstd and retry."
    fi
    ok "  zstd installed"
  fi
  curl -fsSL https://ollama.com/install.sh | sh || \
    fail "ollama install failed. If your Zo box restricts sudo, ask Zo support to enable Ollama, then re-run this script."
  ok "ollama installed"
fi

# ─────────────────────────────────────────────────────────────────────────────
# 5. Ensure ollama daemon is running
# ─────────────────────────────────────────────────────────────────────────────
step "Starting ollama daemon"

if curl -sf http://127.0.0.1:11434/api/tags >/dev/null 2>&1; then
  skip "ollama daemon already responding on 127.0.0.1:11434"
else
  warn "ollama daemon not responding — starting in background"
  nohup ollama serve >/tmp/ollama.log 2>&1 &
  # Wait up to 30s for the daemon to come up
  for i in {1..30}; do
    if curl -sf http://127.0.0.1:11434/api/tags >/dev/null 2>&1; then
      ok "ollama daemon up (logs: /tmp/ollama.log)"
      break
    fi
    sleep 1
    [[ $i -eq 30 ]] && fail "ollama daemon failed to start within 30s. See /tmp/ollama.log"
  done
fi

# ─────────────────────────────────────────────────────────────────────────────
# 6. Pull gemma4:e2b
# ─────────────────────────────────────────────────────────────────────────────
step "Pulling gemma4:e2b"

if ollama list 2>/dev/null | awk '{print $1}' | grep -qx "gemma4:e2b"; then
  skip "gemma4:e2b already present"
else
  warn "gemma4:e2b not present — pulling (this can take several minutes on a fresh box)"
  ollama pull gemma4:e2b
  ok "gemma4:e2b pulled"
fi

# ─────────────────────────────────────────────────────────────────────────────
# 7. Patch RAG config.json to use gemma4:e2b
# ─────────────────────────────────────────────────────────────────────────────
step "Pointing PageIndex RAG at gemma4:e2b"

RAG_CONFIG="$RAG_DIR/config.json"
[[ -f "$RAG_CONFIG" ]] || fail "Missing $RAG_CONFIG"

python3 - <<PYEOF
import json, sys
from pathlib import Path

cfg_path = Path("$RAG_CONFIG")
cfg = json.loads(cfg_path.read_text())
changed = False
for key in ("ollama_model", "summary_model"):
    if cfg.get(key) != "gemma4:e2b":
        cfg[key] = "gemma4:e2b"
        changed = True
if changed:
    cfg_path.write_text(json.dumps(cfg, indent=2) + "\n")
    print("  patched config.json → ollama_model=summary_model=gemma4:e2b")
else:
    print("  config.json already pinned to gemma4:e2b")
PYEOF
ok "RAG config aligned with gemma4:e2b"

# ─────────────────────────────────────────────────────────────────────────────
# 8. Install consumer skills into /home/workspace/Skills/
# ─────────────────────────────────────────────────────────────────────────────
step "Installing consumer skills into $SKILLS_DST"

mkdir -p "$SKILLS_DST"
for skill in spy-tlt-course pageindex-rag-course course-setup; do
  src="$SKILLS_SRC/$skill"
  dst="$SKILLS_DST/$skill"
  if [[ ! -d "$src" ]]; then
    warn "skipping $skill — not present in repo at $src"
    continue
  fi
  if [[ -d "$dst" ]] && [[ "$(readlink -f "$dst" 2>/dev/null || echo)" == "$(readlink -f "$src")" ]]; then
    skip "$skill already symlinked → repo"
    continue
  fi
  rm -rf "$dst"
  ln -s "$src" "$dst"
  ok "$skill → $dst (symlinked to repo so updates flow through git pull)"
done

# ─────────────────────────────────────────────────────────────────────────────
# 9. Verify
# ─────────────────────────────────────────────────────────────────────────────
step "Running verify.sh"
bash "$(dirname "$0")/verify.sh"

# ─────────────────────────────────────────────────────────────────────────────
# Final instructions
# ─────────────────────────────────────────────────────────────────────────────
cat <<'EOF'

──────────────────────────────────────────────────────────────────────────────
  Setup complete. Last step is in Zo chat — bootstrap can't register MCP
  servers for you. Paste this into Zo chat:

    Register two MCP servers from this workspace:
      1. spy-tlt-course        — entry: `uv run spy-tlt-server` from
         professional/servers/spy-tlt-course
      2. page-index-rag-course — entry: `uv run rag-server` from
         professional/servers/page-index-rag-course
    After registering, list the tools each server exposes and confirm the
    RAG server returns at least 7 indexed filings (BLK + HOOD).

  Then start Week 1: zo-professional/week-1/exercise/README.md
──────────────────────────────────────────────────────────────────────────────
EOF
