# AI-Powered Investing for Juniors — 4-Week Course

## Overview

This course teaches high school students how to build AI-powered tools
for tracking and analyzing stocks — using Claude as your builder. You
don't need to know how to code. You'll describe what you want in plain
English, and Claude will build it for you.

**Audience:** High school students (8th-10th grade) interested in investing and AI
**Format:** 30 min reading + 30 min hands-on with Claude per week (4 weeks)
**Prerequisites:** Claude Desktop and Claude Code installed (see `prerequisites.md`)

## What You'll Learn

This is NOT a coding class. You'll learn to:
- **Describe** what you want to Claude so it builds the right thing
- **Evaluate** whether what Claude built actually works correctly
- **Iterate** when the first version isn't quite right
- **Connect** your tools to Claude Desktop so AI can look up real stock data

You'll also pick up some investing basics along the way — like what stock
prices mean, how to compare companies, and why you shouldn't trust AI
to do math.

## Weekly Progression

| Week | Focus | What You'll Build |
|------|-------|-------------------|
| 1 | Getting started with Claude Code | A tool that gives Claude access to stock data for companies you care about |
| 2 | Teaching AI not to make mistakes | A daily stock report with safety checks that keep the AI honest |
| **Bonus** | **Running AI on your own computer (optional)** | **A private Q&A system that can answer questions about company documents** |
| 3 | Designing bigger systems | A plan for connecting multiple AI tools together |
| 4 | AI that watches and alerts you | An AI assistant that monitors stocks and tells you when something important happens |

The bonus module is optional and recommended after Week 2. It works on
any Mac or PC — we'll tell you which AI model to download based on how
much memory your computer has.

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

Each week contains:
```
week-N/
├── reading.md                      # Concepts (30 min read)
└── exercise/
    ├── README.md                   # Step-by-step exercise guide
    ├── conversation_guide.md       # Example prompts for Claude Code
    ├── checklist.md                # How to check your work
    └── reference_solution.md       # What a good result looks like
```

Special files:
- `introduction.md` — Why this course matters (start here)
- `conclusion.md` — What you've accomplished and what's next
- `prerequisites.md` — Complete setup guide with troubleshooting
- `glossary.md` — Every technical term explained in plain language
- `COURSE_BRIEF.md` — Metadata and design direction for book production
- `week-1/exercise/setup.md` — First-time installation guide
- `bonus-local-rag/exercise/ollama_quickstart.md` — Ollama setup guide
