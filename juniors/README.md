# AI-Powered Investing for Juniors — 4-Week Course

## Overview

This course teaches high school students how to build AI-powered tools
for tracking and analyzing stocks — using Claude as your builder. You
don't need to know how to code. You'll describe what you want in plain
English, and Claude will build it for you.

**Audience:** High school students (8th-10th grade) interested in investing and AI
**Format:** 2 Foundations modules + 4 weekly modules (30 min reading + 30 min exercise each)
**Prerequisites:** A Claude account to start; Claude Desktop and Claude Code added for Week 1 (see `prerequisites.md`)

## What You'll Learn

This is NOT a coding class. You'll learn to:
- **Describe** what you want to Claude so it builds the right thing
- **Evaluate** whether what Claude built actually works correctly
- **Iterate** when the first version isn't quite right
- **Connect** your tools to Claude Desktop so AI can look up real stock data

You'll also pick up some investing basics along the way — like what stock
prices mean, how to compare companies, and why you shouldn't trust AI
to do math.

## Course Progression

| Module | Focus | What You'll Do |
|--------|-------|----------------|
| **Foundations 1** | Understanding Claude | Learn what AI can and can't do, set up projects and custom instructions |
| **Foundations 2** | Setting up your workspace | Install Claude Desktop, learn attachments, find the Developer menu |
| **Week 1** | Getting started with Claude Code | Build a tool that gives Claude access to real stock data |
| **Week 2** | Teaching AI not to make mistakes | Add safety checks that keep the AI honest |
| **Bonus** | **Running AI on your computer (optional)** | **A private Q&A system for company documents** |
| **Week 3** | Designing bigger systems | Plan how to connect multiple AI tools together |
| **Week 4** | AI that watches and alerts you | Build a monitor that watches stocks and alerts you |

Start with Foundations 1 --- it requires only a Claude account and a
web browser. The Foundations modules build your understanding before
you start building tools in Week 1.

The bonus module is optional and recommended after Week 2.

## Prerequisites

See `prerequisites.md` for the complete setup guide. You'll need:
1. **Claude Desktop** — [claude.ai/download](https://claude.ai/download)
2. **Claude Code** — See `week-1/exercise/setup.md` for step-by-step instructions

A parent or teacher can help with installation if needed.

## Data Sources

This course uses free data — no paid subscriptions:
- **Yahoo Finance** (via yfinance library) — stock prices and company info
- **SEC EDGAR** — public company filings (annual reports)
- **StockAnalysis.com** — a website for checking stock data

## Structure

Each module contains:
```
foundations-N/ or week-N/
├── reading.md                      # Concepts (30 min read)
└── exercise/
    ├── README.md                   # Step-by-step exercise guide
    ├── conversation_guide.md       # Example prompts
    ├── checklist.md                # How to check your work
    └── reference_solution.md       # What a good result looks like (Weeks 1-4)
```

Special files:
- `introduction.md` — Why this course matters (start here)
- `conclusion.md` — What you've accomplished and what's next
- `prerequisites.md` — Complete setup guide with troubleshooting
- `glossary.md` — Every technical term explained in plain language
- `COURSE_BRIEF.md` — Metadata and design direction for book production
- `week-1/exercise/setup.md` — First-time installation guide
