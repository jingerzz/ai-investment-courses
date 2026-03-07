# Week 3 Exercise: Design a Multi-Server System

## What You'll Do

This week is different. Instead of building one more tool, you'll step back
and think about how to organize multiple MCP servers for your organization.
Then you'll use Claude to help design and build the architecture.

You'll use **Claude Desktop** for the design thinking and **Claude Code**
for building the result.

## Time: 30 minutes

## What You Need

- Claude Desktop
- Claude Code
- Your working server from Weeks 1-2
- The architecture template: `architecture_template.md`

---

## Step 1: Brainstorm with Claude Desktop (10 min)

Open Claude Desktop (not Claude Code) and have a design conversation.
This is about thinking, not building.

Try a prompt like:

```
I'm designing an AI tool system for my investment team. We currently have
one MCP server that tracks a stock watchlist and gives morning briefings.

I want to expand this into a multi-server system. Here's what our team does:
- [Describe your team's workflows — e.g., "We manage a portfolio of 30
  stocks across 6 sectors. Every morning we review positions, check risk
  limits, and look for new ideas."]
- [List the roles — e.g., "2 portfolio managers, 3 analysts, 1 risk
  manager"]
- [Mention data sources — e.g., "We use StockAnalysis.com for fundamentals,
  Yahoo Finance for prices, and read SEC filings"]

Help me think about:
1. What separate MCP servers would make sense?
2. What tools would each server have?
3. What should be shared across servers vs. server-specific?
4. Who needs access to what?
```

Claude Desktop will help you think through the architecture. Take notes or
use the architecture template.

**If you're not sure what to describe,** use this scenario:

```
I work at a mid-size investment firm. We manage equity portfolios.
Our main workflows are:
- Morning review: check positions, P&L, risk limits, market conditions
- Research: read SEC filings, analyze earnings, track investment theses
- Trading: evaluate opportunities, size positions, review trade ideas

We have portfolio managers, analysts, and a risk manager.
We use free data sources: Yahoo Finance, StockAnalysis.com, SEC EDGAR.
```

## Step 2: Fill In the Architecture Template (5 min)

Open `architecture_template.md` and fill in the sections based on your
conversation with Claude Desktop. You can do this by hand or ask Claude
Desktop to help:

```
Based on our conversation, can you fill in this template for me?
[Paste the template sections]
```

The key decisions to capture:
- **How many servers** and what each covers
- **What goes in a shared library** (things multiple servers need)
- **Data sources** with primary/fallback designation
- **Who accesses what** (not everyone needs every tool)

## Step 3: Build the Skeleton with Claude Code (10 min)

Now switch to Claude Code and have it build what you designed.

```bash
cd ~/ai-finance-tools
claude
```

Tell Claude Code:

```
I've designed a multi-server MCP system. I want you to build the
skeleton — the file structure and basic tools for each server.
Don't worry about full implementations yet, just the structure.

Here's what I need:

Server 1: [name] — [purpose]
  Tools: [list from your template]

Server 2: [name] — [purpose]
  Tools: [list from your template]

Server 3: [name] — [purpose] (if applicable)
  Tools: [list from your template]

Shared across all servers:
  - [list shared components]

Create each server as a separate .py file in my project folder.
Each server should have a get_[name]_guide tool that describes
its tools. Use yfinance for any market data.
```

Claude Code will create the file structure and basic implementations.

## Step 4: Connect and Test (5 min)

Ask Claude Code to help you connect multiple servers to Claude Desktop:

```
I now have multiple MCP servers. Can you update my Claude Desktop
config to include all of them? Show me what the config should look like
with multiple servers.
```

Then test in Claude Desktop:

```
What tools do I have available?
```

Claude should see tools from all your servers. Try asking a question that
requires tools from multiple servers:

```
Give me a morning briefing including risk analysis.
```

---

## What You Learned

- How to use Claude Desktop as a **thinking partner** for system design
- How to decompose a complex system into separate, focused servers
- The **shared library** pattern — what to centralize vs. keep separate
- How to connect **multiple MCP servers** to Claude Desktop
- That design thinking is YOUR job — Claude helps execute it

## Architecture Design Principles

These emerged from the reading, and you should see them in your design:

1. **One server per domain.** Portfolio analytics, risk, research — each
   gets its own server.
2. **Each server is independently deployable.** A bug fix in risk doesn't
   touch the signal server.
3. **Shared library for infrastructure.** Data access, auth, and common
   utilities are shared. Domain logic is not.
4. **Least privilege.** The research intern's Claude Desktop connects to
   the research server only, not the trading server.
5. **Guide tool per server.** Each server describes itself so the AI knows
   what it's working with.

## If You Get Stuck

- "I don't know how to split into servers" → Ask Claude Desktop:
  "Would it make sense to separate [X] from [Y]? What are the tradeoffs?"
- "Claude Code created too many files" → Ask it to simplify:
  "Can you consolidate servers 2 and 3? They're too similar to justify
  separate servers."
- "Multiple servers don't work in Claude Desktop" → Ask Claude Code to
  check the config format for you.
