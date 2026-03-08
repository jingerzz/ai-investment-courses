# Week 3 Exercise: Compose a Multi-Server System

## What You'll Do

You already have three MCP servers from Weeks 1-2. This week you'll
connect them all to Claude Desktop simultaneously and experience how
Claude routes questions across servers. Then you'll design how to
extend this into a production architecture.

## Time: 30 minutes

## What You Need

- Claude Desktop
- Claude Code
- Your three servers from Weeks 1-2:
  - `spy-tlt-course` (Week 1 — strategy signals and trade briefings)
  - `my-watchlist` (Week 2 — stock prices and morning briefings)
  - `page-index-rag` (Week 2 — SEC filing Q&A)

---

## Step 1: Connect All Three Servers (3 min)

If you haven't already, make sure all three servers are in your Claude
Desktop config:

**Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "spy-tlt-course": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/YOUR_USERNAME/ai-investment-courses/professional/servers/spy-tlt-course",
        "run",
        "spy-tlt-server"
      ]
    },
    "my-watchlist": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/YOUR_USERNAME/ai-investment-courses/professional/servers/my-watchlist",
        "run",
        "watchlist-server"
      ]
    },
    "page-index-rag": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/YOUR_USERNAME/ai-investment-courses/professional/servers/page-index-rag-course",
        "run",
        "rag-server"
      ]
    }
  }
}
```

Restart Claude Desktop completely. Verify you see tools from all three
servers (look for the hammer icon — it should show tools from each).

## Step 2: Cross-Server Queries (7 min)

Now ask questions that require Claude to use tools from multiple servers.
Watch which tools it calls and from which server.

**Strategy + watchlist:**
```
Refresh the SPY/TLT data, then give me today's signal and tell me how
my watchlist stocks are doing in the context of that signal.
```

Claude should call `refresh_data()` and `get_current_signal()` from
spy-tlt-course, then `get_watchlist_prices()` from my-watchlist. Watch
how it connects the regime signal to your individual stocks.

**Strategy + research:**
```
What's the current SPY/TLT signal? Given the regime, what risk factors
from BlackRock's latest 10-K should I be paying attention to?
```

Claude calls spy-tlt-course for the signal, then page-index-rag to
search BlackRock's filing for relevant risk factors. This is cross-
server synthesis — connecting market regime data with fundamental
research.

**All three:**
```
Give me a complete morning briefing: SPY/TLT signal, my watchlist
performance, and any relevant risk factors from my indexed SEC filings.
```

This is the full multi-server experience. Claude orchestrates across
all three servers to produce a briefing no single server could deliver.

**Notice what happens:**
- Claude picks the right server for each question without you telling it
- The guide tools help Claude understand what each server offers
- Cross-server synthesis produces analysis that's more valuable than
  any single server alone
- Each server stays focused on its domain

## Step 3: Identify Architecture Patterns (5 min)

Open the architecture template (`architecture_template.md`) and fill
it in based on what you just experienced. Or ask Claude Desktop:

```
I have three MCP servers running:
1. spy-tlt-course — strategy signals, trade briefings, pattern analysis
2. my-watchlist — stock prices, sector heatmap, morning briefings
3. page-index-rag — SEC filing search, document Q&A

Help me think about:
- What data is duplicated across servers? (e.g., SPY prices)
- What would a shared library look like for these three?
- If I added a 4th server (risk management), what would it do and
  what would it share with the others?
- Who on a team should have access to which servers?
```

The key decisions to capture:
- **Shared data:** Both spy-tlt and my-watchlist fetch from yfinance
  independently. In production, a shared data layer avoids duplicate
  fetches and ensures consistency.
- **Shared utilities:** CSV I/O, staleness detection, stale data
  warnings — all three servers implement these separately. A shared
  library would centralize this.
- **Access control:** An analyst might need all three. A compliance
  officer might only need page-index-rag. A risk manager needs risk
  tools (not yet built) plus watchlist data.

## Step 4: Add a Shared Data Pattern (10 min)

Use Claude Code to build a concrete improvement: make spy-tlt-course
and my-watchlist share a common data directory so they don't fetch
the same prices twice.

```bash
cd ~/ai-investment-courses/professional/servers/my-watchlist
claude
```

Tell Claude Code:

```
My watchlist server and the spy-tlt-course server both fetch SPY data
from yfinance independently. I want to add a simple shared data pattern:

1. Add a tool called get_spy_context() that reads SPY data from the
   spy-tlt-course server's CSV file at:
   ~/ai-investment-courses/professional/servers/spy-tlt-course/data/SPY-history.csv

2. It should return:
   - Latest SPY close and daily change %
   - Whether SPY is above/below its 50-day and 200-day SMAs
   - The data's date (to detect staleness)
   - data_source: "shared CSV (spy-tlt-course)"

3. Update get_morning_briefing() to use this shared SPY data instead
   of fetching it again from yfinance.

This simulates the shared storage pattern from the reading — multiple
servers reading from common data files.
```

Test in Claude Desktop:
```
Show me the SPY context from my watchlist server. Is it consistent
with what the SPY/TLT strategy server reports?
```

Both servers should show the same SPY data because they're reading
from the same source.

## Step 5: Design a Fourth Server (5 min)

Use Claude Desktop to design (not build) a risk management server:

```
I want to add a risk management server to my system. It should:
- Monitor position concentration (no single stock > 20% of portfolio)
- Track sector exposure (no sector > 35%)
- Check drawdown (alert if portfolio is down > 5% from peak)
- Provide a risk report that my morning briefing can reference

Given my existing servers (spy-tlt-course, my-watchlist, page-index-rag),
design the risk server:
- What tools would it have?
- What data does it need from the other servers?
- What should its guide tool say?
- What approval levels should different risk alerts have?
```

You don't need to build this — the design exercise itself teaches you
to think about server boundaries, data dependencies, and the guide
tool pattern.

---

## What You Learned

- How Claude **routes questions** across multiple servers automatically
- **Cross-server synthesis** produces analysis no single server can
- **Shared data patterns** avoid duplicate fetches and ensure consistency
- How to identify what belongs in a **shared library** vs. domain-specific
  server
- **Access control** design — who needs which servers
- How to **design new servers** that fit into an existing architecture

## Architecture Principles (from the reading)

1. **One server per domain.** Strategy, watchlist, research, risk —
   each gets its own server.
2. **Independently deployable.** A bug fix in the watchlist server
   doesn't touch the strategy server.
3. **Shared data, not shared code (yet).** Start with shared CSV files.
   Graduate to a shared library when duplication becomes painful.
4. **Guide tool per server.** Each server describes itself so Claude
   knows what it's working with across all connected servers.
5. **Least privilege.** Not everyone needs every server.

## If You Get Stuck

- **"Claude isn't using the right server"** — Check that all three
  servers appear in Claude Desktop's tools list. If a server isn't
  showing, check the config path and restart.
- **"Cross-server queries are slow"** — Each server starts its own
  Python process. First calls to each are slower (cold start). This is
  normal for stdio transport.
- **"Shared data file not found"** — Double-check the path to
  SPY-history.csv. Use an absolute path, not relative.
- **"I don't know how to fill in the template"** — Paste the template
  sections into Claude Desktop and ask it to fill them in based on
  your three servers.
