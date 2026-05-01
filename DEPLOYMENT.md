# Where this content is published

This repo (`jingerzz/ai-investment-courses`) is the **canonical source**
for course content. The actual public-facing websites that render this
content live in **separate** repositories. Changes here do not appear on
those websites until each one is updated and rebuilt.

> **For AI agents:** if a user reports "I pushed to this repo but the
> website didn't update," the answer is almost certainly that the
> downstream site repo has its own bundled mirror that has not been
> resynced. Read this file before debugging.

---

## Where each track is published

### `zo-professional/` → Clarion Intelligence Systems site

| Field | Value |
|---|---|
| Live URL | `https://www.clarionintelligencesystems.com/resources/course` |
| Site repo | `https://github.com/jingerzz/clarion-site` (private) |
| Bundled mirror in that repo | `src/content/course/zo-professional/` (Vite-bundled, source of truth at build time) and `public/resources/course/zo-professional/` (raw markdown, downloadable) |
| Sync script | `scripts/sync-course-content.sh` in `clarion-site` |
| Prebuild guard | `scripts/check-course-sync.sh` (fails the build if the bundled mirror differs from this repo's `zo-professional/`) |
| Local working copy | `/home/workspace/Projects/clarion-site/` |
| Production service | user service `svc_m_JjUUvmnEE` (`bun run prod`); republish to rebuild |

**Update flow:**

```
edit zo-professional/...           # in this repo
git commit && git push origin main # this repo

cd /home/workspace/Projects/clarion-site
bun run sync-course-content        # mirrors zo-professional/ into the site repo
bun run build                      # prebuild check verifies sync
git add . && git commit && git push origin main
# republish svc_m_JjUUvmnEE so production picks up the new build
```

If you skip the sync step, `bun run build` will fail with a clear
message pointing back to the sync script.

### `professional/` → `jing.zo.space/course`

The Claude-centric professional track is published as a zo.space route
at `https://jing.zo.space/course` (and `/course-v2`). The route code
lives in the Zo platform's route store, not in a Git repo. Updating
that course requires editing the zo.space route directly via the
`mcp__zo__edit_space_route` tool.

### `juniors/` → not currently published

The Claude-centric juniors track is dormant. The HTML builder used
during the original build is parked at
`docs/future-references/juniors-zo-rewrite/` for the eventual
Zo-centric juniors rewrite. There is no live site for this track today.

---

## Repo separation rationale

`clarion-site` is intentionally a separate repo so the firm's website
(`clarionintelligencesystems.com`) has its own deployment lifecycle and
can be updated without touching course content, and vice versa. The
trade-off is that course content has to be mirrored explicitly. The
sync script + prebuild guard make that mirror visible and enforceable.

Do **not** convert the bundled mirror into a Git submodule unless you
are prepared to handle the CI complexity that introduces. The current
"mirror + check" pattern is intentionally simple.

---

## History

- **2026-04-30** — Original Zo-centric course shipped (commit `2b25a4a`).
- **2026-04-30** — Initial Clarion site build with bundled course
  (`clarion-site` commit `66c1178`).
- **2026-05-01** — Plain-English rewrite landed here as `873f945`,
  mirrored into `clarion-site` as `4fc720e`. This DEPLOYMENT.md was
  written the same day after a "the github push didn't update the
  website" investigation revealed the missing mirror step.
