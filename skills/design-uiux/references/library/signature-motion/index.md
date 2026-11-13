# Signature motion

Use this module when a moment should be brief (< 2 s), self-contained, and
memorable: entering a page, a milestone completing, a number landing, a cursor
or finger meeting a surface. For multi-step narratives driven by scroll,
switch to [scroll story](../scroll-story/index.md).

Read only the topics the request calls for. All snippets follow the
[stack translation](../../creative-catalog.md#adapting-source-material) rules.

| Topic | Use for |
| --- | --- |
| [Kinetic hero](01-kinetic-hero.md) | First-screen headline motion: masked lines, per-word stagger, weight/width shifts |
| [Reveal systems](02-reveal-systems.md) | Content entering a viewport: shared reveal grammar across a page |
| [Numbers and counters](03-numbers-and-counters.md) | Metrics, revenue ticks, progress states landing truthfully |
| [Pointer and device moments](04-pointer-and-device.md) | Cursor-following, tilt, magnetic buttons, gyro/webcam on web |
| [Mobile equivalents](05-mobile-reanimated.md) | Translating the above to Expo + Reanimated, and what to skip |
| [Text focus-in](07-text-focus-in.md) | One short line that is "said" (mascot bubble, assistant greeting, caption): the whole line goes from blurred to sharp in one motion, never word by word |
| [Celebration moments](08-celebration-moments.md) | Confetti, party poppers, milestone alerts: the gates a moment must pass, the yearly/rare/once/routine ladder, three treatments (burst from the subject, milestone card, mascot announces), piece physics, layering and Reduce Motion |
| [Digit pop-in](06-digit-pop-in.md) | A number the user just changed (total, price, filtered stat): the changed digits swap with a spring. The default for discrete changes; its table routes live numbers and words elsewhere |

Non-negotiables carried into every topic:

- The motion job is stated in one sentence before any snippet is chosen
  (continuity, hierarchy, cause-effect, progress, result, personality).
- Every topic ships with its reduced-motion variant; `prefers-reduced-motion`
  or the platform equivalent renders a static frame that still reads.
- Web snippets assume client components with effect cleanup; mobile snippets
  assume the Reanimated worklet thread (see topic 5).

---

Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs + gsap-skills, MIT); see [NOTICE.md](../../../../../NOTICE.md).
