# Changelog

All notable changes to the AI Investment Academy course materials.

## [2.4.0] — 2026-04-30

### Added
- **Platform↔course drift workflow**: `scripts/check_drift.py` produces
  `docs/drift-report.md` (status: IDENTICAL / MINOR ≤30 line diff / MAJOR /
  COURSE-ONLY / PLATFORM-ONLY). Run before any course release or ad-hoc
  when you suspect drift. See `SYNC_GUIDE.md` "Platform ↔ Course Drift".
- **Intentional divergence registry**: `docs/intentional_divergence.md` —
  files where course differs from platform by design (broker-free
  data layer, monolithic `server.py`, verbose teaching guides). Drift
  on these is expected; do NOT port.

### Changed (page-index-rag-course)
- **`llm.py`**: Added LLM backend selection (Ollama or Anthropic), env-var
  precedence for `LLM_BACKEND`, `ANTHROPIC_MODEL`, `SUMMARY_MODEL`,
  `SUMMARY_CONCURRENCY`, `OLLAMA_KEEP_ALIVE`. Added `_get_extractive_threshold()`
  for 3-tier summarization (raw / extractive / LLM).
  Why: Lets students with no Ollama install use Claude API directly; lets
  any single deploy tune concurrency without bumping `config.json`.
- **`pageindex/utils.py`**: Added `extractive_summary()` — zero-dependency
  TF-IDF sentence extraction. Truncates LLM-summary input to ~3000 tokens.
  Caps `max_tokens=256` for summary calls.
  Why: Reduces indexing time substantially on student hardware; medium
  nodes get fast extractive summaries instead of slow LLM calls.
- **`pageindex/page_index_md.py`**: 3-tier summary policy (raw under
  extractive_threshold, extractive between thresholds, LLM only above
  summary_token_threshold).
  Why: Same perf rationale; preserves quality where it matters (large nodes).
- **`pageindex/config.yaml`**: Added (was platform-only file).
- **`server.py`**: Imported `trading_core.security` with import-fallback
  shim so course stays standalone. Added optional `passphrase` kwarg to
  write tools (`fetch_company_filings`, `fetch_company_filings_enhanced`,
  `ingest_drop_folder`, `remove_document`, `embed_documents`); enforced
  via `MCP_TOOL_PASSPHRASE` env var when set. Switched error-string
  formatting from `str(e)` to `sanitize_error(e, context)`.
  Why: Lets a hosted course server (e.g. Fly.io demo) be passphrase-
  protected without changing the standalone path. Sanitized errors
  keep stack-trace fragments out of student-visible output.
- **`config.json`**: Added `ollama_keep_alive: "10m"` and
  `extractive_threshold: 2000` to match the new `llm.py` knobs.
- **`pyproject.toml`**: Added `anthropic>=0.40.0` so `LLM_BACKEND=anthropic`
  works without an extra `uv add`.

### spy-tlt-course (audited, no ports)
The drift report's MAJOR diff on `advisor.py` is mostly platform CLI
scaffolding (`print_*`, `parse_args`, `main`) and ES/MES futures support
(intentionally excluded — course is yfinance-only). Spot-checked
`compute_trading_levels`, `compute_trade_plan`, `_find_pattern_matches`:
no algorithmic bug fixes worth porting. The platform's
`analyze_pattern(start_date, end_date, regime)` filters are a real
educational improvement but a feature addition, not a bug fix; deferred.

### How to verify
```bash
cd /path/to/ai-investment-courses
python3 scripts/check_drift.py --out docs/drift-report.md
# Read the report; the only remaining MAJOR/PLATFORM-ONLY entries
# should match docs/intentional_divergence.md.
```

## [2.3.0] — 2026-04-11

### Added
- **Juniors Foundations 1**: Written from scratch (was TODO stub). Covers
  LLMs, 5 AI failure modes with teen-relevant examples (Tesla stale price,
  Nike wrong CEO, Disney/Netflix fake acquisition), context windows, custom
  instructions, projects, artifacts, and prompting basics.
- **Juniors Foundations 2**: Written from scratch (was TODO stub). Covers
  Claude Desktop installation, interface tour, Developer menu, attachments,
  mobile app, and workspace setup with student-oriented project templates.
- **Juniors Week 1**: "Let Claude Code Handle Setup" one-prompt path —
  students paste a single prompt that creates the project, installs
  dependencies, and configures Claude Desktop automatically.
- **Juniors Weeks 2-4**: AI limitations awareness threaded through all
  modules — verification checks in Week 2, staleness as architecture
  principle in Week 3, Foundations 1 failure mode callbacks in Week 4.
- **Juniors Week 2**: ETF explainer before sector ETFs are introduced.
- **Juniors glossary**: ETF definition.
- **Juniors conclusion**: Verification discipline tied back to Foundations 1.
- **Website update instructions**: `docs/WEBSITE_UPDATE_INSTRUCTIONS.md` — full
  spec for Zo agent to build shared landing page (choose Professional or
  Juniors), juniors course site with its own CSS/design, and staging/
  production deployment flow.

