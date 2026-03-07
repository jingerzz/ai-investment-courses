# First-Time Setup Guide

This guide walks you through installing Claude Code and getting your
environment ready. It assumes you've never used a terminal before.

## Step 1: Open the Terminal

**On Mac:**
- Press `Cmd + Space` to open Spotlight Search
- Type `Terminal` and press Enter
- A window with a text prompt will appear — this is your terminal

**On Windows:**
- Press `Win + R`, type `cmd`, and press Enter
- Or search for "Command Prompt" in the Start menu

You'll see something like:
```
jxie@MacBook ~ %
```
This is the command line. You type commands here and press Enter to run them.

## Step 2: Install Claude Code

Copy and paste this command into your terminal, then press Enter:

```bash
npm install -g @anthropic-ai/claude-code
```

If you see an error about `npm` not being found, you need to install Node.js
first. Go to [nodejs.org](https://nodejs.org), download the LTS version,
install it, close and reopen your terminal, then try the command again.

To verify it worked, type:
```bash
claude --version
```

You should see a version number like `1.x.x`.

## Step 3: Install uv (Python Package Manager)

This is the tool Claude Code will use to manage Python and its libraries.
Copy and paste this command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen your terminal, then verify:
```bash
uv --version
```

## Step 4: Create Your Course Folder

Type these commands one at a time, pressing Enter after each:

```bash
mkdir ~/ai-finance-tools
cd ~/ai-finance-tools
```

This creates a folder called `ai-finance-tools` in your home directory and
moves into it.

## Step 5: Start Claude Code

Type:
```bash
claude
```

Claude Code will start up. You'll see a prompt where you can type messages to
Claude, just like in Claude Desktop — but this version can create files, run
commands, and build software on your computer.

Type a test message:
```
Hello! Can you create a file called hello.txt that says "My first file"?
```

Claude will create the file. You've just built something with Claude Code.

## Step 6: Verify Claude Desktop

Open Claude Desktop (the regular app). You should be able to chat with Claude
normally. In later exercises, you'll connect the tools Claude Code builds to
Claude Desktop.

## You're Ready

Your setup is complete. You have:
- **Terminal** — where you run commands and use Claude Code
- **Claude Code** — the AI that builds tools for you
- **Claude Desktop** — the AI that uses the tools you build
- **uv** — the package manager Claude Code uses for Python

Continue to `README.md` for the Week 1 exercise.

---

## Quick Reference: Terminal Commands You'll Use

| Command | What It Does |
|---------|-------------|
| `cd ~/ai-finance-tools` | Go to your project folder |
| `claude` | Start Claude Code |
| `ls` | List files in the current folder |
| `uv run mcp dev server.py` | Test an MCP server you've built |
| `Ctrl + C` | Stop a running command |
| Up arrow | Repeat your last command |

You don't need to memorize these. Claude Code will run commands for you.
