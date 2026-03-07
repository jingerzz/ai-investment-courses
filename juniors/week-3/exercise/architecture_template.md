# Architecture Design Template

Fill in each section for your AI-powered stock system.

---

## 1. System Overview

**What is this for?** [e.g., school stock club, personal investing tracker]
**Who uses it?** [e.g., club members, research team, club president]
**Main goal:** [one sentence — what does this system help people do?]

---

## 2. Servers

### Server 1: _______________

**What it does:** [what area does this cover?]
**Who uses it:** [who needs this?]

| Tool | What It Does |
|------|-------------|
| | |
| | |
| | |
| | |
| | |

### Server 2: _______________

**What it does:**
**Who uses it:**

| Tool | What It Does |
|------|-------------|
| | |
| | |
| | |
| | |
| | |

### Server 3: _______________ (if needed)

**What it does:**
**Who uses it:**

| Tool | What It Does |
|------|-------------|
| | |
| | |
| | |

---

## 3. Shared Code

What goes in the shared file that all servers use?

| Component | Why It's Shared |
|-----------|----------------|
| Stock price lookup | |
| Market open/closed check | |
| Error handling | |
| [your item] | |
| [your item] | |

---

## 4. Data Sources

| Source | What It Provides | What If It's Down? |
|--------|-----------------|-------------------|
| | | |
| | | |
| | | |

---

## 5. Access (Who Needs What?)

| Person/Role | Server 1 | Server 2 | Server 3 |
|-------------|----------|----------|----------|
| | | | |
| | | | |
| | | | |

---

## 6. Decisions You Made

### Decision 1: _______________
- **Options:** [what did you consider?]
- **You chose:** [which option]
- **Why:** [your reasoning]

### Decision 2: _______________
- **Options:**
- **You chose:**
- **Why:**

---

## 7. Diagram

Draw your system (text diagram is fine):

```
[Claude Desktop]
       |
       | connects to
       |
  ┌────┴────┐
  |          |
[Server 1]  [Server 2]  ...
  |          |
  └────┬─────┘
       |
 [Shared Code]
       |
 [Data Sources]
```
