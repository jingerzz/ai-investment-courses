# Website V2 Instructions

These instructions describe how to deploy the V2 course website as a
staging environment at `jing.zo.space/course-v2`, while keeping the
current V1 course live at `jing.zo.space/course`.

---

## Summary of V2 Changes

The course has been restructured based on user feedback:

1. **Two new Foundations modules** added before Week 1 for absolute
   beginners (system prompts, Claude projects, Desktop/Mobile setup)
2. **Track toggle** in Week 1 lets students choose between "Systematic
   Trading" (SPY/TLT strategy) and "Stock Research" (SEC filing
   analysis with RAG)
3. **Bonus module removed** from navigation (content was already
   absorbed into Week 2 in a prior update)
4. **Prerequisites restructured** — Foundations requires zero installs

### V1 Structure (current live site)
- Week 1 → Week 2 → Bonus → Week 3 → Week 4 → Conclusion

### V2 Structure (staging)
- **Foundations 1: Getting Started with Claude** — What LLMs are,
  system prompts, projects, custom instructions. Zero installs needed.
- **Foundations 2: Claude on Desktop & Mobile** — Install Desktop/Mobile,
  workspace setup, attachments, project management.
- **Week 1: The Tool-Use Pattern** — Install pre-built server, connect
  to Claude Desktop. **Track toggle:** Systematic Trading (spy-tlt-course)
  OR Stock Research (page-index-rag-course).
- **Week 2: Building Your Own AI Tools** — Claude Code + Ollama + RAG.
- **Week 3: System Design and Architecture** — Multi-server composition.
- **Week 4: Autonomous Agents and Controls** — Agent with audit trail.
- **Conclusion: What You've Built** — Updated to reference Foundations.
- **Bonus: REMOVED** from navigation (page still exists but not linked).

---

## Deployment Plan

### Step 1: Upload V2 Assets

Upload all files from `professional/site/` to `/course-content/v2/`
on zo.space. The directory structure mirrors V1:

```
/course-content/v2/
  index.html              ← Updated (Foundations cards, no Bonus card)
  foundations-1.html       ← NEW
  foundations-2.html       ← NEW
  week-1.html              ← Rewritten (track toggle + updated content)
  week-2.html              ← Unchanged from V1
  week-3.html              ← Unchanged from V1
  week-4.html              ← Unchanged from V1
  conclusion.html          ← Updated (mentions Foundations)
  css/course.css           ← Updated (track toggle styles added)
  js/nav.js                ← Updated (Foundations in nav, Bonus removed)
  js/track-toggle.js       ← NEW
```

**Do NOT upload these V1 files to V2:**
- `bonus.html` — removed from navigation
- `demo-*.html` — interactive demos (can be added later if desired)

Asset upload commands:
```
update_space_asset("professional/site/index.html",         "/course-content/v2/index.html")
update_space_asset("professional/site/foundations-1.html",  "/course-content/v2/foundations-1.html")
update_space_asset("professional/site/foundations-2.html",  "/course-content/v2/foundations-2.html")
update_space_asset("professional/site/week-1.html",         "/course-content/v2/week-1.html")
update_space_asset("professional/site/week-2.html",         "/course-content/v2/week-2.html")
update_space_asset("professional/site/week-3.html",         "/course-content/v2/week-3.html")
update_space_asset("professional/site/week-4.html",         "/course-content/v2/week-4.html")
update_space_asset("professional/site/conclusion.html",     "/course-content/v2/conclusion.html")
update_space_asset("professional/site/css/course.css",      "/course-content/v2/css/course.css")
update_space_asset("professional/site/js/nav.js",           "/course-content/v2/js/nav.js")
update_space_asset("professional/site/js/track-toggle.js",  "/course-content/v2/js/track-toggle.js")
```

### Step 2: Create Staging Route

Create a new route for the V2 staging site:

```
update_space_route("/course-v2", route_type="static", path="/course-content/v2/")
```

