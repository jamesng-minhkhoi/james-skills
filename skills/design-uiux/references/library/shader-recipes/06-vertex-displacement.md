# Vertex displacement

Displacement moves vertices along a field instead of moving pixels: mountains
rise from planes, cloth bends, product surfaces ripple, data hills form from
real series. Design task: choose *the field, the direction, and the amplitude*
— all three encode meaning, and all three end up as soft-mock stills on the
option sheet.

## Core recipe

```glsl
// Vertex shader (plane geometry: 64×64 segments is the calibration default)
uniform float uTime, uAmplitude; // uAmplitude: fraction of subject scale — named on sheet
varying float vHeight; varying vec2 vUv;
// 1. Sample the field (noise from topic 03, or real data lines)
float h = fbm(position.xy * uScale + vec2(0.0, uTime * uFlow));
// 2. Displace along the plane's normal (plane Z axis here)
vec3 displaced = position + normal * h * uAmplitude;
vHeight = h;
// 3. New normal from the height field (accurate normals are what sell the form)
// derivative-based: sample h at x+dx and y+dy, cross() the deltas
```

| Field choice | Design meaning |
| --- | --- |
| fbm noise | Organic terrain; time-driftable |
| Real data line (the actual series) | Honest "data terrain"; the sheet's honesty gate prefers this over pretty noise when the metaphor is numbers |
| Radial (distance from a point) | Reconciliation spreading from the focal event |
| Sine + noise | Fabric/waves: regular structure plus organic wobble |

## Amplitude and frequency: relative to subject scale

Amplitude is specified as a fraction of the subject, never raw units: "ridge
height ≈ 12% of plane width". Frequency is specified by ridge count ("about 6
major ridges across the frame"): those two numbers, stated on the sheet, are
what make the look reproducible; every other value is composition.

## Displacement-only deformations (no texture / plane)

- Plane = Bills of properties: 64×64 segments is the calibration budget:
  below it, ripples alias into polygonal facets; above it, cost without
  readable detail (mobile pixel budget).
- Displaced geometry must compute *normals* from the height field: skipping
  normals makes everything look like a cheap normal-land (the classic
  displacement defect); derivative-sampling in the vertex shader is the
  default.
- Edges: an uncontained plane shows a hard rectangle silhouette against the
  page; contain via camera framing, fog, or the designed plate — announced in
  the composition line.

## Morph (same geometry through time)

When the displacement field itself is the story (the mountain is Q1 and
becomes Q4), the fields are blends: `mix(fieldA(position), fieldB(position),
uProgress)`. Both field keyframes get the [three canvas · motion rules](../three-canvas/05-scene-animation.md):
designed end-states, single primary driver scroll/timeline, lerp under
discrete wheel input.

## What displacement must never do

- Displace text-bearing DOM: shader geometry carries the scene; text never
  enters displacement (that's a 2D warp filter, different technique).
- Displacement amplitude with time velocity that fights scroll (scroll-fed
  field must keep single-driver rule).
- Metaphor inversion: heights fallen/rising contradictory to the direction of
  data (a growth story whose peaks recede upward-backwards reads broken).

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs/threejs-shaders, MIT); see [NOTICE.md](../../../../../NOTICE.md).
