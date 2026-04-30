# Course MCP Servers vs. Production Servers

A side-by-side comparison of what students get in the course versus what
runs in the private production stack at `Clarion-trading-platform`. The
course is intentionally a subset — every "missing" capability listed
here is missing on purpose, almost always because it depends on a paid
broker account, a live data feed, or operational infrastructure that
doesn't belong in a student environment.

Last updated: 2026-04-30.

---

## At a glance

| Server | Course tools | Production tools | What you give up | What's the same |
|--------|-------------:|-----------------:|------------------|-----------------|
| **SPY/TLT strategy** | 14 | 37 | ES/MES/ZB futures, options, real-broker risk, multi-bar series tools, breadth regime | Strategy core (signals, levels, patterns, backtest, briefings, SPY history) |
| **SEC RAG** | 14 | 14 | Passphrase auth (off by default), `trading_core` integration | All retrieval, indexing, parsing, search, embeddings, fetcher |
| **Single stock strategy** | 0 (not shipped) | 21 | Per-stock signals, portfolio risk, options ideas | n/a |

The headline: **the course is roughly equivalent to production for SEC
RAG, a teaching subset for the SPY/TLT strategy, and silent on the
single-stock product.**

---

## SPY/TLT strategy — 14 / 37 tools

The course version (`spy-tlt-course`) ships 14 tools focused on
strategy concepts that don't require a broker. Production
(`spy-tlt-strat`) layers on three categories of tools that need
tastytrade live data + the `trading-core` workspace package.

### What's in BOTH (10 — the strategy core)

| Tool | What it does |
|------|--------------|
| `get_strategy_guide(topic)` | Orientation tour |
| `get_current_signal()` | Today's color, signal, exposure target |
| `get_recent_history(days)` | Last N days of signals + actions |
| `get_signal_list()` | All 9 strategy signals by tier |
| `explain_signal(name)` | Detailed breakdown of one signal |
| `get_backtest_summary(start, end)` | CAGR, Sharpe, drawdown vs SPY B&H |
| `get_trading_levels(days)` | SPY pivots, S/R, SMAs, ATR(14) |
| `get_trade_briefing()` | Pre-formatted morning briefing |
| `analyze_pattern(sequence)` | Forward returns for a color sequence |
| `refresh_data()` | Pull fresh prices |

### What's COURSE-ONLY (4 — SPY-history teaching tools)

These are wrapper-style tools that turn the same underlying data into
self-contained "what does SPY do historically" answers. They're useful
in the classroom because they don't require any setup beyond yfinance.

| Tool | What it does |
|------|--------------|
| `spy_extreme_moves(top, threshold)` | Biggest gains/drops, distribution |
| `spy_streaks()` | Win/loss streaks, what happens next |
| `spy_seasonal()` | Day-of-week, monthly, yearly patterns |
| `spy_summary(...)` | All three combined |

(Production exposes the same four under a slightly different shape.)

### What's PRODUCTION-ONLY (23 — broker / futures / options)

Everything in this group requires either tastytrade live data, a real
account, or the `trading-core` package — none of which the course
ships. This is intentional: students should be able to follow the
curriculum end-to-end with no API keys.

**ES/MES futures (9):** `get_es_levels`, `get_es_trade_plan`,
`get_es_signal`, `get_es_session`, `get_es_history`, `get_es_intraday`,
`get_es_bars`, `get_volume_profile`, `get_short_signals`.

**ZB/ZN bond futures (4):** `get_zb_levels`, `get_zb_session`,
`get_bond_equity_correlation`, `get_zb_trade_plan`.

**Options (2):** `get_option_expirations`, `get_option_chain`.

**Risk & sizing (3):** `get_directional_bias`, `get_risk_report`,
`get_position_size`.

**General equities & breadth (5):** `get_daily_series`,
`get_equity_snapshot`, `get_equity_quote`, `get_equity_intraday`,
`get_market_context` (with RSP/SPY breadth regime).

### Why the course doesn't include any of these

