# Architecture Design Template

Fill in each section for your AI-powered investment system.

---

## 1. System Overview

**Organization type:** [e.g., equity L/S fund, multi-asset manager, prop desk]
**Primary users:** [e.g., PMs, analysts, risk team, traders]
**Core question this system answers:** [one sentence]

---

## 2. MCP Servers

### Server 1: _______________

**Domain:** [what area does this cover?]
**Update cadence:** [real-time / daily / on-demand]
**Users:** [who accesses this?]

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| | | |
| | | |
| | | |
| | | |
| | | |

### Server 2: _______________

**Domain:**
**Update cadence:**
**Users:**

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| | | |
| | | |
| | | |
| | | |
| | | |

### Server 3: _______________ (optional)

**Domain:**
**Update cadence:**
**Users:**

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| | | |
| | | |
| | | |

---

## 3. Shared Library

| Component | Shared or Server-Specific? | Rationale |
|-----------|---------------------------|-----------|
| Data provider client | | |
| Authentication | | |
| Position sizing | | |
| Logging / audit | | |
| [your component] | | |
| [your component] | | |

---

## 4. Data Sources

| Source | Type | Primary or Fallback | Update Frequency | Staleness Detection |
|--------|------|--------------------|-----------------|--------------------|
| | | | | |
| | | | | |
| | | | | |

**Data sharing strategy:** [shared files / shared database / event-driven]

---

## 5. Deployment

**Hosting:** [cloud / on-prem / hybrid]
**Authentication:** [OAuth / API keys / SSO]
**Container strategy:** [one per server / shared / serverless]

### Cost Estimate

| Item | Monthly Cost |
|------|-------------|
| Server 1 hosting | $ |
| Server 2 hosting | $ |
| Server 3 hosting | $ |
| LLM API usage | $ |
| Data provider(s) | $ |
| **Total** | **$** |

**Comparison:** [what does this replace or complement? at what cost?]

---

## 6. Monitoring

| Check | Frequency | Alert Threshold |
|-------|-----------|----------------|
| Health endpoint | | |
| Data freshness | | |
| Auth token validity | | |
| Error rate | | |

---

## 7. Trade-offs and Decisions

### Decision 1: _______________
- **Options considered:** [A vs B]
- **Chose:** [which one]
- **Why:** [reasoning]
- **Risk:** [what could go wrong]

### Decision 2: _______________
- **Options considered:**
- **Chose:**
- **Why:**
- **Risk:**

---

## 8. Diagram

Sketch your architecture (text diagram is fine):

```
[Client: Claude Desktop / Code]
         |
         | MCP (OAuth)
         |
   ┌─────┴─────┐
   │            │
[Server 1]  [Server 2]  ...
   │            │
   └─────┬──────┘
         │
   [Shared Library]
         │
   [Data Sources]
```
