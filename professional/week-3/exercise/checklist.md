# Week 3: Evaluation Checklist

Evaluate your architecture design and multi-server implementation.

---

## Architecture Design

- [ ] **2-3 servers with clear boundaries.** Each server covers a distinct
  domain. You can explain in one sentence what each server does.

- [ ] **No tool belongs in two servers.** If you're unsure where a tool goes,
  your boundaries may be unclear. Redraw them.

- [ ] **Shared components identified.** Data fetching, common utilities, and
  any cross-cutting concerns are in a shared file, not duplicated.

- [ ] **Each server has a guide tool.** Every server describes its own
  capabilities so the AI knows how to use it.

- [ ] **Access makes sense.** You can articulate who needs which server.
  Not everyone needs access to everything.

## Multi-Server Setup

- [ ] **All servers run without errors.** Test each server independently
  with the MCP inspector.

- [ ] **All servers connected to Claude Desktop.** The config file has
  entries for each server.

- [ ] **Claude Desktop sees all tools.** Ask "What tools do I have?" —
  Claude should list tools from all servers.

## Cross-Server Functionality

- [ ] **Claude routes correctly.** Ask a risk question — Claude uses
  risk server tools. Ask a portfolio question — Claude uses portfolio
  tools. It doesn't mix them up.

- [ ] **Claude cross-references.** Ask a question that spans servers
  (e.g., "Give me a briefing with risk analysis") — Claude calls tools
  from multiple servers and combines the answers.

- [ ] **Shared code works.** If both servers use shared utilities,
  both return consistent data (same prices, same timestamps).

## Design Quality

- [ ] **Trade-off documented.** You identified at least one decision
  where you chose between options and can explain why.

- [ ] **Data sources specified.** You know which free data source each
  server uses and what happens if it's unavailable.

- [ ] **Architecture template filled in.** The key sections of
  `architecture_template.md` are complete.

---

## Questions to Ask Yourself

- If I add a new analyst to the team, which servers do they need?
- If yfinance goes down, which servers are affected?
- If I want to add a new tool for bond analysis, does my architecture
  have a natural home for it, or do I need a new server?
- Could I explain this architecture to my manager in 2 minutes?
