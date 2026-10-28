# Scroll-fed canvas

Scroll position parameterizes a WebGL or shader scene (camera travel through a
space, material reveal, iterated particle seem). Highest ceiling of scroll
techniques, highest honest-cost: it requires the [three canvas](../three-canvas/index.md)
or [shader recipes](../shader-recipes/index.md) modules as prerequisites, plus
this page's scroll contract.

## The contract between scroll and scene

- **One parameter, one story.** Scroll maps to exactly one canonical
  scene parameter (camera z along a spline, a progress uniform, morph weight).
  Multiple coupled bindings (scroll → camera + rotation + fog together) must
  be named on the sheet as one authored curve, not emergent effects.
- **Design the full camera path visually first:** mock keyframes at progress
  0/25/50/75/100 as stills, verify each *alone* is a good composition, then
  design only the interpolation. A motion path whose endpoints are good but
  whose middle is a mess ships a moment that is bad for 3 of 4 frames.
- **Decouple with lerp:** the scene has its own thermostat — a smoothed value
  chasing progress (≈ 0.08–0.15 lerp factor per frame at 60fps) — never reads
  raw scroll delta. Discrete wheel steps then still read as continuous flight.

```tsx
"use client";
// Inside the single client component owning the <Canvas>
const progress = useRef(0);            // target
useScrollToward((p) => { progress.current = p; });   // from useScroll, outside
useFrame((state, dt) => {
  smoothRef.current += (progress.current - smoothRef.current) * Math.min(1, dt * 8);
  uniforms.uProgress.value = smoothRef.current;
});
```

- Pause when off-screen: IntersectionObserver on the canvas element reacts and
  `frameloop="never"`, or R3F `frameloop="demand"` + invalidate on scroll. A
  scene rendering 60fps while the user edits a form below it kills battery,
  not just FPS.
- SSR/bundle rules from [three canvas · SSR and budget](../three-canvas/06-ssr-and-bundle.md)
  apply non-negotiably.

## Compositions that earn this

| Moment | Why canvas earns it |
| --- | --- |
| Product fly-through with real geometry the brand owns | 2D cannot show true spatial form |
| Particle morph whose metaphors is corpus-driven (many → one, invested vs. escrowed) | Particle physics/density is substance, not style |
| Terrain/data field over time | Represents genuinely n-dimensional data |

And a reminder the honesty gate enforces: an HTML+CSS+Framer Motion terrarian
mock for the same metaphor is frequently *the safer employer* — show it as a
distinct option whenever the 3D does not unlock imagery that 2D literally
cannot produce.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
