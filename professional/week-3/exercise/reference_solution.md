# Week 3: Reference Solution — Multi-Server Architecture

This reference shows a complete architecture for a small equity investment
team. Compare your design against it — yours doesn't need to match, but
should show similar thinking.

---

## Scenario

A 6-person equity investment team:
- 2 portfolio managers
- 3 research analysts
- 1 risk manager

They manage a concentrated portfolio of ~30 US stocks across sectors.
Free data sources only: Yahoo Finance, StockAnalysis.com, SEC EDGAR.

---

## Architecture: 3 Servers + Shared Utilities

```
Claude Desktop
     |
     ├── portfolio-server    (PMs, risk manager)
     ├── risk-server          (risk manager, PMs)
     └── research-server      (analysts, PMs)
             |
        shared_utils.py      (common data fetching)
```

### Server 1: Portfolio Analytics

**Who uses it:** Portfolio managers, risk manager
**Data source:** Yahoo Finance (yfinance)
**Update cadence:** Real-time during market hours

| Tool | Purpose |
|------|---------|
| `get_portfolio_summary` | Total value, daily P&L, position count |
| `get_position_detail` | Deep-dive on a single position |
| `get_sector_breakdown` | Portfolio weights by sector |
| `get_top_movers` | Best and worst performers today |
| `get_performance_history` | Portfolio return over 1w, 1m, 3m, YTD |
| `preview_trade_impact` | What happens to weights if I buy/sell X |
| `get_portfolio_guide` | Describes all tools and flows |

**Key design decisions:**
- This server is read-only. It shows positions and P&L but doesn't
  execute trades. The `preview_trade_impact` tool answers "what if?"
  without actually doing anything.
- All returns include pre-computed values so the AI doesn't do math.

### Server 2: Risk Management

**Who uses it:** Risk manager, portfolio managers
**Data source:** Yahoo Finance + portfolio positions (from shared data)
**Update cadence:** Real-time during market hours

| Tool | Purpose |
|------|---------|
| `get_risk_dashboard` | Overall status: OK / WARNING / BREACH |
| `get_concentration_check` | Single-name and sector limits |
| `get_correlation_matrix` | How positions move together |
| `get_drawdown_status` | Current drawdown vs. limit |
| `get_liquidity_check` | Which positions would be hard to sell |
| `get_risk_guide` | Describes all tools and alert levels |

**Why separate from portfolio?**
- Risk manager needs independent access. They should review risk without
  seeing trade ideas or portfolio commentary.
- Different mental model: portfolio server answers "how am I doing?"
  while risk server answers "am I in danger?"
- If the portfolio server has a bug, risk monitoring keeps working.

### Server 3: Research

**Who uses it:** Analysts, portfolio managers
**Data source:** SEC EDGAR (filings), Yahoo Finance (fundamentals)
**Update cadence:** On-demand (when analyst asks)

| Tool | Purpose |
|------|---------|
| `get_company_overview` | Key fundamentals, description, sector |
| `get_financial_summary` | Revenue, earnings, margins (multi-year) |
| `get_competitor_comparison` | Compare fundamentals vs. peers |
| `fetch_sec_filing` | Download and index a 10-K or 10-Q |
| `search_filing` | Query a specific filing for information |
| `get_analyst_consensus` | Ratings, price targets, estimate trends |
| `get_research_guide` | Describes all tools and research flows |

**Why separate from portfolio?**
- Different users: analysts use this daily; PMs use it occasionally.
- Different data: SEC filings are large documents, not real-time prices.
- Different cadence: research is on-demand; portfolio is real-time.

---

## Shared Utilities

**File:** `shared_utils.py`

What goes here:

```
get_stock_data(ticker)        — fetch current quote via yfinance
get_historical_bars(ticker)   — fetch daily OHLCV data
format_timestamp()            — consistent ISO timestamps
handle_error(exception)       — consistent error dict format
is_market_open()              — check if US market is in session
stale_data_check()            — generate warning if market closed
```

**Why shared:**
- Portfolio and risk servers both need stock quotes. If the yfinance API
  changes, fix it in one place.
- Consistent timestamps and error formats across all servers.
- Stale data logic is identical everywhere.

**What stays server-specific:**
- Risk limit definitions and breach detection (risk server only)
- SEC filing parsing (research server only)
- Trade impact simulation (portfolio server only)

---

## Data Sources

| Source | Type | Used By | Fallback |
|--------|------|---------|----------|
| Yahoo Finance | Prices, fundamentals | All servers | StockAnalysis.com (manual lookup) |
| SEC EDGAR | Company filings | Research server | None (it's the primary source) |
| StockAnalysis.com | Screener, ratings | Research server | Yahoo Finance |

**Staleness handling:** All servers use the shared `stale_data_check()`
function to detect if the market is closed and add warnings.

---

## Claude Desktop Config

Three servers, each running as a separate process:

```json
{
  "mcpServers": {
    "portfolio": {
      "command": "uv",
      "args": ["run", "python", "portfolio_server.py"],
      "cwd": "/Users/you/ai-finance-tools"
    },
    "risk": {
      "command": "uv",
      "args": ["run", "python", "risk_server.py"],
      "cwd": "/Users/you/ai-finance-tools"
    },
    "research": {
      "command": "uv",
      "args": ["run", "python", "research_server.py"],
      "cwd": "/Users/you/ai-finance-tools"
    }
  }
}
```

When Claude Desktop starts, it launches all three servers. Claude can see
tools from all of them and routes to the right server based on the question.

---

## Trade-off: Two Servers vs. Three

**We considered:** Combining portfolio and risk into one server (fewer
moving parts, simpler config).

**We chose:** Separate servers.

**Why:**
- The risk manager needs to review risk independently
- Different failure domains — portfolio bug shouldn't affect risk monitoring
- Access control: junior analysts get research only, not portfolio data

**The cost:** Three config entries instead of two. Three processes running.
This is a small price for the independence and access control benefits.

---

## Cross-Server Questions That Should Work

Once all three servers are connected, Claude Desktop should handle:

| Question | Servers Used |
|----------|-------------|
| "Morning briefing with risk check" | Portfolio + Risk |
| "Research AAPL and check how it fits my portfolio" | Research + Portfolio |
| "Am I over-concentrated in tech?" | Risk + Portfolio |
| "Compare my NVDA position against its latest 10-K" | Portfolio + Research |

This cross-referencing across servers is the main benefit of the multi-server
architecture. Each server does one thing well, and the AI connects them.
