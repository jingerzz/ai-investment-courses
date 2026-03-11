# Week 4 Exercise: Build a Stock Monitor

## What You'll Build

A monitoring system that checks your stocks and alerts you when
something important happens. By the end, you'll have:

- A script that checks all your stocks and flags big moves
- Alerts when prices drop a lot or volume spikes
- A log file that records every check (your audit trail)
- Clear rules about what needs your attention vs. what's routine
- A tool in Claude Desktop so you can ask "Any alerts?"

## Time: 30 minutes

## What You Need

- Claude Code
- Your MCP servers from previous weeks
- Claude Desktop (for testing)

---

## Step 1: Design Your Rules (5 min)

Before building anything, decide your rules. Open Claude Desktop and
think through this:

```
I want to build a monitoring system for my stock watchlist. Help me
think through the rules:

My watchlist: RBLX, SNAP, SPOT, DUOL, CROX

1. What should it check? (price changes, volume spikes, anything else?)
2. What size price move should trigger an alert? 3%? 5%?
3. What should just be logged quietly? (small moves, routine checks)
4. What should NEVER be automated? (buying/selling stocks)

I'd rather get too many alerts at first and tighten later.
```

Write down the rules. You'll give them to Claude Code next.

## Step 2: Build the Monitor (10 min)

```bash
cd ~/ai-stock-tools
claude
```

Tell Claude Code:

```
Build a stock monitoring script called monitor.py that:

1. CHECKS my watchlist stocks (RBLX, SNAP, SPOT, DUOL, CROX):
   - Current price and daily change for each stock
   - Whether any stock is up or down more than 3% today
   - Whether any stock has unusual volume (more than 2x its average)

2. CLASSIFIES each finding:
   - "SILENT" — normal day, nothing unusual (just log it)
   - "ALERT" — worth knowing about (3-5% move, high volume)
   - "URGENT" — needs attention (5%+ move)

3. LOGS everything to a file called monitor_log.json:
   - Timestamp
   - Which stock
   - What was found
   - Classification (SILENT/ALERT/URGENT)

4. PRINTS only the alerts and urgent items to the terminal.

Use yfinance for data. The script should run once and exit — I'll
run it manually when I want to check.
```

Test it:
```
Can you run the monitor script and show me what it outputs?
```

## Step 3: Add the Audit Trail (5 min)

```
Update monitor.py to write more detailed log entries. For each check,
record:

1. timestamp - when the check ran
2. ticker - which stock
3. check_type - what was checked (e.g., "daily_price_move")
4. current_value - what was found (e.g., "-4.2%")
5. threshold - what triggers an alert (e.g., "3%")
6. classification - SILENT / ALERT / URGENT
7. suggested_action - what I might want to do (e.g., "Review for news")
8. data_source - where the data came from

Each run ADDS to the log file — don't overwrite old entries.

Also add a way to see a summary:
"uv run python monitor.py --summary" shows all alerts from the past
7 days.
```

## Step 4: Define the Rules Clearly (5 min)

```
Add a rules section at the top of monitor.py so the rules are easy
to see and change:

RULES = {
    "routine_check": "SILENT - normal check, just log it",
    "small_move": "SILENT - under 3% move, normal volatility",
    "medium_move": "ALERT - 3% to 5% move, tell me about it",
    "big_move": "URGENT - over 5% move, needs my attention now",
    "unusual_volume": "ALERT - volume 2x normal, might be news",
    "buy_or_sell_stocks": "BLOCKED - NEVER automate this",
}

Print the applicable rule with each alert. For BLOCKED rules, make
it clear these actions are NEVER automated — a human always decides.
```

## Step 5: Connect to Claude Desktop (5 min)

Make the alerts available to Claude Desktop:

```
Add a new tool to my stock server called get_monitor_alerts that:

1. Reads monitor_log.json
2. Returns the most recent alerts and urgent items
3. For each alert, includes the classification and suggested action
4. If nothing needs attention, returns {"status": "all_clear",
   "message": "All stocks within normal ranges"}

Update the guide tool to include this new tool.
```

Restart Claude Desktop and test:

```
Any alerts on my stocks?
```

```
Give me my morning report including any monitoring alerts.
```

---

## What You Learned

- How to design **monitoring rules** before building
- The **classification pattern**: SILENT, ALERT, URGENT, BLOCKED
- **Audit trails**: logging every check for later review
- **Approval levels**: what's routine vs. what needs your attention
  vs. what's never automated
- How to connect **monitoring to Claude Desktop** as a tool
- The principle that **AI watches and suggests, humans decide**

## The Key Rule

```
BLOCKED means BLOCKED — forever.

The monitor can say "Snapchat dropped 6%, consider selling."
It can even calculate exactly how many shares to sell.
But it NEVER actually buys or sells.
That's always your decision.

This isn't because the AI isn't smart enough.
It's because investing decisions should always involve a human.
```

## If You Get Stuck

- "The log file is messy" — Ask Claude Code to format it better
- "Too many alerts" — Raise the thresholds (e.g., 5% instead of 3%)
- "Alerts not showing in Claude Desktop" — Check that the tool is
  reading the right file path
