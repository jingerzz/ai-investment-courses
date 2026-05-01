# Juniors track — Zo-centric rewrite (parking lot)

> **Status (2026-05-01):** Future work. Not used by any live build.

## What is this folder?

A holding spot for artifacts that will be useful when we rewrite the
**juniors** track to be Zo-centric (the way the `zo-professional/` track
already is). Right now `juniors/` in the repo root is the original
**Claude-centric** content; it has not been rewritten yet.

## What's here

### `build_website.py`

A standalone Python script that walks `juniors/*.md`, converts the
markdown into static HTML pages, and writes them out to a target
directory (currently hard-coded to a Zo conversation workspace at the
top of the file). It was used during the original Claude-centric
juniors course build to produce `index.html` / `week-1.html` / etc.

It is parked here because:

1. It is the only known builder for the juniors HTML pages.
2. When we rewrite the juniors track to be Zo-centric, we will likely
   want a similar conversion step (markdown → HTML) — either reused
   directly, ported to mirror the `zo-professional/` Vite-bundled
   approach used by the Clarion site, or replaced entirely.
3. It is not referenced by any current build pipeline. Leaving it in
   `juniors/` would imply the juniors track has an active builder,
   which would be misleading.

The script imports nothing outside the Python standard library and is
deliberately self-contained.

## Why park here instead of deleting?

Deleting it would lose institutional knowledge of how the original
juniors HTML pages were produced. Future agents tasked with the
juniors-zo rewrite should start by reading this file and either porting
it or designing a replacement.

## Related context

- `zo-professional/` — flagship Zo-centric track. Pattern to follow
  when rewriting juniors.
- `juniors/` — current Claude-centric juniors content (unchanged).
- `professional/` — current Claude-centric professional content
  (predecessor to `zo-professional/`).
- The Zo-centric rewrite for `zo-professional/` shipped as commit
  `873f945` (2026-04-30 / 2026-05-01) with a plain-English voice
  modeled on `https://jing.zo.space/course`. Apply the same voice when
  rewriting juniors.
