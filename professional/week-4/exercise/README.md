# Week 4 Exercise: Build an Agent Workflow

## What You'll Build

An automated monitoring system that checks your portfolio on a schedule and
sends you alerts when something needs attention. This introduces the concept
of AI that acts proactively — with your approval.

By the end, you'll have:
- A monitoring script that checks your positions periodically
- Alerts sent to you when risk limits are approached or signals fire
- An audit log that records every check and alert
- Clear rules about what requires your approval vs. what runs silently

## Time: 30 minutes

## What You Need

- Claude Code
- Your MCP servers from previous weeks
- Claude Desktop (for testing)

---

## Step 1: Design Your Agent Rules (5 min)

Before building anything, decide your rules. Open Claude Desktop and think
through this:

```
I want to build a monitoring agent for my stock portfolio. Help me think
through the rules:

1. What should it check? (positions, risk limits, price moves, volume)
2. How often? (every 15 min during market hours? once a day?)
3. What warrants an alert? (position down 3%? risk limit approached?)
4. What should just be logged silently? (routine checks, no changes)
5. What should NEVER be automated? (actual trading, changing limits)

My portfolio has [X stocks] and my risk limits are [your limits from
Week 3].
```

Write down the rules Claude Desktop helps you design. You'll give these
to Claude Code in the next step.

## Step 2: Build the Monitor with Claude Code (10 min)

```bash
cd ~/ai-finance-tools
claude
```

Tell Claude Code to build the monitoring script:

```
Build a portfolio monitoring script called monitor.py that:

1. CHECKS these things on my portfolio [your stocks]:
   - Current price and daily change for each position
   - Whether any position is down more than 3% today
   - Whether any position exceeds 20% of portfolio weight
   - Whether any sector exceeds 35% of portfolio weight
   - Whether there's unusual volume (> 2x average) on any position

2. CLASSIFIES each finding:
   - "alert" — needs my attention (limit breach, big move, unusual volume)
   - "warning" — approaching a limit (within 5% of threshold)
   - "info" — routine data, no action needed

3. LOGS everything to a file called monitor_log.json:
   - Timestamp of each check
   - What was checked
   - What was found (all positions, not just alerts)
   - Classification (alert/warning/info)

4. PRINTS a summary to the terminal showing only alerts and warnings.

Use yfinance for data. The script should run once and exit — I'll run it
manually for now. No scheduling yet.
```

Test it:
```
Can you run the monitor script and show me what it outputs?
```

## Step 3: Add an Audit Trail (5 min)

```
Update monitor.py to write a more detailed audit log. For each check,
record:

1. timestamp - when the check ran
2. check_type - what was checked (e.g., "position_concentration")
3. finding - what was found (e.g., "NVDA at 22.3% of portfolio")
4. classification - alert / warning / info
5. threshold - what the limit is (e.g., "20% max")
6. action_required - what the user should consider doing
7. data_source - where the data came from

Store this in monitor_log.json as an array of entries. Each run of the
script appends new entries, it doesn't overwrite old ones.

Also add a command-line option: when I run
"uv run python monitor.py --summary" it should read the log file and
show me a summary of all alerts from the past week.
```

## Step 4: Define Approval Levels (5 min)

Tell Claude Code to add a rules configuration:

```
Add a rules section at the top of monitor.py that defines what each
alert level means in terms of action:

RULES = {
    "routine_check": "SILENT - runs automatically, logged only",
    "price_move_under_3pct": "SILENT - normal volatility, log only",
    "price_move_3_to_5pct": "ALERT - notify me, I decide what to do",
    "price_move_over_5pct": "URGENT - notify me immediately",
    "approaching_position_limit": "ALERT - notify me to consider trimming",
    "breaching_position_limit": "URGENT - notify me, suggest trim size",
    "unusual_volume": "ALERT - notify me, might indicate news",
    "place_trade": "BLOCKED - never auto-trade, always requires my action",
    "change_risk_limits": "BLOCKED - never auto-modify limits",
}

Print the applicable rule with each alert so I can see the system's
reasoning. For BLOCKED rules, add a note in the guide that says these
actions are never automated.
```

## Step 5: Connect to Your MCP Servers (5 min)

Now make the monitoring data available to Claude Desktop as a tool:

```
Add a new tool to my existing portfolio server called
get_monitor_alerts that:

1. Reads the monitor_log.json file
2. Returns the most recent check's alerts and warnings
3. Includes the approval level and suggested action for each
4. Returns an empty alerts list with status "all_clear" if nothing
   needs attention

That way I can ask Claude Desktop "Any alerts on my portfolio?" and
it uses real monitoring data.
```

Update your guide tool and restart Claude Desktop.

Test in Claude Desktop:
```
Are there any alerts on my portfolio I should know about?
```

---

## What You Learned

- How to design **monitoring rules** before building anything
- The **classification pattern**: alert / warning / info
- **Audit trails**: logging every check so you can review later
- **Approval levels**: which actions are silent, which need you, which
  are blocked entirely
- How to connect **monitoring output to Claude Desktop** as a tool
- The principle that **AI proposes, humans decide** — the monitor
  alerts you but never trades

## Key Concepts from This Week

### The Autonomy Spectrum

```
SILENT    → Runs without telling you (routine checks)
ALERT     → Tells you something needs attention
URGENT    → Tells you something needs immediate attention
BLOCKED   → Never happens without your explicit action
```

Start everything at ALERT. Move things to SILENT only after you've
verified they work correctly over time.

### The Audit Trail Matters

Every check is logged, even routine ones that find nothing. This means:
- You can review what the monitor was doing while you were away
- You can spot patterns ("NVDA triggered alerts 3 times this week")
- You have a record if something goes wrong
- Compliance can review the system's behavior

### AI Proposes, Humans Decide

The monitor can say "NVDA is at 22.3% of portfolio, above your 20%
limit — consider trimming 50 shares to bring it to 18%." But it never
actually places a trade. That's the BLOCKED level — no matter how
clear the right action is, a human must do it.

This isn't a temporary training-wheels limitation. It's a permanent
design principle for financial AI systems.

## If You Get Stuck

- "The log file is getting messy" → Ask Claude Code to format it better
  or switch to a structured format
- "The alerts are too noisy" → Adjust the thresholds (e.g., 5% instead
  of 3% for price moves)
- "I want email/Slack alerts" → Ask Claude Code to add notifications,
  but that's a stretch goal beyond this course
