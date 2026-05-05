#!/usr/bin/env bash
# zo-course.sh — One-line installer for the AI Investing (Zo-professional) course.
#
# Hosted at: https://www.clarionintelligencesystems.com/install/zo-course.sh
# Usage:
#   curl -fsSL https://www.clarionintelligencesystems.com/install/zo-course.sh | bash
#
# What it does:
#   1. Clones (or updates) the course repo at /home/workspace/ai-investment-courses
#   2. Symlinks the course-setup skill into /home/workspace/Skills/
#   3. Hands off to bootstrap.sh for the actual install
#
# Idempotent. Safe to re-run on an existing setup — the underlying bootstrap
# is also idempotent.

set -euo pipefail

GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
BOLD='\033[1m'
RESET='\033[0m'

step()  { printf "\n${BOLD}▸ %s${RESET}\n" "$*"; }
ok()    { printf "  ${GREEN}✓${RESET} %s\n" "$*"; }
warn()  { printf "  ${YELLOW}⚠ %s${RESET}\n" "$*"; }
fail()  { printf "  ${RED}✗${RESET} %s\n" "$*"; exit 1; }

REPO_URL="${ZO_COURSE_REPO_URL:-https://github.com/jingerzz/ai-investment-courses.git}"
REPO_DIR="${ZO_COURSE_REPO:-/home/workspace/ai-investment-courses}"
SKILLS_DST="${ZO_SKILLS_DIR:-/home/workspace/Skills}"

cat <<'BANNER'
══════════════════════════════════════════════════════════════════════════════
  AI Investing on Zo Computer — one-line installer
  https://www.clarionintelligencesystems.com/resources/course
══════════════════════════════════════════════════════════════════════════════
BANNER

# ─────────────────────────────────────────────────────────────────────────────
# 1. Clone or update the repo
# ─────────────────────────────────────────────────────────────────────────────
step "Fetching course repo"

command -v git >/dev/null 2>&1 || fail "git not found — install git and retry"

if [[ -d "$REPO_DIR/.git" ]]; then
  warn "repo already at $REPO_DIR — resetting to latest origin/main"
  # `git reset --hard` guarantees the working tree matches the published commit no
  # matter what state a previous failed run left behind. The course repo is
  # canonical and read-only from a student's perspective; students who want to
  # tinker should fork.
  ( cd "$REPO_DIR" && git fetch origin main && git reset --hard origin/main )
  ok "repo updated to $(cd "$REPO_DIR" && git rev-parse --short HEAD)"
else
  if [[ -e "$REPO_DIR" ]]; then
    fail "$REPO_DIR exists but is not a git checkout — move it aside and retry"
  fi
  mkdir -p "$(dirname "$REPO_DIR")"
  git clone --depth 1 "$REPO_URL" "$REPO_DIR"
  ok "repo cloned to $REPO_DIR"
fi

# ─────────────────────────────────────────────────────────────────────────────
# 2. Symlink the course-setup skill so Zo can discover it immediately
# ─────────────────────────────────────────────────────────────────────────────
step "Registering course-setup skill"

mkdir -p "$SKILLS_DST"
SKILL_SRC="$REPO_DIR/zo-professional/skills/course-setup"
SKILL_DST="$SKILLS_DST/course-setup"

[[ -d "$SKILL_SRC" ]] || fail "course-setup skill missing in repo at $SKILL_SRC"

if [[ -L "$SKILL_DST" ]] && [[ "$(readlink -f "$SKILL_DST")" == "$(readlink -f "$SKILL_SRC")" ]]; then
  ok "course-setup skill already symlinked"
else
  rm -rf "$SKILL_DST"
  ln -s "$SKILL_SRC" "$SKILL_DST"
  ok "course-setup skill → $SKILL_DST"
fi

# ─────────────────────────────────────────────────────────────────────────────
# 3. Hand off to bootstrap
# ─────────────────────────────────────────────────────────────────────────────
step "Running bootstrap (this will take a few minutes on a fresh box)"

export ZO_COURSE_REPO="$REPO_DIR"
export ZO_SKILLS_DIR="$SKILLS_DST"

bash "$REPO_DIR/zo-professional/skills/course-setup/scripts/bootstrap.sh"