| Reason | Affects |
|--------|---------|
| Requires a paid tastytrade account | All 23 production-only tools |
| Requires `trading-core` workspace package | All 23 |
| Requires live ES/MES/ZB futures data | 13 |
| Requires options chain feed | 2 |
| Requires real broker positions for sizing | 3 |
| Adds 30+ minutes of setup before lesson 1 | All |

If you want to teach futures or options, the platform is the right
target — but only after a student has graduated past "Claude can call
MCP tools" into "Claude can manage real money".

---

## SEC RAG — 14 / 14 tools

This is the case where course and production are essentially
**equivalent**. Both expose the same 14 tools with the same signatures
and behavior. The differences are operational, not capability-driven.

### What's in BOTH (all 14)

**Filing lifecycle (5):**
`check_company_indexed`, `fetch_company_filings`,
`fetch_company_filings_enhanced`, `check_indexing_status`,
`check_filings_available`.

**Search and retrieval (4):**
`search_with_citations`, `get_document_overview`,
`get_document_section`, `batch_query`.

**Indexing utilities (3):**
`ingest_drop_folder`, `remove_document`, `embed_documents`.

**Inventory (2):**
`list_documents`, `get_rag_guide`.

### Subtle differences (none affect what students can do)

| Item | Course | Production | Why |
|------|--------|-----------|-----|
| Default Ollama model | `qwen3.5:0.8b` (small, fast) | `gemma4:e2b` (better quality) | Student hardware varies; small model loads on a laptop |
| LLM backend | Ollama by default; Anthropic available | Same code path | New as of 2026-04-30 |
| Passphrase on write tools | Optional, off by default | Same code, used in cloud deploys | Hosted demo can be locked; local stays open |
| `get_rag_guide()` content | Verbose `query_routing` dict + "always check filings first" instruction | Trimmed for context efficiency | Course teaches; production agent has system prompt |
| `search_with_citations` docstring | Long, pedagogical | Short | Same reason |

These are configuration differences. The actual retrieval engine,
parser pipeline, indexer, embeddings module, and SEC fetcher are the
**same code on both sides** as of 2026-04-30.

### Why the course tracks production so closely here

SEC RAG has no broker dependency — the only external service is SEC
EDGAR (free + public) and a local Ollama (free + open-source). So the
production-vs-course gap that exists for the trading strategy doesn't
exist here. Students can reproduce essentially the production
experience locally.

---

## Single-stock strategy — 0 / 21 tools

Production ships a third MCP server (`single-stock-strat`) covering
nine individual stocks (AAPL, MSFT, NVDA, JPM, XOM, etc.) with
per-ticker signals, technicals, options ideas, and portfolio risk.

**The course does not include this server.** Students learn the MCP
patterns through SPY/TLT and SEC RAG; the per-stock signal universe
would inflate the course without adding new technical concepts.

If a future course version teaches "scaling MCP servers across many
tickers", this is the natural template.

---

## What this means for the classroom

- **For the trading strategy unit:** students learn the same signal
  vocabulary, the same backtest mechanics, the same morning briefing
  flow as the live system. They just can't trade futures or options
  through it. That's a feature, not a bug.
- **For the SEC RAG unit:** what students build is what production
  runs, period. The same `search_with_citations` invocation will
  return functionally identical results.
- **For investing strategy more broadly:** the course intentionally
  stops at "you can analyze and reason about positions"; production
  goes the rest of the way to "you can size, risk, and execute".

---

## Keeping this document honest

This file is regenerated by hand whenever the drift report
(`docs/drift-report.md`) flags new MAJOR or PLATFORM-ONLY entries that
change what the course can do. The drift detector itself
(`scripts/check_drift.py`) doesn't update this file — that requires a
human judgment call about whether a platform addition is "a new
capability students should know about" or "yet another broker-specific
plumbing tool that doesn't belong in the curriculum."

When in doubt, see `docs/intentional_divergence.md` for the canonical
list of "course differs by design — don't port".
