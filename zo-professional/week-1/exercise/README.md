# Exercise: Run the SPY/TLT Course Server from Zo

## Goal

Use Zo to inspect and run the SPY/TLT teaching server, then ask AI questions backed by tool output.

## Source Server

Use the updated course server:

`professional/servers/spy-tlt-course`

Do not copy production-only assumptions into the course server. The course version is intentionally smaller.

## Steps

1. In Zo, open the course repo.
2. Inspect the SPY/TLT server folder.
3. Read its `pyproject.toml` and main server file.
4. Run the server's available command-line checks.
5. Ask Zo to explain what tools the server exposes.
6. Ask Zo to compare the current output to the design pattern from the reading.

## Prompts to Use

```text
Inspect the SPY/TLT course server and summarize the tool interface. Which outputs are computed deterministically, and which parts should the AI only explain?
```

```text
Run the available SPY/TLT course checks. Report the current regime output exactly as returned by the tool, then explain what a human investor should review before acting.
```

## Checkpoint

You are done when you can identify:

- the data inputs
- the tool outputs
- the stale-data guardrail
- the difference between tool computation and AI explanation
- why the course server is smaller than the production server
