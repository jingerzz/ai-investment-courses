# Handoff: AI Limitations & Verification Content — Website Updates

## Overview

New content about AI hallucinations, numerical errors, and verification discipline
has been added to the **markdown source files** on branch `ai-limitations-content`.
This handoff provides precise instructions for updating the **HTML website files**
(`professional/site/*.html`) to match.

**Branch:** `ai-limitations-content` (in the `ai-investment-courses` repo)
**Markdown source of truth:** The reading.md files already contain all new content.
**Your job:** Update the corresponding HTML files to include this content.

## Important Context

- The HTML files are NOT auto-generated from markdown — they are hand-crafted HTML
  that follows a consistent pattern (see HTML Conventions below).
- The markdown source and HTML versions diverge in structure (HTML has tabs, exercises,
  demos, callouts). The HTML is the more polished version.
- CSS is loaded from `css/course.css` (served by zo.space). You do NOT need to modify CSS.
- The site is served at `https://jing.zo.space/course-v2` via an iframe shell.

## HTML Conventions (follow these exactly)

### Element patterns used in the existing HTML:
- **Section headers:** `<h2>` for major sections, `<h3>` for subsections
- **Body text:** `<p>` tags, no classes needed
- **Bold terms:** `<strong>` inside `<p>`
- **Inline code:** `<code>` (e.g., `<code>stale_data_warning</code>`)
- **Callout boxes:** `<div class="callout"><div class="callout-title">Title</div><p>Content</p></div>`
- **Warning/guardrail callouts:** `<div class="callout callout-guardrail">...</div>`
- **Tables:** Plain `<table>` with `<thead>` and `<tbody>`, no classes
- **Ordered lists:** `<ol style="margin-left: 1.5rem; margin-bottom: var(--md);">`
- **Unordered lists:** `<ul>` (no special styles needed)
- **Key Takeaways:** Wrapped in `<div class="takeaways"><h3>Key Takeaways</h3><ol>...</ol></div>`
- **Em-dashes:** Use `—` (literal character), not `&mdash;`

### Style guidelines:
- Indent HTML consistently (2 spaces per level, matching surrounding code)
- Keep paragraph text as flowing prose — no line breaks within `<p>` tags
- Use `<strong>` for the lead term in definition-style paragraphs (e.g., `<p><strong>The handle error.</strong> An AI quoting...`)

---

## Change 1: Foundations 1 — New "How AI Gets Things Wrong" Section

**File:** `professional/site/foundations-1.html`

**Location:** AFTER the "Fundamental Tension" callout box (currently around line 63), BEFORE the `<h2>The Context Window</h2>` heading (currently around line 65).

**What to insert:** A new `<h3>` subsection with 5 failure mode descriptions and a framing callout.

**Exact HTML to insert between the closing `</div>` of the "Fundamental Tension" callout and `<h2>The Context Window</h2>`:**

```html
        <h3>How AI Gets Things Wrong</h3>

        <p>Before we go further, you need a mental model for the specific ways AI fails in investment contexts. These aren't theoretical — they're patterns you will encounter, and recognizing them is a core skill.</p>

        <p><strong>Stale magnitude errors.</strong> AI may quote the S&P 500 index in the 5,000s when it's actually trading in the 6,000s. This happens because the model's training data reflects an earlier period. The format looks correct — it's a plausible number for an index level — which makes it dangerous. You won't get a 6-digit number that's obviously wrong. You'll get a 4-digit number that <em>was</em> right six months ago.</p>

        <p><strong>Confabulated company facts.</strong> AI will confidently state that a company made an acquisition that never happened, name a wrong CEO, or cite a financial metric that doesn't match reality. The language is fluent and authoritative — there's nothing in the tone that signals "I'm making this up." This is called <em>hallucination</em>, and it's an inherent property of how language models work: they generate plausible text, and sometimes plausible text is wrong.</p>

        <p><strong>Hallucinated reasoning chains.</strong> This is the most dangerous failure mode. The AI builds an investment thesis on a premise that is simply false — "Given that Company X recently acquired Y..." when no such acquisition happened. The logic from that point forward is internally consistent and may even be insightful. But the foundation is fabricated, and the conclusion is worthless. The reasoning <em>quality</em> masks the data <em>quality</em> problem.</p>

        <p><strong>Numerical plausibility traps.</strong> The AI generates numbers that are in the right ballpark but wrong — revenue of $4.2B when it's actually $6.8B, or a P/E ratio of 18 when it's actually 28. These are close enough to not trigger alarm bells, but wrong enough to change an investment decision. Unlike a blatant error, a plausible-but-wrong number can survive casual review.</p>

        <div class="callout callout-guardrail">
          <div class="callout-title">The Core Problem</div>
          <p>AI does not signal uncertainty the way humans do. A hallucinated fact and a correct fact are presented with identical confidence. There is no "I'm guessing" flag. This means the burden of verification falls entirely on you, and you need to know where to look.</p>
          <p>Throughout this course, you'll learn engineering solutions to many of these problems — tools that feed live data to AI, guardrails that prevent it from doing math, templates that lock in exact numbers. But the engineering only works if you also develop the habit of critical verification. The tools are the first line of defense. You are the second.</p>
        </div>
```

