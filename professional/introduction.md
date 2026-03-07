# Introduction: Why This Matters

---

Every investment professional has felt it: the gap between what AI
promises and what it actually delivers in practice. You've seen the
demos. You've read the reports. Maybe you've even asked ChatGPT to
analyze a stock and gotten a confident-sounding answer based on
two-year-old training data.

The problem isn't AI capability — it's connection. Today's AI models
are remarkably good at reasoning, synthesis, and pattern recognition.
But they're cut off from your data. They don't have access to your
watchlist, your risk parameters, your firm's documents, or even
current market prices. Without that connection, AI is just a very
articulate colleague who hasn't read the briefing materials.

This course teaches you how to build that connection.

---

## What You'll Actually Do

Over four weeks, you'll build a suite of AI-powered tools that connect
Claude to real market data and your own workflows. By the end, you'll
have:

- A **watchlist server** that gives Claude live access to stock prices,
  fundamentals, and comparisons across your portfolio
- A **morning briefing tool** with guardrails that prevent AI from
  making math errors or presenting stale data as current
- A **system architecture** for deploying multiple AI-connected servers
  across your organization
- An **agent workflow** with approval rules, escalation logic, and a
  complete audit trail

If you do the optional bonus module, you'll also have a **private
document Q&A system** that processes SEC filings entirely on your
machine — no data leaves your laptop.

These aren't toy examples. They use real market data from Yahoo Finance,
real SEC filings from EDGAR, and real architectural patterns from
production systems. The tools you build will work after the course ends.

---

## You Don't Need to Code

This might be the most important sentence in the course: **you will not
write a single line of code yourself.**

You'll use Claude Code — Anthropic's command-line AI tool — to build
everything. You describe what you want in plain English. Claude writes
the code, creates the files, installs the dependencies, and runs the
tests. Your job is to:

1. **Describe** what you need clearly (Week 1 teaches this)
2. **Evaluate** whether what Claude built is correct (Week 2 teaches this)
3. **Iterate** when the first version isn't right (every week practices this)
4. **Design** systems that are worth building (Weeks 3-4 teach this)

These are the same skills you'd need to manage a development team
building AI tools for your firm — except here, the development team
is Claude, and you can go from idea to working tool in 30 minutes.

---

## How the Course Works

Each week has two parts:

**Reading (30 minutes):** Concepts, patterns, and design principles.
No prerequisites beyond your existing finance knowledge. The reading
explains how AI systems work at the level you need to make good
decisions — not at the level of writing code.

**Exercise (30 minutes):** Hands-on building with Claude Code. You'll
open your terminal, start Claude Code, and describe what you want to
build. A conversation guide shows you example prompts. A checklist
helps you evaluate the result. A reference solution shows what good
output looks like.

The weeks build on each other. Week 1's server becomes the foundation
for Week 2's guardrails. Week 3 designs a system that uses everything
you've built. Week 4 adds agent capabilities on top. By the end,
you've built a complete, connected system — and you understand every
design decision because you made them.

---

## Who This Course Is For

You work in investment management. You might be an analyst building
models, a portfolio manager making allocation decisions, or an IT
manager evaluating AI tools for your firm. You understand markets,
instruments, and financial workflows.

You don't need to understand Python, APIs, servers, or machine learning.
Those concepts are introduced as needed, in the context of the financial
tools you're building. The glossary at the back defines every technical
term used in the course.

What you do need: curiosity about what AI can actually do for your work,
willingness to open a terminal and type commands, and 60 minutes a week
for four weeks.

---

## A Note on the Approach

This course takes a specific stance: **AI should enhance your judgment,
not replace it.**

Every tool you build follows the same principle. AI proposes; you
decide. AI surfaces information; you interpret it. AI monitors
portfolios; you approve trades. The guardrails, approval workflows,
and audit trails aren't afterthoughts — they're the point. Building
AI tools that your compliance team would actually approve is harder
than building ones that just look impressive in a demo. That's what
we teach.

The patterns in this course come from a production trading platform.
They've been tested with real money, real regulators, and real
operational constraints. You're learning what actually works.

Let's build.
