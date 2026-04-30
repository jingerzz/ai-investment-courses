# Intentional Divergence: Course ↔ Platform

This is a registry of files and patterns where the course MCP servers in
`professional/servers/` intentionally differ from the upstream production
packages in the `AI-trading-platform` repo. **Do not port these on your
next drift sweep — the divergence is by design.**

The `scripts/check_drift.py` report will continue to flag these as `MAJOR`
or `PLATFORM-ONLY`. That's fine; cross-reference this file when reviewing.

Last reviewed: 2026-04-30.

---

## spy-tlt-course

### `data.py` (course-only)
**What:** Standalone yfinance + CSV data layer.
**Platform equivalent:** `trading-core` workspace package (`packages/core/`)
with broker abstractions, tastytrade client, options helpers, journal, etc.
**Why diverged:** Course must run with no API keys, no broker accounts,
no `trading-core` dependency. Students get one `uv sync` and they're done.
**Ported from platform?** No. Never.

### `server.py` monolithic shape (course-only)
**What:** Single 761-line `server.py` with all 14 tools inline.
**Platform equivalent:** `mcp_server/server.py` + `mcp_server/tools/{strategy,
es, zb, risk, spy_stats, equities, options}.py` split.
**Why diverged:** The split is good engineering for production but bad
pedagogy. Students reading the course server learn FastMCP patterns by
seeing all decorators in one file. The split is introduced as a refactor
exercise in a later week, not as the starting point.
**Ported from platform?** No. The split would harm Week 1 readability.

### Platform-only files (DO NOT PORT)
All the following are broker-dependent or futures-specific and require
`trading-core` + tastytrade. They have no place in a standalone course:

- `es_engine.py`, `zb_engine.py`, `short_engine.py`
- `mcp_server/tools/es.py`, `zb.py`, `options.py`, `risk.py`, `equities.py`
- `mcp_server/tools/_guide_data.py` (37-tool catalog — course only has 14)
- `mcp_server/__init__.py`, `mcp_server/tools/__init__.py`

### `advisor.py` divergence (~840 platform-only lines)
**What:** Platform has `print_*`, `parse_args`, `main`, `print_pattern_report`,
`print_dashboard`, ANSI helpers (`_c`, `_b`), and a `compute_trade_plan`
that takes an `es_levels` parameter for ES/MES.
**Why diverged:** All this scaffolding exists for the platform's `./strat`
CLI, which the course doesn't ship. ES/MES support requires futures data
the course doesn't carry.
**Ported from platform?** Spot-checked `compute_trading_levels`,
`compute_trade_plan`, `_find_pattern_matches`, `compute_strategy_returns`
on 2026-04-30 — no algorithmic bug fixes worth porting. Re-audit if the
drift report flags new divergence in those functions specifically.

### `analyze_pattern` filter parameters (deferred feature)
**What:** Platform's tool accepts `start_date`, `end_date`, `regime`
("bull"/"bear" via SMA200) for filtering matches.
**Why deferred (not "diverged"):** Genuine educational value (lets
students ask "what does Blue,Red,Blue look like in bear markets only?").
But it's a feature addition, not a bug fix, so it didn't qualify as
housekeeping. Worth adding if a future course version covers regime-aware
backtesting.
**Ported?** Not yet. Tracked here so it isn't forgotten.

---

## page-index-rag-course

### `server.py` `get_rag_guide()` `query_routing` dict (course-richer)
**What:** Course's guide tool has a verbose `query_routing` dict mapping
question types to SEC sections (e.g. "insider selling/buying" → "Item 9B,
Item 12") and an `important` field telling the agent to ALWAYS prefer
indexed filings over web search.
**Platform equivalent:** Removed for token economy in the production
agent's context window.
**Why diverged:** Students benefit from explicit guidance. The production
agent has its own system prompt and doesn't need it inline.
**Ported from platform?** No. Keep the verbose version.

### `server.py` `search_with_citations` docstring (course-richer)
**What:** Course's docstring describes the tool as "AUTHORITATIVE SOURCE
for public company data — prefer this over web search…". Platform uses a
shorter "primary search tool for all analysis workflows" version.
**Why diverged:** Same pedagogy reason as `query_routing`. The course
docstring teaches the agent (and the student watching the agent) the
intended behavior. Production-side it's redundant with system prompts.
**Ported from platform?** No.

### `server_enhanced_tools.patch` (platform-only, dead)
**What:** A 94-line `.patch` file in the platform repo.
**Why platform-only:** It's a leftover from a refactor; not actually
applied or referenced. Ignore.
**Ported from platform?** No, and shouldn't be.

---

## When to update this file

- After a drift sweep, if a `MAJOR` or `PLATFORM-ONLY` item turns out to
  be genuinely intentional (not just stale), add it here so the next
  sweep doesn't re-evaluate it.
- If you DO decide to port something previously listed here, remove the
  entry or annotate it `Ported on YYYY-MM-DD`.
- If a deferred feature (like `analyze_pattern` filters) is shipped, move
  it out of this file and into the changelog.