---

## Change 2: Foundations 1 — New Key Takeaway bullet

**File:** `professional/site/foundations-1.html`

**Location:** Inside the `<div class="takeaways">` section, AFTER the last `<li>` (currently the "Prompting for finance is about precision" bullet), BEFORE the closing `</ol>`.

**Currently the last item is (around line 211):**
```html
            <li><strong>Prompting for finance is about precision.</strong> Specify timeframes, instruments, and analysis types. Tell Claude your framework. Ask it to show its reasoning so you can evaluate where the logic is sound and where the data might be stale.</li>
```

**Insert this new `<li>` after it:**

```html
            <li><strong>AI fails silently — verification is your responsibility.</strong> AI presents hallucinated facts with the same confidence as correct ones. Any specific number, date, name, or claim from AI output should be verified against a primary source before you act on it. This habit matters more than any technical feature.</li>
```

---

## Change 3: Week 1 — "Why These Patterns Exist" Subsection

**File:** `professional/site/week-1.html`

**Location:** AFTER the "Order execution" paragraph (around line 402), BEFORE the Key Takeaways section (around line 404).

**Currently:**
```html
        <p><strong>Order execution:</strong> The AI should never directly place trades. It proposes; a separate system (with human approval) executes. We'll cover this in Week 4.</p>

        <!-- Key Takeaways -->
```

**Insert this between them:**

```html
        <h3>Why These Patterns Exist: Connecting Back to AI Failure Modes</h3>

        <p>In Foundations 1, you learned the specific ways AI gets things wrong in investment contexts — stale magnitudes, confabulated facts, hallucinated reasoning chains, numerical plausibility traps. The tool-use patterns you learned this week are direct engineering responses to those failure modes:</p>

        <table>
          <thead>
            <tr><th>Failure Mode</th><th>Tool Design Response</th></tr>
          </thead>
          <tbody>
            <tr><td>Stale magnitude errors (SPX in 5,000s vs 6,000s)</td><td>Tools call live APIs — AI never relies on training-data prices</td></tr>
            <tr><td>Confabulated company facts</td><td>Tools return structured data from authoritative sources — AI interprets, doesn't invent</td></tr>
            <tr><td>Hallucinated numbers (12% vs 1.2%)</td><td>Python pre-computes all math — AI never calculates</td></tr>
            <tr><td>Plausible-but-wrong numbers</td><td>Pre-formatted templates lock in exact figures — AI presents them verbatim</td></tr>
            <tr><td>Stale data presented as current</td><td><code>stale_data_warning</code> field flags when data isn't fresh</td></tr>
          </tbody>
        </table>

        <p>This isn't accidental. Every design principle in this course exists because of a specific failure mode that was observed in practice. When you build your own tools in Week 2, you'll implement these patterns yourself.</p>

```

---

## Change 4: Week 2 — Real-World Errors + Verification Discipline

**File:** `professional/site/week-2.html`

**Location:** This is the trickiest change because week-2.html has a different structure than the reading.md. The HTML doesn't have a section called "Guardrails: Preventing AI Math Errors" in the same way — it's woven into the exercises and prompt engineering sections.

**Strategy:** Add two new subsections in the **Reading tab** area, after the existing guardrails/prompt-engineering content and before the exercise section. Look for the transition point between reading content and exercise content.

Search for the `<h2>` that begins the exercise portion of the reading tab. The new content should go BEFORE the exercise heading.

**Specifically:** Find the section where the reading content about guardrails ends. Search for the text about "Describing Guardrails" (around line 555-556) — the new sections should go AFTER the guardrails description content and BEFORE the testing/checklist sections.

**IMPORTANT:** Because week-2.html's structure diverges from the reading.md, you need to find the best insertion point by reading the file. Look for a natural break after guardrail concepts are discussed and before exercises begin. The content below should be inserted there.

**HTML to insert:**

