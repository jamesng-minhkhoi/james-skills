# Reveal systems

A reveal grammar is one shared rule — distance, easing, stagger count, trigger
point — applied to every block entering view. Invent it once, name it, and
reuse it; a page where each section animates differently reads as a template
stitch. Inconsistency here is exactly what `slop-and-consistency` flags.

## Define the system before applying it

| Field | One decision per product |
| --- | --- |
| Travel | Distance and direction (e.g. 24 px up, no horizontal) |
| Curve | One entrance curve, one entrance speed; exits may differ |
| Stagger | Max concurrent elements (< 5); cadence if more |
| Trigger | Viewport entry point (e.g. 0.12 from bottom) for ALL blocks |
| Unit | What gets its own beat vs. what shares one |
| Exceptions | Named moments exempt (hero, a single scroll story) |

## Framer Motion viewport grammar

```tsx
"use client";
// One exported reveal used everywhere; per-use children, fixed grammar.
import { motion, useReducedMotion } from "framer-motion";

export function Reveal({ children, delay = 0 }: { children: React.ReactNode; delay?: number }) {
  const reduced = useReducedMotion();
  return (
    <motion.div
      initial={reduced ? {} : { opacity: 0, y: 24 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-12% 0px" }}
      transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1], delay }}
    >
      {children}
    </motion.div>
  );
}
```

- `once: true` keeps content stable on back-scroll: re-animating everything on
  return is noise, not delight.
- `margin`/`amount` is the *distance from the trigger line*, in typography's
  favor: reveal while the first line still would, not after it fades in.
- Nesting reveals (section staggers its children) is the only legitimate
  second layer; a child starting its own independent third layer breaks the
  rhythm.

## GSAP batch equivalent

When the page already runs ScrollTrigger and blocks arrive in clusters:

```ts
gsap.utils.toArray("[data-reveal]").forEach((el) => {
  gsap.fromTo(el, { y: 24, opacity: 0 }, {
    y: 0, opacity: 1, ease: "power2.out", duration: 0.6,
    scrollTrigger: { trigger: el, start: "top 88%", once: true },
  });
});
```

Same grammar, one source of truth: export the start point and duration as
constants next to the grouped selectors so the system is auditable.

## Anti-patterns to reject on the option sheet

- Reveal distance > one text line of travel: reads as "content teleported in".
- Arbitrary per-section style differences that read as AI-template joins.
- Reveal-everything-on-view pages: reserve the system for at most 2–3 moments;
  everything else stays visible with no entrance.
- Opacity-only reveals of text bodies end in 0.0 blur: resolve to opacity 1;
  sub-1 resting states are `unverified` contrast.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(gsap-skills, MIT); see [NOTICE.md](../../../../../NOTICE.md).
