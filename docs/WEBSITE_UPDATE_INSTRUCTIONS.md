# Website Update Instructions for Zo Agent

Instructions for building the juniors course website and updating the
home page to support both courses.

**Staging URL:** `https://jing.zo.space/course-v2`
**Production URL:** `https://jing.zo.space/course` (mirror from staging when approved)

**Source repo:** `https://github.com/jingerzz/ai-investment-courses`
**Branch:** `main`

---

## CRITICAL: No Navigation in HTML Files

The zo.space shell provides its own navigation bar for all pages. **Do NOT
add any navigation to the HTML files you create or deploy.** This means:

- **No `<nav>` elements** in any HTML file
- **No `nav.js`** or any JavaScript that creates navigation
- **No `<header>` with navigation links**
- **No `.site-nav` CSS class** (it has been removed from course.css)
- **No script tags that inject navigation into the DOM**

The HTML files should start directly with their content (hero section,
course cards, module content, etc.). The zo.space shell handles all
page-to-page navigation automatically.

**This mistake has recurred three times.** If you are generating HTML and
think "this page needs a nav bar," the answer is NO — zo.space provides it.

---

## Overview of Changes

The site currently serves only the professional course. This update:

1. Creates a **shared landing page** where visitors choose Professional or Juniors
2. Moves the existing professional course under a `/professional/` sub-path
3. Adds a new **juniors course site** under a `/juniors/` sub-path
4. Both sub-sites have their own index page, module pages, and CSS

---

## Site Architecture

```
/course-v2/
  index.html                  ← NEW: shared landing page (choose course)
  professional/
    index.html                ← EXISTING: current professional course home
    css/course.css            ← EXISTING: professional CSS (no changes)
    js/track-toggle.js        ← EXISTING: professional JS (no changes)
    foundations-1.html         ← EXISTING
    foundations-2.html         ← EXISTING
    week-1.html               ← EXISTING
    week-2.html               ← EXISTING
    week-3.html               ← EXISTING
    week-4.html               ← EXISTING
    conclusion.html           ← EXISTING
    demo-*.html               ← EXISTING
  juniors/
    index.html                ← NEW: juniors course home
    css/course.css            ← NEW: juniors CSS (different colors from professional)
    foundations-1.html         ← NEW: from juniors/foundations-1/reading.md + exercise
    foundations-2.html         ← NEW: from juniors/foundations-2/reading.md + exercise
    week-1.html               ← NEW: from juniors/week-1/reading.md + exercise
    week-2.html               ← NEW: from juniors/week-2/reading.md + exercise
    week-3.html               ← NEW: from juniors/week-3/reading.md + exercise
    week-4.html               ← NEW: from juniors/week-4/reading.md + exercise
    conclusion.html           ← NEW: from juniors/conclusion.md
```

---

## Page 1: Shared Landing Page (`index.html`)

This is the entry point at `/course-v2/`. Simple, clean, and fast.

### Content

**Title:** AI Investment Academy

**Tagline:** Build AI tools for investing --- no coding required.

**Two course cards** side by side (stacked on mobile):

**Card 1 --- Professional Course:**
- Label: "Professional"
- Title: "AI-Powered Investment Management"
- Description: "For investment analysts, portfolio managers, and IT managers. Connect Claude to live market data, build MCP tool servers, design multi-server architecture, and deploy autonomous agents with compliance controls."
- Format: "2 Foundations + 4 Weeks"
- Button: "Start Professional Course" linking to `professional/index.html`

**Card 2 --- Juniors Course:**
- Label: "Juniors"
- Title: "AI-Powered Investing for Juniors"
- Description: "For high school students curious about investing and AI. Build stock tracking tools, add safety checks, design systems, and create a monitoring assistant --- all by describing what you want in plain English."
- Format: "2 Foundations + 4 Weeks"
- Button: "Start Juniors Course" linking to `juniors/index.html`

**Below the cards:**

"Both courses teach the same core skills --- directing AI, building tools, adding guardrails, and designing systems. The professional course assumes finance knowledge and uses institutional examples. The juniors course teaches finance alongside AI and uses companies everyone knows."

### Design

- Use the shared brand fonts (Inter, JetBrains Mono) from `brand/shared.md`
- Neutral color scheme for the landing page (not biased toward either course):
  - Background: `#FFFFFF`
  - Text: `#1A1A2E`
  - Muted text: `#6B7280`
  - Card borders: `#E2E4E9`
- Professional card accent: `#1B2A4A` (the professional primary color)
- Juniors card accent: `#1A73E8` (the juniors primary color)
- Cards should have hover effect (subtle border color change + shadow)
- Mobile responsive: cards stack vertically on screens under 640px
- Keep it simple. No nav bar needed on this page (zo.space shell provides navigation)
- No pricing section on this page

---

## Page 2: Juniors Course Home (`juniors/index.html`)

### Design System

