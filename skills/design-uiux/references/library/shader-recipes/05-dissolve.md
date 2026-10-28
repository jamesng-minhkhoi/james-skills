# Dissolve

Dissolve replaces a state with noise-driven erosion rather than opacity: a
surface breaks apart along an organic threshold until it is gone (or the
inverse reveals it). Job: a *state change* materialized — upload complete,
session expired, entity reconciled into the ledger. It is a transition
technique; like all transitions it has a start design, an end design, and a
designed edge, or it is just noise.

## Core recipe

```glsl
// Fragment
float n = fbm(vUv * uScale);                       // same noise family as topic 03
float edge = smoothstep(uProgress - uEdgeWidth, uProgress + uEdgeWidth, n);
if (uProgress >= 1.0) discard;                     // fully gone
// Edge band: the rim line of erosion, a DESIGN decision, not fringe
float edgeBand = smoothstep(uProgress - uEdgeWidth, uProgress, n) - edge;
vec3 color = mix(uColorEnd, uEdgeColor, edgeBand) + edgeBand * uEdgeGlow;
```

The three design meanings of `uProgress`:

| Progress read | Start design | End design |
| --- | --- | --- |
| 0→1 erasure | Full content visible (the true state) | Fully gone + plate beneath holds composition |
| 1→0 reveal | Plate/empty visible | Full content (must equal the same resting frame the DOM calls "loaded") |
| 0→1→0 cross | A morphing transition (swap) | Both keyframes are real states; tween only between them |

## Edge design (the part people forget)

| Edge choice | Reads as |
| --- | --- |
| Thin bright band (uEdgeWidth ~0.03, uEdgeGlow) | Energy/burning away, "active process" |
| Wide soft band | Melt/erosion, deliberate, slower |
| No band (hard pow) | Crisp cut — only acceptable with hard geometry aesthetics |
| Band colored by brand token via `uEdgeColor` | The token line on the sheet keeps it owned |

## Timing and reduced motion

- Erasure takes 0.6–1.2 s semantic-matched (see
  [scene animation · morphing](../three-canvas/05-scene-animation.md)); slow
  dissolves for death/decay stories only when the threshold beat matters.
- Under reduced motion, dissolve swaps to the DOM's standard crossfade or an
  instant state replace: the design names that swap on the option sheet
  (`prefers-reduced-motion` static equivalent), since the dissolve's meaning
  (change of state) still needs a visible signal.
- `discard` caution: alpha-discard leaves hard edges at pixel ratios below 2 —
  the sheet's mobile column expects the ID-pass sampled-threshold (or
  dithering) variant instead of the bare `discard`.

## Never dissolve

- Critical reason-something states away (form errors): errors never dissolve
  into a "clean plate"; they stay until resolved.
- Data the user is currently reading (table rows disappearing under a cursor).
- Anything twice in five seconds: dissolve IS the celebration budget; looped
  dissolve reads as decoration with no job.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs/threejs-shaders, MIT); see [NOTICE.md](../../../../../NOTICE.md).
