# Week 3: Designing Bigger Systems

## 3.1 One Server or Many?

In Weeks 1 and 2, you built a single server with all your tools in one
file. That works great for a few tools. But what happens when you want
to build a lot more?

Imagine a school stock club that tracks three things:
- **Stock performance** — prices, daily changes, comparisons
- **Research** — reading company annual reports, comparing competitors
- **Alerts** — watching for big moves and notifying the club

Putting everything in one giant server creates problems:

```
Everything in one file:
  Problem: Fix a bug in alerts → accidentally break stock data
  Problem: New member only needs research → gets alert controls too
  Problem: If one thing crashes, everything crashes
```

Splitting into separate servers solves these:

```
Multiple smaller servers:
  Each server does one thing well
  Fix alerts without touching stock data
  New members get access to just what they need
  If research crashes, stock data still works
```

This is called **separation of concerns** — a fancy way of saying
"don't mix unrelated things together."

---

## 3.2 The Shared Library Pattern

Separate servers don't mean copying the same code everywhere. Things
that multiple servers need should live in one shared file.

Think about it: both your stock tracker and your alert system need to
look up stock prices. If you write that code twice:
- When Yahoo Finance changes something, you have to fix it in two places
- You might fix one and forget the other
- Your two servers might show different prices for the same stock

The fix: put common code in a **shared file** that all servers use.

```
shared_utils.py (used by everyone):
  - Look up stock prices
  - Check if the market is open
  - Format timestamps consistently
  - Handle errors the same way

stock_server.py (stock-specific):
  - Watchlist management
  - Comparisons
  - Morning report

research_server.py (research-specific):
  - SEC filing search
  - Company fundamentals
  - Competitor comparison

alert_server.py (alert-specific):
  - Price alerts
  - Volume spikes
  - Daily digest
```

Each server imports the shared file for common stuff, then adds its
own specialized tools. If you need to fix how stock prices are fetched,
you fix it once in the shared file and all servers benefit.

---

## 3.3 Connecting Multiple Servers to Claude Desktop

Here's the cool part: Claude Desktop can connect to multiple servers
at the same time. It sees all the tools from all servers and picks
the right one based on your question.

If you ask "How are my stocks doing?", Claude uses the stock server.
If you ask "What does Roblox's annual report say about competition?",
Claude uses the research server.
If you ask "Give me a morning overview with any alerts", Claude uses
*both* servers and combines the answers.

This cross-referencing is the real power of multiple servers. Each
server does one thing really well, and Claude connects them into a
complete answer.

---

## 3.4 Thinking About Who Needs What

Not everyone needs access to everything. In a school stock club:

- **All members** need the stock tracker (to see prices and comparisons)
- **Research team** also needs the research server (to read filings)
- **Club leaders** also need the alert server (to manage notifications)

When you design a system, think about who uses what. This becomes
important as systems grow — you don't want someone accidentally
triggering an alert they weren't supposed to touch.

---

## 3.5 Where Does Data Come From?

Your AI tools are only as good as the data feeding them. In this course,
we use free data sources:

| Source | What It Provides | Notes |
|--------|-----------------|-------|
| Yahoo Finance (yfinance) | Stock prices, fundamentals | Free, no account needed |
| SEC EDGAR | Company annual reports | Free government website |
| StockAnalysis.com | Stock research, ratings | Free to browse |

**What if a data source goes down?** Good systems have a backup plan.
If Yahoo Finance stops working, your tools should:
1. Try the backup source (if you have one)
2. If that fails too, return a clear error message
3. Never return old data pretending it's current

This is the same stale data warning pattern from Week 2 — but now
applied at the system level.

> **Investing 101: The GTA Effect**
>
> When Take-Two (TTWO) announced GTA VI, the stock jumped — even though
> the game wouldn't ship for over a year. Why do announcements move
> stock prices before anything actually ships? Because stock prices
> reflect what investors *expect* to happen in the future, not just
> what's happening today. A research server that tracks company
> announcements and filings can help you spot these moments before
> everyone else catches on.

---

## 3.6 Design Is a Skill

This week's exercise is different from the others. Instead of jumping
straight into building, you'll start by **designing** — thinking about
what servers you need, what tools each should have, and how they connect.

You'll use Claude Desktop as a thinking partner for the design, then
switch to Claude Code to build it.

This is an important skill. The best builders don't just start writing
code — they plan first. In the professional world, architects design
buildings before construction starts. Software architects design systems
before coding starts. This week, you're the architect.

---

## Key Takeaways

1. **Separate servers for separate jobs** — don't mix unrelated tools
   in one giant file
2. **Shared code for common needs** — stock price lookups, timestamps,
   and error handling go in a shared file
3. **Claude Desktop connects everything** — it sees tools from all
   servers and picks the right ones
4. **Think about access** — not everyone needs everything
5. **Plan for data failures** — have backup sources and clear error
   messages
6. **Design before building** — thinking first saves time and produces
   better results