```html
        <h3>Real-World Errors That Guardrails Catch</h3>

        <p>The patterns above aren't theoretical. Here are errors observed in practice with financial AI systems:</p>

        <p><strong>The handle error.</strong> An AI quoting the S&P 500 in the 5,000s when the index is trading in the 6,000s. This happens because the model's training data distribution includes a period when the 5,000 level was current. The number has the right format and the right number of digits — it just reflects a different era. A pre-formatted template with a live API price eliminates this entirely.</p>

        <p><strong>Cross-asset confusion.</strong> ES futures (~6,800) and the SPY ETF (~$670) track the same index but differ by roughly 10x. AI sometimes conflates them because they're contextually similar — both represent "the S&P 500." If your tool returns an ES level and the AI presents it as a SPY price (or vice versa), position sizing could be off by an order of magnitude. The fix: tools should include the <code>instrument</code> field in every return value so the AI knows exactly which asset it's quoting.</p>

        <p><strong>Hallucinated comparisons.</strong> A tool returns correct Q3 earnings data. The AI, wanting to add context, "remembers" the Q2 number for comparison — but the remembered number is wrong. The trend analysis looks reasonable, but the baseline is fabricated. The fix: if your tool wants the AI to discuss trends, pre-compute the comparison yourself (return both <code>current_quarter</code> and <code>prior_quarter</code> fields, plus a <code>change_pct</code> field). Don't leave gaps that invite the AI to fill in from memory.</p>

        <p><strong>Confidently wrong thesis construction.</strong> The AI builds an investment case starting from a false premise — "Given that Company X generates 40% of revenue from China..." when the real figure is 12%. Every conclusion that follows is internally consistent and sounds smart. The premise was hallucinated. This is the hardest error to catch because the <em>reasoning quality</em> masks the <em>data quality</em> problem.</p>

        <h3>Verification Discipline: The Human Layer</h3>

        <p>Engineering guardrails are the first line of defense. But even well-designed tools have gaps — and you'll also use AI outside of your custom tools (in general Claude conversations, in other AI products, in third-party platforms). You need a personal verification discipline.</p>

        <p><strong>Magnitude check.</strong> Does the number have the right handle? Is the S&P in the 6,000s (not 5,000s)? Is AAPL around $200 (not $150)? Is revenue in the right order of magnitude? This is a two-second sanity check that catches the most common errors.</p>

        <p><strong>Fact check key premises.</strong> When AI builds a thesis, identify the 2–3 factual claims the conclusion depends on. Verify those against a primary source (a filing, a Bloomberg terminal, a company IR page). If the premises are right, the reasoning is usually sound. If one premise is hallucinated, the entire thesis collapses.</p>

        <p><strong>Recency check.</strong> Does the information match the current period? AI may reference an earnings report from two quarters ago as if it were the latest, or cite a CEO who has since been replaced. Ask yourself: "When was this actually true?"</p>

        <p><strong>The specificity trap.</strong> Counter-intuitively, the more specific and confident an AI claim is — exact dates, exact percentages, specific names — the more important it is to verify. In human conversation, specificity correlates with knowledge. In AI output, it doesn't. A confidently stated "revenue of $4.237B in Q3 2025" is no more likely to be accurate than a vague "revenue in the low single-digit billions."</p>

        <div class="callout">
          <div class="callout-title">Cross-Reference Rule of Thumb</div>
          <p>Before acting on any AI-sourced data point in a real investment decision, verify it against one independent source. This doesn't mean distrusting every word — it means building a habit of checking the data that matters before the data becomes a position.</p>
        </div>
```

---

## Change 5: Week 4 — Expanded "Risk" bullet with agent-specific cascading errors

**File:** `professional/site/week-4.html`

**Location:** Inside the ordered list under "Why Full Autonomy Is Wrong for Finance" (around line 131-135).

**Currently (around lines 131-135):**
```html
          <li><strong>Risk:</strong> AI can be confidently wrong. A hallucinated signal or misinterpreted data point could lead to a catastrophic trade. Human review catches "this doesn't feel right" moments.</li>
          <li><strong>Trust:</strong> Building trust with AI is incremental. Starting with full autonomy means the first mistake destroys confidence. Starting with approve-everything and gradually expanding autonomy builds trust.</li>
```

**Replace the Risk `<li>` with this expanded version (keep Trust unchanged):**

```html
          <li><strong>Risk:</strong> AI can be confidently wrong. A hallucinated signal or misinterpreted data point could lead to a catastrophic trade. Human review catches "this doesn't feel right" moments.
            <p style="margin-top: 0.75rem;">This risk is amplified in agent workflows because errors can <strong>cascade</strong>. Consider: an agent queries a tool, gets valid data, but misinterprets the signal. It then builds a trade thesis on the misinterpretation, proposes a position, and writes a justification in its audit log. Each step looks reasonable in isolation. The narrative quality of the justification can actually make the error harder to spot — well-written reasoning feels trustworthy even when the premise is wrong.</p>
            <p>Approval workflows exist precisely for this reason. When reviewing an agent's trade proposal, don't just evaluate the reasoning chain — <strong>verify the source data independently</strong>. Check that the signal the agent cited actually matches what the tool returned. Check that the price level is in the right range. The human reviewer's job isn't to judge whether the argument is persuasive — it's to confirm that the facts are real.</p>
          </li>
```

