"""LLM client: Ollama or Anthropic backend, selected by config.

Supports two backends:
  - **ollama** (default): Native /api/chat endpoint with thinking-mode control.
  - **anthropic**: Anthropic Messages API via the SDK. Uses ANTHROPIC_API_KEY
    from environment. Ideal for servers without a local Ollama instance.

Set ``"llm_backend": "anthropic"`` in config.json to switch.
"""

import json
import logging
import os
import time
import asyncio
import urllib.request
from contextlib import asynccontextmanager
from pathlib import Path

try:
    import aiohttp
    _HAS_AIOHTTP = True
except ImportError:
    _HAS_AIOHTTP = False

logger = logging.getLogger("pageindex-rag")

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = ROOT / "config.json"


def _load_config():
    if CONFIG_PATH.exists():
        try:
            return json.loads(CONFIG_PATH.read_text())
        except Exception:
            return {}
    return {}


def _get_llm_backend() -> str:
    """Return 'ollama' or 'anthropic'. Env var LLM_BACKEND takes precedence."""
    env = os.environ.get("LLM_BACKEND")
    if env:
        return env.lower()
    cfg = _load_config()
    return cfg.get("llm_backend", "ollama")


def _get_ollama_base_url():
    cfg = _load_config()
    url = cfg.get("ollama_base_url", "http://localhost:11434/v1")
    # Strip /v1 suffix if present — we call native /api/chat directly
    return url.removesuffix("/v1").removesuffix("/v1/")


def _get_ollama_model():
    cfg = _load_config()
    return cfg.get("ollama_model", "qwen3-coder:30b")


def _get_anthropic_model():
    """Env var ANTHROPIC_MODEL takes precedence over config."""
    env = os.environ.get("ANTHROPIC_MODEL")
    if env:
        return env
    cfg = _load_config()
    return cfg.get("anthropic_model", "claude-haiku-4-5-20251001")


def _get_default_model():
    """Return the default model for the configured backend."""
    if _get_llm_backend() == "anthropic":
        return _get_anthropic_model()
    return _get_ollama_model()


def _get_summary_model():
    """Model for summary generation. Env var SUMMARY_MODEL takes precedence."""
    env = os.environ.get("SUMMARY_MODEL")
    if env:
        return env
    cfg = _load_config()
    return cfg.get("summary_model") or _get_default_model()


def _get_summary_concurrency():
    """Max concurrent async summary LLM calls. Env var SUMMARY_CONCURRENCY takes precedence.

    Returns None if not configured (unlimited).
    """
    env = os.environ.get("SUMMARY_CONCURRENCY")
    if env:
        return int(env)
    cfg = _load_config()
    val = cfg.get("summary_concurrency")
    return int(val) if val else None


def _get_summary_token_threshold():
    """Token count below which nodes skip LLM summarization. Defaults to 200."""
    cfg = _load_config()
    val = cfg.get("summary_token_threshold")
    return int(val) if val else 200


def _get_extractive_threshold():
    """Token count above which nodes get extractive (non-LLM) summarization.

    Nodes between extractive_threshold and summary_token_threshold use fast
    TF-IDF sentence extraction. Nodes above summary_token_threshold use LLM.
    Nodes below extractive_threshold use raw text. Defaults to 2000. Set to 0 to disable.
    """
    cfg = _load_config()
    val = cfg.get("extractive_threshold")
    return int(val) if val is not None else 2000


def _get_thinning_threshold():
    """Min token count for tree thinning. Nodes below this merge into parent. 0 disables."""
    cfg = _load_config()
    val = cfg.get("thinning_threshold")
    return int(val) if val else 0


def _get_max_tokens():
    """Max tokens per completion. 16384 gives headroom for large PDF TOC JSON extraction."""
    cfg = _load_config()
    return int(cfg.get("max_tokens", 16384))


def _get_ollama_keep_alive():
    """How long Ollama keeps the model resident after a call.

    Default 10m keeps the model hot across the fetch→index→search pipeline so
    queries don't pay a ~10s reload. Override per-call via OLLAMA_KEEP_ALIVE env.
    """
    env = os.environ.get("OLLAMA_KEEP_ALIVE")
    if env:
        return env
    cfg = _load_config()
    return cfg.get("ollama_keep_alive", "10m")


@asynccontextmanager
async def _maybe_semaphore(sem):
    """Async context manager that acquires sem if provided, otherwise is a no-op."""
    if sem is not None:
        async with sem:
            yield
    else:
        yield


# ── Native Ollama HTTP helpers ──────────────────────────────────────────────

def _ollama_chat_sync(model: str, messages: list[dict], max_tokens: int,
                      think: bool = False) -> dict:
    """Synchronous call to Ollama native /api/chat. Returns parsed JSON response."""
    base = _get_ollama_base_url()
    url = f"{base}/api/chat"
    body = {
        "model": model,
        "messages": messages,
        "stream": False,
        "think": think,
        "keep_alive": _get_ollama_keep_alive(),
        "options": {
            "temperature": 0,
            "num_predict": max_tokens,
            "num_ctx": 4096,
        },
    }
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data,
                                headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as resp:
        return json.loads(resp.read())


