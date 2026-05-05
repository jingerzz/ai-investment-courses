---
name: spy-tlt-course
description: SPY/TLT color-day market regime classification and signal lookup for the AI Investing course (Week 1+). Invoke whenever the student asks "what kind of day is it?", "what's today's signal?", "what's the current regime?", or anything about SPY/TLT positioning, color days (Green/Orange/Blue/Red), exposure targets, or refreshing market data. Backed by the spy-tlt-course MCP server (14 tools) — must be registered with Zo before use. This is the course-edition server (no broker/futures/options); students who want the full 37-tool production server should follow the production track instead.
compatibility: Created for Zo Computer
metadata:
  author: jing.zo.computer
  course: zo-professional
  week: 1
---

# spy-tlt-course

Agent guidance for the **course edition** of the SPY/TLT strategy MCP server. The student installs and registers it via the `course-setup` skill; this skill explains how to use it once it's live.

## Server fingerprint

- **Server name (in Zo MCP registry):** `spy-tlt-course`
- **Tool count:** 14 (course subset of the 37-tool production server)
- **Source:** `professional/servers/spy-tlt-course/`
- **Entry point:** `uv run spy-tlt-server`
- **Data:** SPY + TLT daily prices via `yfinance`, cached locally

If the tool count isn't 14 or the server isn't registered, route the student back to the `course-setup` skill.

## When to invoke

The student is asking a question that requires a market-regime tool call — not narrative analysis. Examples:

- "What's today's signal?"
- "Are we in a Green day or Orange day?"
- "What's SPY doing right now?"
- "Is the strategy data fresh?"
- "Explain the current signal."

**Do not invoke** for: portfolio construction advice, trade execution, options strategy, or anything outside the SPY/TLT color-day framework. The course server is intentionally minimal.

## The 6-step workhorse pattern

Every SPY/TLT question follows this pattern. Memorize it:

1. `get_strategy_guide` — call ONCE per session, first thing. Tells you what this strategy actually does.
2. `refresh_data` — call before any market-data query. Pulls latest SPY + TLT prices.
3. `get_current_signal` — returns today's color (Green / Orange / Blue / Red) + exposure target + `stale_data_warning`. **Quote every field verbatim.**
4. `explain_signal` — call with the signal name from step 3. Returns the strategy's own explanation, not your interpretation.
5. `get_market_context` — SPY/QQQ/IWM/DIA/RSP extension and breadth. Use when the student asks "is the market healthy?" or for cross-index context.
6. Cite the tool call when you answer. Format: `(via spy-tlt-course / get_current_signal)`.

## Critical rules

- **Quote tool output verbatim before interpreting.** Phantom prices — numbers from training memory dressed up as "the latest" — are the failure mode this course is designed to break. If you can't name the tool call you got a number from, don't say the number.
- **Pass through `stale_data_warning` even when `null`.** The student needs to see that field to learn the discipline.
- **Color days are exclusive — pick one, no hedging.** "It's a Green day" not "it's Green-leaning."
- **Refresh before reading.** If the cached prices are >1 trading day old, `get_current_signal` may report a stale regime. `refresh_data` first, then `get_current_signal`.

## Tools at a glance

| Tool | Purpose |
| --- | --- |
| `get_strategy_guide` | Strategy overview — call first in a session. |
| `refresh_data` | Pull latest SPY + TLT prices. Run before any data query. |
| `get_current_signal` | Today's color + exposure target + freshness warning. |
| `explain_signal` | Plain-English explanation of a named signal. |
| `get_market_context` | SPY/QQQ/IWM/DIA/RSP extension + breadth snapshot. |
| `get_equity_quote` | Single-ticker latest quote. |
| `get_equity_snapshot` | Single-ticker richer snapshot (price, range, volume). |
| `get_daily_series` | Daily OHLC with SMA20/50/200 overlays. |
| `get_levels` | Key support/resistance levels for SPY/TLT. |
| `get_pattern` | Identified chart patterns. |
| `run_backtest` | Backtest the color-day strategy over a window. |
| `get_briefing` | Daily market briefing — synthesized output. |
| `get_signal_history` | Recent N days of color-day classifications. |
| `get_help` | Catalog of available tools and their args. |

## Course context

This is the **Week 1** centerpiece. The reading at `zo-professional/week-1/reading.md` motivates *why* tool-grounded answers beat phantom answers from training memory; the exercise at `zo-professional/week-1/exercise/README.md` walks the student through the 6-step pattern above.

Production divergence: the production server has 37 tools (futures, options, broker risk, live account integration). Those are intentionally excluded from the course — see `zo-professional/SERVER_CONTEXT.md` and `docs/intentional_divergence.md` on `origin/main` for the full divergence registry.
