# Brand Guidelines — Junior Course

"AI-Powered Investing for Juniors"

Visual identity for the 8th-10th grade course. Inherits from
`shared.md`. Designed for high school students with no assumed
finance or programming knowledge.

---

## Design Inspiration

The visual language draws from teen-focused financial education and
fintech brands:

- **Greenlight:** Bright green accents, clean modern layout, card-based
  UI, friendly but not childish. Treats teens as capable — doesn't
  dumb things down visually. Rounded elements feel approachable without
  being cartoonish.

- **Next Gen Personal Finance (NGPF):** Clean educational design,
  blue-orange palette, strong use of callout boxes and sidebars.
  Content-rich but well-organized. Good model for how to present
  financial concepts to young learners without patronizing them.

- **The Stock Market Game (SIFMA):** Game-like engagement hooks,
  progress tracking, achievement framing. The "you built something
  real" feeling at the end of each week.

- **Junior Achievement:** Empowering tone, bright but professional
  palette, focus on real-world skills. Positions young people as
  future professionals, not as kids playing pretend.

**Our synthesis:** Greenlight's modern fintech aesthetic + NGPF's
educational clarity + Junior Achievement's empowering positioning.
The design should say "you're learning real skills that real
professionals use" — not "here's a dumbed-down version for kids."

---

## Color Palette

### Primary Palette

| Token | Hex | Swatch | Usage |
|-------|-----|--------|-------|
| `primary` | `#1A73E8` | Bright blue | Headings, primary brand color |
| `primary-light` | `#4A90D9` | Medium blue | Hover states, secondary accents |
| `secondary` | `#F59E0B` | Warm amber | Callout accents, highlights, "Investing 101" boxes |

### Neutral Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `surface` | `#FFFFFF` | Page background |
| `surface-alt` | `#F0F4F8` | Code blocks, callout backgrounds, sidebars |
| `text` | `#1F2937` | Primary body text |
| `text-muted` | `#6B7280` | Captions, timestamps, secondary info |
| `border` | `#D1D5DB` | Table borders, dividers |

### Semantic Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `success` | `#059669` | Stock gains, "hot" status, passing checks |
| `danger` | `#DC2626` | Stock losses, "cold" status, errors |
| `info` | `#1A73E8` | Tips, notes (same as primary) |

### Code Block Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `code-bg` | `#F8FAFC` | Light code block background |
| `code-text` | `#334155` | Code foreground text |
| `code-comment` | `#94A3B8` | Code comments |
| `code-keyword` | `#1A73E8` | Keywords, JSON keys (matches primary) |
| `code-string` | `#059669` | String values (matches success) |
| `code-number` | `#D97706` | Numeric values (warm amber) |

Light code blocks on a light page feel less intimidating for students
who haven't seen code before. The code still stands out via the
`surface-alt` background but doesn't create the stark dark-on-light
contrast of the professional version.

---

## Typography Refinements

Inherits the type scale from `shared.md` with these adjustments:

- **Body text:** 17pt (slightly larger than professional for easier
  reading). Line height 1.7.
- **Maximum line length:** 65 characters (shorter than professional —
  easier for younger readers).
