# Week 4 Exercise: Build an Agent Workflow

## What You'll Build

A monitoring agent that uses your existing MCP servers to check signals,
watchlist positions, and SEC filings — then classifies findings, logs
everything, and alerts you when something needs attention.

By the end, you'll have:
- A monitoring script that calls your SPY/TLT and watchlist server tools
- Classified alerts (silent / alert / urgent / blocked)
- An audit trail logging every check and finding
- A new MCP tool that exposes monitoring alerts to Claude Desktop

## Time: 30 minutes

## What You Need

- Claude Code
- Claude Desktop with all three servers connected (from Week 3)
- Your three MCP servers: spy-tlt-course, my-watchlist, page-index-rag

---

## Step 1: Design Your Monitoring Rules (5 min)

Before building, decide what the agent should monitor. Open Claude
Desktop and think through the rules:

```
I want to build a monitoring agent for my investment workflow. I have
three MCP servers:

1. spy-tlt-course — gives me SPY/TLT signals (colors, tiers, exposure)
2. my-watchlist — tracks AAPL, MSFT, NVDA, AMZN, GOOGL prices
3. page-index-rag — searches SEC filings for BLK and HOOD

Help me design monitoring rules:
1. What should it check from the strategy server? (signal changes,
   danger state, regime shifts)
2. What should it check from the watchlist? (big movers, concentration)
3. What should it check from the research server? (new filings available)
4. What warrants an alert vs. a silent log entry?
5. What should NEVER be automated? (trading, changing limits)
```

Write down the rules. You'll give these to Claude Code next.

## Step 2: Build the Monitor (10 min)

```bash
cd ~/ai-investment-courses/professional/servers/my-watchlist
claude
```

Tell Claude Code to build the monitoring script:

```
Build a monitoring script called monitor.py that checks my investment
tools and produces classified alerts. Here's what it should do:

1. GATHER data by importing and calling tools from the existing servers:
   - Call the spy-tlt-course server's advisor functions to get the
     current signal, color, tier, and exposure recommendation.
     (Import from spy_tlt_course.advisor and spy_tlt_course.data)
   - Use yfinance to check my watchlist stocks: AAPL, MSFT, NVDA,
     AMZN, GOOGL — get current price and daily change %.

2. CLASSIFY each finding:
   - "SILENT" — routine check, nothing notable (e.g., signal unchanged,
     all stocks within normal range)
   - "ALERT" — needs my attention (e.g., new signal fired, stock down
     > 3%, danger state activated)
   - "URGENT" — needs immediate attention (e.g., Tier 1 signal fired,
     stock down > 5%, danger state in bear regime)
   - "BLOCKED" — things the agent must NEVER do (place trades, change
     risk limits, modify strategy parameters)

3. LOG everything to monitor_log.json as an array of entries. Each
   entry should have:
   - timestamp
   - check_type (e.g., "signal_check", "watchlist_scan")
   - finding (what was found)
   - classification (SILENT / ALERT / URGENT)
   - data_source
   - action_suggested (what I should consider doing)

4. PRINT a summary to terminal showing only ALERT and URGENT findings.
   Include the suggested action for each.

The script should run once and exit. Use the spy-tlt-course data
directory at:
~/ai-investment-courses/professional/servers/spy-tlt-course/data/

Make sure to handle errors gracefully — if a data source is
unavailable, log the error as an ALERT, don't crash.
```

Test it:
```
Run the monitor script and show me the output.
```

Check the output:
- Does it correctly report the current SPY/TLT signal?
- Are watchlist stocks showing reasonable prices?
- Is the classification sensible? (A normal day should be mostly SILENT)
- Does monitor_log.json have structured entries?

## Step 3: Add the Audit Trail (5 min)

```
Enhance the monitor log to include the full reasoning chain. For each
check, I want to see:

1. what_was_checked — the tool or data source
2. raw_data — the actual values returned (prices, signal, color)
3. rule_applied — which monitoring rule triggered (e.g., "stock_down_3pct")
4. classification — SILENT / ALERT / URGENT
5. reasoning — why this classification (e.g., "NVDA down 3.2%, exceeds
   3% threshold")
6. action_suggested — what to consider doing
7. approval_level — what level of human action is needed

Also add a --summary flag: when I run "uv run python monitor.py --summary"
it reads monitor_log.json and shows:
- Total checks run (all time)
- Alert count by classification
- Most frequent alert types
- Last 5 ALERT or URGENT entries
```