This serves `jing.zo.space/course-v2` from the V2 assets without
touching the V1 site at `jing.zo.space/course`.

### Step 3: Verify Staging

Test at `jing.zo.space/course-v2`:

1. **Homepage:** 7 cards visible (F1, F2, W1-W4, Conclusion). No Bonus
   card. "Choose Your Track" section present.
2. **Navigation:** Click through every nav link. Verify sequence:
   Home → Foundations 1 → Foundations 2 → Week 1 → Week 2 → Week 3 →
   Week 4 → Conclusion. Prev/next buttons work on every page.
3. **Foundations 1:** 3 tabs (Reading, Exercise, Checklist). "What You
   Need" callout at top says "just a Claude account." No demo card.
4. **Foundations 2:** 3 tabs. "Looking Ahead to Week 1" callout at end
   of Exercise tab.
5. **Week 1 Track Toggle:** Reading, Exercise, and Prompts tabs each
   have a pill-style toggle: "Systematic Trading" / "Stock Research".
   - Default: Systematic Trading (active)
   - Click Stock Research → content swaps in all three tabs
   - Navigate to Week 2 and back → track choice persists (localStorage)
   - Both tracks have complete content (no empty sections)
6. **Week 1 Checklist:** No track toggle (shared across tracks).
7. **Weeks 2-4:** Unchanged from V1. Verify no visual regressions.
8. **Conclusion:** References "Foundations 1-2" in progression summary.
9. **Mobile:** Resize to 640px. Check nav overflow (horizontal scroll),
   card stacking, track toggle layout.

### Step 4: Cutover (When Ready)

When V2 is verified, switch the production URL:

```
update_space_route("/course", route_type="static", path="/course-content/v2/")
```

V1 assets remain at `/course-content/` for rollback:

```
# Rollback if needed:
update_space_route("/course", route_type="static", path="/course-content/")
```

---

## New Files — Detail

### `foundations-1.html` (447 lines)

**Content:** Understanding Claude — Your AI Research Partner
- **Reading tab (6 sections):**
  - F1.1: What LLMs Are (analyst-without-Bloomberg analogy)
  - F1.2: The Context Window (working memory, ~200K tokens)
  - F1.3: System Prompts and Custom Instructions
  - F1.4: Projects in Claude (organizing by topic)
  - F1.5: Artifacts (tables, reports, standalone outputs)
  - F1.6: Prompting for Investment Work (finance-specific tips)
- **Exercise tab (5 steps):** Create a project, write custom
  instructions, compare responses, add documents, try mobile
- **Checklist tab (3 sections):** Concepts, Hands-On, Ready for F2

**Structure:** `.page-wrapper` > `.content` > `.chapter-header`
(label: "Foundations 1") > `.section-tabs` (3 tabs) > `.tab-content`
divs. Same pattern as week pages but no demo card.

### `foundations-2.html` (562 lines)

**Content:** Claude on Desktop and Mobile — Your Workspace Setup
- **Reading tab (6 sections):**
  - F2.1: Why Desktop and Mobile? (browser vs native apps)
  - F2.2: Installing Claude Desktop (download, tour)
  - F2.3: Projects Across Devices (sync behavior)
  - F2.4: Working with Attachments (formats, tips)
  - F2.5: The Claude Mobile App (iOS/Android)
  - F2.6: Building Your Workspace (project templates by role)
- **Exercise tab (6 steps):** Install Desktop, verify project sync,
  attachment workflow, install mobile, set up work projects, find
  Settings > Developer. Ends with "Looking Ahead to Week 1" callout.
- **Checklist tab (5 sections):** Installation, Sync, Attachments,
  Workspace, Week 1 Readiness

### `track-toggle.js` (32 lines)

Handles the Systematic Trading / Stock Research pill toggle.
- Reads saved choice from `localStorage("course-track")`
- Defaults to "systematic" if no saved choice
- Toggles `.active` class on `.track-btn` and `.track-content` elements
- Persists choice to localStorage on click

