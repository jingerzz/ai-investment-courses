# Foundations 2 Exercise: Setting Up Your Workspace

## What You'll Do

You'll install Claude on your desktop and phone, set up purpose-specific
projects for your investment work, and practice a cross-device workflow
with a real finance document. By the end, you'll have a workspace ready
for Week 1 — when you'll connect Claude Desktop to live market data.

## Time: 20 minutes

## What You Need

- A Mac or PC
- An iPhone or Android phone
- Your Anthropic account (the same one you used on claude.ai)
- A finance document to test with — an earnings PDF, research note,
  or any document from your actual work

---

## Step 1: Install Claude Desktop (3 min)

1. Go to [claude.ai/download](https://claude.ai/download).
2. Download and install the app for your platform (Mac or Windows).
3. Open Claude Desktop and sign in with your Anthropic account.
4. Verify you can see the sidebar with your conversation history and
   any projects you created in Foundations 1.

If you created a project in Foundations 1 on claude.ai, it should
appear in the sidebar automatically. Open it and confirm your custom
instructions are there.

---

## Step 2: Verify Project Sync (2 min)

If you have an existing project from Foundations 1:

1. Open it in Claude Desktop.
2. Check that your custom instructions carried over (click the project
   name and look at the project settings).
3. Open a previous conversation in that project and confirm the history
   is intact.

If you don't have an existing project, create one now:

1. Click "New Project" in the sidebar.
2. Name it "Course Sandbox."
3. Add a simple custom instruction: "I'm an investment professional
   taking a course on AI tools. Help me learn by explaining things
   clearly and using finance examples."

---

## Step 3: Try an Attachment Workflow (5 min)

Find a finance document on your computer. Good options:

- An earnings report or press release (PDF)
- A research note from your firm or a public source
- A spreadsheet of holdings or transactions (save as CSV)
- A screenshot of a chart

Drag the document into a Claude Desktop conversation (or use the
paperclip icon). Then try these prompts in sequence:

**Prompt 1 — Summarize:**
```
Summarize the key points of this document in 5 bullet points.
Focus on what an equity analyst would care about most.
```

**Prompt 2 — Extract specifics:**
```
Extract the following from this document:
- Revenue and revenue growth
- Operating margin
- Free cash flow
- Forward guidance (if any)
- Any mentions of risk factors

Present this as a table.
```

**Prompt 3 — Analyze:**
```
Based on this document, what are the two most important things
an investor should focus on? Why?
```

Notice how Claude's answers reference the actual content of your
document — not generic information from its training data. This is
the difference between asking "tell me about this company" and
giving Claude the primary source.

---

## Step 4: Go Mobile (3 min)

1. Download the Claude app from the
   [App Store](https://apps.apple.com/app/claude/id6473753684) (iOS)
   or [Google Play](https://play.google.com/store/apps/details?id=com.anthropic.claude)
   (Android).
2. Sign in with the same Anthropic account.
3. Open the same project you were just using on desktop.
4. In the same conversation where you analyzed your document, ask a
   follow-up question:

```
Based on our earlier discussion of this document, what's the
single most important question I should ask management on the
next earnings call?
```

You didn't re-upload anything. You didn't repeat context. The
conversation history carried over. This is the cross-device workflow
in practice.

---

## Step 5: Set Up Your Work Projects (5 min)

Create 2-3 projects tailored to your actual role. Use the templates
below as starting points — customize them for your coverage, your
instruments, and your firm's terminology.

### For an Equity Analyst:

**Project: "Equity Research"**
```
I'm an equity analyst covering [your sector]. When I share
earnings data, 10-Ks, or research notes, extract key financial
metrics and compare them to prior periods.

Format preferences:
- Use tables for financial comparisons
- Flag deviations from consensus estimates
- Note data sources and dates
- Don't speculate on stock price direction

My coverage: [list your stocks]
```

### For a Portfolio Manager:

**Project: "Portfolio Management"**
```
I manage a [describe your strategy — e.g., long/short equity,
multi-asset, fixed income]. When I share portfolio data, analyze
position sizing, concentration risk, and factor exposures.

Key constraints:
- Max position size: [X]% of NAV
- Benchmark: [your benchmark]
- Risk budget: [your framework]

Always present risk metrics alongside return metrics.
```

### For a Macro Strategist:

**Project: "Macro Strategy"**
```
I'm a macro strategist focused on [rates/FX/commodities/cross-asset].
Help me interpret economic data, central bank communications,
and cross-asset signals.

Preferences:
- Be precise with basis points and decimal places
- Frame analysis in terms of the current cycle
- When I share data, compare to historical analogs
- Distinguish between levels and changes
```

Don't overthink these instructions. You'll refine them over the coming
weeks as you discover what works. The important thing is to have the
projects created so you can start using them.

---

## Step 6: Find the Developer Menu (2 min)

This step is simple but important:

1. In Claude Desktop, open **Settings** (gear icon).
2. Find the **Developer** section.
3. Look at the MCP server configuration area. It should be empty.

You don't need to change anything. But in Week 1, this is exactly
where you'll paste a configuration that connects Claude to a live
trading strategy server. When you do, Claude will gain the ability
to answer questions like "What's today's market signal?" using real
computed data instead of its training knowledge.

Knowing where this menu lives saves you five minutes of searching
next week.

---

## What You Learned

- How to install and navigate Claude Desktop
- How projects and conversations sync across web, desktop, and mobile
- How to use attachments for document analysis — the most immediately
  useful capability for investment professionals
- How to set up purpose-specific projects with custom instructions
  tailored to your role
- Where the Developer menu lives — your entry point for Week 1's
  MCP tool connections

---

## Looking Ahead to Week 1

In Week 1, you'll install a pre-built MCP server called the
**SPY/TLT Course Edition**. This server connects Claude Desktop to a
real trading strategy with live market data. You'll open Claude
Desktop, ask "What's today's signal?", and get a real answer — based
on a real strategy — computed from real data.

The Developer menu you just found is where that connection gets
configured. The projects you just created are where you'll use
those tools. Everything you set up today makes Week 1 smoother.

You've gone from "using Claude in a browser" to "Claude on every
device, organized for investment work." That's the foundation.
Now you're ready to connect it to real data.