The juniors site uses a **different CSS** from the professional site.
The full design spec is in `brand/juniors.md`. Key differences:

| Property | Professional | Juniors |
|----------|-------------|---------|
| Primary color | `#1B2A4A` (dark navy) | `#1A73E8` (bright blue) |
| Secondary color | `#4A9BA8` (teal) | `#F59E0B` (warm amber) |
| Code blocks | Dark background (`#1E293B`) | Light background (`#F8FAFC`) |
| Body font size | 16px | 17px |
| Max line length | 75ch | 65ch |
| H2 bottom border | `#E2E4E9` (neutral) | `#F59E0B` (amber) |

**Create `juniors/css/course.css`** by starting from the professional
`css/course.css` and updating the CSS custom properties (`:root` block)
to match `brand/juniors.md` color tokens. Also update:
- Code block styles to use light background
- Body font-size to 17px
- Max paragraph width from 75ch to 65ch

### Content

The juniors index.html follows the same structure as the professional
index.html (`professional/site/index.html`) but with juniors content:

**Title:** AI-Powered Investing for Juniors

**Tagline:** Build AI-powered stock tools --- no coding required.

**Lead:** A hands-on course for high school students. Two foundations modules plus four weeks. Real tools connected to real stock data.

**Course cards** (same grid layout as professional index):

| Card | Label | Title | Description |
|------|-------|-------|-------------|
| 1 | Foundations 1 | Understanding Claude | Learn what AI can and can't do. Set up projects with custom instructions. No installs needed. |
| 2 | Foundations 2 | Setting Up Your Workspace | Install Claude Desktop, try attachments, find the Developer menu. |
| 3 | Week 1 | Build Your First Stock Tracker | Use Claude Code to build a tool that gives Claude access to real stock data. |
| 4 | Week 2 | Teaching AI Not to Make Mistakes | Add safety checks that prevent math errors, warn about old data, and format reports correctly. |
| 5 | Week 3 | Designing Bigger Systems | Design how multiple AI tools work together. Think like an architect. |
| 6 | Week 4 | AI That Watches and Alerts | Build a monitor that watches your stocks and tells you when something important happens. |
| 7 | Conclusion | What You've Built | Review your complete system and chart your path forward. |

**"How It Works" section:**
"Start with two Foundations modules that require nothing but a Claude account --- learn how Claude works, understand how AI gets things wrong, and set up your workspace. Then move into four weekly modules, each with 30 minutes reading and 30 minutes hands-on building."

"By the end, you'll have built a complete set of AI-powered stock tools: a tracker, a daily report with safety checks, a multi-server system design, and a monitoring assistant. All using real stock data from companies you know --- Apple, Nike, Disney, Tesla, Netflix."

**"What Makes This Different" section:**

- **No Coding Required:** You describe what you want in plain English. Claude Code writes all the code. You evaluate, iterate, and improve.
- **Real Stock Data:** Your tools connect to real prices for real companies. Not toy examples --- tools that work after the course ends.
- **AI Honesty Built In:** Week 2 is entirely about AI mistakes and how to catch them. You'll learn guardrails that real professionals use.
- **Learn Investing Too:** Stock market basics, what tickers mean, how to compare companies, why you should never let AI trade for you.

Each card links to its corresponding HTML page (e.g., `foundations-1.html`).

---

## Pages 3-9: Juniors Module Pages

Create one HTML page per module from the markdown source files.

### Source File Mapping

| HTML Page | Reading Source | Exercise Source |
|-----------|--------------|----------------|
| `foundations-1.html` | `juniors/foundations-1/reading.md` | `juniors/foundations-1/exercise/README.md` |
| `foundations-2.html` | `juniors/foundations-2/reading.md` | `juniors/foundations-2/exercise/README.md` |
| `week-1.html` | `juniors/week-1/reading.md` | `juniors/week-1/exercise/README.md` |
| `week-2.html` | `juniors/week-2/reading.md` | `juniors/week-2/exercise/README.md` |
| `week-3.html` | `juniors/week-3/reading.md` | `juniors/week-3/exercise/README.md` |
| `week-4.html` | `juniors/week-4/reading.md` | `juniors/week-4/exercise/README.md` |
| `conclusion.html` | `juniors/conclusion.md` | (none) |

### HTML Structure per Module Page

Follow the same pattern as the professional module pages. Each page has:

1. **Chapter header:** Label (e.g., "Foundations 1"), title, reading time + exercise time
2. **Section tabs:** "Reading" | "Exercise" | "Checklist" (| "Prompts" if conversation_guide exists)
3. **Reading tab:** Render the reading.md content as HTML. Use the CSS classes from course.css (callouts, code blocks, tables, etc.)
4. **Exercise tab:** Render the exercise README.md as HTML. Use step numbering (`.step` class with `data-step` attribute)
5. **Checklist tab:** Render checklist.md as HTML using the `.checklist` class
6. **Prompts tab:** Render conversation_guide.md if present
7. **Page navigation:** Previous/next links at the bottom

