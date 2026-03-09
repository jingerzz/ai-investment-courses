# Website Update Instructions

These instructions describe the changes made to the course materials
that need to be reflected on the website at `jing.zo.space`.

---

## Summary of Changes

The course has been restructured to follow a **"use before you build"**
pedagogy. The bonus module has been eliminated — its content is now
integrated into Week 2.

### Old Structure
- Week 1: Build an MCP server from scratch (Claude Code)
- Week 2: Add guardrails and reasoning patterns
- Bonus: Local RAG with Ollama (optional, separate)
- Week 3: System design
- Week 4: Autonomous agents

### New Structure
- **Week 1: The Tool-Use Pattern** — Install and USE pre-built servers.
  No coding. Students experience AI tools backed by real market data
  before building their own.
- **Week 2: Building Your Own AI Tools** — Build with Claude Code +
  set up Ollama + page-index-rag. Guardrails, RAG, and local models
  are all here now.
- **Week 3: System Design and Architecture** — Compose a multi-server
  system using the three servers from Weeks 1-2.
- **Week 4: Autonomous Agents and Controls** — Build a monitoring agent
  with audit trail using existing servers.
- **Bonus: REMOVED** — content absorbed into Week 2

---

## Files Changed

### Course content (update website pages from these):

| File | Website Page | What Changed |
|------|-------------|--------------|
| `prerequisites.md` | prerequisites.html | **Major rewrite.** Split into "Week 1" (minimal) and "Week 2+" (additional). Removed bonus module references. Fixed Ollama default to qwen3.5:0.8b. Added ZIP download alternative for git clone. Added external resources section. |
| `week-1/reading.md` | week-1.html | Added framing callouts: "you don't need to memorize this" before strategy section, "you won't write this code" before Python examples. |
| `week-1/exercise/README.md` | week-1.html (exercise) | Added Settings > Developer > Edit Config path for JSON editing. Added path verification step before config edit. Improved troubleshooting. |
| `week-2/reading.md` | week-2.html | Complete rewrite (unchanged from previous commit). |
| `week-2/exercise/README.md` | week-2.html (exercise) | Complete rewrite (unchanged from previous commit). |
| `week-3/reading.md` | week-3.html | Minor opening paragraph update. |
| `week-3/exercise/README.md` | week-3.html (exercise) | Rewritten to use existing 3 servers. |
| `week-4/reading.md` | week-4.html | Minor reference fixes (SPY instead of ES/MES). |
| `week-4/exercise/README.md` | week-4.html (exercise) | Rewritten to use existing servers. |
| `introduction.md` | intro page | Updated weekly progression. |
| `conclusion.md` | conclusion page | Updated week descriptions. |

---

## Prerequisites Page — Specific Changes

This is the biggest structural change on the website. The current page
front-loads too many installs before Week 1.

### New structure:

**"Software for Week 1"** (minimal, ~15 min):
1. Claude Desktop — download and sign in
2. Terminal — already on their machine, with link to tutorial
3. uv — one command
4. Course files — git clone OR ZIP download (new alternative)

**"Additional Software for Week 2"** (install later):
5. Node.js
6. Claude Code
7. Ollama with `qwen3.5:0.8b` as default (was `qwen3.5:4b`)

**Verification checklists** are split: one for Week 1 (4 items), one
for Week 2 (3 additional items).

### Remove from prerequisites page:
- All "bonus module" references
- "Software — Bonus Module" section header
- `nomic-embed-text` model pull (not needed for vectorless RAG)
- Reference to `bonus-local-rag/exercise/ollama_quickstart.md`

