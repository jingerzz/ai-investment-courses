# Prompts: Foundations 1

Use these prompts after you draft your workflow map. They are designed for Zo chat with a general-purpose model.

## Map the Workflow

```text
Review my investment workflow map. Separate the work into five buckets: files, deterministic scripts, hosted services, dashboards, and scheduled agents. Keep the recommendation practical and identify the first two workflows I should automate.
```

```text
Look at this workflow map as an operating system design. Which parts should be durable files, which parts should be computed by tools, and which parts should stay as human judgment?
```

## Add Guardrails

```text
Identify every place in this workflow where an AI model could hallucinate, use stale data, or make an unsafe assumption. For each risk, propose a deterministic tool, source citation, or human approval step.
```

```text
Rewrite my workflow map so that the AI explains and orchestrates, but source data, prices, filing text, and calculations come from inspectable tools.
```

## Choose a Starting Point

```text
Rank these workflow components by build priority. Favor the smallest useful workflow that improves decision quality without creating operational risk.
```

```text
Turn this workflow map into a two-week build plan for a Zo workspace. Include the exact files, scripts, pages, or agents I should create first.
```
