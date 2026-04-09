# Foundations 2: Claude on Desktop and Mobile — Your Workspace Setup

---

## F2.1 Why Desktop and Mobile?

In Foundations 1, you used Claude through a web browser. That works
fine for quick conversations. But for the work ahead — connecting
real data tools, analyzing documents, building workflows — you need
a proper workspace.

Claude comes in three forms:

- **claude.ai (web)** — Quick access from any browser. Good for one-off
  questions, light research, sharing a conversation link with a colleague.
  Think of it as your Bloomberg terminal's web client.

- **Claude Desktop (Mac/Windows app)** — Your primary workstation. Same
  Claude, but with one critical capability the browser doesn't have:
  **MCP server connections.** In Week 1, you'll connect Claude Desktop
  to a live trading strategy that feeds it real market data. That only
  works in the desktop app.

- **Claude Mobile (iOS/Android)** — Your field notebook. Same account,
  same projects. Best for quick lookups, voice input, and continuing
  conversations you started on desktop. Not ideal for heavy analysis,
  but valuable when you're away from your desk.

Why does this matter? Because the entire arc of this course — connecting
Claude to market data, building custom tools, designing multi-server
systems — runs through Claude Desktop. If you only use the browser,
you'll hit a wall in Week 1. Installing the desktop app now means
Week 1 is setup, not troubleshooting.

The three platforms share everything: your account, your projects,
your conversation history, your custom instructions. Work you do in
one place is available everywhere. The difference is capability, not
content.

---

## F2.2 Installing Claude Desktop

### Download and Install