---

## Change 6: Conclusion — New "Practitioner's Compact" Section

**File:** `professional/site/conclusion.html`

**Location:** AFTER the "Go deeper technically" `<ul>` closing tag (around line 74), BEFORE `<h2>The Bigger Picture</h2>` (around line 77).

**Currently:**
```html
            </ul>

            <!-- Section: The Bigger Picture -->
            <h2>The Bigger Picture</h2>
```

**Insert between them:**

```html
            <!-- Section: The Practitioner's Compact -->
            <h2>The Practitioner's Compact</h2>

            <p>Throughout this course, you learned engineering defenses against AI errors — pre-computed math, live data feeds, stale data warnings, verbatim templates. These are powerful. But they don't cover every situation, and you'll use AI tools beyond the ones you built here.</p>

            <p>These five principles are your personal defense layer. They apply to every AI tool you use — not just the ones from this course.</p>

            <ol style="margin-left: 1.5rem; margin-bottom: var(--md);">
              <li><strong>Never trust a number you didn't source.</strong> If AI states a price, level, ratio, or metric, verify it came from a tool call or primary source. If you can't trace where the number came from, don't use it.</li>
              <li><strong>Fluency is not accuracy.</strong> A well-written AI response is not more likely to be correct than an awkwardly phrased one. The quality of the language tells you nothing about the quality of the data. This is the single hardest habit to internalize because our brains are wired to trust articulate sources.</li>
              <li><strong>Verify the premise, not just the logic.</strong> When AI builds an investment thesis, the reasoning chain is usually sound — it's what AI does best. The vulnerability is the starting facts. Identify the 2–3 claims the conclusion depends on and check them. A perfectly reasoned conclusion built on a hallucinated fact is still wrong.</li>
              <li><strong>Magnitude-check everything.</strong> Is the S&P 500 in the right thousands? Is the stock price in the right range? Is revenue in the right order of magnitude? This two-second sanity check catches the most common errors — and they're the easiest to miss because the format looks correct.</li>
              <li><strong>AI improves, but the discipline doesn't change.</strong> Models will get better — they'll hallucinate less often, handle numbers more reliably, and cite sources more accurately. But "less often" is not "never." The verification habits you build today protect you from the errors that remain, no matter how infrequent they become. The cost of checking is low. The cost of a wrong position is not.</li>
            </ol>

```

---

## Verification Checklist

After making all 6 changes, verify:

1. **Visual inspection:** Load each page in browser and confirm:
   - New sections render correctly with proper heading hierarchy
   - Callout boxes display with correct styling
   - Tables render with proper alignment
   - No broken HTML (unclosed tags, mismatched quotes)
   - Content flows naturally with surrounding material

2. **Specific checks per page:**
   - `foundations-1.html`: "How AI Gets Things Wrong" appears between "Fundamental Tension" callout and "The Context Window" heading. New takeaway bullet appears at end of takeaways list.
   - `week-1.html`: Table renders after "Order execution" paragraph, before Key Takeaways
   - `week-2.html`: New subsections appear in reading content area (not inside exercise tabs)
   - `week-4.html`: Expanded Risk bullet has two additional paragraphs indented under the list item
   - `conclusion.html`: "Practitioner's Compact" section appears between "Go deeper technically" and "The Bigger Picture"

3. **Tab functionality:** On pages with tabs (week-1, week-2, week-4), confirm the tab switching still works after edits. New content should be inside the reading tab only.

4. **Mobile responsiveness:** Check that tables don't break on narrow viewports. The week-1 table has only 2 columns and short text, so it should be fine.

## Files Modified (Markdown Source — Already Done)

These files on branch `ai-limitations-content` already contain the new content:
- `professional/foundations-1/reading.md` — +54 lines
- `professional/week-1/reading.md` — +21 lines
- `professional/week-2/reading.md` — +74 lines
- `professional/week-4/reading.md` — +17 lines
- `professional/conclusion.md` — +41 lines

## Files To Modify (HTML Website — Your Job)

- `professional/site/foundations-1.html` — Changes 1 and 2
- `professional/site/week-1.html` — Change 3
- `professional/site/week-2.html` — Change 4
- `professional/site/week-4.html` — Change 5
- `professional/site/conclusion.html` — Change 6

## Rollback

To revert everything: `git checkout v2-refresh -- professional/` from the repo root.
Or simply switch back to the `v2-refresh` branch.
