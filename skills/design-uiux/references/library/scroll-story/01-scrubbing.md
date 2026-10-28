# Scrubbing basics

Scrub = a viewer's scrollbar position directly parameterizing the visual.
Everything else (pinning, canvas feeds) composes on top of it.

## Design in tolerance bands, not pixel positions

A scrub designed at exact scroll offsets breaks on different viewport heights
and zoom levels. Design bands by document-fraction and check the four corners:
very short view, very tall view, slow smooth-scroll, jumpy discrete wheel.

| Field | Design decision |
| --- | --- |
| Progress source | The element's viewport travel, not `window.scrollY` — same story must scrub identically in any document position |
| Start/stop anchors | Named by layout landmarks (section top hitting X% viewport), never fixed px |
| Velocity | Whether motion uses raw scroll delta or lerps toward target (lerp smooths discrete wheel steps; raw is more honest) |
| End-state truth | Scrub is an *interpolation between two designed states*; both keyframes must be complete designs, not one design plus noise |

## Framer Motion scrub

```tsx
"use client";
const ref = useRef<HTMLDivElement>(null);
const { scrollYProgress } = useScroll({ target: ref, offset: ["start end", "end start"] });
const rotate = useTransform(scrollYProgress, [0, 1], [-8, 8]);   // both ends designed
const scale  = useTransform(scrollYProgress, [0, 1], [0.92, 1.0]);
```

`useVelocity` on the motion value powers effects that respond to scroll
*energy* (blur amount, letter spacing, color lean) — decaying the scalar keeps
it from reading as jitter.

## GSAP ScrollTrigger scrub (pin without dialogue)

When Framer Motion cannot express the orchestration (nested timelines,
label-scrub together with pin):

```ts
gsap.to(scene, {
  scrub: 1,                       // 1s catchup lerp; 0 = raw finger
  scrollTrigger: {
    trigger: section,
    start: "top bottom",          // both ends by layout landmark
    end:   "center center",
    invalidateOnRefresh: true,    // recompute on resize/fonts loaded
  },
});
```

When design intent is "state N replaces state M at a boundary", use
`onEnter`/`onLeaveBack` steps, not interpolation: a scrubbed crossfade between
two texts is designed opacity choreography; a scrubbed *position jump* is a
different behavior, choose one and name the difference on the option sheet.

## Harness rules

- The resting frame after the section scrolls out of view equals the end
  keyframe exactly. Scrub leaving a half-interpolated placeholder is a defect.
- Pre-hydration state: a scrub section must show its *start* design during
  SSR/hydration, not a blank box that pops in on a JS effect.
- Reduced motion freezes at whichever keyframe matches the un-scrolled state.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(gsap-skills, MIT); see [NOTICE.md](../../../../../NOTICE.md).
