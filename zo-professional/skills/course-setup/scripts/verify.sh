#!/usr/bin/env bash
# verify.sh — Green/red checklist for the AI Investing course environment.
# Safe to run any time. Exits 0 if everything passes, 1 if anything fails.

set -uo pipefail

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
BOLD='\033[1m'
DIM='\033[2m'
RESET='\033[0m'

PASS=0
FAIL=0

check() {
  local label="$1"; shift
  if "$@" >/dev/null 2>&1; then
    printf "  ${GREEN}✓${RESET} %s\n" "$label"
    PASS=$((PASS+1))
  else
    printf "  ${RED}✗${RESET} %s\n" "$label"
    FAIL=$((FAIL+1))
  fi
}

note() { printf "  ${DIM}↳ %s${RESET}\n" "$*"; }

# ─────────────────────────────────────────────────────────────────────────────
# Locate repo (same logic as bootstrap)
# ─────────────────────────────────────────────────────────────────────────────
if [[ -n "${ZO_COURSE_REPO:-}" ]] && [[ -d "$ZO_COURSE_REPO" ]]; then
  REPO="$ZO_COURSE_REPO"
elif [[ -d "/home/workspace/AI-Investing-Course/repo" ]]; then
  REPO="/home/workspace/AI-Investing-Course/repo"
elif [[ -d "/home/workspace/ai-investment-courses" ]]; then
  REPO="/home/workspace/ai-investment-courses"
else
  printf "${RED}Course repo not found.${RESET} Run bootstrap.sh first.\n"
  exit 1
fi

SPY_TLT_DIR="$REPO/professional/servers/spy-tlt-course"
RAG_DIR="$REPO/professional/servers/page-index-rag-course"
RAG_INDEXES="$RAG_DIR/data/indexes"
SKILLS_DST="${ZO_SKILLS_DIR:-/home/workspace/Skills}"

printf "\n${BOLD}Course environment check${RESET}\n"
note "repo:   $REPO"
note "skills: $SKILLS_DST"
echo

# ─────────────────────────────────────────────────────────────────────────────
# Tooling
# ─────────────────────────────────────────────────────────────────────────────
printf "${BOLD}Tooling${RESET}\n"
check "uv on PATH"                          command -v uv
check "ollama on PATH"                      command -v ollama
check "ollama daemon responding"            curl -sf http://127.0.0.1:11434/api/tags
check "gemma4:e2b model present"            bash -c "ollama list 2>/dev/null | awk '{print \$1}' | grep -qx gemma4:e2b"
echo

# ─────────────────────────────────────────────────────────────────────────────
# Course servers
# ─────────────────────────────────────────────────────────────────────────────
printf "${BOLD}Course servers${RESET}\n"
check "spy-tlt-course venv exists"          test -d "$SPY_TLT_DIR/.venv"
check "spy-tlt-server entry point"          bash -c "cd '$SPY_TLT_DIR' && uv run --no-sync spy-tlt-server --help 2>&1 | head -1"
check "page-index-rag-course venv exists"   test -d "$RAG_DIR/.venv"
check "rag-server entry point"              bash -c "cd '$RAG_DIR' && uv run --no-sync rag-server --help 2>&1 | head -1"
check "RAG config pinned to gemma4:e2b"     bash -c "python3 -c \"import json; c=json.load(open('$RAG_DIR/config.json')); assert c['ollama_model']=='gemma4:e2b' and c['summary_model']=='gemma4:e2b'\""
echo

# ─────────────────────────────────────────────────────────────────────────────
# Pre-indexed filings (BLK + HOOD)
# ─────────────────────────────────────────────────────────────────────────────
printf "${BOLD}Pre-indexed filings${RESET}\n"
BLK_COUNT=$(find "$RAG_INDEXES" -maxdepth 1 -name "BLK_*.json" 2>/dev/null | wc -l | tr -d ' ')
HOOD_COUNT=$(find "$RAG_INDEXES" -maxdepth 1 -name "HOOD_*.json" 2>/dev/null | wc -l | tr -d ' ')
check "≥1 BLK filing indexed (found $BLK_COUNT)"   test "$BLK_COUNT" -ge 1
check "≥1 HOOD filing indexed (found $HOOD_COUNT)" test "$HOOD_COUNT" -ge 1
echo

# ─────────────────────────────────────────────────────────────────────────────
# Skills installed
# ─────────────────────────────────────────────────────────────────────────────
printf "${BOLD}Skills installed${RESET}\n"
check "course-setup skill present"          test -f "$SKILLS_DST/course-setup/SKILL.md"
check "spy-tlt-course skill present"        test -f "$SKILLS_DST/spy-tlt-course/SKILL.md"
check "pageindex-rag-course skill present"  test -f "$SKILLS_DST/pageindex-rag-course/SKILL.md"
echo

# ─────────────────────────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────────────────────────
TOTAL=$((PASS+FAIL))
if [[ $FAIL -eq 0 ]]; then
  printf "${GREEN}${BOLD}All %d checks passed.${RESET} Setup is ready.\n" "$TOTAL"
  printf "${DIM}Next: register the MCP servers with Zo (see bootstrap output).${RESET}\n"
  exit 0
else
  printf "${RED}${BOLD}%d of %d checks failed.${RESET}\n" "$FAIL" "$TOTAL"
  printf "${YELLOW}Fix: re-run bootstrap.sh — it is idempotent and will repair most failures.${RESET}\n"
  printf "${DIM}If a specific check keeps failing, share its line with course support.${RESET}\n"
  exit 1
fi
