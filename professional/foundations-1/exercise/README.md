# Exercise: Your First Claude Project

## What You'll Do

You'll set up a Claude project tailored to your investment work,
experience the difference that custom instructions make, and learn
how project knowledge transforms Claude from a generic assistant into
a research partner that understands your context.

## Time: 30 minutes

## What You Need

- A Claude account at [claude.ai](https://claude.ai) (Pro or Team plan)
- A web browser
- A finance document you can upload (any PDF --- a research report,
  an earnings transcript, a 10-K excerpt, or even a one-page strategy
  summary). If you don't have one handy, you can download any 10-K
  from [SEC EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=10-K)

---

## Step 1: Ask Claude a Finance Question (5 min)

Go to [claude.ai](https://claude.ai) and start a new conversation ---
not inside a project. Just a plain conversation.

Ask Claude a question you'd normally research manually. Something
substantive, not a simple fact lookup. For example:

```
What are the key risks to the US equity market in the current
macro environment? Focus on the three most likely scenarios that
would cause a drawdown of 10% or more.
```

Read the response carefully. Notice:
- How detailed is it? Does it feel generic or specific?
- Does Claude make assumptions about your role or expertise level?
- Are there specific numbers? If so, are they current or potentially
  outdated?
- Does the framing match how you'd discuss this with a colleague?

Don't dismiss the response --- it will probably be reasonable. But
note its tone, its assumptions, and its level of specificity. You're
about to see how much better this gets.

## Step 2: Create a Project with Custom Instructions (10 min)

Now create a project that tells Claude who you are.

1. In the left sidebar of claude.ai, find **Projects**
2. Click **Create project** (or the + icon)
3. Name it something specific: "Equity Research", "Macro Analysis",
   or "Portfolio Review" --- whatever matches your actual work
4. In the project instructions, write something like this (adapt it
   to your actual role):

```
You are assisting a [your role] at a [your firm type].
I focus on [your coverage area or strategy].

When analyzing markets or companies:
- [Your primary analytical framework --- e.g., "Use a top-down macro
  framework starting with rates and credit conditions"]
- [Key metrics you care about --- e.g., "I evaluate companies on FCF
  yield, ROIC, and revenue durability"]
- [Your style --- e.g., "Always present the bear case, even for
  positions I own"]

When responding:
- Be direct and concise. I'll ask for detail if I need it.
- Use institutional-level terminology, not retail language.
- If you're uncertain about a specific data point, flag it explicitly
  rather than presenting it as fact.
- Skip boilerplate disclaimers about not being financial advice.
```

Take a few minutes to make this genuinely reflect how you work. The
more specific your instructions, the more useful the exercise will be.

## Step 3: Compare Responses (5 min)

Inside your new project, start a conversation and ask the **exact
same question** from Step 1:

```
What are the key risks to the US equity market in the current
macro environment? Focus on the three most likely scenarios that
would cause a drawdown of 10% or more.
```

Now compare the two responses side by side. You should notice:

- **Framing:** The project response should be calibrated to your role.
  If you said you're a PM, it might discuss portfolio implications.
  If you said you're an analyst, it might go deeper on specific
  sectors.
- **Terminology:** The language should match your instructions. If you
  asked for institutional terminology, you should see it.
- **Depth and focus:** The response should emphasize the analytical
  dimensions you specified. If you said you care about credit
  conditions, credit should feature prominently.
- **Tone:** If you asked for directness, the response should skip
  hedging language and get to the point.

The same model, the same question, but meaningfully different output
--- because you gave Claude context about who you are and how you
think.

## Step 4: Add Project Knowledge (7 min)

Now give Claude something specific to work with.

1. In your project settings, find the knowledge section
2. Upload a document: a research report, an earnings transcript, a
   10-K filing, or any finance document you work with regularly
3. Start a new conversation within the project

Ask Claude questions that require the document:

```
Summarize the key financial takeaways from the document I uploaded.
Focus on anything that surprised you or diverged from consensus
expectations.
```

Then go deeper:

```
What are the three most important risk factors mentioned in this
filing? For each one, tell me whether you think it's a standard
boilerplate disclosure or a genuinely material risk, and why.
```

And try cross-referencing:

```
Based on the financials in this document, which metrics are
trending in the wrong direction? What questions would you want
answered before getting comfortable with this company?
```

Notice how different this is from asking Claude generic questions.
With project knowledge, Claude is analyzing a specific document ---
your document --- through the lens of your analytical framework. This
is closer to having a research partner who has actually read the
briefing materials.

## Step 5: Try Claude on Mobile (3 min)

If you have the Claude mobile app installed
([iOS](https://apps.apple.com/app/claude-by-anthropic/id6473753684) /
[Android](https://play.google.com/store/apps/details?id=com.anthropic.claude)),
open it and navigate to the same project.

Notice what's the same:
- Your project instructions carry over
- Your uploaded documents are accessible
- The same analytical framing applies

Notice what's different:
- Shorter responses may work better on a small screen
- Voice input can be faster than typing complex questions
- You can do quick checks --- "remind me of the key risks from that
  10-K" --- without sitting at your desk

If you don't have the mobile app, skip this step. It's useful but not
essential.

---

## What You Learned

- **Custom instructions reshape Claude's output.** The same question
  produces materially different responses when Claude knows your role,
  your framework, and your preferences. This isn't cosmetic --- it
  changes what Claude emphasizes, how it frames analysis, and what
  assumptions it makes.

- **Projects keep context organized.** Instead of one conversation
  that tries to do everything, you can maintain separate workspaces
  with focused instructions and relevant documents.

- **Project knowledge turns Claude into a research partner.** Generic
  questions get generic answers. Questions grounded in your actual
  documents get specific, actionable analysis.

- **Claude works across devices.** Your projects, instructions, and
  knowledge are available on web and mobile, so you can continue
  your work wherever you are.

- **The quality of Claude's output depends on the quality of your
  input.** Specific instructions and focused questions consistently
  outperform vague ones. This is a skill you'll develop throughout
  the course.