async def _ollama_chat_async(model: str, messages: list[dict], max_tokens: int,
                             think: bool = False) -> dict:
    """Async call to Ollama native /api/chat."""
    base = _get_ollama_base_url()
    url = f"{base}/api/chat"
    body = {
        "model": model,
        "messages": messages,
        "stream": False,
        "think": think,
        "keep_alive": _get_ollama_keep_alive(),
        "options": {
            "temperature": 0,
            "num_predict": max_tokens,
            "num_ctx": 4096,
        },
    }

    if _HAS_AIOHTTP:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=body, timeout=aiohttp.ClientTimeout(total=600)) as resp:
                return await resp.json()
    else:
        # Fallback: run sync call in thread pool
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None, _ollama_chat_sync, model, messages, max_tokens, think
        )


# ── Anthropic API helpers ──────────────────────────────────────────────────

def _anthropic_chat_sync(model: str, messages: list[dict], max_tokens: int) -> dict:
    """Synchronous call to Anthropic Messages API. Returns Ollama-shaped dict."""
    import anthropic

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=0,
    )
    content = resp.content[0].text if resp.content else ""
    done_reason = "length" if resp.stop_reason == "max_tokens" else "stop"
    return {"message": {"content": content}, "done_reason": done_reason}


async def _anthropic_chat_async(model: str, messages: list[dict], max_tokens: int) -> dict:
    """Async call to Anthropic Messages API. Returns Ollama-shaped dict."""
    import anthropic

    client = anthropic.AsyncAnthropic()
    resp = await client.messages.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=0,
    )
    content = resp.content[0].text if resp.content else ""
    done_reason = "length" if resp.stop_reason == "max_tokens" else "stop"
    return {"message": {"content": content}, "done_reason": done_reason}


# ── Public API (drop-in replacements for ChatGPT_API functions) ─────────────

def _chat_sync(model: str, messages: list[dict], max_tokens: int, think: bool = False) -> dict:
    """Dispatch sync chat to the configured backend."""
    if _get_llm_backend() == "anthropic":
        return _anthropic_chat_sync(model, messages, max_tokens)
    return _ollama_chat_sync(model, messages, max_tokens, think=think)


async def _chat_async(model: str, messages: list[dict], max_tokens: int, think: bool = False) -> dict:
    """Dispatch async chat to the configured backend."""
    if _get_llm_backend() == "anthropic":
        return await _anthropic_chat_async(model, messages, max_tokens)
    return await _ollama_chat_async(model, messages, max_tokens, think=think)


def llm_call(model=None, prompt="", api_key=None, chat_history=None):
    """Synchronous LLM call. Drop-in replacement for ChatGPT_API."""
    max_retries = 10
    resolved_model = model or _get_default_model()
    max_tokens = _get_max_tokens()

    for i in range(max_retries):
        try:
            if chat_history:
                messages = list(chat_history)
                messages.append({"role": "user", "content": prompt})
            else:
                messages = [{"role": "user", "content": prompt}]

            result = _chat_sync(resolved_model, messages, max_tokens)
            return result.get("message", {}).get("content", "")
        except Exception as e:
            logger.error(f"LLM call error (attempt {i+1}): {e}")
            if i < max_retries - 1:
                time.sleep(1)
            else:
                logger.error(f"Max retries reached for prompt: {prompt[:100]}...")
                return "Error"


def llm_call_with_finish_reason(model=None, prompt="", api_key=None, chat_history=None):
    """Synchronous LLM call returning (content, finish_status).

    Drop-in replacement for ChatGPT_API_with_finish_reason.
    """
    max_retries = 10
    resolved_model = model or _get_default_model()
    max_tokens = _get_max_tokens()

    for i in range(max_retries):
        try:
            if chat_history:
                messages = list(chat_history)
                messages.append({"role": "user", "content": prompt})
            else:
                messages = [{"role": "user", "content": prompt}]

            result = _chat_sync(resolved_model, messages, max_tokens)
            content = result.get("message", {}).get("content", "")

            done_reason = result.get("done_reason", "stop")
            if done_reason == "length":
                return content, "max_output_reached"
            else:
                return content, "finished"
        except Exception as e:
            logger.error(f"LLM call error (attempt {i+1}): {e}")
            if i < max_retries - 1:
                time.sleep(1)
            else:
                logger.error(f"Max retries reached for prompt: {prompt[:100]}...")
                return "Error", "error"


async def llm_call_async(model=None, prompt="", api_key=None, semaphore=None,
                         max_tokens=None):
    """Async LLM call. Drop-in replacement for ChatGPT_API_async.

    semaphore: optional asyncio.Semaphore to limit concurrency. The semaphore
    is held for the entire duration of the call (including retries) so that at
    most N calls are in-flight at once.
    max_tokens: override for num_predict. Defaults to config max_tokens (16384).
    """
    max_retries = 10
    resolved_model = model or _get_default_model()
    max_tokens = max_tokens or _get_max_tokens()
    messages = [{"role": "user", "content": prompt}]

    async with _maybe_semaphore(semaphore):
        for i in range(max_retries):
            try:
                result = await _chat_async(resolved_model, messages, max_tokens)
                return result.get("message", {}).get("content", "")
            except Exception as e:
                logger.error(f"Async LLM call error (attempt {i+1}): {e}")
                if i < max_retries - 1:
                    await asyncio.sleep(1)
                else:
                    logger.error(f"Max retries reached for prompt: {prompt[:100]}...")
                    return "Error"
