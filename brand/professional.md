# Brand Guidelines — Professional Course

"AI-Powered Investment Management"

Visual identity for the professional/adult course. Inherits from
`shared.md`. Designed for investment analysts, portfolio managers,
and IT managers at investment firms.

---

## Design Inspiration

The visual language draws from the institutional investment world —
firms like Citadel, Point72, Millennium Management, Two Sigma, and
Bridgewater Associates. Their design principles:

- **Citadel:** Deep navy and black, serif accents, ultra-minimal.
  Nothing decorative. Authority through restraint. The website feels
  like a leather-bound portfolio — no wasted elements.

- **Point72:** Blue-gray palette, generous whitespace, modern sans-serif.
  Clean data presentation. Photography is abstract and architectural.
  Feels like a well-organized research desk.

- **Millennium Management:** Dark, sophisticated, almost monochromatic.
  Minimal color means every accent carries weight. Corporate elegance
  without flash.

- **Two Sigma:** More tech-forward than peers. Data-visualization
  aesthetics, blues and teals, geometric patterns. The intersection
  of finance and technology — which is exactly what this course teaches.

- **Bridgewater Associates:** Slightly warmer, more intellectual.
  Thought-leadership positioning. Red-orange accents against neutral
  backgrounds. Content-dense but well-organized.

**Our synthesis:** Two Sigma's tech-meets-finance positioning +
Citadel's restraint + Point72's clarity. We're teaching finance
professionals to build technology — the design should feel like both
worlds meeting.

---

## Color Palette

### Primary Palette

| Token | Hex | Swatch | Usage |
|-------|-----|--------|-------|
| `primary` | `#1B2A4A` | Deep navy | Headings, primary brand color |
| `primary-light` | `#2D4A7A` | Medium navy | Hover states, accent borders |
| `secondary` | `#4A9BA8` | Teal | Subheadings, links, interactive elements |

### Neutral Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `surface` | `#FFFFFF` | Page background |
| `surface-alt` | `#F5F6F8` | Code blocks, callout backgrounds, table stripes |
| `text` | `#1A1A2E` | Primary body text |
| `text-muted` | `#6B7280` | Captions, timestamps, secondary info |
| `border` | `#E2E4E9` | Table borders, dividers |

### Semantic Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `success` | `#0D7C5F` | Stock gains, positive values, checkmarks |
| `danger` | `#C4272E` | Stock losses, errors, warnings, disclaimers |
| `info` | `#2D4A7A` | Notes, tips (same as primary-light) |

### Code Block Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `code-bg` | `#1E293B` | Dark code block background (Citadel-inspired) |
| `code-text` | `#E2E8F0` | Code foreground text |
| `code-comment` | `#64748B` | Code comments |
| `code-keyword` | `#7DD3FC` | Python keywords, JSON keys |
| `code-string` | `#86EFAC` | String values |
| `code-number` | `#FCA5A5` | Numeric values |

Dark code blocks on a light page create a strong visual contrast —
this is the Two Sigma / Citadel approach. Code and data stand out
as distinct elements, not inline with prose.

---

## Typography Refinements

Inherits the type scale from `shared.md` with these additions:

- **Chapter titles (H1):** Use `primary` (#1B2A4A). All caps optional
  for part headers (PART I, PART II) but not for chapter names.
- **Section headers (H2):** Use `primary`. A 2px bottom border in
  `border` color to anchor sections.
- **Subsection headers (H3):** Use `text` color. No border.
- **Body text:** Use `text`. 16pt / 1.6 line height. Maximum 75
  characters per line.

### Heading Hierarchy Example

```
PREREQUISITES                           ← Part label: all caps, primary, 14pt, letterspaced
# Making Your Data AI-Accessible        ← H1: primary, 34pt, bold
## 1.2 Model Context Protocol           ← H2: primary, 26pt, semibold, bottom border
### The Return Contract                 ← H3: text, 20pt, semibold
```

---

## Component Styles

### Prompt Example Block
- Background: `surface-alt` (#F5F6F8)
- Left border: 4px solid `secondary` (#4A9BA8)
- Label: "Tell Claude Code:" in `secondary`, small caps, 13pt
- Content: monospace, dark text on light background

### Tool Return Block (JSON)
- Background: `code-bg` (#1E293B) — dark theme
- Label: "What it returns:" in `text-muted`, positioned above block
- Syntax highlighting per code color tokens above

### Key Design Decision Callout
- Background: `surface-alt`
- Left border: 4px solid `primary` (#1B2A4A)
- Title: "Design Decision" in `primary`, bold
- For guardrail patterns, use "Guardrail Pattern" as title

### Warning / Disclaimer
- Background: `#FEF2F2` (very light red)
- Left border: 4px solid `danger` (#C4272E)
- Icon: alert triangle (Lucide `alert-triangle`)

### Checklist
- Background: white
- Checkbox style: square, unchecked state uses `border` color
- Section headers in `primary`

### Table Style
- Header row: `surface-alt` background, `primary` text, bold
- Body rows: alternating white / `surface-alt`
- Borders: 1px `border` color
- Number columns: right-aligned, tabular figures
- Financial values: green (`success`) for positive, red (`danger`) for negative

---

## Tone and Voice

**Persona:** A senior colleague who's been building these systems and
is showing you how. They're direct, experienced, and occasionally dry.
They don't oversimplify, but they don't showboat either.

**Register:** Professional. Assumes you know finance. Explains AI
concepts without condescension. Uses industry terminology correctly
(regime, alpha, drawdown, risk-off) without defining it.

**Specific guidance:**
- Use "you" not "the participant" or "the user"
- Contractions are fine ("don't", "it's", "you'll")
- No exclamation marks unless quoting a terminal error
- No emoji
- Technical terms unbolded after first introduction
- Reference real tools: Bloomberg, FactSet, tastytrade — not "your
  existing systems"
- Financial examples use realistic figures, not round numbers
  ($195.20 not $200.00)

**Example — good:**
> "The AI received pre-computed risk metrics from your tool. It
> didn't calculate portfolio VaR — Python did. The AI's contribution
> was connecting the risk posture to the current regime and explaining
> why the hedge is working."

**Example — too casual:**
> "Pretty cool, right? The AI figured out the risk stuff and told
> you what's up with your portfolio!"

**Example — too academic:**
> "The language model, having received structured output from the MCP
> tool function, proceeds to perform cross-referential synthesis across
> the signal and risk domains."

---

## Page Layout

### Chapter Opening
- Chapter number: small, `text-muted`, above title
- Chapter title: H1, `primary`
- Opening paragraph: slightly larger body text (18pt) for first
  paragraph only
- No decorative elements

### Exercise Pages
- Step numbers: circled numerals in `primary` color
- Time estimate: right-aligned, `text-muted`
- Code prompts: prompt example blocks (see component styles)

### Reference Solution Pages
- Tool table at top: summary of all tools
- Each tool section: name as H3, "What it returns:" JSON block,
  "Key design decisions:" as bullet list
- Design decision bullets use `primary` color for the decision name

---

## Do's and Don'ts

**Do:**
- Use restrained, institutional design language
- Let whitespace carry the sophistication
- Make data and code the visual focus
- Use dark code blocks for strong contrast
- Keep decorative elements to zero

**Don't:**
- Use gradients, drop shadows, or rounded corners on content blocks
- Add stock photography of people in suits looking at screens
- Use bright or saturated accent colors
- Add decorative illustrations or icons in margins
- Use light/pastel code block backgrounds — they reduce contrast
