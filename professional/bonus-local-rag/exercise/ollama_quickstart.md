# Ollama Quick-Start Guide

Everything you need to know about Ollama in 5 minutes.

---

## Installing Ollama

If you don't have it yet, go to [ollama.com](https://ollama.com) and
download the Mac installer. Run it like any other app.

After installing, Ollama runs in the background automatically. You'll see
a small llama icon in your menu bar.

---

## Essential Commands

Open your terminal (`Cmd + Space`, type `Terminal`, press Enter) and try
these commands.

### Check Ollama is running

```bash
ollama --version
```

You should see a version number like `0.3.x`. If you get "command not
found," Ollama isn't installed or isn't in your path.

### Pull (download) a model

```bash
ollama pull nomic-embed-text
```

This downloads the embedding model (~275MB). You'll see a progress bar.
It only downloads once — after that, it's stored locally.

Pull a text model too:

```bash
ollama pull qwen3.5:4b
```

This one is ~3.4GB. On a Mac Mini with decent internet, it takes a few minutes.

### List your downloaded models

```bash
ollama ls
```

Output:
```
NAME                    SIZE      MODIFIED
nomic-embed-text:latest 274 MB    2 minutes ago
qwen3.5:4b             3.4 GB    5 minutes ago
```

This shows everything you've downloaded and how much space it uses.

### Test a model interactively

```bash
ollama run qwen3.5:4b
```

This opens a chat where you can type messages and see responses. Try:

```
What are the main sections of an SEC 10-K filing?
```

Press `Ctrl + D` or type `/bye` to exit.

### Remove a model you don't need

```bash
ollama rm qwen3.5:4b
```

This deletes the model and frees up disk space. You can always `pull` it
again later.

### Check what's running

```bash
ollama ps
```

Shows which models are currently loaded in memory. Models load when first
used and unload after a period of inactivity to free RAM.

### Start/stop Ollama

Ollama typically runs automatically in the background. If you need to
start it manually:

```bash
ollama serve
```

To stop it, click the llama icon in the menu bar and choose Quit, or
press `Ctrl + C` if you started it from the terminal.

---

## Command Reference

| Command | What It Does | Example |
|---------|-------------|---------|
| `ollama pull <model>` | Download a model | `ollama pull nomic-embed-text` |
| `ollama ls` | List downloaded models | `ollama ls` |
| `ollama rm <model>` | Delete a model | `ollama rm qwen3.5:4b` |
| `ollama run <model>` | Chat with a model | `ollama run qwen3.5:4b` |
| `ollama ps` | Show running models | `ollama ps` |
| `ollama serve` | Start Ollama manually | `ollama serve` |
| `ollama --version` | Check version | `ollama --version` |

---

## Models for This Course

You need the embedding model plus one text model. Everyone pulls the
embedding model. Pick the text model that matches your machine:

**Step 1: Pull the embedding model (everyone):**

```bash
ollama pull nomic-embed-text
```

**Step 2: Pull your text model:**

| Your RAM | Command | Disk Needed |
|----------|---------|-------------|
| 8GB | `ollama pull qwen3.5:0.8b` | ~1.3GB total |
| 16GB | `ollama pull qwen3.5:4b` | ~3.7GB total |
| 32GB+ | `ollama pull qwen3.5:9b` | ~7.3GB total |

Not sure how much RAM you have? On Mac, click the Apple menu → About This
Mac. On Windows, open Settings → System → About.

**Most participants should use `qwen3.5:4b`:**

```bash
ollama pull qwen3.5:4b
```

All three models produce the same kind of output — larger models just give
better quality answers. The 0.8B model is perfectly fine for this exercise;
Claude Desktop handles the sophisticated reasoning on top of what the local
model retrieves.

---

## How Your Code Talks to Ollama

You don't need to understand this in detail — Claude Code will write the
code. But here's the concept:

Ollama runs a local API at `http://localhost:11434`. When your MCP server
needs to embed text or generate a response, it sends a request to this
local address. No internet is involved.

```
Your MCP Server  →  http://localhost:11434  →  Ollama  →  Local Model
     (Python)          (local network)         (app)      (on your GPU/CPU)
```

Claude Code will handle all of this. You just need Ollama running with
the models pulled.
