# Kinetic hero

The hero's first movement is the product's handshake. Job options: focus
attention on the promise (mask-and-stagger), signal craft (typographic
weight/width shift), or establish theme (ambiance that drifts behind the type).
Job must be stated before choosing; a hero that animates everything animates
nothing.

## Masked line stagger (Framer Motion default)

Lines clipped by overflow masks, translating up into view with a slight
stagger. Direction is a vocabulary choice: up = arrival, down = reveal-from-above,
left = lateral storytelling. Keep $y$ offsets to roughly 0.6–1.1 em of the
heading size so motion reads as theatrical, not travel.

```tsx
"use client";
// Lines wrapped in overflow-hidden containers; spring > duration: accelerates
// out of stillness and overshoots slightly, which duration curves cannot.
const lineVariants = {
  hidden: { y: "110%" },
  show: (i: number) => ({
    y: "0%",
    transition: { type: "spring", stiffness: 120, damping: 20, delay: 0.35 + i * 0.08 },
  }),
};
```

- Stagger inside a line (per-word) only when the headline is short (< 6 words);
  longer text staggers per-line.
- Content must not be readable during motion and unreadable after: end state is
  the design truth; verify the resting frame against `landing-visual` rules.
- Web fonts: motion before the font loads flashes wrong metrics. Trigger the
  reveal from font readiness (`document.fonts.ready`) or accept the flash and
  note it.

## Weight or width shift (variable-font signal)

A single variable-axis transition on hover/focus — weight 300→600, width
condensed→normal — signals editability or interactivity with zero layout
stress, because the glyphs themselves change. Pair with a static state change
(color or underline) so the affordance exists without motion. Fails loudly
with static fonts: detect thevariable-axis availability or skip to the static
fallback.

## When GSAP earns its place

Reach for GSAP when the reveal needs orchestration beyond CSS-variable-driven
motion: parsing text into per-character spans, timeline branching (skippable
chapters), or one timeline serving multiple surfaces:

```ts
import { gsap } from "gsap";
// SplitText-class parsing, adapted: split once, animate the splits.
const split = headline.querySelectorAll("[data-word]");
gsap.from(split, {
  yPercent: 110, stagger: 0.06, ease: "power3.out", duration: 0.9,
  scrollTrigger: { trigger: headline, start: "top 85%", once: true },
});
```

Register `ScrollTrigger` client-side once (`gsap.registerPlugin`) inside the
nearest client boundary. GSAP is a runtime dependency for the whole page
budget: justify it when Framer Motion variants could carry the same grammar.

## Reduced-motion and failure frames

`prefers-reduced-motion` renders the resting frame immediately (variants
`initial={false}` or a media-query guard) — plus a *no-JS or blocked-font*
static layout that still communicates the promise. The hero must not be empty
during hydration: server-render the headline with a CSS-only fallback
appearance, and let motion be an enhancement on top.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(gsap-skills, MIT); see [NOTICE.md](../../../../../NOTICE.md).
