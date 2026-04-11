# Week 2: Teaching AI Not to Make Mistakes

## 2.1 AI Is Smart, But It Makes Things Up

Last week you built tools that give Claude access to real stock data.
That was a big deal — Claude went from guessing to knowing. But there's
a problem: even with real data, AI can still mess things up.

Here are three ways AI gets things wrong with financial data:

**Problem 1: Bad Math**

Ask Claude to calculate the average return of five stocks, and it might
get it wrong. Not because it's dumb — it's actually very smart at
language — but because math isn't its strength. It might add percentages
when it should average them, or round numbers in weird ways.

Example: If your five stocks returned +2%, -1%, +3%, -0.5%, and +1.5%,
the average is +1.0%. But the AI might say +1.2% or +5% (if it adds
them instead of averaging).

**Problem 2: Showing Old Data Without Warning**

The stock market is only open from 9:30 AM to 4:00 PM Eastern, Monday
through Friday. If you check your stocks on Saturday morning, the prices
you see are from Friday afternoon. That's fine — but the AI should
*tell you* that. Without a warning, you might think you're looking at
live prices.

**Problem 3: Rewording Numbers**

If a tool returns that Apple's price is $195.20, the AI might say "Apple
is trading at around $195" or "Apple is just under $196." Both are
technically wrong. In finance, exact numbers matter.

This week, you'll add **guardrails** — safety checks that prevent these
three problems.

---

## 2.2 Guardrail #1: Do the Math in Code

This is the most important guardrail. The rule is simple:

**Never let the AI calculate anything. Do all math in your tool's code
and give the AI the finished answer.**

Here's the difference:

```
WITHOUT guardrail:
Tool returns: each stock's daily return
AI tries to calculate: average return = (2% + (-1%) + 3% + (-0.5%) + 1.5%) / 5
AI might get: 1.2% (wrong!) or 5% (very wrong!)

WITH guardrail:
Tool returns: each stock's daily return AND average_daily_return = 1.0%
AI just reports: "Your average daily return is 1.0%"
No calculation needed. No chance of error.
```

This applies to everything: daily changes, returns, averages, totals,
comparisons. If a number needs to be calculated, the tool should
calculate it and hand the finished result to the AI.

Think of it like a restaurant. You don't give the waiter raw ingredients
and a recipe — you give them the finished dish to deliver to the table.
The waiter's job is delivery and presentation, not cooking.

---

## 2.3 Guardrail #2: Stale Data Warnings

A **stale data warning** is a field in your tool's return that says
"heads up, this data isn't from right now."

Here's what it looks like:

```
During market hours (9:30 AM - 4:00 PM ET on weekdays):
  "stale_data_warning": null    (no warning needed, data is live)

After hours, weekends, holidays:
  "stale_data_warning": "Market closed. Prices are from Friday,
   March 15 at 4:00 PM ET."
```

When the AI sees this warning, it starts its response with something like:

> **Note:** The market is currently closed. These prices are from Friday
> at 4:00 PM ET.

Without this, imagine you check your stocks at 8 AM on Saturday. The AI
says "Apple is at $195.20" — and you think that's the current price.
But it's actually from Friday afternoon. The stale data warning prevents
this confusion.

---

## 2.4 Guardrail #3: Pre-Formatted Sections

A **pre-formatted section** is a piece of output that the tool builds
with exact numbers, and the AI presents exactly as-is without changing
anything.

Here's why this matters. Say your tool returns this data:

```
AAPL: $195.20, +0.85%
TSLA: $178.50, +3.21%
NKE:  $97.80,  +0.12%
DIS:  $112.60, -1.82%
NFLX: $628.40, -0.35%
```

Without a pre-formatted section, the AI might say "Apple is up about 1%
at around $195." That's imprecise. With a pre-formatted section, the
tool builds a table with exact numbers:

```
| Stock | Price   | Daily Change |
|-------|---------|-------------|
| AAPL  | $195.20 | +0.85%      |
| TSLA  | $178.50 | +3.21%      |
| NKE   | $97.80  | +0.12%      |
| DIS   | $112.60 | -1.82%      |
| NFLX  | $628.40 | -0.35%      |
```

