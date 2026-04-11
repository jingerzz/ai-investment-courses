# /course-v2 Route Changes — Pricing Scroll Improvements

**Date:** 2026-04-11
**Route:** `/course-v2` (zo.space page route, not a filesystem file)
**Base commit:** 931d0a0

## What changed

The `/course-v2` route wraps an iframe (course content) and a `#pricing` section inside a snap-scroll container. These changes improve the scroll transition between them.

### 1. Snap behavior tightened

- Container: added `snap-mandatory` (was only `snap-y`)
- Iframe: added `snap-start` class (pricing section already had it)
- Together these ensure the viewport decisively locks to either the course content or the pricing section — no half-states.

### 2. Smooth scrolling

- Added `scrollBehavior: "smooth"` to the scroll container's inline style
- Snap transitions now animate rather than jumping instantly

### 3. Scroll-down indicator

Injected a small element between the iframe and `#pricing`:

- Displays "Pricing & enrollment" label with a bouncing chevron (SVG, `animate-bounce`)
- Clickable — smooth-scrolls to `#pricing` on click
- Fades to 30% opacity once the user scrolls past 80px (tracked via `useRef` + scroll listener)
- Styled: `text-zinc-500`, `text-xs`, `py-3`, `bg-zinc-900`, `border-t border-zinc-800`

### 4. React additions

- Imported `useRef`, `useEffect`
- Added `scrollRef` on the scroll container
- Added `showIndicator` state (boolean, default `true`)
- `useEffect` attaches a passive scroll listener that sets `showIndicator = scrollTop < 80`

## Current route code location

This route exists only in zo.space (not on the filesystem). To inspect or edit:

```
# List routes
zo.space → list_space_routes()

# Get full code
zo.space → get_space_route("/course-v2")
```

## Next steps

- Review scroll feel on mobile — `snap-mandatory` can be aggressive on touch devices
- When ready, replicate these changes to the production `/course` route
