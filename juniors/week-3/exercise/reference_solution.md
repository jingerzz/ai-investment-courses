# Week 3: Reference Solution — Multi-Server Architecture

This reference shows a complete architecture for a school stock club.
Your design doesn't need to match, but should show similar thinking.

---

## Scenario

A school stock club with 10 members:
- 1 club president (manages everything)
- 3 research team members (study companies)
- 6 regular members (track stocks, follow along)

They track ~15 stocks, research companies, and want alerts for big moves.
Free data sources: Yahoo Finance, SEC EDGAR, StockAnalysis.com.

---

## Architecture: 2 Servers + Shared Code

```
Claude Desktop
     |
     ├── stock-server      (all members)
     └── research-server   (research team, president)
            |
       shared_utils.py     (common functions)
```

### Server 1: Stock Tracker

**Who uses it:** Everyone in the club
**Data source:** Yahoo Finance (yfinance)

| Tool | What It Does |
|------|-------------|
| `get_stock_snapshot` | Detailed view of one stock |
| `get_watchlist_summary` | Overview of all tracked stocks |
| `get_stock_comparison` | Compare two stocks side by side |
| `get_market_overview` | How the overall market is doing |
| `get_sector_check` | Which sectors are up and down |
| `get_report_formatted` | Pre-built daily report with exact numbers |
| `get_tracker_guide` | Describes all stock tracking tools |

**Key design decisions:**
- This server is read-only — it shows data, it doesn't buy or sell.
- All numbers are pre-computed so the AI doesn't do math.
- Includes the stale data warning from Week 2.

### Server 2: Research

**Who uses it:** Research team members, club president
**Data source:** Yahoo Finance (fundamentals), SEC EDGAR (filings)

| Tool | What It Does |
|------|-------------|
| `get_company_overview` | What the company does, how big it is, CEO |
| `get_financial_summary` | Revenue, earnings, and margins over 3 years |
| `get_competitor_comparison` | Compare two companies on key metrics |
| `search_filing` | Search a company's annual report for topics |
| `get_research_guide` | Describes all research tools |

**Why separate from stock tracker?**
- Different users: research team uses this a lot; regular members
  mostly just check prices.
- Different data: annual reports are large documents, not real-time
  prices.
- Different purpose: stock tracker answers "how is it doing right now?"
  while research answers "is this a good company?"

---

## Shared Code

**File:** `shared_utils.py`

```
get_stock_data(ticker)        — fetch current price via yfinance
get_company_info(ticker)      — fetch company details via yfinance
format_timestamp()            — consistent timestamps
handle_error(exception)       — consistent error messages
is_market_open()              — check if US market is open
stale_data_check()            — generate warning if market closed
```

**Why shared:**
- Both servers need stock prices. Fix it once, both benefit.
- Consistent timestamps and error messages everywhere.
- Same stale data logic for all tools.

**What stays server-specific:**
- Daily report formatting (stock server only)
- SEC filing search (research server only)
- Competitor comparison logic (research server only)

---

## Data Sources

| Source | What It Provides | What If It's Down? |
|--------|-----------------|-------------------|
| Yahoo Finance | Prices, fundamentals | Show error message, suggest checking StockAnalysis.com manually |
| SEC EDGAR | Annual reports | Show error message (no fallback for government filings) |
| StockAnalysis.com | Reference for checking data | Manual only — not used by code |

---

## Claude Desktop Config

Two servers, each running separately:

```json
{
  "mcpServers": {
    "stock-tracker": {
      "command": "uv",
      "args": ["run", "python", "stock_server.py"],
      "cwd": "/Users/you/ai-stock-tools"
    },
    "research": {
      "command": "uv",
      "args": ["run", "python", "research_server.py"],
      "cwd": "/Users/you/ai-stock-tools"
    }
  }
}
```

When Claude Desktop starts, it launches both servers. Claude sees tools
from both and picks the right one based on your question.

---

## Why Two Servers Instead of Three?

**We considered:** Adding a separate alerts server.

**We chose:** Two servers for now.

**Why:**
- The club is small (10 members). Keeping things simpler is better.
- Alerts can be added to the stock server later without much complexity.
- Two servers are easier to manage than three.
- If the club grows or alerts get complex, we can split later.

**The lesson:** Start simple. You can always add more servers later.
It's much harder to un-split servers than to split them.

---

## Cross-Server Questions That Should Work

| Question | Servers Used |
|----------|-------------|
| "How are our stocks doing today?" | Stock tracker |
| "Tell me about Nike as a company" | Research |
| "Give me a full report on Apple — stock and company" | Both |
| "Compare Tesla and Apple — both stock performance and fundamentals" | Both |
| "Which company on our watchlist has the best financials?" | Both |

This cross-referencing is the main benefit. Each server does one thing
well, and Claude connects them into a complete answer.
