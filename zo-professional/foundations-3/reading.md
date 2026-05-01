# Foundations 3: Persistent Context for Investment AI

## F3.1 Every Analyst Keeps Notes

A research analyst three years into a coverage list does not start every meeting from scratch. They keep notes — on the company, on management's track record, on what changed last quarter, on the question they were going to ask the CFO next time. That accumulated context is most of the difference between a senior analyst and a junior one.

An AI without memory is a junior analyst on day one, every time you open a chat. It does not remember what you decided about a position last week, what you concluded about the regime in March, what your sizing rules are, or whether the watchlist you keep referencing has 12 names or 50.

You can re-explain all of this every session. Most people do, then quietly stop using AI for the workflows that need it most. The friction is what kills the use case, not the model.

A memory system fixes the floor. It does not make the AI smarter. It makes the AI start each conversation from where you left off.

> **The goal of this module:** by the end, the AI should be able to read your context at the start of every conversation, and you should be able to inspect and edit that context in plain markdown.

## F3.2 What "Memory" Means Here

There are several plausible designs for AI memory. Most production systems use vector databases, embeddings, retrieval pipelines. They are powerful, and they are expensive to maintain.

For investment workflows on Zo, the right starting design is much simpler: **a small set of plain markdown files that the AI reads at the start of every conversation, and writes to during the conversation when something worth keeping comes up.** No database. No vectors. Just files in your workspace, structured well enough that the AI can navigate them.

The reasons this works:

- **Files are inspectable.** You can open `USER.md` or `MEMORY.md` and read exactly what the AI thinks it knows about you. No black box.
- **Files are editable.** When the AI gets something wrong, you change a line. No retraining, no admin UI, no migration.
- **Files travel.** Snapshots, backups, and version control all just work, because the memory system is not a separate service — it is text in your workspace.
- **Files compose with everything else.** A research note in `notes/` and a memory entry in `memory/` are the same kind of thing. Anything that reads one can read the other.

The design trades scale for legibility. Up to a few hundred entries it works fine. By the time you reach thousands, you have a clear sense of what you actually need, and a database-backed search becomes a sensible upgrade — not a guess.

## F3.3 The Five Pieces

A complete file-based memory system has five components.

| Piece | What it holds | Who edits it |
| --- | --- | --- |
| `USER.md` | Your profile: role, communication style, hard rules | You |
| `MEMORY.md` | One-line index pointing at every memory entry | The AI |
| `memory/` | Folders of memory entries grouped by type | The AI |
| `memory/SYSTEM_CONFIG.md` | Plain-English description of the system + a "pending changes" section | You |
| Two **Rules** | Automation that reads memory at conversation start and writes during conversations | You set them once |

The split between "you edit" and "AI edits" is deliberate. You own the profile and the system spec. The AI owns the index and the entries. If you wanted to wipe the AI's memory tomorrow, you would delete `memory/` and leave `USER.md` and `SYSTEM_CONFIG.md` alone — the next session would be a clean slate that still knows who you are.

The hands-on exercise walks through creating each of these from scratch using the public quick-start guide. You do not need to memorize the structure now.

## F3.4 What Belongs in Memory

Memory works best when it is opinionated about what gets saved. The default is **less, not more**. A bloated index is harder for the AI to use than a tight one.

Four types of entry tend to earn their keep:

- **User** — durable facts about you. Your role, your firm, how you prefer to be communicated with, what you actively follow.
- **Feedback** — corrections and validated approaches. *"Don't speculate on numbers — always run the script."* *"When I ask about a setup, lead with the spy-tlt color before the stock signal."* Each one prevents you from giving the same correction twice.
- **Project** — what is currently in motion. The pitch you are working on. The position you opened last week and your thesis. The dataset you are still cleaning. These age out quickly — re-evaluate every few weeks.
- **Reference** — pointers to where things live elsewhere. *"Earnings transcripts are in Google Drive folder X."* *"The breadth dashboard is at Y."* The AI uses these to know where to look without you re-stating it.

