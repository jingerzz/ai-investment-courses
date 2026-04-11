# Changelog

All notable changes to the AI Investment Academy course materials.

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
- **Website update instructions**: `WEBSITE_UPDATE_INSTRUCTIONS.md` — full
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
  explicit "no navigation" constraints to `WEBSITE_UPDATE_INSTRUCTIONS.md`
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
