# Exercise: Your First Claude Project

## What You'll Do

You'll set up Claude for stock research, see firsthand how AI gets
things wrong, learn how custom instructions improve your results,
and create your first project with uploaded documents.

## Time: 20 minutes

## What You Need

- A Claude account at [claude.ai](https://claude.ai)
- A web browser
- A news article or document about a company you're interested in
  (a news article, earnings summary, or anything you can copy-paste
  or save as a PDF)

---

## Step 1: See Stale Data Firsthand (3 min)

Go to [claude.ai](https://claude.ai) and start a new conversation
-- not inside a project. Just a plain conversation.

Type this:

```
What is Tesla's stock price right now?
```

Read the response. Now open a new browser tab and search "Tesla
stock price" on Google to see the actual current price.

- [ ] I asked Claude for a stock price
- [ ] I looked up the real price
- [ ] I noticed the difference

**What to notice:** Claude gave you a number, but it's probably
wrong -- maybe by a little, maybe by a lot. It didn't say "I'm not
sure" or "this might be outdated." It just stated a number with
full confidence. This is Failure Mode 1 (stale magnitude) from the
reading. Remember this feeling -- it's easy to trust a
confident-sounding answer.

Now try one more:

```
Which company grew revenue faster last year, Nike or Disney?
```

Notice how Claude answers -- does it hedge? Does it give specific
numbers? Can you trust those numbers?

---

## Step 2: Set Up Custom Instructions (4 min)

Now let's make Claude work better for you.

1. Click your profile icon in the bottom-left of claude.ai
2. Go to **Settings**
3. Find **Custom instructions** (sometimes called "Profile")
4. Paste in something like this (edit it to match you):

```
You are helping a high school student who is learning about the
stock market and investing.

When explaining things:
- Use clear, simple language -- not Wall Street jargon
- If you use a finance term, explain what it means
- Give examples using companies I know (Apple, Nike, Disney,
  Tesla, Netflix)
- Be honest when you're not sure about something

When I ask about stocks or companies:
- Remind me that your data might be outdated
- Explain your reasoning step by step
- Tell me both the good and bad sides
- Keep responses concise
```

5. Save your instructions

- [ ] I wrote custom instructions that reflect who I am
- [ ] I saved them

---

## Step 3: See the Difference (3 min)

Start a **new conversation** (so the instructions take effect) and
ask:

```
What are the biggest risks to Apple's stock price over the next
year?
```

Compare this response to how Claude answered your questions in
Step 1 (before custom instructions). You should notice:

- Simpler language and explained terms
- A tone that matches your level
- More honest hedging about uncertain data

- [ ] I asked a question with custom instructions active
- [ ] I noticed the difference from Step 1

---

## Step 4: Create a Project (5 min)

Now set up a workspace for stock research.

1. In the left sidebar of claude.ai, find **Projects**
2. Click **Create project** (or the + icon)
3. Name it: **Stock Research**
4. In the project instructions, write:

```
This project is for researching stocks and learning about
companies. I'm a high school student interested in investing.

When I ask about a company:
- Start with what the company does and how it makes money
- Then cover the good stuff (growth, advantages)
- Then cover the risks (competition, problems)
- Use a table if comparing multiple companies
- Flag any numbers that might be outdated

Companies I'm most interested in: Apple, Nike, Disney, Tesla,
Netflix.
```

5. Now upload a document to project knowledge:
   - Find a news article about a company you like (or go to Google
     News and search for "Apple" or "Nike")
   - Copy the article text and paste it into a text file, or save
     the page as a PDF
   - Upload it to your project's knowledge base

6. Start a conversation inside the project and ask:

```
Based on the article I uploaded, what are the key takeaways?
What's good news and what's bad news for the company?
```

- [ ] I created a project called "Stock Research"
- [ ] I wrote project instructions
- [ ] I uploaded a document
- [ ] I asked Claude to analyze my document

---

## Step 5: Try Prompting Techniques (3 min)

Still inside your Stock Research project, try these prompts to
practice what you learned in the reading:

**Be specific:**
```
Compare Nike and Disney -- which company has a stronger brand
with teenagers? Give me three reasons for your pick.
```

**Ask for reasoning:**
```
Walk me through the bull case and bear case for Netflix. What
are the strongest arguments on each side?
```

**Push back:**
After Claude gives you an answer, respond with something like:
```
You didn't mention competition from YouTube and TikTok. How
does that change your analysis of Netflix?
```

- [ ] I tried a specific prompt
- [ ] I asked for reasoning
- [ ] I pushed back on an answer

---

## Step 6: Try Claude on Mobile (Optional, 2 min)

If you have the Claude app on your phone
([iOS](https://apps.apple.com/app/claude-by-anthropic/id6473753684) /
[Android](https://play.google.com/store/apps/details?id=com.anthropic.claude)),
open it and find your Stock Research project.

Notice that your project instructions and documents carry over.
Try asking a quick question by voice.

- [ ] I opened Claude on my phone (or skipped this step)

---

## Step 7: Reflection (1 min)

Think about these questions (you don't need to write answers, but
it helps if you do):

1. **What did you notice about the stock price Claude gave you?**
   Was it close? Way off? Did Claude warn you it might be wrong?

2. **How did custom instructions change the responses?** Did Claude
   feel more like a helpful tutor or still like a generic chatbot?

3. **What surprised you most about using Claude?** What was better
   than expected? What was worse?

- [ ] I reflected on what I learned

---

## What You Learned

- **AI doesn't know current prices.** You saw this firsthand. Claude
  gave you a stock price with full confidence, and it was wrong.
  This is why verification matters.

- **Custom instructions make a real difference.** The same AI gives
  you very different answers when it knows who you are and what you
  need.

- **Projects keep things organized.** Your Stock Research project
  has its own instructions and documents, separate from everything
  else.

- **Uploading documents gives Claude real context.** Asking about
  a specific article you uploaded gets you a much better answer
  than asking a generic question.

- **Prompting is a skill.** Specific questions, asking for
  reasoning, and pushing back all produce better results. You'll
  get better at this throughout the course.
