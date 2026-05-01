# Prompts: Foundations 2

These prompts make your workspace legible to future AI sessions. Run them after you have created the folder structure and README.

A general-purpose chat model is fine for all of these — you do not need a coding-grade model for Foundations 2.

## Review the Folder Structure

```text
Review my workspace structure under AI-Investing-Course/. Are the folder
names clear enough that a new AI assistant could place files correctly
without asking? Suggest any renames or additions before I start creating
servers, dashboards, and agents.
```

> Run this once, fix anything that genuinely is unclear, and then leave the structure alone. Frequent renames break references everywhere.

```text
Act as a workspace librarian. Tell me where research notes, source
documents, scripts, datasets, dashboards, and agent specs should live.
Quote the README rules where relevant.
```

> The AI's answer should match the README. If it does not, the README is unclear.

## Sharpen the Workspace README

```text
Draft a concise README for AI-Investing-Course. Cover: purpose, user
profile, folder map, what AI can do without asking, what requires
confirmation. Keep the whole thing under 60 lines.
```

> Use this if your initial README is too short. Then trim by hand.

```text
Convert this workspace README into instructions a future AI assistant
can follow without asking me where files belong. Highlight any place
where the README leaves a behavior ambiguous.
```

> The output is most useful as a critique of the existing README, not as a replacement.

## Check Secrets and Channels

```text
Look at the planned workflows in this course (regime tool, SEC filing
RAG, multi-service architecture, scheduled agent). For each, identify
which values would be secrets, which would be access tokens, and which
can safely live in plain markdown.
```

> Useful early because it forces you to think about security boundaries before you write any code.

```text
For each planned output in my workflow map, recommend the right Zo
surface: chat, Telegram, email, hosted page, API route, or scheduled
agent. Explain in one sentence why that surface fits the output.
```

> Save the output. It feeds directly into Week 3 architecture work.

## When to Iterate

If the AI keeps asking the same clarification question, the README is missing the answer to that question. Add a sentence to the README, then rerun. After two or three rounds, the AI should stop needing to ask.
