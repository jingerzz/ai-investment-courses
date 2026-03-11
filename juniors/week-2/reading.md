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

If a tool returns that Roblox's price is $59.80, the AI might say "Roblox
is trading at around $60" or "Roblox is just under $60." Both are
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
says "Roblox is at $59.80" — and you think that's the current price.
But it's actually from Friday afternoon. The stale data warning prevents
this confusion.

> **Investing 101: What Does "Profitable" Mean?**
>
> Crocs (CROX) makes money on every pair of foam clogs it sells. Snapchat
> (SNAP) has over 400 million users but has never turned a profit. How
> can a company with 400 million users not make money? Because their
> costs (servers, employees, R&D) are higher than their ad revenue. A
> company you use every day can still be a bad investment if it can't
> turn users into profits. Your daily report will help you spot the
> difference.

---

## 2.4 Guardrail #3: Pre-Formatted Sections

A **pre-formatted section** is a piece of output that the tool builds
with exact numbers, and the AI presents exactly as-is without changing
anything.

Here's why this matters. Say your tool returns this data:

```
RBLX: $59.80,  +1.65%
DUOL: $97.42,  +0.38%
CROX: $80.49,  +0.12%
SPOT: $517.31, -0.45%
SNAP: $4.86,   -2.21%
```

Without a pre-formatted section, the AI might say "Roblox is up about 2%
at around $60." That's imprecise. With a pre-formatted section, the
tool builds a table with exact numbers:

```
| Stock | Price   | Daily Change |
|-------|---------|-------------|
| RBLX  | $59.80  | +1.65%      |
| DUOL  | $97.42  | +0.38%      |
| CROX  | $80.49  | +0.12%      |
| SPOT  | $517.31 | -0.45%      |
| SNAP  | $4.86   | -2.21%      |
```

The tool also returns a flag called `present_verbatim: true`, which
tells the AI: "Show this table exactly as I gave it to you. Don't
round the numbers, don't reword it, don't change the formatting."

The AI can still add its own commentary *after* the table — like
"Roblox is your best performer today" — but the table itself stays
exactly as the code built it.

---

## 2.5 Connecting the Dots: Cross-Referencing

Here's where AI really shines. Your tools provide different pieces of
data — individual stock prices, overall market direction, which
industries are doing well or poorly. The AI's job is to connect these
pieces into a story.

For example, say:
- Snapchat (SNAP) is down 2.21% today
- The Communication Services sector is down 1.8% today
- The overall market is slightly down

The AI can connect these: "Snapchat is down today, but this looks like a
sector-wide thing — Communication Services is the weakest sector. SNAP
is actually underperforming its sector a bit more than average."

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
   moves to sector trends to market conditions — that's what AI does
   better than any dashboard.
