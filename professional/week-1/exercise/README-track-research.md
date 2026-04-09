# Week 1 Exercise — Stock Research Track: Steps 2–6 Alternative

> Steps 2–6 below replace the corresponding steps in the main exercise
> for the Stock Research track. Step 1 (install uv) is shared.

## Step 2: Download the Course Server (3 min)

The Page-Index RAG Course Edition server is included in your course
materials. Navigate to it:

```bash
cd ~/ai-investment-courses/professional/servers/page-index-rag-course
```

Install the server and its dependencies:

```bash
uv sync
```

This downloads Python (if needed) and installs the required packages
including `mcp`, `beautifulsoup4`, and the PageIndex engine. Takes
about 30 seconds.

Verify the server works:
```bash
uv run rag-server &
```

You should see the server start without errors. Press `Ctrl+C` to stop
it (or close the terminal).

## Step 3: Connect to Claude Desktop (5 min)

Now tell Claude Desktop where to find your server.

**Open your Claude Desktop config file:**

The easiest way: in Claude Desktop, go to **Settings > Developer >
Edit Config**. This opens the config file in your default text editor.

If that option isn't available, find the file manually:
- **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

If the file doesn't exist, create it. If it already exists and has
content, you'll add to the existing `mcpServers` section.

**Before you edit, verify your path.** In your terminal, run:

Mac:
```bash
ls ~/ai-investment-courses/professional/servers/page-index-rag-course/
```

Windows:
```
dir %USERPROFILE%\ai-investment-courses\professional\servers\page-index-rag-course\
```

You should see `pyproject.toml`, a `data/` folder, and a `config.json`
file. If you see "No such file or directory," your course files are in
a different location — find the correct path before proceeding.

**Add this to the config file** (replace `YOUR_USERNAME` with your
actual username):

Mac example:
```json
{
  "mcpServers": {
    "page-index-rag-course": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/YOUR_USERNAME/ai-investment-courses/professional/servers/page-index-rag-course",
        "run",
        "rag-server"
      ]
    }
  }
}
```

Windows example:
```json
{
  "mcpServers": {
    "page-index-rag-course": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Users\\YOUR_USERNAME\\ai-investment-courses\\professional\\servers\\page-index-rag-course",
        "run",
        "rag-server"
      ]
    }
  }
}
```

**Restart Claude Desktop** completely (quit and reopen, not just close
the window). When you start a new conversation, you should see the
page-index-rag tools available — look for a hammer icon at the bottom
of the chat input area. Click it to see the list of available tools.

**If you don't see tools after restarting,** the most common cause is a
wrong path. Double-check that the `--directory` path matches the output
from the `ls` command above.

## Step 4: Your First Conversation (5 min)

Open a new conversation in Claude Desktop and try these prompts. After
each one, observe what happens — which tools Claude calls, what data
comes back, how Claude presents it.

**Start with orientation:**
```
What document analysis tools do you have available?
```

Claude should call `get_rag_guide()` and explain the available tools
and recommended workflows.

**See what's indexed:**
```
What documents are currently indexed? Show me the full list.
```

Claude calls `list_documents()` and shows you the pre-indexed filings
for BlackRock (BLK) and Robinhood (HOOD).

**Ask your first document question:**
```
What are BlackRock's largest risk factors according to their most
recent 10-K filing?
```

Claude calls `search_with_citations()` targeting the BLK 10-K. It will
return specific passages from the Risk Factors section with citations
you can verify. Notice: every claim comes from the actual filing, not
from Claude's training data.

## Step 5: Explore the Design Principles (7 min)

Now look for the four design principles from the reading. Each prompt
below highlights a specific principle.

**Principle 1 — Pre-computed results:**
```
Show me the structural overview of the BlackRock 10-K.
```

Claude calls `get_document_overview()`. Look at the response: a
hierarchical table of contents showing every section, subsection, and
their page ranges. The server pre-computed this structure during
indexing. Claude presents it — it didn't parse the document itself.

**Principle 2 — Context metadata:**
```
Search the Robinhood 10-K for information about payment for order flow revenue.
```

Look at the citations in the response. Each passage includes a document
ID, section reference, and page number. This metadata lets you verify
every claim. Without it, you'd have no way to check whether the AI is
quoting the filing accurately.

**Principle 3 — One tool per question:**
```
How does Robinhood's revenue model differ from BlackRock's?
```

Claude calls `batch_query()` across both companies' filings — one
focused tool for cross-document analysis. It doesn't need to load
structural overviews or check indexing status.

**Principle 4 — The guide tool:**
```
What's the recommended workflow for analyzing a new company's filings?
```

Claude calls `get_rag_guide()` and returns the recommended sequence:
check if indexed → fetch filings → wait for indexing → search and
analyze. The guide orients Claude on the right tool order.

## Step 6: Try Real Analysis (7 min)

Now use the tools for actual investment analysis. These prompts go
beyond single tool calls — they show how the AI synthesizes across
multiple documents.

**Comparative analysis:**
```
Compare the competitive landscape discussions in BlackRock's 10-K
versus Robinhood's 10-K. What threats does each company identify?
```

Claude searches both filings and synthesizes the comparison. Notice
how it cites specific passages from each filing — you can trace
every claim back to the source.

**Deep dive into a specific topic:**
```
What does BlackRock's 10-K say about their iShares ETF business?
Pull the relevant sections and summarize the key metrics they report.
```

Claude may call `search_with_citations()` and then follow up with
`get_document_section()` to read specific sections in full context.

**Regulatory analysis:**
```
What regulatory risks does Robinhood disclose in their 10-K? Are any
of these risks shared with BlackRock?
```

This is where the AI adds real value — cross-referencing regulatory
disclosures across two different companies with different business
models, citing the specific language each company uses.

**Due diligence question:**
```
If I were considering investing in Robinhood, what are the three most
important things I should understand from their 10-K filing? Cite the
specific sections.
```

Claude synthesizes across the entire filing to surface the most
material disclosures, with citations for each. This is the kind of
analysis that would take an analyst hours to compile manually.

---

## What You Learned

- How to install an MCP server and connect it to Claude Desktop
- How Claude discovers and calls document analysis tools based on your questions
- How RAG (Retrieval-Augmented Generation) grounds AI responses in actual documents
- How citations let you verify every claim the AI makes
- How the guide tool orients Claude in a new session
- How Claude synthesizes across multiple documents for comparative analysis

## If You Get Stuck

**"uv: command not found"** — Close your terminal and open a new one.
The installer added `uv` to your PATH, but the current terminal doesn't
see it yet.

**"Tools don't appear in Claude Desktop"** — Make sure you restarted
Claude Desktop completely (quit the app, not just close the window).
Check that the path in `claude_desktop_config.json` points to the
correct directory.

**"Tool call failed"** — The most common cause is a wrong path in the
config file. Double-check that the `--directory` path matches where you
actually installed the course materials.

**"No documents found"** — The server comes with pre-indexed filings.
If `list_documents()` returns nothing, the data directory may not have
been included. Re-download the course files and check that
`servers/page-index-rag-course/data/indexes/` contains files.

## Next Week

In Week 2, you'll use Claude Code to **build your own** MCP server —
a watchlist tracker with a morning briefing and guardrails. You'll also
set up Ollama to run AI models locally for private document analysis.
The page-index-rag server you used today serves as your reference
implementation: when you're evaluating what Claude Code built, you can
compare it to what you've experienced here.
