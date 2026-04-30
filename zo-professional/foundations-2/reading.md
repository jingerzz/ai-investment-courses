# Foundations 2: Setting Up the Investment Workspace

Your Zo workspace should make the right thing easy: keep source material, code, outputs, and decisions in predictable places.

## Workspace Design

Use plain folders and plain files. Fancy organization usually fails because it is hard to maintain.

Recommended structure:

| Folder | Purpose |
| --- | --- |
| `notes/` | research notes, prompts, decision logs |
| `servers/` | local copies of course or custom MCP servers |
| `datasets/` | data files, DuckDB databases, CSVs |
| `dashboards/` | page specs, screenshots, chart notes |
| `agents/` | scheduled workflow specs and run logs |

The AI should be able to infer where something belongs without asking every time.

## Secrets

Secrets belong in Zo settings, not in code.

Examples:

- API keys
- bearer tokens
- webhook secrets
- provider credentials

Course examples use free sources where possible. When a production workflow needs credentials, store them as environment variables and read them from scripts.

## Channels

Zo can talk to you through chat, Telegram, email, and other channels depending on your setup.

For investment workflows, channel choice matters:

- Chat is best for interactive building.
- Telegram is useful for short alerts.
- Email is useful for longer reports.
- Hosted pages are useful for repeatable dashboards and shareable research.

## Browser and Hosting

Zo can use a browser session for research and can host pages or services. That means a workflow can move from "I asked a question" to "I have a durable internal tool" without leaving the environment.

The course uses this progression repeatedly.

