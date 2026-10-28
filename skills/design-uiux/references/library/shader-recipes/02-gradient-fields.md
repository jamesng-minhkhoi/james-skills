# Gradient fields

Gradient *fields* (shader gradients) are the designed successor to CSS
gradient stops: smooth interpolation across curved coordinates, animated
without banding, and keyed to brand tokens instead of "purple-to-blue" defaults.

## The three base fields

```glsl
// § Linear: direction a design decision (rise = growth metaphor)
float t = smoothstep(0.0, 1.0, vUv.y + uWarp * noise(vUv));
vec3 color = mix(uColorA, uColorB, t);

// § Radial: distance from a focal point (spotlight/concentration metaphor)
float d = distance(vUv, uFocus);
vec3 color = mix(uColorA, uColorB, smoothstep(uInner, uOuter, d));

// § Angular: sweep around a point (compass/cycle/stadium metaphor)
float angle = atan(vUv.x - 0.5, vUv.y - 0.5) / (PI * 2.0) + 0.5;
vec3 color = mix(uColorA, uColorB, fract(angle + uProgress));
```

Metaphor-first: a gradient earns its space when its form is the data's shape —
rise for growth, radial for focus/concentration, angular for cycles. A
decorative "aurora blob" with no metaphor is the gradient slop tell
([landing visual](../../landing-visual.md) already rejects it).

## Multi-stop control

Two colors is one statement. Three stops need a designed order (which is
shadow, which is highlight, which meets the copy):

```glsl
vec3 color = mix(
  mix(uColorA, uColorB, smoothstep(0.0, uStop1, t)),
  uColorC,
  smoothstep(uStop1, 1.0, t)
);
```

Stops that go too light bang into the banding zone; versioned dithering:

```glsl
color += (hash(vUv * uResolution + uTime) - 0.5) / 255.0 * uDither;
```

## Animation dials (each named on the sheet)

| Dial | Effect | Defect when wrong |
| --- | --- | --- |
| `uWarp` | Field wobble via noise | Above ~0.8 with text on top: the gradient swallows copy |
| `uSpeed` | Motion tempo of the field | Speed > ~0.6 and it reads as noise video, not ambience |
| `uContrast` | Ramp spread | Both endpoints too close = "muddy gray blob" defect |
| `uFocus` (radial) | Hot-spot position | Instability if driven directly by pointer without easing |

Dials freeze under `uReduced`: the field shows one designed still (usually the
progress mid-point or a hero crop), which must look correct at any scroll
position rather than only at progress 0.

## Contrast with DOM gradients (the option for the sheet)

A shader gradient wins when: (1) it animates continuously and smoothly,
(2) it follows curved UVs, (3) it dithers against banding at large surfaces.
A CSS linear-gradient wins when: static, straight, two stops, and must be
pixel-perfect behind text. The sheet should show the CSS option at this cost
ratio (near-zero JS) for the same moment.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs/threejs-shaders, MIT); see [NOTICE.md](../../../../../NOTICE.md).
