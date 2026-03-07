# Week 3: Conversation Guide

This week uses both Claude Desktop (for design) and Claude Code (for building).

---

## Design Conversations in Claude Desktop

### Starting the architecture brainstorm

```
I'm designing an AI tool system for my investment team. We currently have
a simple stock watchlist server. I want to expand to a full system.

Here's our team and workflow:
- [Your team description]
- [Your key workflows]
- [Your data sources]

Help me think about what separate MCP servers I should build. For each
server, suggest 5-7 tools it should have.
```

### Getting more specific about each server

```
Let's go deeper on the research server. Our analysts spend most of their
time reading SEC filings and earnings transcripts. What tools would help
them? Think about:
- Finding relevant sections in filings
- Comparing this quarter to last quarter
- Tracking investment theses over time
```

### Deciding what to share

```
I'm trying to decide what should be shared across all servers vs. specific
to one server. Here's my list — can you help me classify each one?

- Market data fetching (yfinance calls)
- Portfolio position data
- Risk limit calculations
- SEC filing parser
- Stock fundamentals lookup
- Authentication
```

### Evaluating tradeoffs

```
I'm debating whether to combine portfolio analytics and risk management
into one server, or keep them separate. What are the pros and cons?
Our risk manager needs to review risk independently of portfolio decisions.
```

---

## Building with Claude Code

### Creating the multi-server structure

```
I've designed a 3-server system. Create the file structure:

1. portfolio_server.py — Portfolio analytics (positions, P&L, sectors)
2. risk_server.py — Risk management (limits, concentration, drawdown)
3. research_server.py — SEC filing analysis and earnings data

Each server should:
- Use FastMCP
- Have a guide tool
- Have placeholder tools (just return sample data for now)
- Use yfinance for any market data needed

Also create a shared_utils.py with common functions like fetching
stock data and formatting timestamps.
```

### Fleshing out one server

```
Let's fully implement the risk_server.py. I want these tools:

1. get_risk_dashboard - Overall risk status (OK/WARNING/BREACH)
2. get_concentration_check - Largest positions as % of portfolio
3. get_sector_exposure - Portfolio weight by sector
4. get_risk_guide - Describes all risk tools

My portfolio is: [list your holdings and approximate weights]

Risk limits:
- No single stock > 20% of portfolio
- No sector > 35% of portfolio
- Flag any position that's within 5% of its limit
```

### Adding shared utilities

```
Both my portfolio server and risk server need to look up current
stock prices. Can you create a shared_utils.py file with a function
called get_stock_data(ticker) that both servers import? This way
I only have one place to change if I switch data providers.
```

### Connecting multiple servers to Claude Desktop

```
I now have 3 server files:
- ~/ai-finance-tools/portfolio_server.py
- ~/ai-finance-tools/risk_server.py
- ~/ai-finance-tools/research_server.py

Show me the exact Claude Desktop config JSON to add all three.
Each server needs its own entry in the config.
```

---

## Evaluating Your Design

After building, test these in Claude Desktop:

### Does Claude know what's available?

```
What tools do I have across all my servers?
```

### Can Claude route to the right server?

```
What are my biggest risk exposures right now?
(Should use risk server tools, not portfolio tools)
```

### Can Claude cross-reference servers?

```
Give me a morning briefing that covers my portfolio performance
AND my current risk status.
(Should use tools from multiple servers)
```

### Does the separation make sense?

```
I want to add a tool that checks if a proposed trade would breach
any risk limits. Which server should this go in?
(Good test: does your architecture have a natural home for this?)
```

---

## Tips for Week 3

1. **Design first, build second.** Spend the first 15 minutes thinking
   with Claude Desktop. The building goes fast once you know what you want.

2. **Two servers is fine.** Don't force a three-server architecture if two
   makes more sense. Simpler is better.

3. **Shared code prevents drift.** If two servers need the same data, put
   the data fetching in a shared file. Otherwise you'll fix a bug in one
   server and forget the other.

4. **Test cross-server questions.** The real power of multiple servers is
   when the AI combines data from different domains. Make sure this works.