The tool also returns a flag called `present_verbatim: true`, which
tells the AI: "Show this table exactly as I gave it to you. Don't
round the numbers, don't reword it, don't change the formatting."

The AI can still add its own commentary *after* the table — like
"Tesla is your best performer today" — but the table itself stays
exactly as the code built it.

---

## 2.5 Connecting the Dots: Cross-Referencing

Here's where AI really shines. Your tools provide different pieces of
data --- individual stock prices, overall market direction, which
industries are doing well or poorly. The AI's job is to connect these
pieces into a story.

**Quick note: What's an ETF?** An ETF (Exchange-Traded Fund) is a
basket of stocks you can buy as one unit. For example, SPY holds all
500 stocks in the S&P 500 index --- it tells you how the overall market
is doing. XLK holds technology stocks, XLF holds financial stocks, and
XLE holds energy stocks. Sector ETFs let you see if a whole industry is
moving, not just one company.

For example, say:
- Disney (DIS) is down 1.82% today
- The Communication Services sector is down 2.1% today
- The overall market (SPY) is slightly down

The AI can connect these: "Disney is down today, but this looks like a
sector-wide thing --- Communication Services is the weakest sector. DIS
is actually doing better than its sector average."

This is something a dashboard can't do. A dashboard shows you three
separate numbers. The AI explains what they mean *together*.

To make cross-referencing work well, your tools need to include context.
For each stock, it helps to include:
- What sector it belongs to
- Whether it's outperforming or underperforming its sector
- Whether anything unusual is happening (big move, high volume)

---

## 2.6 The Morning Report: Putting It All Together

This week you'll build a **morning report** — a tool that:

1. Checks how the overall market is doing
2. Looks at which industries are up and down
3. Reviews all your watchlist stocks
4. Builds a pre-formatted summary with exact numbers
5. Adds stale data warnings if the market is closed

When you ask Claude Desktop "Give me my morning report", it calls these
tools and gives you a complete, accurate summary. The numbers are exact
(because the code calculated them). The data freshness is clear (because
of stale data warnings). And the analysis connects everything together
(because the AI is good at telling stories with data).

---

## 2.7 Checking AI's Work: Three Quick Tests

Even with guardrails, you should always double-check what AI tells you.
Here are three simple tests you can run in your head:

**Test 1: Is the number in the right ballpark?**
If the AI says Apple's stock is $19.52, that's obviously wrong --- it
should be closer to $200. If the AI says Nike's market cap is $4 trillion,
that's also wrong --- only a handful of companies are worth that much.
You don't need to know the exact number. You just need to know if the
number is wildly off.

**Test 2: Where did the number come from?**
Check the `data_source` field in the tool's return. Does it say "yfinance"?
Good --- that's real data. Does it say nothing? Then the AI might be
guessing from its training data. Always ask: "Is this a fact from a
tool, or is the AI making this up?"

**Test 3: Is the data current?**
Check the `as_of` timestamp. If the data is from three days ago and
there's no stale data warning, something is wrong. If the market was
open today but the data says "as of Friday", something is wrong.
Timestamps are your friend.

These three checks take seconds, and they catch most problems. Make
them a habit.

---

## Key Takeaways

1. **AI makes three types of mistakes** with financial data: bad math,
   showing old data as current, and rewording exact numbers
2. **Guardrail #1: Do math in code.** Never let the AI calculate. Give
   it finished numbers.
3. **Guardrail #2: Stale data warnings.** Tell the AI when data isn't
   live so it can warn the user.
4. **Guardrail #3: Pre-formatted sections.** Build tables and summaries
   in code. Tell the AI to present them exactly as-is.
5. **Cross-referencing is where AI adds real value.** Connecting stock
   moves to sector trends to market conditions --- that's what AI does
   better than any dashboard.
6. **Always check AI's work.** Three quick tests: Is the number in the
   right ballpark? Where did it come from? Is the data current?
