# Brand Guidelines — Shared Foundation

This document defines the parent brand for both courses. The
professional and junior courses each have their own visual identity
(see `professional.md` and `juniors.md`), but both inherit from
this shared foundation.

---

## Brand Name

**Parent brand:** AI Investment Academy

**Course names:**
- Professional: "AI-Powered Investment Management"
- Junior: "AI-Powered Investing for Juniors"

Always lead with "AI-Powered" — this positions both courses in the
same family. The subtitle differentiates the audience.

**Tagline options (shared):**
- "Build AI tools. No coding required."
- "From idea to working tool in 30 minutes."

---

## Mission

Teach people to direct AI to build real tools — not to write code,
not to understand machine learning theory, but to describe workflows
in plain English and get working software back. The skills transfer
to any domain; finance is the vehicle.

---

## Core Values (Both Courses)

1. **Honesty over impressiveness.** Guardrails, stale data warnings,
   and "AI proposes, humans decide" aren't caveats — they're the
   point. We teach responsible AI use.

2. **Building over theorizing.** Every week produces a working tool.
   Concepts serve the exercise, not the other way around.

3. **Real data, not toy examples.** Yahoo Finance, SEC EDGAR, actual
   stock prices. The tools work after the course ends.

4. **Skill, not magic.** Directing AI is a learnable skill. Good
   descriptions produce good tools. Evaluation and iteration matter
   more than the first attempt.

---

## Typography

### Font Families

**Primary heading font:** A geometric sans-serif with authority.
- Preferred: **Inter** (free, widely available)
- Alternatives: Söhne, Helvetica Neue, SF Pro Display

**Body text font:** A readable sans-serif optimized for long-form reading.
- Preferred: **Inter** (consistent with headings)
- Alternative: Source Sans Pro, IBM Plex Sans

**Code / monospace font:** For code blocks, JSON examples, terminal commands.
- Preferred: **JetBrains Mono** (free, ligatures, excellent readability)
- Alternatives: Fira Code, SF Mono, Cascadia Code

### Type Scale

| Element | Size | Weight | Leading |
|---------|------|--------|---------|
| H1 (chapter title) | 32-36pt | Bold (700) | 1.2 |
| H2 (section) | 24-28pt | Semibold (600) | 1.25 |
| H3 (subsection) | 18-20pt | Semibold (600) | 1.3 |
| Body text | 16pt | Regular (400) | 1.6 |
| Code blocks | 14pt | Regular (400) | 1.5 |
| Captions / labels | 13pt | Medium (500) | 1.4 |
| Table content | 14-15pt | Regular (400) | 1.4 |

---

## Shared Color Tokens

These semantic color roles are used by both courses. The actual hex
values differ per course (see individual brand files).

| Token | Role | Usage |
|-------|------|-------|
| `primary` | Brand anchor | Headings, primary buttons, accent lines |
| `primary-light` | Lighter variant | Hover states, subtle backgrounds |
| `secondary` | Supporting color | Subheadings, secondary elements |
| `surface` | Page background | Main content area |
| `surface-alt` | Alternate background | Code blocks, callout boxes, tables |
| `text` | Primary text | Body copy, headings |
| `text-muted` | Secondary text | Captions, metadata, timestamps |
| `border` | Dividers | Table borders, section separators |
| `success` | Positive / up | Stock gains, passing checks |
| `danger` | Negative / down | Stock losses, errors, warnings |
| `info` | Informational | Tips, notes, neutral callouts |
| `code-bg` | Code background | Code blocks, inline code |
| `code-text` | Code foreground | Code syntax |

---

## Iconography

- Use **line icons** (not filled) for UI elements and navigation
- Icon stroke weight: 1.5-2px, matching body text weight
- Prefer open-source icon sets: Lucide, Phosphor, or Heroicons
- Do not use emoji as functional icons (emoji may appear in content
  only if the course brief specifies it)

---

## Layout Principles

### Grid
- Maximum content width: **720px** for reading content (optimal line
  length for body text)
- Maximum content width: **960px** for tables and code blocks
- Page margins: minimum 48px on each side (desktop), 24px (mobile)

### Spacing Scale
Use a consistent 8px base unit:
- `xs`: 8px
- `sm`: 16px
- `md`: 24px
- `lg`: 32px
- `xl`: 48px
- `2xl`: 64px

### Content Blocks
- Paragraphs: maximum 4-5 sentences. Break earlier rather than later.
- Lists: prefer bulleted over numbered unless order matters
- Tables: use for structured comparisons. Left-align text, right-align numbers.
- Code blocks: always include language identifier for syntax highlighting

---

## Recurring Content Elements

These elements appear in both courses and should have consistent
visual treatment (with per-course color variations):

### 1. Prompt Example
Shows what to type into Claude Code. Style as a distinct callout
with a label like "Tell Claude Code:" or "Try This:".

### 2. Tool Return Example
JSON blocks showing what MCP tools return. Use syntax-highlighted
code blocks with a label like "What it returns:".

### 3. Concept Callout
Key concept highlighted in a box. Professional course uses
"Key Design Decision" framing; junior course uses "Why This Matters".

### 4. Checklist
End-of-chapter self-assessment. Use checkbox-style formatting with
clear pass/fail criteria.

### 5. Warning / Disclaimer
Important caveats (stale data, not financial advice). Distinct from
regular callouts — use `danger` color token.

### 6. Guide Tool Block
Shows what the guide tool returns. Styled like a tool return but
with a distinct label ("Guide Tool" or "AI Menu").

---

## Photography and Illustration

- **Professional course:** No illustrations. Photography only if needed
  — abstract, minimal (screens with data, hands on keyboard, city
  skylines). Avoid stock photos of people pointing at charts.
- **Junior course:** Illustrations preferred over photography.
  Clean line art or flat illustration style. No cartoonish mascots.

---

## Voice and Tone Principles

Both courses share these principles (tone differs — see per-course files):

1. **Lead with the point.** Don't build up to the answer. State it,
   then explain.
2. **Concrete over abstract.** Show an example before explaining the
   theory.
3. **Honest about limitations.** AI makes mistakes. Local models are
   less capable than cloud. Math in AI is unreliable. Say so.
4. **Active voice.** "The tool returns a dict" not "A dict is returned
   by the tool."
5. **No filler.** Cut "it's important to note that" and "as we
   discussed earlier." Just say the thing.

---

## File Naming Conventions

- All lowercase, hyphens for spaces: `reading.md`, `reference_solution.md`
- Underscores in compound names: `conversation_guide.md`, `shared_utils.py`
- Course-specific prefixes not needed (folder structure handles it)
- Brand files: `shared.md`, `professional.md`, `juniors.md`

---

## Version Control

- Both courses live in the same repository
- Changes to shared brand elements require updates to both per-course files
- See `SYNC_GUIDE.md` for the content synchronization protocol
