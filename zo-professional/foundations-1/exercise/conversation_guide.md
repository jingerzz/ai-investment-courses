# Prompts: Foundations 1

These prompts are paired with the Foundations 1 exercise. Use them after you have drafted `workflow-map.md`. They work in Zo chat with any reasonable general-purpose model — you do not need a coding-grade model for this module.

Each prompt is followed by a one-line note explaining what it is for and what kind of answer you should expect.

## Map the Workflow

```text
Read AI-Investing-Course/notes/workflow-map.md. For each entry, classify it
as one of: files, tools (deterministic scripts or servers), surfaces
(hosted pages or dashboards), or scheduled agents. Identify the two
workflows that look like the strongest candidates to automate first.
```

> Use this first. The AI will assign each item to a layer and pick two starter workflows. The two it picks may not be the two you would pick — that disagreement is useful.

```text
Look at this workflow map as if you were designing an operating system for
a small investment team. Which parts should live as durable files, which
should be computed by tools, and which should remain human judgment?
```

> Use this when you want a higher-level architectural answer instead of an item-by-item assignment.

## Add Guardrails

```text
Identify every place in this workflow where an AI model could hallucinate,
use stale data, or make an unsafe assumption. For each risk, propose a
deterministic tool, source citation, or human approval step.
```

> Run this after the first prompt. The output is a punch list of places where the AI is most likely to fail you. Save it; you will refer back to it in Week 4 when you write agent specs.

```text
Rewrite my workflow map so that the AI explains and orchestrates, but
source data, prices, filing text, and calculations come from inspectable
tools. Highlight any item where I am still relying on the model for
something it should not be doing.
```

> Use this when you want to turn the punch list above into a concrete set of edits to your map.

## Choose a Starting Point

```text
Rank these workflow components by build priority. Favor the smallest
useful workflow that improves decision quality without creating
operational risk. Justify each ranking in one sentence.
```

> Useful when you have many candidate workflows and need a tiebreaker. The "in one sentence" constraint forces the AI to commit.

```text
Turn this workflow map into a two-week build plan for a Zo workspace.
Include the exact files, scripts, pages, or agents I should create first.
Each item should fit on one line.
```

> Save the result. It becomes the rough plan you will refine in Week 3 when you have seen the multi-service pattern.

## A Note on Iterating

The AI's first answer to any of these is rarely its best. Treat each response like a draft from a junior analyst — push back where the assignment seems off, ask for justification when it skips reasoning, and tell it explicitly when it is being too generic. Two or three rounds of refinement on the same prompt will usually produce a much better artifact than one fresh start.
