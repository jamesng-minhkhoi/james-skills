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
