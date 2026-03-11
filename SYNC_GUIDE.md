# Course Sync Guide

How to keep the professional and junior courses aligned when one is
edited. Both courses teach the same technology — MCP servers, Claude
Code, Claude Desktop, guardrail patterns — but differ in tone,
examples, and assumed knowledge.

---

## File Mapping

Every file in `professional/` has a 1:1 counterpart in `juniors/`.
The structure is identical:

```
professional/                    juniors/
├── README.md                    ├── README.md
├── COURSE_BRIEF.md              ├── COURSE_BRIEF.md
├── introduction.md              ├── introduction.md
├── prerequisites.md             ├── prerequisites.md
├── glossary.md                  ├── glossary.md
├── conclusion.md                ├── conclusion.md
├── week-N/                      ├── week-N/
│   ├── reading.md               │   ├── reading.md
│   └── exercise/                │   └── exercise/
│       ├── README.md            │       ├── README.md
│       ├── conversation_guide   │       ├── conversation_guide
│       ├── checklist.md         │       ├── checklist.md
│       ├── reference_solution   │       ├── reference_solution
│       └── (setup.md, etc.)     │       └── (setup.md, etc.)
└── bonus-local-rag/             └── bonus-local-rag/
    └── (same structure)             └── (same structure)
```

---

## What Is Shared vs. Different

### Structurally shared (changes MUST propagate)

These elements are the same in both courses. If you change one, the
other needs the same change:

- **MCP tool patterns.** Both courses teach the same FastMCP patterns.
  Tool return schemas, `@mcp.tool()` decorators, dict-based returns.
- **Architecture concepts.** Separation of concerns, multi-server
  design, shared utility library, Claude Desktop configuration.
- **Guardrail patterns.** Pre-computed values, stale data warnings,
  verbatim sections, human-in-the-loop.
- **Monitoring framework.** SILENT/ALERT/URGENT/BLOCKED levels, audit
  trail structure, append-only logging.
- **Tool names and return schemas.** `get_stock_quote()`,
  `get_daily_report()`, `get_monitor_alerts()` — same function
  signatures, same return dict structure.
- **Week ordering and topics.** Week 1 = stock data, Week 2 = daily
  report, Week 3 = multi-server, Week 4 = monitoring, Bonus = local
  RAG.
- **Technical prerequisites.** Python, uv, Claude Desktop, Claude
  Code — same tools, same versions.
- **Exercise structure.** Same number of steps per week, same general
  flow (read → design → build → test → connect).

### Intentionally different (do NOT blindly copy)

These elements differ by design between courses:

| Element | Professional | Junior |
|---------|-------------|--------|
| **Tone** | Senior colleague, direct | Cool older sibling, encouraging |
| **Finance knowledge** | Assumed (no definitions) | Taught inline ("Investing 101" sidebars) |
| **Default stocks** | AAPL, MSFT, NVDA, JPM, XOM | RBLX, SNAP, SPOT, DUOL, CROX (primary); TTWO, NFLX, DIS (extended) |
| **Project folder** | `~/ai-finance-tools` | `~/ai-stock-tools` |
| **Status labels** | outperforming/underperforming | hot/cold/steady |
| **Week 3 scenario** | Equity L/S fund (3 servers) | School stock club (2 servers) |
| **Code blocks** | Dark theme (`#1E293B` bg) | Light theme (`#F8FAFC` bg) |
| **JSON annotations** | None | Plain-English translations (weeks 1-2) |
| **Analogies** | Industry references (Bloomberg, FactSet) | Everyday (smoke detector, restaurant waiter) |
| **Financial terms** | Used without definition | Defined on first use |
| **Paragraph length** | Max 4-5 sentences | Max 3-4 sentences |
| **Brand colors** | Deep navy + teal | Bright blue + amber |
| **Illustrations** | None | Clean flat/line art for concepts |
| **Unique elements** | "Key Design Decision" callouts | "Investing 101", "Why This Matters" callouts |

---

## Sync Workflow

### When you edit a file in one course:

1. **Identify the change type.** Is it structural (new concept, bug
   fix, changed tool schema) or cosmetic (rewording, tone adjustment)?

2. **Structural changes → propagate.** Open the counterpart file in
   the other course and make the equivalent change, adapted to that
   course's tone and audience. Examples:
   - Adding a new MCP tool → add to both courses
   - Fixing a JSON schema error → fix in both
   - Changing exercise step order → change in both
   - Adding a new guardrail pattern → add to both

3. **Cosmetic changes → skip.** Rewording a paragraph for clarity in
   one course doesn't require touching the other. The courses have
   different voices.

4. **Mixed changes → separate them.** If you rewrote a section AND
   added a new concept, propagate the concept but not the rewrite.

### When you add a new file:

- Add the counterpart file in the other course
- Adapt tone, examples, and assumed knowledge
- Update both course briefs if the file changes the course structure

### When you delete a file:

- Delete from both courses
- Update both course briefs and any cross-references

---

## Quick Reference: Propagation Rules

| Change type | Propagate? | How |
|------------|-----------|-----|
| New MCP tool or schema change | Yes | Adapt examples to course audience |
| Bug fix in code/JSON | Yes | Same fix, both courses |
| New exercise step | Yes | Adapt framing and language |
| New concept or pattern | Yes | Professional: state it. Junior: explain it. |
| Tone/wording adjustment | No | Courses have different voices |
| New analogy | No | Analogies are audience-specific |
| New "Investing 101" sidebar | No | Junior-only element |
| New "Key Design Decision" callout | No | Professional-only element |
| Brand/color change | Check | Update the relevant `brand/*.md` file |
| Prerequisite change | Yes | Same tools for both courses |

---

## CI Integration

The GitHub Actions workflow (`.github/workflows/sync-check.yml`)
runs on every push and PR. It compares the file trees of both
courses and flags:

- **Missing counterpart:** A file exists in one course but not the
  other. This is always a problem (except for course-specific files
  that don't exist yet).
- **Structure drift:** The two courses have different directory
  structures. This shouldn't happen.

The CI check does NOT compare file contents — the courses are
supposed to have different content. It only checks that the file
structure stays in sync.

---

## Brand File Updates

The three brand files in `brand/` govern visual identity:

- `shared.md` — Parent brand. Changes here affect both courses.
- `professional.md` — Adult course only.
- `juniors.md` — Teen course only.

If you change a shared design token (e.g., the type scale), update
`shared.md`. If you change a course-specific color, update only that
course's brand file.

See `brand/shared.md` for the full list of semantic color tokens and
which ones are shared vs. course-specific.