### Add to prerequisites page:
- ZIP download alternative for git clone
- Terminal tutorial link: [Learn Enough Command Line to Be Dangerous](https://www.learnenough.com/command-line-tutorial/basics)
- "Recommended External Resources" section with links to free courses

### Hardware table fix:
- Change "Recommended — Needed for bonus Ollama module" to
  "Recommended — Can run larger local models in Week 2"

### Data sources table fix:
- Change SEC EDGAR "Used In" from "Bonus module" to "Week 2+"

---

## Week 1 Page — Specific Changes

### Reading additions:

Two new callout blocks (render as highlighted boxes or blockquotes):

1. **Before section 1.2** (the strategy):
   > "You don't need to memorize any of this. The server handles all the
   > signal logic automatically. You're reading this so you can understand
   > what the tools are doing under the hood..."

2. **Before the code example in section 1.4** (anatomy of a tool):
   > "You'll see Python code in this section. You don't need to understand
   > it — it shows how the tools work internally. You won't write or edit
   > this code."

### Exercise changes:

**Step 3 (Connect to Claude Desktop):**
- Add note: "The easiest way: in Claude Desktop, go to Settings >
  Developer > Edit Config."
- Add path verification step before editing the config
- Add detail about the hammer icon and what to do if tools don't appear

---

## External Resources to Link

Add these as a sidebar, footer section, or "Learn More" callouts on
relevant pages. All are free and high-credibility.

### On Prerequisites page (already added to source file):

**Terminal basics:**
- [Learn Enough Command Line to Be Dangerous](https://www.learnenough.com/command-line-tutorial/basics)
- [freeCodeCamp: Command Line for Beginners](https://www.freecodecamp.org/news/command-line-for-beginners/)

**MCP deep dives (after Week 1):**
- [Anthropic: Introduction to MCP](https://anthropic.skilljar.com/introduction-to-model-context-protocol) — free official course, certificate included
- [DeepLearning.AI: MCP Build Rich-Context AI Apps](https://learn.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic/lesson/fkbhh/introduction) — free, by Andrew Ng + Anthropic
- [MCP Official Documentation](https://modelcontextprotocol.io)

**Claude Code (before Week 2):**
- [Anthropic: Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) — free official course, certificate
- [Claude Code Documentation](https://code.claude.com/docs/en/overview)

**Claude Desktop setup help:**
- [Claude Help Center: Local MCP Servers](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)
- [MCP Docs: Connect to Local Servers](https://modelcontextprotocol.io/docs/develop/connect-local-servers)

**Going further (after the course):**
- [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course/en/unit0/introduction) — free 4-unit course
- [Anthropic: MCP Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) — production patterns

### Suggested placement on website:

| Page | Resources to Feature |
|------|---------------------|
| Prerequisites | Terminal tutorial, "you'll learn more about MCP in Week 1" |
| Week 1 | MCP courses (Anthropic Skilljar, DeepLearning.AI), Claude Help Center for setup |
| Week 2 | Claude Code course and docs, Claude Code in Action |
| Conclusion | Hugging Face MCP course, MCP Advanced Topics, MCP official docs |

---

## Navigation / Table of Contents

Remove any "Bonus Module" or "Bonus: Local RAG" entries from navigation.
The course is now strictly 4 weeks with no bonus. Remove "under
construction" labels from Weeks 3-4.

Update the weekly overview/progression table anywhere it appears:
- Week 1: "The Tool-Use Pattern" (install and explore pre-built servers)
- Week 2: "Building Your Own AI Tools" (Claude Code + Ollama + RAG)
- Week 3: "System Design and Architecture" (compose multi-server system)
- Week 4: "Autonomous Agents and Controls" (monitoring agent with audit trail)

---

## Interactive Demo Update (Optional)

The current Week 1 demo uses a generic `get_position_summary("AAPL")`
example. Consider updating it to use the actual SPY/TLT tools students
will interact with — e.g., `get_current_signal()` returning a Blue
regime with a Tier 2 signal. This would make the demo feel connected
to the exercise rather than abstract.

---

## What NOT to Change

- The glossary is unchanged
- Week 3 and Week 4 readings are only lightly updated (minor reference fixes)
- The overall site layout and design direction are unchanged
