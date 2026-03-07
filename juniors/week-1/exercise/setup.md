# First-Time Setup Guide

This guide walks you through installing Claude Code and getting your
computer ready. It assumes you've never used a terminal before. If you
get stuck, ask a parent, teacher, or tech-savvy friend for help.

## Step 1: Open the Terminal

The terminal is a text window where you type commands. It looks old-school,
but it's powerful.

**On Mac:**
- Press `Cmd + Space` to open Spotlight Search
- Type `Terminal` and press Enter
- A window with a text prompt will appear — this is your terminal

**On Windows:**
- Press `Win + R`, type `cmd`, and press Enter
- Or search for "Command Prompt" in the Start menu

You'll see something like:
```
yourname@computer ~ %
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

This is a behind-the-scenes tool that Claude Code needs. Copy and paste
this command:

**Mac:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen your terminal, then verify:
```bash
uv --version
```

## Step 4: Create Your Project Folder

Type these commands one at a time, pressing Enter after each:

```bash
mkdir ~/ai-stock-tools
cd ~/ai-stock-tools
```

This creates a folder called `ai-stock-tools` in your home directory and
moves into it. This is where all your tools will live.

## Step 5: Start Claude Code

Type:
```bash
claude
```

Claude Code will start up. You'll see a prompt where you can type messages
to Claude, just like in Claude Desktop — but this version can create files,
run commands, and build software on your computer.

Try a test message:
```
Hello! Can you create a file called hello.txt that says "My first file"?
```

Claude will create the file. You just built something with Claude Code!

## Step 6: Verify Claude Desktop

Open Claude Desktop (the regular app, not Claude Code). You should be
able to chat with Claude normally. In later steps, you'll connect the
tools Claude Code builds to Claude Desktop.

## You're Ready

Your setup is complete. You have:
- **Terminal** — where you run commands and use Claude Code
- **Claude Code** — the AI that builds tools for you
- **Claude Desktop** — the AI that uses the tools you build
- **uv** — a behind-the-scenes tool manager

Continue to `README.md` for the Week 1 exercise.

---

## Quick Reference: Terminal Commands You'll Use

| Command | What It Does |
|---------|-------------|
| `cd ~/ai-stock-tools` | Go to your project folder |
| `claude` | Start Claude Code |
| `ls` | List files in the current folder |
| `uv run mcp dev server.py` | Test a tool you've built |
| `Ctrl + C` | Stop a running command |
| Up arrow | Repeat your last command |

You don't need to memorize these. Claude Code will run commands for you.