- **Paragraph length:** Maximum 3-4 sentences. Break aggressively.
- **Chapter titles (H1):** Use `primary` (#1A73E8).
- **Section headers (H2):** Use `primary`. Bottom border in `secondary`
  (#F59E0B) — adds warmth.
- **Subsection headers (H3):** Use `text` color.

### Heading Hierarchy Example

```
# Connecting AI to Real Data              ← H1: primary blue, 34pt, bold
## 1.2 How AI Connects to Data            ← H2: primary blue, 26pt, amber bottom border
### Rule 1: Do the Math in the Tool       ← H3: text color, 20pt, semibold
```

---

## Component Styles

### Prompt Example Block ("Try This")
- Background: `surface-alt` (#F0F4F8)
- Left border: 4px solid `primary` (#1A73E8)
- Label: "Try This:" or "Tell Claude Code:" in `primary`, bold, 14pt
- Content: monospace, dark text on light background
- Slightly more padding than professional version (16px → 20px)

### Tool Return Block (JSON)
- Background: `code-bg` (#F8FAFC) — light theme
- Label: "What it returns:" in `text-muted`, positioned above block
- First 2-3 chapters: include a plain-English annotation below the
  JSON block explaining what each field means
- Later chapters: JSON stands alone (students are comfortable by now)

### "Investing 101" Sidebar
*Unique to junior course.* Finance concept explanation inline with
AI content.
- Background: `#FFFBEB` (very light amber)
- Left border: 4px solid `secondary` (#F59E0B)
- Title: "Investing 101:" in `secondary` color, bold
- Icon: lightbulb (Lucide `lightbulb`) in `secondary`
- Keep brief: 2-4 sentences max

### "Why This Matters" Callout
*Unique to junior course.* Connects a technical concept to something
teens care about.
- Background: `surface-alt`
- Left border: 4px solid `primary` (#1A73E8)
- Title: "Why This Matters" in `primary`, bold
- Example: "This is the same pattern used by real hedge funds. You're
  learning the actual architecture, not a simplified version."

### Warning / Disclaimer
- Background: `#FEF2F2` (very light red)
- Left border: 4px solid `danger` (#DC2626)
- Icon: alert triangle (Lucide `alert-triangle`)
- Used for: risk disclaimers, "these tools are for learning" notes

### Checklist ("Did It Work?")
- Background: white
- Checkbox style: rounded square, `primary` color when checked
- Section headers in `primary`
- Title of checklist section: "Did It Work?" (not "Evaluation Checklist")

### Table Style
- Header row: `primary` background, white text, bold
- Body rows: alternating white / `surface-alt`
- Borders: 1px `border` color, slightly rounded corners (4px)
- Number columns: right-aligned
- Stock gains: `success` green. Stock losses: `danger` red.

---

## Illustration Style

The junior course uses illustrations where the professional course
uses none. Guidelines:

- **Style:** Clean flat illustration or line art. Moderate detail.
  Think "editorial illustration" not "children's book."
- **Color:** Draw from the course palette. Primary blue, amber accent,
  success green, danger red. Neutral grays for structure.
- **Subjects:**
  - System diagrams: how AI connects to tools, how servers talk to
    each other, the monitoring loop
  - Concept illustrations: the "smoke detector" analogy, the
    "restaurant waiter" analogy, the "USB port" analogy
  - Progress markers: visual showing what you've built so far
    (cumulative across weeks)
- **Do not:** Use clip art, cartoon mascots, overly childish imagery,
  or realistic character illustrations

---

## Tone and Voice

**Persona:** A cool older sibling or young mentor who's genuinely
excited about this stuff. They're clear and encouraging but never
condescending. They assume you're smart — you just don't have the
context yet.

**Register:** Conversational but informative. Explains both finance
AND AI concepts. Uses analogies freely. Defines terms on first use.

**Specific guidance:**
- Use "you" and "your" throughout
- Contractions always ("don't", "it's", "you'll", "that's")
- Occasional informal phrasing is fine ("Here's the cool part",
  "That's a big deal")
- No emoji (per shared brand)
- Define financial terms on first use, inline or in "Investing 101"
  sidebar
- Use relatable company examples: Roblox, Snapchat, Spotify, Duolingo, Crocs (primary); Take-Two, Netflix, Disney (extended)
- Use relatable analogies: smoke detector, restaurant waiter, movie
  director, menu at a restaurant
- Risk disclaimers should be honest but not scary

**Example — good:**
> "Roblox is your standout today — up 2.35% with more than double its
> normal trading volume, even while the overall market is slightly
> down. That kind of strength against a weak market is worth paying
> attention to."

**Example — too childish:**
> "Wow, Roblox is on FIRE today! Super cool to see it going up while
> everything else is going down, right?? Let's see what happens next!"

**Example — too adult:**
> "RBLX exhibits notable relative strength, outperforming the broader
> market on elevated volume, suggesting institutional accumulation
> during a risk-off session."

---

## Page Layout

### Chapter Opening
- Chapter number: large numeral in `primary`, semi-transparent (0.15
  opacity), positioned as background element
- Chapter title: H1, `primary`
- Opening hook: 1-2 sentences, slightly larger text (19pt), explaining
  why this chapter is interesting
- Optional: small illustration related to the chapter topic

### Exercise Pages
- Step numbers: large bold numerals in `primary` with `surface-alt`
  circle background
- Time estimate: pill badge, right-aligned, `text-muted`
- "Try This" blocks interspersed (from conversation guide)
- More whitespace between steps than professional version

### Reference Solution Pages
- Tool table at top: summary of all tools
- Each tool section: name as H3, JSON block, "What's smart about this
  design:" as bullet list (not "Key design decisions" — more engaging
  framing)
- Consider showing a "before and after" for the first tool: what the
  AI would say without the tool vs. with it

---

## Unique Elements (Junior Only)

These elements don't exist in the professional course:

### 1. "Investing 101" Sidebar
Quick finance concept explanations. See component styles above.

### 2. "Why This Matters" Callout
Connecting technical concepts to teen interests.

### 3. JSON Annotation
For the first few chapters, show plain-English translations alongside
JSON tool returns:

```
{
  "ticker": "RBLX",           ← The stock's code name
  "current_price": 59.80,     ← What one share costs right now
  "daily_change_pct": 1.65,   ← Up 1.65% today (code did this math)
  "data_source": "yfinance"   ← Where the data came from
}
```

Drop annotations by Week 3 — students will be comfortable by then.

### 4. Weekly Progress Tracker
Visual element showing cumulative progress:
```
Week 1: [■] Stock tracker
Week 2: [■] + Daily report + Safety checks
Week 3: [■] + Multi-server design
Week 4: [■] + Monitor + Audit trail
```

### 5. Risk Disclaimer Box
Appears in introduction and at key points. Not preachy — just honest.

---

## Do's and Don'ts

**Do:**
- Treat students as smart people who lack context, not as children
- Use bright, modern design that feels like a fintech app
- Include illustrations for system concepts and analogies
- Add "Investing 101" sidebars for finance terms
- Make JSON less intimidating with annotations early on
- Use the amber accent to add warmth and energy

**Don't:**
- Use cartoonish mascots or childish clip art
- Dumb down the actual technology (same MCP, same patterns)
- Use dark code blocks (too intimidating for new learners)
- Add gamification elements (points, badges, leaderboards)
- Use slang or try too hard to sound "teen" — be genuine
- Make the risk disclaimers preachy or lecture-like
