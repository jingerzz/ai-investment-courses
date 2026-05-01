# Exercise: Prepare Your Zo Course Workspace

## Goal

Set up a clean, predictable workspace that the AI can use without asking you where things go. By the end of this exercise, your course folder will have:

- All five subfolders from the reading
- A README that briefs the AI
- A decision log file
- Confirmed access to the Settings, Hosting, and Automations areas

This is a one-time setup. Every later module assumes it is done.

Time: about 30 minutes.

## Steps

### 1. Create the folder structure

If you skipped folder setup in Prerequisites, create them now:

```
AI-Investing-Course/
├── notes/
├── servers/
├── datasets/
├── dashboards/
└── agents/
```

You can do this manually in the workspace UI, or ask the AI:

```text
Create the following folders inside AI-Investing-Course if they do not
already exist: notes, servers, datasets, dashboards, agents. Confirm
which were created and which already existed.
```

### 2. Write the workspace README

Create `AI-Investing-Course/README.md`. The README is the first thing the AI reads when it opens this folder. Keep it short and specific.

Use this template, then customize it:

```markdown
# AI-Investing-Course

This workspace contains the work for the Zo-centric AI investment
management course. The user is [your name / role]. The AI assistant
should treat the user as a [your level: senior analyst / PM / founder
/ retail investor].

## Folder Map

- `notes/`        Research notes, prompts, decision log
- `servers/`      Local copies of MCP servers (course and custom)
- `datasets/`     Data files (CSV, DuckDB, JSON)
- `dashboards/`   Page specs, chart sketches, screenshots
- `agents/`       Scheduled-job specs and run logs

## Allowed Without Asking

- Creating new files inside any folder
- Editing course exercise files
- Running the course MCP servers locally

## Requires Confirmation

- Renaming any of the five top-level folders
- Deleting files older than 7 days
- Editing or deleting any agent spec under `agents/`
- Sending external messages (email, Telegram) on behalf of the user

## Decision Log

See `notes/decision-log.md` for any non-trivial change to the workspace.
```

The two lists ("Allowed Without Asking" and "Requires Confirmation") are doing real work. The AI reads them and adjusts behavior. Be specific.

### 3. Create the decision log

Create `notes/decision-log.md` with a single entry to start it off:

```markdown
# Decision Log

## 2026-04-30 — Initial workspace setup

Set up AI-Investing-Course with the standard five-folder structure and
this decision log. Source: Foundations 2 exercise.
```

Going forward, write a one-line entry every time you make a non-trivial change. The next AI session reads this and learns what is current.

### 4. Walk through Settings

Open Zo's `Settings` area. Click into each of the following at least once and confirm you can find it. You do not need to change anything yet.

- **Settings → AI → Models** — pick a default model
- **Settings → AI → Rules** — where conditional behavior gets stored
- **Settings → Advanced → Secrets** — where API keys live (you have none yet)
- **Settings → Advanced → Access Tokens** — where Zo-API tokens live (you have none yet)

If any of these surprise you, or you cannot find them, ask the AI: *"Show me where Secrets live in Zo settings, and explain what should and should not go there."* The AI will narrate the path.

### 5. Walk through Hosting and Automations

Open `Hosting → Sites` and `Hosting → Services`. Then open `Automations`. Each may be empty, which is fine — the goal here is just to know where they are. Later modules will deploy things to each.

### 6. Confirm with a sanity-check prompt

Run this prompt in chat:

```text
Read AI-Investing-Course/README.md. Summarize what you understand about
the workspace, the user's preferences, and the rules I have set for what
you can do without asking. Then list any ambiguities you would want me
to clarify.
```

A good response will:

- restate the folder structure
- restate the "allowed" and "requires confirmation" lists
- ask a clarifying question or two if anything was vague

If the AI's clarifying questions catch something you genuinely had not decided, update the README and rerun the prompt. The point is to leave the workspace in a state where future AI sessions do not need to re-ask basic questions.

## Checkpoint

You are done when:

- All five folders exist
- The README describes the workspace and the rules
- `notes/decision-log.md` has at least one entry
- You have opened Settings, Hosting, and Automations and know what is in each
- The AI's sanity-check response demonstrates it read your README

If everything passes, you are ready for Week 1.
