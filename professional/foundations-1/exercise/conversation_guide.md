# Conversation Guide: Foundation Prompts

Example prompts to use in your Foundations 1 project. Each one
demonstrates a specific technique. Adapt them to your own coverage
area and analytical style.

---

## Setting the Stage

These prompts establish context at the start of a conversation.
They work best as opening messages.

**Define your focus:**
```
For this conversation, I want to focus on the US regional banking
sector. I'm evaluating whether credit quality deterioration has
been fully priced in or if there's further downside.
```
*Why it works:* Gives Claude a specific sector, a specific question,
and a clear analytical direction. Every subsequent response will be
framed around this.

**Establish your framework:**
```
I evaluate companies using a quality-at-a-reasonable-price framework.
Quality means: sustainable competitive advantage, high ROIC, and
management with a track record of capital allocation discipline.
Reasonable price means: FCF yield above 5% or a discount to
intrinsic value using a conservative DCF.
```
*Why it works:* Claude now knows exactly what metrics and standards
to apply. When you ask "Is this company interesting?", Claude can
answer within your framework instead of giving a generic take.

---

## Analysis

These prompts ask Claude to do substantive analytical work.

**Sector comparison:**
```
Compare the investment cases for Palo Alto Networks, CrowdStrike,
and Fortinet. For each, give me: the bull thesis in two sentences,
the bear thesis in two sentences, and the single metric that most
differentiates it from the other two.
```
*Why it works:* The structure (bull, bear, differentiator) forces
Claude to be concise and comparative rather than writing three
separate summaries. The constraint on length prevents padding.

**Risk assessment:**
```
I own a concentrated position in NVDA. Steel-man the bear case
for me. What are the three scenarios where this position loses
30% or more over the next 12 months? Be specific about catalysts
and timing.
```
*Why it works:* "Steel-man the bear case" tells Claude to present
the strongest version of the opposing view, not a straw man.
Specifying a loss threshold and timeframe makes the scenarios
concrete and actionable.

**Macro framework:**
```
Walk me through how a 50bps rate cut by the Fed would flow through
to corporate earnings for S&P 500 companies. Start with the direct
effects on interest expense, then move to second-order effects on
consumer spending and capital investment. Which sectors benefit
most and least?
```
*Why it works:* The chain-of-reasoning structure (direct effects,
then second-order effects, then sector implications) produces a
thorough analysis. Claude follows the logical flow you've laid out.

---

## Working with Documents

Use these after uploading a document to your project knowledge.

**Extract key metrics:**
```
From the 10-K I uploaded, extract the following for the last three
fiscal years: revenue, gross margin, operating margin, free cash
flow, and net debt. Present them in a table. Flag any year where
a metric changed by more than 5 percentage points.
```
*Why it works:* Specific metrics, a specific format (table), and a
specific threshold for what's notable. Claude will go find the
numbers in the document rather than generating them from training
data.

**Identify what matters:**
```
Read the risk factors section of this 10-K. Separate the boilerplate
risks (generic disclosures every company includes) from the
company-specific risks that could actually affect the investment
thesis. For each company-specific risk, rate it as high, medium,
or low probability.
```
*Why it works:* The boilerplate/specific distinction is something
experienced analysts do intuitively. Asking Claude to do it
explicitly surfaces the risks that actually matter.

**Compare two documents:**
```
I've uploaded earnings transcripts from Q3 and Q4. Compare
management's tone and language about demand trends between the
two quarters. Did anything shift? Quote specific phrases that
show the change.
```
*Why it works:* Asking for specific quotes forces Claude to ground
its analysis in the actual text rather than making vague claims
about "improved sentiment."

---

## Iteration and Pushback

These prompts refine Claude's initial analysis. Use them when the
first response is good but not sharp enough.

**Challenge the analysis:**
```
You're weighting the margin expansion story too heavily. Their
margins expanded because they cut R&D, which is a one-time
benefit that comes at the expense of future growth. Redo the
analysis accounting for normalized R&D spending.
```
*Why it works:* You're bringing domain expertise that Claude
doesn't have. The correction makes the next iteration
meaningfully better.

**Request alternatives:**
```
That's the consensus view. Give me the non-consensus take ---
what would a contrarian argue? And what evidence would you need
to see to believe the contrarian is right?
```
*Why it works:* Pushes Claude past the obvious answer. The
"what evidence would you need" follow-up keeps it grounded
rather than speculative.

**Ask for more depth:**
```
Go deeper on the competitive dynamics. You mentioned pricing
pressure --- from whom? What's their cost structure versus the
incumbents? Is this a temporary disruption or a structural shift?
```
*Why it works:* Directs Claude to the specific area that needs
more depth rather than asking for "more detail" generically.
