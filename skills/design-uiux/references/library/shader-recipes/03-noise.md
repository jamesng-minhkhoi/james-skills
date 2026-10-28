# Noise

Perlin-style noise is the atom of organic looks: aurora, smoke, liquid,
topography, grain. Everything else in this file is noise moved through time or
space with a designed intent.

## Value noise in ~8 lines (adapted; GLSL ES has no built-in noise)

```glsl
float hash(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
float noise(vec2 p) {
  vec2 i = floor(p), f = fract(p);
  vec2 u = f * f * (3.0 - 2.0 * f);            // smooth hermite: no seams
  return mix(mix(hash(i), hash(i + vec2(1, 0)), u.x),
             mix(hash(i + vec2(0, 1)), hash(i + vec2(1, 1)), u.x), u.y);
}
// fbm: 3–4 octaves is plenty; each octave doubles cost
float fbm(vec2 p) {
  float v = 0.0, a = 0.5;
  for (int i = 0; i < 4; i++) { v += a * noise(p); p *= 2.03; a *= 0.5; }
  return v;
}
```

## The four designed motions

| Motion | Recipe core | Reads as |
| --- | --- | --- |
| Breathe (in place) | `n = fbm(vUv * uScale + uTime * 0.05)` | Aurora, mist, calm |
| Flow (direction) | `fbm(vUv * uScale - vec2(uTime * uSpeed, 0.0))` | Water, wind, conveyor of data |
| Crawl/surface | Sample noise in *world* space of geometry | Liquid surface, cloth |
| Terrain/height | `h = fbm(vUv * uScale)` fed to geometry | Mountains, dunes, data fields |

Direction of flow is meaning: downward = deposit, outward = distribution,
rises = accumulation. On the option sheet each noise moment states its
direction and why, so a "which way is it flowing?" review has an answer.

## The designed choices that keep noise from reading as "shader demo"

- **Scale jumps:** one – two octaves with a scale ratio near 2.0 reads as
  organic terrain; many-octave stacks with random ratios read as "Twitter
  shader default".
- **Amplitude framing:** noise output spans 0→1, but the designed surface
  read uses the *middle band* (e.g. remap fbm by `smoothstep(0.35, 0.9, n)`),
  which removes the random-flicker cell texture and keeps painted sweep.
- **Colorization is NOT in the noise:** pick colors from the ramp *after* the
  height — mix(uColorB, uColorA, n) rather than gradient-by-noise inside the
  pattern (keeps brand control, exactly like displacement topic).
- **Grain is a finishing pass, not the pattern:** film-grain overlays the
  page texture (1-line hash dithering) should be in the DOM's `mix-blend-mode:
  overlay` layer where possible, saving the GPU for the field.

## Reduced motion

`uTime` is frozen by a UI-preference uniform; the field must be designed so
the frozen frame still *reads as terrain/aurora and not as a JPEG of static*:
check the frozen frame at 3 arbitrary times, any of which must hold up.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs/threejs-shaders, MIT); see [NOTICE.md](../../../../../NOTICE.md).
