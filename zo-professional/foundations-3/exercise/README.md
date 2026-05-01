# Exercise: Build Your Memory System

## Goal

Set up a working file-based memory system on Zo, then verify that a fresh conversation reads it. By the end of this exercise, you will have:

- `USER.md` describing who you are
- `MEMORY.md` acting as the index
- A `memory/` folder with the right subfolders
- A `SYSTEM_CONFIG.md` you can edit to evolve the system
- Two Rules — one to read at conversation start, one to write during the conversation
- One verified end-to-end test

Time: about 30 minutes.

## The Quick-Start Guide Does the Setup

Most of this exercise is following the public quick-start guide:

> **[Zo Memory System Quick Start](https://www.clarionintelligencesystems.com/resources/memory-system-quick-start)**

It contains the exact prompts to paste into a Zo chat, in order. Run through Steps 1 through 6 in that guide. They take roughly 20 minutes if you copy-paste each prompt and verify the output before moving to the next.

When you fill in your profile in Step 1, lean into the **investment** context. Useful fields to include:

- Role and seniority (e.g., *"PM at a long/short equity fund,"* or *"independent investor running a small concentrated book"*)
- Coverage focus (sectors, geographies, market-cap range)
- Communication preferences (concise vs. expansive, bullet points vs. prose, technicality level)
- Strategy hard rules (e.g., *"never recommend an entry without a risk/reward ratio,"* *"always quote the spy-tlt regime before single-stock signals"*)

Hard rules in the profile travel into every conversation. They are quiet and effective.

## After the Quick-Start

Three small additions specific to this course.

### 1. Add a project entry for the course

Run this prompt in chat:

```text
Create a project memory entry for the AI-Investing-Course.
- Path: /home/workspace/memory/projects/ai-investing-course.md
- Purpose: track which modules I have completed and what I built in each.
- Include a list with all seven modules (Foundations 1, Foundations 2,
  Foundations 3, Week 1, Week 2, Week 3, Week 4) and a "completed: yes/no"
  line for each.
- Mark Foundations 1, Foundations 2, and Foundations 3 as completed.
- Add a one-line entry to MEMORY.md.
```

This entry is what the AI will read at the start of Week 1 to know you are ready for the SPY/TLT material.

### 2. Cross-reference the course folder

Run this prompt in chat:

```text
Read AI-Investing-Course/README.md and AI-Investing-Course/notes/decision-log.md.
Create a reference memory entry at /home/workspace/memory/reference/ai-investing-course.md
that points the AI at these files for course context. Add a one-line
entry in MEMORY.md.
```

This makes sure that even if you switch to a fresh chat with no obvious course context, the AI can find its way back to the workspace.

### 3. Sanity-check Rule 1

Open a brand-new chat (close any existing one). Send only this:

```text
What do you know about me?
```

A correctly-set-up memory system produces a response that:

- Names you correctly
- Mentions your role and a few preferences from `USER.md`
- References at least one entry from `MEMORY.md`
- Does not ask *"what would you like to work on?"* without first acknowledging context

If the AI starts cold — *"Hi! How can I help?"* — Rule 1 is not firing. The most common cause is that the rule was registered with the wrong condition. Re-run the Step 3 prompt from the quick-start guide.

## Checkpoint

You are done when:

- `USER.md` exists and describes you with enough specificity that a stranger could read it and know how to interact with you
- `MEMORY.md` has at least three one-line entries
- `memory/projects/`, `memory/feedback/`, and `memory/daily/` each have at least one file
- `SYSTEM_CONFIG.md` exists and is your edit surface
- A fresh chat passes the sanity-check above

If everything passes, you are ready for Week 1. The SPY/TLT exercises will write daily notes automatically as you work, and the regime context will start carrying over between sessions.