1. Go to [claude.ai/download](https://claude.ai/download).
2. Download the installer for your platform (Mac or Windows).
3. Run the installer. On Mac, drag Claude to Applications. On Windows,
   follow the standard install wizard.
4. Open Claude Desktop and sign in with the same Anthropic account you
   used on claude.ai.

That's it. You should see a clean conversation window that looks
similar to the web interface but feels snappier.

### Quick Tour of the Interface

The desktop app has a few elements worth noting:

- **Sidebar (left):** Your conversation history and project list.
  Click any conversation to resume it. Click a project to scope your
  work.
- **Project selector:** At the top of the sidebar. Switch between
  projects to change context. Each project carries its own custom
  instructions.
- **Model selector:** Choose which Claude model to use. For this
  course, the default model works fine.
- **Attachment button:** The paperclip icon in the message bar. This
  is how you'll add PDFs, CSVs, images, and other files to your
  conversations.
- **Settings (gear icon):** General preferences, account info, and —
  critically — the **Developer** menu.

### The Developer Menu

Open **Settings > Developer**. You'll see a section for MCP server
configuration. Right now, it's empty. In Week 1, you'll add a
configuration here that connects Claude to a live trading strategy
server. For now, just note where it lives.

Think of it like this: the Developer menu is where you plug in your
data feeds. The browser version of Claude doesn't have this menu.
That's the fundamental reason we're installing the desktop app.

---

## F2.3 Projects Across Devices

You already created a project in Foundations 1. If you open Claude
Desktop now and check the sidebar, that project should be there —
along with its custom instructions and conversation history. This
sync happens automatically through your Anthropic account.

### What Syncs

- Projects and their names
- Custom instructions (the system-level context you set for each project)
- Conversation history within each project
- Starred or bookmarked conversations

### What Doesn't Sync

- MCP server connections (these are local to Claude Desktop on a
  specific machine — the config file lives on your hard drive)
- Files on your local disk that you've referenced in conversations

### A Practical Workflow

Here's a pattern that works well for investment professionals:

1. **Desktop (morning):** Open your "Equity Research" project. Upload
   an earnings transcript. Have a detailed conversation analyzing
   guidance, margins, and capital allocation. Claude remembers the
   full context.

2. **Mobile (commute or meeting):** Open the same project on your phone.
   Ask "What were the three biggest risks management highlighted in
   that transcript?" Claude has the full conversation history and
   answers immediately.

3. **Web (quick check):** At a colleague's desk, open claude.ai in
   a browser. Pull up the same project to reference a point from
   your earlier analysis.

The project is the container. The device is just the access point.

---

## F2.4 Working with Attachments

One of the most practical capabilities for investment work: you can
give Claude documents to read and analyze. This turns a generic AI
assistant into something closer to a junior analyst who actually
reads the source material.

### How to Add Files

- **Desktop:** Drag and drop a file directly into the conversation,
  or click the paperclip icon to browse. You can add multiple files
  to a single message.
- **Mobile:** Tap the attachment icon and select files from your
  device. Works with files stored locally, in iCloud, or in Google
  Drive.
- **Web:** Click the paperclip icon or drag and drop.

### Supported Formats

| Format | Best For |
|--------|----------|
| **PDF** | Earnings reports, 10-Ks, research notes, pitch books |
| **CSV** | Price data, portfolio holdings, transaction history |
| **Images** (PNG, JPG) | Chart screenshots, whiteboard photos, slide decks |
| **Text files** (.txt, .md) | Notes, meeting minutes, model assumptions |
| **Code files** (.py, .json, etc.) | Configuration files, scripts (relevant in later weeks) |

### Tips for Finance Documents

**Earnings PDFs:** Upload the full transcript or press release. Ask
Claude to extract specific metrics: "What was free cash flow guidance
for FY25?" or "Compare gross margins to last quarter." Claude reads
the actual document — it's not guessing from training data.

**Spreadsheet data:** Save a sheet as CSV before uploading. Claude
handles tabular data well: "Which positions have the highest
concentration risk?" or "Calculate the weighted average P/E of this
portfolio."

**Chart screenshots:** Take a screenshot of a chart from your
Bloomberg terminal, TradingView, or broker platform. Ask Claude to
describe what it sees: "What pattern do you see in this chart?" or
"Is this a head-and-shoulders formation?" Note: Claude can describe
visual patterns, but it cannot read exact pixel-level values from
charts. Pair chart screenshots with the underlying data when
precision matters.

### Size Limits and Workarounds

Claude can handle substantial documents — a typical 10-K or earnings
transcript is well within limits. For very large documents (100+
pages), consider:

- Uploading just the relevant sections (MD&A, risk factors, financial
  statements)
- Splitting the document across multiple messages
- Asking Claude to focus on specific sections: "Read pages 45-60 and
  summarize the segment reporting"

---

## F2.5 The Claude Mobile App

### Getting Started

1. Download from the [App Store](https://apps.apple.com/app/claude/id6473753684)
   (iOS) or [Google Play](https://play.google.com/store/apps/details?id=com.anthropic.claude)
   (Android).
2. Sign in with your Anthropic account.
3. Your projects and conversations appear automatically.

### What Works Well on Mobile

**Quick questions with existing context.** If you've been analyzing
a company on desktop, you can ask follow-up questions on mobile
without re-uploading anything. The conversation history is already
there.

**Voice input.** Use your phone's dictation to speak your prompts
instead of typing. This is surprisingly effective for analytical
questions: "What's the bull case for this stock based on what we
discussed?" is faster to speak than type.

**Morning prep.** Before you sit down at your desk, ask Claude to
summarize where you left off yesterday. "What were the key takeaways
from our analysis of MSFT's earnings?" while you're getting coffee.

**Meeting follow-up.** After a portfolio review meeting, dictate your
notes into Claude: "Here are my notes from the investment committee
meeting. Can you organize these into action items and flag anything
that contradicts our earlier analysis?"

### What's Better on Desktop

**Long documents.** Reading and analyzing a 50-page 10-K is a desktop
task. The larger screen, easier file management, and ability to drag
and drop files make desktop the right choice for document-heavy work.

**Complex multi-step analysis.** If you're building a thesis that
requires multiple attachments, several rounds of back-and-forth, and
detailed numerical work — do it on desktop.

**MCP tool connections.** Only Claude Desktop supports connecting to
external data servers. Your live market data tools (Week 1 and beyond)
only work on desktop.

### The Right Mental Model

Mobile isn't a lesser version of desktop. It's a different tool for
different moments. A portfolio manager who reviews analysis on the
train, a trader who checks a thesis before placing an order, an
analyst who captures an idea between meetings — these are all
legitimate use cases that desktop can't serve.

---

## F2.6 Building Your Workspace

Now that you have Claude on every device, the question is: how do you
organize your work? The answer is projects — and the key is making
each project focused enough to be useful.

### Recommended Project Structure

Here's a starting point for an investment professional. You don't need
all of these — pick the ones that match your role:

**"Equity Research"** — For company-specific analysis, earnings
reviews, competitive comparisons.

Custom instructions example:
```
I'm an equity analyst covering technology stocks. When I share
earnings data or financial documents, extract key metrics and
compare them to prior periods. Flag anything that deviates
significantly from consensus or historical trends.

Always note the source and date of any data you reference.
If I ask about a company, use only the documents I've provided
in this conversation — don't rely on training data for specific
financial figures.
```

**"Macro / Rates"** — For interest rate analysis, economic data
interpretation, cross-asset themes.

Custom instructions example:
```
I focus on macro strategy and fixed income. Help me interpret
economic data releases, Fed communications, and cross-asset
signals. When I share data, present it in the context of the
current rate cycle.

Be precise with basis points and percentage changes. Don't
round unless I ask you to.
```

**"Portfolio Review"** — For position-level analysis, risk assessment,
rebalancing decisions.

Custom instructions example:
```
I manage a multi-asset portfolio. When I share holdings data,
calculate concentration metrics, sector exposures, and factor
tilts. Flag positions that exceed 5% of the portfolio.

Present risk metrics clearly: max drawdown, Sharpe ratio, and
correlation to SPY. When suggesting changes, always note the
tax implications.
```

**"Compliance / Ops"** — For regulatory questions, policy drafts,
operational workflows.

Custom instructions example:
```
I work in investment compliance. Help me draft policies, review
procedures, and interpret regulatory requirements. When I share
regulatory text, summarize the key obligations and deadlines.

Be conservative in interpretations. When something is ambiguous,
flag it rather than assuming.
```

### Iterating on Instructions

Your first set of custom instructions will be imperfect. That's fine.
Use this process:

1. Start with basic instructions (role, preferences, constraints).
2. Use the project for a few conversations.
3. Notice when Claude does something you don't like — gives too much
   detail, uses the wrong format, makes wrong assumptions.
4. Update the instructions to address those patterns.
5. Repeat.

This is exactly like onboarding a new analyst. You don't hand them a
50-page manual on day one. You give them basic guidance, observe their
work, and refine expectations over time.

---

## Key Takeaways

1. **Claude Desktop is not optional for this course.** The MCP tool
   connections that power Week 1 through Week 4 only work in the
   desktop app. Install it now.

2. **Projects are your organizational unit.** Create focused projects
   with clear custom instructions. They sync across all devices.

3. **Attachments turn Claude into a document analyst.** Upload earnings
   transcripts, spreadsheets, and research notes. Claude reads the
   actual content — it's not guessing.

4. **Mobile extends your workspace.** Use it for follow-up questions,
   voice input, and capturing ideas on the go. Don't try to do
   heavy analysis on your phone.

5. **The Developer menu is your Week 1 on-ramp.** You don't need to
   touch it yet, but knowing where it is means you're ready when
   the time comes.

6. **Custom instructions improve with use.** Start simple, observe
   what works, and refine. The best instructions come from real
   interactions, not upfront planning.