### `week-1.html` (1,224 lines — rewritten)

Major rewrite from the V1 version. Now matches the current markdown
content (V1 HTML was out of sync with the "use before you build"
restructure).

**Reading tab:**
- Section 1.1 (shared): A Working Strategy — Your First AI Tool
- **Track toggle** before section 1.2
- Section 1.2 Systematic: The SPY/TLT Color Strategy (colors, signals,
  tiers, safety rules, backtest results)
- Section 1.2 Research: A Document Intelligence System — Analyzing SEC
  Filings (RAG concepts, structure-first indexing, BLK/HOOD pre-indexed,
  14 tools overview)
- Sections 1.3-1.6 (shared): From Spreadsheet to AI Tool, MCP, Four
  Design Principles, How AI Adds Value

**Exercise tab:**
- **Track toggle**
- Systematic: 6 steps to install spy-tlt-course server, connect to
  Claude Desktop, explore signals/briefings/patterns
- Research: 6 steps to install page-index-rag-course server, connect to
  Claude Desktop, explore filing analysis/comparisons/due diligence

**Prompts tab:**
- **Track toggle**
- Systematic: Prompts for signals, briefings, pattern analysis,
  historical context, cross-referencing
- Research: Prompts for document exploration, cross-document analysis,
  due diligence workflows

**Checklist tab:** Shared (no track toggle). Covers MCP concepts,
design principles, hands-on verification.

---

## Modified Files — Detail

### `index.html`

- **Cards:** Added Foundations 1 and Foundations 2 cards at top of grid.
  Removed Bonus card. Updated Week 1/2 card titles and descriptions.
  Conclusion card description updated.
- **Tagline:** Changed "Four weeks" to "Two foundations modules plus
  four weeks"
- **How It Works:** Updated to mention Foundations as starting point
- **Added:** "Choose Your Track" section under "What Makes This
  Different"

### `nav.js`

Pages array updated:
```javascript
const pages = [
  { id: "home",          href: "index.html",          label: "Home" },
  { id: "foundations-1", href: "foundations-1.html",   label: "Foundations 1" },
  { id: "foundations-2", href: "foundations-2.html",   label: "Foundations 2" },
  { id: "week-1",        href: "week-1.html",         label: "Week 1" },
  { id: "week-2",        href: "week-2.html",         label: "Week 2" },
  { id: "week-3",        href: "week-3.html",         label: "Week 3" },
  { id: "week-4",        href: "week-4.html",         label: "Week 4" },
  { id: "conclusion",    href: "conclusion.html",     label: "Conclusion" },
];
```

Changes: added `foundations-1` and `foundations-2`, removed `bonus`.
Navigation now has 8 items. Existing `overflow-x: auto` on `.nav-links`
handles horizontal scroll on narrow viewports.

### `course.css`

Added at end of file (~60 lines):

- `.track-toggle` — Container with border, background, flex layout
- `.track-label` — "Choose your track:" text
- `.track-pills` — Pill container with border radius
- `.track-btn` — Individual pill buttons (inactive: transparent,
  active: `--secondary` teal with white text)
- `.track-content` — Hidden by default, shown with `.active` class
- Responsive: track toggle stacks vertically at 768px

### `conclusion.html`

- Updated "What You Accomplished" section: added Foundations 1-2
  summary, updated Week 1 and Week 2 descriptions to match V2 content
- Removed bonus module reference

---

## What NOT to Change

- `week-2.html`, `week-3.html`, `week-4.html` — unchanged from V1
- `demo-*.html` — interactive demos, not included in V2 deployment
- `bonus.html` — kept in repo but not linked or deployed to V2
- The glossary content is unchanged
- The overall site layout, color scheme, and design direction are
  unchanged

---

## Rollback Plan

If V2 needs to be rolled back after cutover:

```
update_space_route("/course", route_type="static", path="/course-content/")
```

V1 assets are untouched at `/course-content/`. V2 assets remain at
`/course-content/v2/` and can be updated independently.
