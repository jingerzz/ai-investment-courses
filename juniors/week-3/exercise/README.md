# Week 3 Exercise: Design a Multi-Server System

## What You'll Do

This week is different. Instead of building one more tool, you'll step
back and think about how to organize multiple servers. Then you'll use
Claude to help design and build the system.

You'll use **Claude Desktop** for thinking and **Claude Code** for
building.

## Time: 30 minutes

## What You Need

- Claude Desktop
- Claude Code
- Your working server from Weeks 1-2
- The architecture template: `architecture_template.md`

---

## Step 1: Brainstorm with Claude Desktop (10 min)

Open Claude Desktop (not Claude Code) and have a design conversation.
This is about thinking, not building yet.

Try a prompt like:

```
I'm designing an AI tool system for a school stock club. We currently
have one server that tracks stocks and gives daily reports.

I want to expand this into a multi-server system. Here's what our
club does:
- We track a watchlist of stocks we're interested in (Apple, Nike,
  Disney, Tesla, Netflix, and others)
- We research companies by reading their annual reports and comparing
  competitors
- We want alerts when stocks make big moves or have unusual volume
- We do weekly presentations on our top picks

Help me think about:
1. What separate servers would make sense?
2. What tools should each server have?
3. What should be shared across servers?
4. Who in the club needs access to what?
```

Claude Desktop will help you think through the design. Take notes or
use the architecture template.

**If you want a different scenario,** make one up:

```
I'm building an AI system for tracking my favorite sports teams'
business performance. I want to track their parent companies' stocks,
research their financial health, and get alerts when news breaks.
Help me design the server architecture.
```

## Step 2: Fill In the Architecture Template (5 min)

Open `architecture_template.md` and fill in the sections based on your
conversation with Claude Desktop. You can ask Claude Desktop to help:

```
Based on our conversation, can you fill in this template for me?
[Paste the template sections]
```

The key decisions to capture:
- **How many servers** and what each one does
- **What goes in a shared file** (things multiple servers need)
- **Data sources** and what happens if they're unavailable
- **Who needs access** to which server

## Step 3: Build the Skeleton with Claude Code (10 min)

Now switch to Claude Code and have it build what you designed.

```bash
cd ~/ai-stock-tools
claude
```

Tell Claude Code:

```
I've designed a multi-server system. I want you to build the basic
structure — the files and starter tools for each server.

Server 1: stock-tracker — prices, watchlist, comparisons
  Tools: get_stock_snapshot, get_watchlist_summary, get_stock_comparison,
         get_market_overview, get_report_formatted, get_tracker_guide

Server 2: research — company info, SEC filings, competitor comparison
  Tools: get_company_overview, get_financial_summary,
         get_competitor_comparison, get_research_guide

Shared file (shared_utils.py):
  - Stock price lookup (so both servers use the same data function)
  - Market open/closed check
  - Stale data warning generator
  - Error handling

Create each server as a separate .py file. Each server should have
a guide tool. Use yfinance for market data.
```

Claude Code will create the files and basic tools.

## Step 4: Connect and Test (5 min)

Ask Claude Code to connect everything to Claude Desktop:

```
I now have multiple MCP servers. Can you update my Claude Desktop
config to include all of them? Show me the config with both servers.
```

Then test in Claude Desktop:

```
What tools do I have available?
```

Claude should see tools from all servers. Try a cross-server question:

```
Tell me about Apple — how is the stock doing today and what do we
know about the company?
```

Claude should use tools from both servers to answer.

---

## What You Learned

- How to use Claude Desktop as a **thinking partner** for design
- How to split a system into separate, focused servers
- The **shared file** pattern — what to centralize vs. keep separate
- How to connect **multiple servers** to Claude Desktop
- That **design is your job** — Claude helps you think and build, but
  the architecture decisions are yours

## Design Principles

These should show up in your design:

1. **One server per topic.** Stock tracking, research, alerts — each
   gets its own server.
2. **Each server works independently.** A bug in research doesn't
   break stock tracking.
3. **Shared code for shared needs.** Data fetching and utilities are
   shared. Domain-specific logic is not.
4. **Guide tool per server.** Each server describes itself so the AI
   knows what it has available.

## If You Get Stuck

- "I don't know how to split into servers" — Ask Claude Desktop:
  "Would it make sense to separate stock tracking from research?
  What are the pros and cons?"
- "Claude Code created too many files" — Ask it to simplify:
  "Can you combine servers 2 and 3? They're too similar."
- "Multiple servers don't work in Claude Desktop" — Ask Claude Code
  to check the config format.