### Tab JavaScript

Use inline JavaScript for tab switching (same pattern as professional pages).
Do NOT use a separate JS file. Do NOT include track-toggle.js (juniors has no track toggle).

### Rendering Guidelines

When converting markdown to HTML:

- Markdown `#` headings become `<h2>` (the page title is the `<h1>`)
- Markdown `##` headings become `<h3>`
- Markdown code blocks (triple backtick) become `<pre class="code-block">`
- Markdown tables become `<table>` with `<thead>` and `<tbody>`
- Markdown bold (`**text**`) becomes `<strong>`
- Markdown blockquotes (`>`) become `<div class="callout">`
- Checkboxes (`- [ ]`) become `.checklist-item` with `.checklist-box`
- Links render as `<a>` tags

### Juniors-Specific Elements

From `brand/juniors.md`, the juniors course has unique callout types:

- **"Investing 101" sidebar:** Light amber background (`#FFFBEB`), amber left border, lightbulb icon. Use for inline finance term definitions in reading content.
- **"Why This Matters" callout:** `surface-alt` background, blue left border. Connects technical concepts to teen interests.
- **JSON annotations:** For Foundations and Week 1, include plain-English comments alongside JSON examples (see `brand/juniors.md` section on "JSON Annotation").

---

## Professional Site Updates

The existing professional files move under `/professional/` sub-path.
No content changes to professional pages. Only update internal links:

- `css/course.css` stays at `professional/css/course.css`
- `js/track-toggle.js` stays at `professional/js/track-toggle.js`
- Internal page links (e.g., `href="week-1.html"`) stay relative (no change needed)

---

## Standing Constraints (from ZO_DEPLOY_BRIEF.md)

These constraints still apply:

- **Deploy ONLY files explicitly listed.** Do NOT modify files beyond what is specified.
- **Do NOT change the pricing section or navigation shell on zo.space.**
- **CRITICAL --- double nav bar:** The zo.space shell already provides page navigation (the dark bar at the top). HTML files must NOT include their own navigation. Specifically:
  - Do NOT create `nav.js` or any navigation JavaScript file
  - Do NOT inject `<nav>`, `<header>`, or any element with class `site-nav` into HTML
  - Do NOT add `<script>` tags that generate navigation bars
  - The `.site-nav` CSS has been intentionally removed from course.css --- do NOT re-add it
  - If HTML source files do not contain a `<nav>` element, do NOT add one during deployment
  - This mistake has happened three times already. If you are unsure, do NOT add navigation.
- **Known pitfall --- unicode escapes:** Use literal unicode characters (e.g., checkmark), not CSS escape sequences.
- **Known pitfall --- stale cache:** Test with `?v=TIMESTAMP` query string after CSS changes.

---

## Deployment Sequence

### Step 1: Deploy to Staging (`/course-v2`)

Deploy the shared landing page and juniors site to staging first:

```
# Shared landing page
update_space_asset("/course-content/v2-staging/index.html", source=<landing page>)

# Professional course (existing files, just re-routed)
update_space_asset("/course-content/v2-staging/professional/index.html", source=<professional index>)
update_space_asset("/course-content/v2-staging/professional/css/course.css", source=<professional css>)
update_space_asset("/course-content/v2-staging/professional/js/track-toggle.js", source=<professional js>)
# ... all professional/*.html files

# Juniors course (new files)
update_space_asset("/course-content/v2-staging/juniors/index.html", source=<juniors index>)
update_space_asset("/course-content/v2-staging/juniors/css/course.css", source=<juniors css>)
# ... all juniors/*.html files
```

### Step 2: Verify on Staging

- [ ] Landing page loads at `/course-v2`
- [ ] Both course cards render and link correctly
- [ ] Professional course pages load with correct styling
- [ ] Professional track toggle still works on Week 1 and Week 2
- [ ] Juniors course pages load with correct styling (bright blue/amber, light code blocks)
- [ ] Juniors tab navigation works on all module pages
- [ ] All internal links work (no broken links)
- [ ] Mobile responsive: landing page cards stack, content is readable
- [ ] No double navigation bar on any page
- [ ] No console errors

### Step 3: Promote to Production

Once staging is verified, mirror to production by deploying the same
files to the production route (`/course-content/v2/`).

---

## Source Files Reference

All source markdown files are in the GitHub repo at:
`https://github.com/jingerzz/ai-investment-courses/tree/main/`

Professional HTML files (already built):
`professional/site/` directory

Juniors markdown files (to be rendered to HTML):
`juniors/` directory

Brand guidelines:
- `brand/shared.md` --- shared typography, spacing, layout
- `brand/professional.md` --- professional colors and tone
- `brand/juniors.md` --- juniors colors, tone, and unique components
