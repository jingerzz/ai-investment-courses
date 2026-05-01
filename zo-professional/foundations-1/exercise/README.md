# Exercise: Map One of Your Investment Workflows onto Zo

## Goal

Take one investment workflow you actually do today, and write down where each piece of it should live on Zo.

By the end of this exercise, you should have a short markdown file (`workflow-map.md`) inside your course folder that captures: what data you use, what documents you read, what calculations you make, what decisions you take, and what outputs you want. That file becomes the seed for everything you build later in the course.

This exercise is **not about coding**. It is about installing the four-layer mental model from the reading and applying it to your own work.

Time: about 30 minutes.

## What You Will Need

- Your Zo workspace open in the browser
- The `notes/` folder you created in Prerequisites
- An honest answer to "what do I actually do every week as an investor?"

## Steps

### 1. Open Zo and find your course folder

Open your Zo workspace and navigate to `AI-Investing-Course/notes/`. If the folder does not exist, create it. If you skipped the folder setup in Prerequisites, do it now — every later exercise builds on that structure.

### 2. Create `workflow-map.md`

Inside `notes/`, create a new markdown file called `workflow-map.md`. You can either:

- Right-click in the workspace and create a new file, or
- Ask the AI in chat: *"Create a file at AI-Investing-Course/notes/workflow-map.md with five top-level headings: Data I use, Documents I read, Metrics I calculate, Decisions I make, Outputs I want."*

Either approach is fine. The chat approach gives you a feel for how the AI uses files; do that one if you have not seen it before.

### 3. Fill in the five sections

Under each heading, list 3–5 real examples from your investment process. Be specific. "Watch the market" is not specific. "Check SPY's level relative to its 200-day moving average and compare to last week" is.

Here is a worked example to give you the right shape:

```markdown
# Data I Use
- Daily closing prices for SPY, TLT, QQQ, IWM (Yahoo Finance)
- Weekly TIC data on foreign Treasury holdings (Treasury website)
- Monthly CPI release (BLS)
- Quarterly 13F filings from a tracked list of value investors

# Documents I Read
- 10-Ks and 10-Qs for portfolio companies
- DEF 14A proxy filings during proxy season
- Quarterly letters from Berkshire, Pershing Square, Greenlight
- Federal Reserve FOMC statements

# Metrics I Calculate
- 200-day moving average vs current price for each watchlist name
- Net flow into a sector ETF over the past 4 weeks
- Position size as a percent of NAV
- 1-year forward P/E based on consensus estimates

# Decisions I Make
- Should I add to an existing position?
- Should I cut a losing position?
- Should I start a new position from my watchlist?
- Should I rebalance the portfolio for sector drift?

# Outputs I Want
- A weekly portfolio review note
- A daily SPY/TLT regime brief
- A monthly factor exposure summary
- A quarterly 13F change tracker
```

Yours should look similar in structure but with your actual workflow.

### 4. Ask Zo to classify each item by layer

Once your draft is in place, ask the AI to take the five lists and assign each item to one of the four layers from the reading: **files**, **tools**, **surfaces**, or **agents**. Some items belong to more than one layer. That is fine.

Use this prompt:

```text
Read AI-Investing-Course/notes/workflow-map.md. For each entry under each
heading, classify it as one of: files, tools (deterministic scripts or
servers), surfaces (hosted pages or dashboards), or scheduled agents. Some
items will belong to more than one. Then list the two workflows that look
like the strongest candidates to automate first, and explain why.
```

### 5. Save the AI's classification back into your file

Have the AI append its classification and the two recommended workflows to the same `workflow-map.md` file. The point is that your draft becomes a real artifact you can come back to in Week 3 when you start designing architectures.

## What You Should See

A reasonable AI response will:

- assign most data items to "tools" (since they need to be pulled or computed)
- assign most documents to "files" plus a "tool" for retrieval
- assign metric calculations to "tools" (these must not be done by the model)
- assign decisions to "humans only" (the AI should never recommend pure decisions yet)
- assign outputs to a mix of surfaces (dashboard) and agents (recurring brief)

If the AI's classification surprises you, push back. "Why did you put portfolio drift checks into agents instead of tools?" is a good question to ask. The reading taught you the layers; the exercise tests whether you can apply them under your own pressure.

## Checkpoint

You are done when you can answer all of these:

- Which items in your workflow need exact computation (and therefore must come from code)?
- Which items need source documents (and therefore must be retrieved with citations)?
- Which items produce outputs a human reviews before deciding?
- Which items should never be delegated to an AI model?
- Which two workflows are the strongest candidates to automate first?

If you can answer those, you are ready for Foundations 2.