### Changed
- **Juniors prerequisites**: Replaced Node.js + npm install with native
  Claude Code installer (`curl | bash` / `irm | iex`). Dropped Node.js as
  a prerequisite entirely. Added progressive disclosure (Foundations =
  browser only, Week 1 = Desktop + Claude Code + uv).
- **Juniors setup.md**: Native installer, Windows now opens PowerShell
  instead of cmd (required for install script).
- **Juniors README**: Added Foundations modules to course progression table
  and file structure section.
- **Juniors COURSE_BRIEF**: Added Foundations chapters to book mapping table.
- **ZO_DEPLOY_BRIEF**: Added staging route and juniors course reference.

### Fixed
- **Sync-check CI**: Excluded `*-track-research.md` files from the file
  structure check — these are professional-only (SEC filing RAG with
  BLK/HOOD) and intentionally have no juniors equivalent.
- **Juniors COURSE_BRIEF / README**: Removed stale references to deleted
  `bonus-local-rag/` directory.
- **Juniors F1 checklist**: Fixed "session" to "every conversation" for
  custom instructions scope.
- **Juniors F1 conversation guide**: Rewrote "What's your source?" prompt
  to avoid triggering fabricated citations from Claude.
- **Juniors F2 conversation guide**: Replaced Microsoft with Nike (not in
  approved stock list).
- **Juniors F2 reading**: Changed "Starred or bookmarked conversations" to
  "Favorited conversations" (accurate UI terminology).
- **Double nav bar (root cause)**: Removed all `.site-nav` CSS from
  `professional/site/css/course.css`. The Zo agent was reading these
  styles and generating `nav.js` + injecting `<nav class="site-nav">`
  during deployment, duplicating the zo.space shell navigation. Added
  explicit "no navigation" constraints to `docs/WEBSITE_UPDATE_INSTRUCTIONS.md`
  and `ZO_DEPLOY_BRIEF.md`.

## [2.1.0] — 2026-04-10

### Fixed
- **Week 1 exercise**: Added missing "Download the Course Materials" step with
  `git clone` command and ZIP fallback — participants previously had no way to
  get the repo before being told to `cd` into it
- **Week 1 exercise**: Removed misleading `uv run server &` verification step —
  MCP stdio servers produce no visible output, confusing beginners. Claude
  Desktop launches servers automatically.
- **Week 1 demo**: Fixed checkmark rendering — CSS `\u2713` escape was stripped
  during deployment, showing literal "u2713" text instead of ✓
- **All modules**: Removed `nav.js` script tags from HTML — the zo.space shell
  handles navigation, and nav.js was causing a duplicate navigation bar
- **Week 3**: Removed hardcoded `~/ai-finance-tools/` directory path from
  exercise prompts

### Changed
- **ES/MES price examples**: Updated all code examples from stale 5,xxx range
  to current 6,xxx range across Week 2, Week 4, and their demos (the course
  teaches students to catch this exact error — our own examples had it)
- **Week 1 exercise**: Renamed "Download the Course Server" to "Install the
  Server" (the step installs dependencies, it doesn't download anything)
- **Week 2**: Changed `claude code .` command to `claude` (correct CLI syntax)

### Added
- **Foundations 2**: Terminal prep paragraph in "Looking Ahead to Week 1" —
  reassures participants who have never used a command line
- **Week 1**: "Two Tracks, Same Concepts" callout before the track toggle —
  explains what Systematic Trading vs Stock Research means
- **Week 2**: "What is Claude Code?" intro callout before the exercise —
  explains the tool before asking participants to use it
- **AI limitations content**: Added hallucination awareness and verification
  discipline across Foundations 1, Weeks 1-4, and Conclusion (taxonomy of 5
  failure modes, design-response mapping, real-world error examples,
  Practitioner's Compact)
- **Interactive demos**: Added demo pages for all weekly modules and conclusion

### Removed
- **Bonus module**: Removed `bonus.html` and `demo-bonus.html` — this was a
  stale pre-V1 module whose content was integrated into weekly modules

## [2.0.0] — 2026-04-09

### Added
- **Foundations 1**: New module — Understanding Claude (LLMs, tokens, prompting,
  projects). No installs required.
- **Foundations 2**: New module — Claude on Desktop and Mobile (workspace setup,
  attachments, cross-device sync)
- **Track toggle**: Week 1 now offers two tracks — Systematic Trading (SPY/TLT)
  and Stock Research (SEC filing RAG) with localStorage persistence
- **V2 site**: Full HTML course site deployed to zo.space with tabbed layout
  (Reading, Exercise, Prompts, Checklist per module)

### Changed
- **Course structure**: Restructured from "build first" to "use before you
  build" pedagogy — participants experience a working tool in Week 1 before
  building their own in Week 2
- **Prerequisites**: Progressive disclosure — each module's Exercise tab has its
  own "What You Need" callout instead of a separate prerequisites page

## [1.0.0] — 2026-03-15

### Added
- Initial course: 4 weeks + bonus module
- Two parallel courses: Professional (finance) and Juniors (high school)
- Pre-built servers: spy-tlt-course (14 tools), page-index-rag-course (14 tools)
- MIT license
