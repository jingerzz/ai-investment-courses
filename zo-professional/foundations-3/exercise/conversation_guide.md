# Prompts: Foundations 3

These prompts make memory active in your investment workflow. Run them after you have completed the quick-start setup.

A general-purpose chat model is fine for all of these.

## Inspect the System

```text
Show me what is currently in /home/workspace/USER.md and /home/workspace/MEMORY.md.
For each entry in MEMORY.md, give me a one-line summary of what it captures.
Then tell me which entries look thin or stale and could be improved.
```

> Use this once a week. Early on, expect the answer to be small and tidy. Over time it grows.

```text
List every file under /home/workspace/memory/ grouped by subfolder. For each
file, print the frontmatter (name, description, type). Do not read the bodies.
```

> The output is a quick visual map of your memory state. If a folder is empty for weeks, consider whether you actually need it.

## Add or Refine an Entry

```text
I want to add a feedback entry: when I ask for a SPY/TLT view, always lead with
the color day, then exposure, then a one-line rationale. Why: I read these on
the phone and need the headline first.

Create the appropriate memory entry with the right frontmatter. Add a one-line
entry to MEMORY.md. Confirm when done.
```

> Every time you correct the AI's format, ask whether it is worth saving as feedback. Half the time it is.

```text
The project entry at /home/workspace/memory/projects/ai-investing-course.md is
now out of date — I have completed Week 2. Update it to reflect the current
state and update MEMORY.md if needed.
```

> Project entries decay fast. Keep them current or trim them.

## Use Memory in a Workflow

```text
Read the project memory for AI-Investing-Course. Based on what I have completed
and what is still pending, propose what we should work on in this session. Keep
the proposal under five lines.
```

> The AI uses memory to plan. The plan is only as good as the memory.

```text
What did we conclude about [a ticker you have discussed] the last time we
discussed it? Cite the daily note(s) you read.
```

> Tests both Rule 1 (memory read) and the citation discipline. The AI should name a specific file, not paraphrase from training.

## Maintain the System

```text
Read /home/workspace/MEMORY.md. If it has more than 50 entries or feels noisy,
propose a consolidation: which entries can be merged, archived, or deleted, and
why. Do not make changes yet — just propose.
```

> Run this every couple of months. Memory hygiene compounds.

```text
I want a new memory folder type: memory/positions/, where you save the thesis,
trigger, invalidation, and time horizon for any open position I tell you about.
Update SYSTEM_CONFIG.md and MEMORY.md, and create the folder. Confirm.
```

> Use `SYSTEM_CONFIG.md` as the spec; the AI applies the change. Repeat the pattern any time the structure needs to evolve.

## When to Iterate

If the AI keeps surfacing the same correction, the feedback memory entry is missing or wrong. Read the relevant entry, sharpen the *Why* and *How to apply* lines, and the correction usually stops being needed.