A fifth, lighter type is the **daily note**. After a substantive conversation, the AI saves a one-page summary under `memory/daily/YYYY-MM-DD.md`. Days when you did real work leave a trace; days you did nothing leave nothing.

What does **not** belong in memory:

- Anything you can re-derive by reading the workspace. The current folder structure, what scripts exist, what models are configured.
- The full text of a research note. Save the note in `notes/`; save a one-line memory entry pointing at it.
- The contents of a filing. The SEC RAG server already indexes those.
- A long log of every chat. Memory is curated context, not a transcript.

When in doubt, ask: *would I actually want a future me to read this in three months?* If yes, save it. If no, let it go.

## F3.5 How the System Grows

The system has two ways to capture memories, both driven by Rule 2.

**Reactive capture.** When you say something that matches a clear trigger — a preference, a project update, a correction — the AI saves the entry without being asked. You say *"I only act on a setup if the risk/reward is at least 2-to-1"* and a `memory/feedback/` file appears. You do not have to remember to ask.

**Proactive offer.** When a conversation produces meaningful work but does not trigger reactive capture, the AI asks: *"Want me to save a note on this?"* You answer yes or no. If yes, a daily note lands in `memory/daily/`. The friction is one word.

Together, the two modes mean you do not have to remember to maintain memory — the AI does. Your job is to occasionally edit `SYSTEM_CONFIG.md` when you want the system itself to change.

## F3.6 Memory and the Guardrail Pattern

The guardrail pattern from Foundations 1 was: **AI should explain and orchestrate. Code should compute. Sources should substantiate. Humans should decide.** Memory reinforces every part of that — without changing the pattern.

- **Explanation gets better with context.** An AI that knows your firm's risk tolerance produces a different summary than one that does not.
- **Computation does not get cheated.** Memory is not where the math lives. The price still comes from a quote tool, not from a memory entry.
- **Sources still substantiate.** A memory note saying *"we concluded NVDA's exposure to TSMC is the key risk"* is not a citation. The 10-K passage you cited last quarter is still the source. The memory entry just tells the AI *that* you cited it.
- **Decisions are still yours.** A memory entry is not authority to act. It is context that informs the next decision.

A useful way to think about memory is that it gives the AI a longer **working horizon** without giving it more **authority**. It can connect a conversation today to a conclusion you reached last month — but it still has to call tools to refresh data, cite filings to substantiate claims, and ask before acting on capital.

## F3.7 Memory in Investment Practice

Three concrete examples of how memory pays for itself in this course's workflows.

**Regime continuity.** You ask the AI on Monday to assess SPY/TLT. It runs the regime tool, reports Orange, and writes a daily note. On Friday you ask *"what changed since Monday?"* The AI reads the daily note, runs the regime tool again, and gives you a delta. Without memory, the comparison is on you.

**Thesis tracking.** You open a position in NVDA on a Wednesday after a long discussion of the supply concentration risk. The AI saves a project entry with the thesis, the trigger, and the invalidation level. Three weeks later, when something material changes, the AI flags it against the original thesis instead of treating the position as a stranger.

**Filing follow-ups.** You read a 10-K passage about a company's customer concentration and tell the AI you want to revisit this on the next 10-Q. A memory entry captures the question. When the next 10-Q is indexed, asking *"any update on the question I had about customer concentration?"* returns a real answer instead of a *"could you remind me what you were tracking?"*

In each case, memory is doing the same work a notebook does for an analyst: turning a series of single conversations into a coherent thread.

## Key Takeaways

- **Memory is the difference between a senior and a junior analyst.** An AI without it is junior every time.
- **File-based is the right starting design.** Inspectable, editable, version-controlled, no infrastructure to maintain.
- **Five pieces, two roles.** `USER.md` and `SYSTEM_CONFIG.md` are yours; `MEMORY.md` and the entries belong to the AI.
- **Save what a future you would want to read.** Skip what can be re-derived.
- **Two capture modes.** Reactive on clear triggers; proactive offer when the conversation merits it.
- **Memory does not change the guardrail pattern; it sharpens it.** Longer working horizon, no extra authority.
