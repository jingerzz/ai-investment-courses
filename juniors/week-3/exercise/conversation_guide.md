# Week 3: Conversation Guide

This week uses both Claude Desktop (for design) and Claude Code
(for building).

---

## Design Conversations in Claude Desktop

### Starting the brainstorm

```
I'm designing an AI tool system for a school stock club. We currently
have a stock tracker server. I want to expand to a full system.

Our club:
- Tracks stocks of companies we like
- Researches companies by reading annual reports
- Wants alerts for big price moves
- Does weekly presentations on stock picks

Help me think about what separate servers I should build. For each
server, suggest 4-5 tools it should have.
```

### Going deeper on one server

```
Let's go deeper on the research server. Our members want to compare
companies and understand what makes them successful or risky. What
tools would help? Think about:
- Looking up company basics (revenue, employees, what they do)
- Comparing two companies side by side
- Reading through annual reports for specific topics
```

### Deciding what to share

```
I'm trying to decide what should be shared across all servers vs.
specific to one server. Here's my list — can you help me sort it?

- Stock price lookup
- Company fundamentals
- SEC filing search
- Alert trigger logic
- Market open/closed check
- Error message formatting
```

### Evaluating tradeoffs

```
Should I combine stock tracking and alerts into one server, or keep
them separate? What are the pros and cons? Our club president manages
alerts but regular members just check stock prices.
```

---

## Building with Claude Code

### Creating the multi-server structure

```
I've designed a 2-server system. Create the file structure:

1. stock_server.py — Stock tracking (prices, watchlist, comparisons,
   daily report)
2. research_server.py — Company research (fundamentals, competitor
   comparison, SEC filing search)

Each server should:
- Use FastMCP
- Have a guide tool
- Use yfinance for market data

Also create a shared_utils.py with common functions like fetching
stock data and checking if the market is open.
```

### Building out one server

```
Let's fully implement the research_server.py. I want these tools:

1. get_company_overview - Basic info about a company (what they do,
   how big they are, CEO, number of employees)
2. get_financial_summary - Revenue and earnings for the last 3 years
3. get_competitor_comparison - Compare two companies on key metrics
4. get_research_guide - Describes all the research tools

Use yfinance for the data. Pre-compute everything. Include data_source
and as_of fields in every return.
```

### Connecting multiple servers to Claude Desktop

```
I have two server files:
- ~/ai-stock-tools/stock_server.py
- ~/ai-stock-tools/research_server.py

Show me the exact Claude Desktop config to add both servers.
```

---

## Testing in Claude Desktop

### Does Claude see everything?

```
What tools do I have across all my servers?
```

### Does Claude pick the right server?

```
How is Roblox's stock doing today?
(Should use stock server)

Tell me about Roblox as a company — what do they do?
(Should use research server)
```

### Can Claude combine servers?

```
Give me a full overview of Roblox — both how the stock is doing
and what the company looks like fundamentally.
(Should use tools from both servers)
```

---

## Tips for Week 3

1. **Design first, build second.** Spend the first half thinking with
   Claude Desktop. Building goes fast once you know what you want.

2. **Two servers is fine.** Don't force three servers if two makes
   more sense. Simpler is better.

3. **Shared code prevents problems.** If two servers need the same
   data, put it in a shared file. Otherwise you'll fix a bug in one
   and forget the other.

4. **Test cross-server questions.** The real power is when Claude
   combines data from different servers. Make sure this works.
