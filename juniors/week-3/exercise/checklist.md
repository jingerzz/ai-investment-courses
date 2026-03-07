# Week 3: Did It Work? Checklist

Check your architecture design and multi-server setup.

---

## Architecture Design

- [ ] **2-3 servers with clear jobs.** Each server covers a distinct
  topic. You can explain in one sentence what each server does.

- [ ] **No tool belongs in two servers.** If you're unsure where a tool
  goes, your server boundaries may be unclear.

- [ ] **Shared code identified.** Common functions (stock price lookup,
  market hours check) are in a shared file, not copied into each server.

- [ ] **Each server has a guide tool.** Every server describes its own
  tools so the AI knows what's available.

## Multi-Server Setup

- [ ] **All servers run without errors.** Test each server individually
  with the MCP inspector.

- [ ] **All servers connected to Claude Desktop.** The config file has
  entries for each server.

- [ ] **Claude Desktop sees all tools.** Ask "What tools do I have?" —
  Claude should list tools from all servers.

## Cross-Server Functionality

- [ ] **Claude picks the right server.** Ask a stock question — Claude
  uses stock server tools. Ask a research question — Claude uses
  research tools.

- [ ] **Claude combines servers.** Ask something that needs both servers
  (e.g., "Tell me about Apple — stock performance and company info")
  — Claude uses tools from multiple servers.

- [ ] **Shared code works.** If both servers use shared utilities, they
  return consistent data (same prices, same timestamps).

## Design Quality

- [ ] **You made a decision.** You identified at least one choice (like
  "two servers vs. three") and can explain why you chose what you did.

- [ ] **Data sources specified.** You know which data source each server
  uses and what happens if it's unavailable.

- [ ] **Architecture template filled in.** The key sections of the
  template are complete.

---

## Questions to Ask Yourself

- If a new member joins the club, which servers do they need?
- If Yahoo Finance goes down, which servers stop working?
- If you want to add crypto tracking, does your architecture have a
  natural place for it, or do you need a new server?
- Could you explain your design to a friend in 2 minutes?
