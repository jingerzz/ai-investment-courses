# Checklist: Week 4

Use this to evaluate your controlled investment agent design.

## Agent Scope

- [ ] **The agent has one clear job.**
- [ ] **The schedule is justified by the workflow.**
- [ ] **Allowed inputs are explicit.**
- [ ] **Allowed tools are explicit.**
- [ ] **The output format is short enough to review.**

## Controls

- [ ] **The agent cannot place trades.**
- [ ] **The agent cannot change strategy rules without approval.**
- [ ] **The agent cannot publish personal or portfolio-specific information by default.**
- [ ] **External messages, service edits, public posts, and automation changes have approval boundaries.**
- [ ] **Failure states are visible rather than hidden.**

## Audit Trail

- [ ] **Each run records timestamp, inputs, tools used, outputs, and errors.**
- [ ] **The audit log distinguishes observation from recommendation.**
- [ ] **The human decision is recorded separately from the AI output.**

## Course Completion

- [ ] **You can explain the full loop: agent observes, tools compute, sources substantiate, AI summarizes, human decides, system records.**
- [ ] **You have one practical agent spec that could be built later.**
- [ ] **You can describe why automation is useful only when the control boundary is clear.**
