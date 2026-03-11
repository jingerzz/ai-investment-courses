# Week 2: Conversation Guide

How to talk to Claude Code when adding safety checks (guardrails)
to your stock tools.

---

## Building on What You Already Have

When you open Claude Code in your project folder, it can see the files
from Week 1. You don't need to re-describe everything.

**Good:**
```
I have a server.py from last week with stock snapshot and watchlist
tools. I want to add market overview and sector tools. Can you add
them to the existing file?
```

**Less effective:**
```
[Re-describing everything from scratch]
```

Claude Code will read your existing `server.py` and add to it.

---

## Describing Safety Checks

### The pre-formatted section pattern

```
I want a tool that returns a pre-built markdown table with exact
numbers. The AI should show this table exactly as returned — no
rounding, no changing numbers. The tool should have a field called
"present_verbatim" set to true so the AI knows not to modify it.
```

### The stale data warning pattern

```
Every tool should check if the stock market is currently open. If
it's closed (weekend, after 4 PM ET), add a "stale_data_warning"
field with a message like "Market closed. Prices are from the last
trading day." If the market is open, set this to null.
```

### The no-calculation rule

```
The AI should never calculate percentages or averages from raw numbers.
Pre-compute everything in the tool. For example, don't return individual
stock returns and expect the AI to average them — return the
pre-computed average.
```

---

## When the AI Gets Something Wrong

This is the most important skill in Week 2: spotting when the AI
makes a mistake and fixing it by talking to Claude Code.

### The AI makes up numbers

```
When I asked Claude Desktop for my average return, it said 2.3%, but
the individual returns don't add up to that. The AI is doing math
wrong.

Can you add a pre-computed "avg_daily_return_pct" field to
get_watchlist_movers so the AI doesn't need to calculate it?
```

### The AI ignores the formatted section

```
My get_report_formatted tool returns a markdown table, but the AI is
rewriting the numbers in its own words instead of showing the table.
Can you update the guide tool to say: "Always present the
formatted_section from get_report_formatted exactly as-is. Do not
reword or reformat the numbers."
```

### The AI doesn't connect the dots

```
The report mentions that Snapchat is down 2.2% but doesn't mention that
the whole Communication Services sector is also down. Can you add a
field to get_watchlist_movers that shows each stock's sector and
whether the stock is doing better or worse than that sector? That
should help the AI make the connection.
```

---

## Testing Prompts for Claude Desktop

After building your report tools, try these in Claude Desktop:

**Basic report:**
```
Give me my morning report.
```

**Testing for math errors:**
```
What's my average return across all stocks today?
(Watch if AI calculates or uses the pre-computed value)
```

**Stale data test (try in the evening or on a weekend):**
```
How are my stocks doing right now?
(Should include stale data warning)
```

**Cross-reference test:**
```
Which of my stocks is doing the best compared to its sector?
(Should connect stock performance to sector data)
```

**Error handling test:**
```
How is FAKE_TICKER doing today?
(Should report the error nicely, not crash)
```

---

## Tips for Week 2

1. **Build one tool at a time.** Add one tool, test it, then add the
   next. If something breaks, you'll know which tool caused it.

2. **Test with Claude Desktop, not just the inspector.** The inspector
   shows you raw tool output. Claude Desktop shows you how the AI
   *uses* that output. Both matter.

3. **Safety checks are about tool design.** The best safety check is
   a tool that returns data the AI can't misinterpret — not a prompt
   that says "please don't make mistakes."

4. **The guide tool is your best safety check.** It tells the AI the
   rules. If the AI isn't following a rule, check if the guide tool
   mentions it.
