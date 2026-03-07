# Ollama Quick-Start Guide

Everything you need to know about Ollama in 5 minutes.

---

## Installing Ollama

Go to [ollama.com](https://ollama.com) and download the installer for
your computer (Mac or Windows). Install it like any other app.

After installing, Ollama runs in the background automatically. On Mac,
you'll see a small llama icon in your menu bar. On Windows, look for
it in your system tray.

---

## Essential Commands

Open your terminal and try these commands.

### Check Ollama is installed

```bash
ollama --version
```

You should see a version number. If you get "command not found," Ollama
isn't installed yet.

### Download a model

```bash
ollama pull nomic-embed-text
```

This downloads the search model (~275MB). You'll see a progress bar.
It only downloads once — after that, it's saved on your computer.

Download an answer model too:

```bash
ollama pull qwen3.5:4b
```

This one is bigger (~3.4GB). It might take a few minutes depending on
your internet speed.

### See what models you have

```bash
ollama ls
```

Output:
```
NAME                    SIZE      MODIFIED
nomic-embed-text:latest 274 MB    2 minutes ago
qwen3.5:4b             3.4 GB    5 minutes ago
```

### Chat with a model

```bash
ollama run qwen3.5:4b
```

This opens a chat where you can type messages. Try asking it something:

```
What is a stock?
```

Press `Ctrl + D` or type `/bye` to exit the chat.

### Delete a model you don't need

```bash
ollama rm qwen3.5:4b
```

This frees up disk space. You can always download it again later.

### Check what's running right now

```bash
ollama ps
```

Shows which models are currently loaded in your computer's memory.

### Start Ollama manually (if needed)

```bash
ollama serve
```

Usually Ollama starts automatically. Use this if it's not running.

---

## Command Reference

| Command | What It Does | Example |
|---------|-------------|---------|
| `ollama pull <model>` | Download a model | `ollama pull nomic-embed-text` |
| `ollama ls` | List your models | `ollama ls` |
| `ollama rm <model>` | Delete a model | `ollama rm qwen3.5:4b` |
| `ollama run <model>` | Chat with a model | `ollama run qwen3.5:4b` |
| `ollama ps` | Show running models | `ollama ps` |
| `ollama serve` | Start Ollama manually | `ollama serve` |
| `ollama --version` | Check version | `ollama --version` |

---

## Models for This Course

You need the search model plus one answer model.

**Step 1: Download the search model (everyone):**

```bash
ollama pull nomic-embed-text
```

**Step 2: Download your answer model:**

| Your RAM | Command | Total Disk Needed |
|----------|---------|-------------------|
| 8GB | `ollama pull qwen3.5:0.8b` | ~1.3GB |
| 16GB | `ollama pull qwen3.5:4b` | ~3.7GB |
| 32GB+ | `ollama pull qwen3.5:9b` | ~7.3GB |

Not sure how much RAM you have?
- **Mac:** Apple menu > About This Mac > look for "Memory"
- **Windows:** Right-click Start > System > look for "Installed RAM"

**Most people should use `qwen3.5:4b`:**

```bash
ollama pull qwen3.5:4b
```

All three models do the same thing — larger ones just give better
quality answers. The smallest model (0.8b) is fine for this exercise.

---

## How Your Tools Talk to Ollama

You don't need to understand this in detail — Claude Code writes all
the code. But here's the basic idea:

Ollama runs a local service on your computer at `http://localhost:11434`.
When your tool needs to search a document or generate an answer, it
sends a request to this address. No internet is involved — it all
happens on your machine.

```
Your Tool  →  localhost:11434  →  Ollama  →  AI Model
(Python)      (local only)       (app)     (on your computer)
```

Claude Code handles all of this. You just need Ollama running with
the models downloaded.
