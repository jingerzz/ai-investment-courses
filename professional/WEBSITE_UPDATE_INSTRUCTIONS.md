# Website Update Instructions

These instructions describe the changes made to the course materials
that need to be reflected on the website at `jing.zo.space`.

---

## Summary of Changes

The course has been restructured to follow a **"use before you build"**
pedagogy. The bonus module has been eliminated — its content is now
integrated into Week 2.

### Old Structure
- Week 1: Build an MCP server from scratch (Claude Code)
- Week 2: Add guardrails and reasoning patterns
- Bonus: Local RAG with Ollama (optional, separate)
- Week 3: System design
- Week 4: Autonomous agents

### New Structure
- **Week 1: The Tool-Use Pattern** — Install and USE pre-built servers.
  No coding. Students experience AI tools backed by real market data
  before building their own.
- **Week 2: Building Your Own AI Tools** — Build with Claude Code +
  set up Ollama + page-index-rag. Guardrails, RAG, and local models
  are all here now.
- Week 3: System design (unchanged)
- Week 4: Autonomous agents (unchanged)
- **Bonus: REMOVED** — content absorbed into Week 2

---

## Files Changed

### Course content (update website pages from these):

| File | Website Page | What Changed |
|------|-------------|--------------|
| `week-1/reading.md` | week-1.html | Complete rewrite. Now covers: SPY/TLT color strategy (colors, 9 signals, 3 tiers, danger state, greed trim, backtest), MCP fundamentals (anatomy of a tool, return contract, transport), four design principles (pre-compute, context metadata, one-tool-per-question, guide tool), where AI adds value. |
| `week-1/exercise/README.md` | week-1.html (exercise section) | Complete rewrite. Now: install uv, install spy-tlt-course server, connect to Claude Desktop, guided exploration of 14 tools through specific prompts, troubleshooting. No Claude Code needed. |
| `week-2/reading.md` | week-2.html | Complete rewrite. Now covers: Claude Code as builder, tool docstring design, return contracts, three guardrail patterns (pre-compute, pre-formatted templates, stale data warnings), Ollama local models, structure-first RAG for financial documents, where AI reasoning adds value. |
| `week-2/exercise/README.md` | week-2.html (exercise section) | Complete rewrite. Part A (20 min): build watchlist server with Claude Code. Part B (10 min): install Ollama + page-index-rag, query pre-indexed BLK/HOOD filings. |
| `introduction.md` | intro page | Updated "What You'll Actually Do" section and weekly progression description. |
| `conclusion.md` | conclusion page | Updated week descriptions. Removed bonus module reference. |

### Supporting files (update if referenced on website):

| File | What Changed |
|------|--------------|
| `README.md` | Rewritten — new weekly progression table, included servers, updated structure tree |
| `COURSE_BRIEF.md` | Updated learning outcomes, chapter mapping, removed bonus chapter |

### New server packages (NOT website content, but referenced in exercises):

| Package | Description |
|---------|-------------|
| `servers/spy-tlt-course/` | Pre-built SPY/TLT strategy server with 14 MCP tools. Students install this in Week 1. |
| `servers/page-index-rag-course/` | Pre-built RAG server with 14 MCP tools + 7 pre-indexed SEC filings (BLK, HOOD). Students install this in Week 2. |

---

## Key Content Differences to Reflect

### Week 1 page (biggest change)

**Before:** Students use Claude Code to build a watchlist server.
The reading explained MCP concepts abstractly.

**After:** Students install a pre-built server and explore it. The
reading explains the SPY/TLT strategy in detail (this is new — the
old course never explained the strategy, it just assumed knowledge).

Key sections to render on the page:
1. The SPY/TLT Color Strategy — table of 4 colors, 9 signals by tier,
   danger state rules, backtest results table
2. MCP anatomy — code example of `get_current_signal()` with the four
   components labeled
3. Four design principles — each grounded in a real tool from the
   SPY/TLT server
4. Exercise — 6 steps, each with specific Claude Desktop prompts to try

### Week 2 page (major rewrite)

**Before:** Adding guardrails to Week 1's server. RAG was in a separate
bonus module.

**After:** Two-part exercise. Part A builds a new server from scratch
with Claude Code. Part B sets up Ollama and page-index-rag.

Key sections to render:
1. Claude Code development loop
2. Tool docstring design (weak vs strong examples)
3. Three guardrail patterns with code examples
4. Ollama introduction + model selection table (by RAM)
5. Structure-first RAG explanation + tree diagram
6. Exercise Part A: build watchlist server (step-by-step prompts)
7. Exercise Part B: install Ollama + page-index-rag (4 steps)

### Week 3 page (exercise rewritten, reading lightly updated)

**Reading:** Minor update to opening paragraph — now references the
three servers students already have instead of "In Weeks 1-2, you
built a single MCP server." Rest of reading unchanged.

**Exercise (rewritten):** Instead of designing a hypothetical system,
students connect their three existing servers to Claude Desktop and
experience cross-server queries:
1. Connect all 3 servers simultaneously
2. Cross-server queries (strategy + watchlist, strategy + research, all three)
3. Identify architecture patterns (shared data, shared library candidates)
4. Build a shared data pattern (watchlist reads SPY CSV from spy-tlt-course)
5. Design a 4th server (risk management) — design only, not built

Key sections to render:
1. Exercise steps with specific Claude Desktop prompts for cross-server queries
2. Architecture principles list (5 items)
3. Troubleshooting section

### Week 4 page (exercise rewritten, reading lightly updated)

**Reading:** Minor updates — replaced MES/ES futures references with
SPY equivalents (students don't have futures tools). Concepts unchanged.

**Exercise (rewritten):** Students build a monitoring agent that uses
their existing SPY/TLT and watchlist servers:
1. Design monitoring rules with Claude Desktop
2. Build monitor.py that calls spy-tlt-course tools + yfinance
3. Classify findings: SILENT / ALERT / URGENT / BLOCKED
4. Add audit trail with full reasoning chain
5. Expose alerts as MCP tool (get_monitor_alerts)
6. Test the full agent loop: monitor → alerts in Claude Desktop →
   cross-server synthesis → proposed actions

Key sections to render:
1. Step-by-step exercise with Claude Code prompts
2. Autonomy spectrum diagram (SILENT → ALERT → URGENT → BLOCKED)
3. "AI Proposes, Humans Decide" section
4. Troubleshooting section

### Navigation / Table of Contents

Remove any "Bonus Module" or "Bonus: Local RAG" entries from navigation.
The course is now strictly 4 weeks with no bonus. Remove "under
construction" labels from Weeks 3-4.

Update the weekly overview/progression table anywhere it appears:
- Week 1: "The Tool-Use Pattern" (install and explore pre-built servers)
- Week 2: "Building Your Own AI Tools" (Claude Code + Ollama + RAG)
- Week 3: "System Design and Architecture" (compose multi-server system)
- Week 4: "Autonomous Agents and Controls" (monitoring agent with audit trail)

---

## What NOT to Change

- The glossary is unchanged
- Prerequisites content is unchanged (though Week 1 now only needs
  uv + Claude Desktop, not Claude Code — Claude Code is first needed
  in Week 2)
