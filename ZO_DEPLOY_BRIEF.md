# Zo Agent Deployment Brief — Course Site

Reference document for deploying course HTML changes to jing.zo.space/course.
The Zo agent's role is **deploy only** — all file edits happen in this repo
and are pushed to GitHub before deployment.

---

## Current State

**Latest deployed commit:** `04c8188`
**Route:** `/course` serves `/course-content/v2/`
**Files managed:** HTML files in `professional/site/` deploy to `/course-content/v2/`

## Deployment Pattern

1. Changes are made to HTML files in `professional/site/` and committed to `main`
2. The Zo agent deploys using `update_space_asset()` with raw GitHub URLs
3. URL format: `https://raw.githubusercontent.com/jingerzz/ai-investment-courses/{SHA}/professional/site/{filename}`

## Standing Constraints

These apply to ALL deployments:

- **Deploy ONLY files explicitly listed.** Do NOT modify any files beyond what is specified.
- **Do NOT change the pricing section, navigation shell, or any route.**
- **Do NOT modify CSS or JavaScript files** unless explicitly listed.
- **Do NOT add, remove, or edit content** beyond what is already in the files at the GitHub URL.
- **Known pitfall — double nav bar:** The zo.space shell provides navigation. HTML files must NOT include their own nav scripts. Never add `nav.js` or similar.
- **Known pitfall — unicode escapes:** Use literal unicode characters (e.g., `✓`), not CSS escape sequences (e.g., `\u2713`), which get stripped during deployment.
- **Known pitfall — stale cache:** zo.space caches CSS aggressively. Test with `?v=TIMESTAMP` query string after CSS changes.

## Verification (run after every deployment)

- [ ] No double navigation bar on any page
- [ ] No console errors (DevTools > Console)
- [ ] Track toggle works on Week 1 and Week 2 (Systematic Trading / Stock Research)
- [ ] Track choice persists across page navigation (localStorage)
- [ ] Pricing section intact on homepage

---

## Deployment History

### V2.2.2 — 2026-04-10 (commit `04c8188`)

**Files deployed:**
```
update_space_asset("/course-content/v2/week-1.html",
    source="https://raw.githubusercontent.com/jingerzz/ai-investment-courses/04c8188/professional/site/week-1.html")

update_space_asset("/course-content/v2/week-2.html",
    source="https://raw.githubusercontent.com/jingerzz/ai-investment-courses/04c8188/professional/site/week-2.html")
```

**Changes:**
- Replaced Node.js + npm install instructions with Claude Code's native installer (`curl`/`irm`) in Week 1 exercise callouts (both tracks) and Week 2 exercise "What is Claude Code?" callout

**Rollback to:** `408f814`

### V2.2.1 — 2026-04-10 (commit `408f814`)

**Files deployed:**
```
update_space_asset("/course-content/v2/week-1.html",
    source="https://raw.githubusercontent.com/jingerzz/ai-investment-courses/408f814/professional/site/week-1.html")

update_space_asset("/course-content/v2/week-2.html",
    source="https://raw.githubusercontent.com/jingerzz/ai-investment-courses/408f814/professional/site/week-2.html")
```

**Changes:**
- Fixed broken "Prerequisites" link in Week 1 Claude Code callouts — replaced with self-contained inline install instructions
- Fixed track-specific `get_portfolio_summary()` references in Week 2 Prompts tab — replaced with track-agnostic `get_market_overview()`/`get_sector_heatmap()`

**Rollback to:** `00a3398`

### V2.2.0 — 2026-04-10 (commit `00a3398`)

**Files deployed:**
```
update_space_asset("/course-content/v2/week-1.html",
    source="https://raw.githubusercontent.com/jingerzz/ai-investment-courses/00a3398/professional/site/week-1.html")

update_space_asset("/course-content/v2/week-2.html",
    source="https://raw.githubusercontent.com/jingerzz/ai-investment-courses/00a3398/professional/site/week-2.html")
```

**Changes:**
- Added "Let Claude Code Handle Setup" callouts to Week 1 exercise (both tracks)
- Added track toggle to Week 2 reading tab (systematic + research examples)
- Added inline explanations for ES, VWAP, and pivot points in systematic track
- Added `<script src="js/track-toggle.js"></script>` to week-2.html

**Rollback to:** `35ca7b3`

### V2.1.0 — 2026-04-10 (commit `35ca7b3`)

Baseline V2 deployment. All pages, CSS, JS, and demos deployed.