## Step 4: Expose Alerts as an MCP Tool (5 min)

Connect the monitoring output to Claude Desktop so you can ask about
alerts conversationally:

```
Add a new tool to server.py called get_monitor_alerts() that:

1. Reads monitor_log.json
2. Returns the most recent run's findings, filtered to ALERT and
   URGENT only
3. For each alert, includes: check_type, finding, classification,
   reasoning, action_suggested, approval_level
4. If no alerts, returns {"status": "all_clear", "last_check": <timestamp>}
5. Include a stale_data_warning if the last monitor run was more than
   1 hour ago

Docstring: "Returns recent monitoring alerts for the portfolio.
Call this when the user asks about alerts, warnings, or anything
that needs attention. Returns only ALERT and URGENT findings —
routine checks are logged but not surfaced."

Update the guide tool to mention this new tool and add a rule:
"For BLOCKED actions (trading, limit changes), always remind the user
these require manual action — the monitor will never automate them."
```

Restart Claude Desktop and test:

```
Are there any alerts on my portfolio?
```

```
Run the monitor (from terminal), then come back and ask:
What did the monitor find? Anything I should worry about?
```

## Step 5: Test the Full Loop (5 min)

Now experience the complete agent pattern: gather → reason → propose →
(approve) → log.

Run the monitor from your terminal:
```bash
cd ~/ai-investment-courses/professional/servers/my-watchlist
uv run python monitor.py
```

Then in Claude Desktop, ask:

```
Check my monitoring alerts and the current SPY/TLT signal. Given both,
what should I be doing right now? Walk me through your reasoning.
```

Claude should:
1. Call `get_monitor_alerts()` from your watchlist server
2. Call `get_current_signal()` from the spy-tlt-course server
3. Synthesize: connect the alerts to the signal context
4. Propose actions (but NOT execute them — that's BLOCKED)

This is the Level 2-3 autonomy from the reading: the agent gathers
data and proposes, you decide.

**Try the audit trail:**
```
Show me a summary of all monitoring activity.
```

If you added the `--summary` flag, run it from the terminal:
```bash
uv run python monitor.py --summary
```

---

## What You Learned

- The **agent loop** pattern: gather → classify → log → alert
- **Classification levels**: SILENT, ALERT, URGENT, BLOCKED
- **Audit trails**: every check is logged with full reasoning chain
- **BLOCKED actions**: things the agent must never automate (trading,
  limit changes)
- How to **expose monitoring data** as an MCP tool for conversational
  access
- The **full loop**: monitor runs → alerts surfaced in Claude Desktop →
  Claude synthesizes with other servers → proposes actions → you decide

## The Autonomy Spectrum

```
SILENT    → Runs without telling you (routine checks)
ALERT     → Something needs your attention
URGENT    → Something needs immediate attention
BLOCKED   → Never happens without your explicit action
```

Start everything at ALERT. Move things to SILENT only after you've
verified they work correctly over time. Never move trading to anything
below BLOCKED.

## The Audit Trail Matters

Every check is logged, even routine ones. This means:
- You can review what the monitor saw while you were away
- You can spot patterns ("NVDA triggered alerts 3 times this week")
- You have a record if something goes wrong
- Compliance can review the system's behavior

## AI Proposes, Humans Decide

The monitor can say "SPY/TLT fired a Tier 2 Blue signal — consider
adding exposure to 1.5x." But it never places a trade. That's BLOCKED.

This isn't a temporary limitation. It's a permanent design principle
for financial AI systems.

## If You Get Stuck

- **"Import errors from spy_tlt_course"** — Make sure the spy-tlt-course
  package is installed. From the my-watchlist directory, you may need to
  tell Claude Code to add it as a path dependency or import the CSV data
  directly instead.
- **"monitor_log.json is messy"** — Ask Claude Code to format it better
  or add pretty-printing.
- **"Alerts are too noisy"** — Adjust thresholds (5% instead of 3% for
  price moves). Some noise on the first run is normal.
- **"I want scheduled monitoring"** — That's a stretch goal. For now,
  run manually. A cron job or scheduled task is the next step but beyond
  this exercise.
