# Prompts: Week 1

Use these prompts while inspecting and running the SPY/TLT course server from Zo.

## Inspect the Server

```text
Inspect the SPY/TLT course server. Summarize the tool interface, the data inputs, and the exact outputs each tool returns. Separate deterministic computation from AI explanation.
```

```text
Read the SPY/TLT course server README and main implementation. Explain the recommended tool-use flow a student should follow.
```

## Run and Interpret

```text
Run the available SPY/TLT course checks. Report the regime output exactly as returned by the tool, including timestamps and stale-data warnings. Then explain what a human investor should review before acting.
```

```text
Compare the current regime output to the professional standard from the reading: regime, data freshness, levels, invalidation, and human decision point.
```

## Understand the Teaching Subset

```text
Compare this course server to the production-style architecture described in the course. What is intentionally simplified, and why is that useful for learning?
```

```text
Identify any place where a model might be tempted to invent a signal. Rewrite the workflow so the tool output remains the source of truth.
```
