# Checklist: Week 3

Use this to evaluate your multi-service architecture.

## Architecture Basics

- [ ] **The workflow supports one specific investment decision.**
- [ ] **Inputs are named exactly, not generically.**
- [ ] **Each component has a narrow job.**
- [ ] **No component is doing work that belongs somewhere else.**

## Zo Surface Mapping

- [ ] **Durable notes belong in files.**
- [ ] **Exact computation belongs in scripts or services.**
- [ ] **Source document retrieval belongs in a RAG tool.**
- [ ] **Human-readable state belongs on a page or dashboard.**
- [ ] **Scheduled checks belong in agents only after the manual flow works.**

## Controls

- [ ] **Human approval points are explicit.**
- [ ] **Private versus public outputs are labeled.**
- [ ] **At least three failure modes are documented.**
- [ ] **The audit trail records inputs, outputs, and decisions.**

## Ready for Week 4

- [ ] **You have a module-level architecture template filled in.**
- [ ] **You know which part could become a scheduled agent.**
- [ ] **You know what the agent must not be allowed to do.**
