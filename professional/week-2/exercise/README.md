# Week 2 Exercise: Build Your Own MCP Server + Set Up Document Q&A

## What You'll Do

**Part A** — Use Claude Code to build a working MCP server from scratch.
You'll describe tools in English and iterate until you have a server
that answers questions about a stock watchlist with real market data.

**Part B** — Install the page-index-rag server and Ollama to run local
AI for SEC filing analysis. You'll query pre-indexed BlackRock and
Robinhood filings from Claude Desktop.

## Time: 30 minutes (20 + 10)

## What You Need

- Claude Code installed (see [Week 1 setup](../week-1/exercise/README.md#recommended-let-claude-code-handle-setup))
- Claude Desktop installed
- A terminal application
- `uv` installed (from Week 1)

---

# Part A: Build a Watchlist Server with Claude Code (20 min)

## Step 1: Create a New Project (2 min)

```bash
mkdir ~/ai-investment-courses/professional/servers/my-watchlist
cd ~/ai-investment-courses/professional/servers/my-watchlist
```

Open Claude Code:
```bash
claude
```

Tell Claude Code to set up the project:

```
Create a new MCP server project using FastMCP. I want:

- Python package using uv, named "my-watchlist"
- Dependencies: mcp>=1.20.0, yfinance>=0.2.0, pandas>=2.0.0
- Entry point: watchlist-server = "my_watchlist.server:main"
- A basic server.py that imports FastMCP and creates a server named
  "my-watchlist"

Use the same project structure as the spy-tlt-course server in
~/ai-investment-courses/professional/servers/spy-tlt-course/ for
reference.
```

After Claude Code creates the files, install:
```bash
uv sync
```

## Step 2: Add Your First Tools (5 min)

Now tell Claude Code to add tools. Be specific about what each tool
returns — this is how you get good docstrings and return contracts.

```
Add these tools to my server. Pre-compute everything — the AI should
never need to do math. All tools return dicts, never raise. Use an
"error" field for failures. Include "data_source" and
"stale_data_warning" fields in every return.

1. get_watchlist_prices(tickers: list[str] = None)
   Returns current price, daily change %, and 50-day SMA for a default
   watchlist: AAPL, MSFT, NVDA, AMZN, GOOGL.
   If tickers are provided, use those instead.
   Flag any stock that moved more than 2% today as "notable".
   Sort by daily return, worst to best.

2. get_market_overview()
   Returns how the major indices are doing: SPY, QQQ, DIA, IWM.
   Include daily change % and whether each is above or below its
   50-day moving average. Add a simple regime label: "risk-on" if
   SPY is up and above 50-day SMA, "risk-off" if SPY is down and
   below 50-day SMA, "mixed" otherwise.

3. get_sector_heatmap()
   Returns the 11 S&P sectors (XLK, XLF, XLE, XLV, XLI, XLY, XLP,
   XLU, XLRE, XLC, XLB) with today's performance. Sort best to worst.
   Flag any sector up or down more than 1.5%.

Use yfinance for all data. Fetch fresh data on each call (no caching
needed for now).
```

Test the server:
```
Can you run the MCP inspector so I can test these tools?
```

Try calling each tool in the inspector. Check that:
- Prices look correct
- Daily changes are reasonable
- The regime label makes sense
- Stale data warnings appear when the market is closed

## Step 3: Add a Pre-Formatted Briefing (5 min)

This is the key guardrail pattern from the reading. Tell Claude Code:

```
Add a tool called get_morning_briefing() that:

1. Calls the other tools internally to gather all data
2. Builds a pre-formatted markdown section with exact numbers:
   - Market regime status and index performance table
   - Sector heatmap (sorted, with notable sectors flagged)
   - Watchlist table: ticker, price, daily change %, above/below 50d SMA
3. Returns the formatted markdown in a "formatted_section" field
4. Returns "present_verbatim": true
5. Returns "ai_interpretation_notes" with plain English key points
   the AI should elaborate on (e.g., "NVDA is the biggest mover,
   and Technology is the strongest sector — these are related")

The docstring should say: "Returns a pre-formatted morning briefing.
Present the formatted_section verbatim — do not reformat, round, or
recalculate any numbers. Use ai_interpretation_notes for additional
context."
```

Test in the inspector. The formatted section should be clean markdown
with exact numbers.

## Step 4: Add a Guide Tool (3 min)

```
Add a get_guide() tool that returns:
- A list of all tools with one-line descriptions
- A recommended morning briefing workflow:
  1. get_market_overview → understand the environment
  2. get_sector_heatmap → see where money is flowing
  3. get_watchlist_prices → how my stocks are doing in context
  4. get_morning_briefing → get the complete pre-formatted summary
- Rules:
  - "ALWAYS present formatted_section verbatim when present_verbatim
    is true. Do not reformat or recalculate numbers."
  - "If stale_data_warning is not null, display it prominently."
  - "Do NOT compute aggregate returns by adding individual percentages."
```

## Step 5: Connect to Claude Desktop and Test (5 min)

Add your new server to Claude Desktop's config. Open:

**Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Add your server alongside the SPY/TLT server (keep both):

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
    }
  }
}
```

Restart Claude Desktop completely (quit and reopen). Then try:

```
Give me my morning briefing.
```

Check the output against the guardrail checklist:

- [ ] Pre-formatted section appears with exact numbers (not rounded)
- [ ] Market regime is labeled and explained
- [ ] Cross-references between sector and stock performance
- [ ] Stale data warning appears if market is closed

Now try a tricky prompt:

```
What's my portfolio's total return today?
```

If the AI adds up individual stock returns (mathematically wrong —
percentages don't add across different position sizes), that's a
guardrail gap. Tell Claude Code:

```
The AI is calculating total return by adding individual stock returns,
which is wrong. Add an "avg_daily_return" field to get_watchlist_prices
that computes the equal-weight average return. That way the AI uses the
pre-computed number.
```

Rebuild, restart Claude Desktop, and verify the fix.

---

# Part B: Set Up Page-Index-RAG for SEC Filing Q&A (10 min)

## Step 1: Install Ollama (3 min)

**Mac:**
```bash
brew install ollama
```

**Windows:** Download from [ollama.com/download](https://ollama.com/download)

Start Ollama and pull the course model:
```bash
ollama serve &
ollama pull qwen3.5:0.8b
```

Verify it works:
```bash
ollama run qwen3.5:0.8b "What is a 10-K filing?"
```

You should get a brief answer. The quality won't match Claude — that's
expected. The local model handles document search; Claude Desktop does
the reasoning. Press `Ctrl+D` to exit.

## Step 2: Install the Page-Index-RAG Server (3 min)

The page-index-rag server is included in your course materials with
pre-indexed SEC filings for BlackRock (BLK) and Robinhood (HOOD).

```bash
cd ~/ai-investment-courses/professional/servers/page-index-rag-course
uv sync
```

The server comes with 7 pre-indexed filings:
- BLK 10-K (annual report, Feb 2026)
- BLK 10-Q × 2 (quarterly reports, 2025)
- HOOD 10-K (annual report, Feb 2026)
- HOOD 10-Q × 3 (quarterly reports, 2025)

No fetching or indexing needed — you can start querying immediately.

## Step 3: Connect to Claude Desktop (2 min)

Add the page-index-rag server to your Claude Desktop config:

```json
{
  "mcpServers": {
    "spy-tlt-course": { "...": "..." },
    "my-watchlist": { "...": "..." },
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

Restart Claude Desktop.

## Step 4: Query SEC Filings (2 min)

Open a new conversation in Claude Desktop and try these prompts:

**Basic document Q&A:**
```
What documents do you have indexed?
```

Claude calls `list_documents()` and shows the 7 available filings.

**Section navigation:**
```
Show me the table of contents for BlackRock's latest 10-K.
```

Claude calls `get_document_overview()` and displays the filing's
hierarchical structure — the same tree structure described in the
reading.

**Targeted question:**
```
What are BlackRock's main risk factors related to market volatility?
```

Claude calls `search_with_citations()` to find the relevant section,
then `get_document_section()` to read the full text. Notice the
citation — it tells you exactly which section the answer came from.

**Cross-company comparison:**
```
Compare Robinhood's and BlackRock's revenue growth in their most
recent annual reports.
```

Claude calls `batch_query()` to search both companies' 10-Ks
simultaneously, then synthesizes the comparison.

---

## What You Learned

- How to **build an MCP server from scratch** by describing tools to
  Claude Code in English
- The **pre-formatted template** pattern: Python builds the briefing,
  the AI presents it verbatim
- The **stale data warning** pattern: tools tell the AI when data isn't
  fresh
- How to **find and fix guardrail gaps** through iterative testing
- How to **install Ollama** and run local AI models for document search
- How **structure-first RAG** preserves document hierarchy for
  citation-grade answers on SEC filings
- The **hybrid approach**: local models for search, cloud models for
  reasoning

## If You Get Stuck

**Claude Code isn't generating working code:**
- Paste the error message back to Claude Code — it can usually fix it
- Make sure you ran `uv sync` after the initial project setup

**"Tool call failed" in Claude Desktop:**
- Check the path in `claude_desktop_config.json` — most errors are
  wrong paths
- Verify the server starts: `cd` into the directory and run
  `uv run watchlist-server`

**Ollama is slow or not responding:**
- Make sure `ollama serve` is running in the background
- The `qwen3.5:0.8b` model should respond in 2-5 seconds. If it's
  much slower, your machine may need the even smaller model or more RAM

**page-index-rag errors:**
- Make sure Ollama is running (`ollama serve`)
- Check that the model is downloaded: `ollama list` should show
  `qwen3.5:0.8b`

## Next Week

In Week 3, you'll learn about **system design** — how MCP servers
compose into larger systems, how to handle state across conversations,
and how to design multi-server architectures. You'll also explore
testing strategies and deployment patterns for production use.
