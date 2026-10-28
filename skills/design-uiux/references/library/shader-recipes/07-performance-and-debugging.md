# Performance and debugging

Shader and canvas moments fail review on two axes: they stutter on target
hardware, and they look subtly wrong in ways designers cannot name. This topic
gives both a checklist and the fix vocabulary for handback.

## Frame budget contract (design-level)

| Design duty | Check |
| --- | --- |
| Most surfaces are per-vertex; per-fragment work earns pixel budget | Count the per-fragment ops (noise octaves, dissolve masks, rim) — 3 big ones per canvas is already heavy for mid-tier phones |
| DPR capped: `Math.min(devicePixelRatio, 2)` on desktop, 1.5 targeted on Android mid-tier | Also caps plateau effects on 3× iPhones (battery vs. crispness tradeoff is named) |
| Pause off-screen: IntersectionObserver + `frameloop="demand"`/`never` | Verified by watching GPU/time in devtools with canvas scrolled away |
| Static-twin renders on `prefers-reduced-motion` and WebGL-missing | Verified by forcing the media/site condition — never assumed |

## Common visual bugs (vocabulary for the review sheet)

| Symptom | Usual cause | Fix |
| --- | --- | --- |
| Gradient bands (stair lines) | 8-bit output over a low-contrast ramp | Dithering (hash noise at ±1/255) — this is a designed fix, name it |
| "Flickery TV static" instead of mist | Too many octaves / too-high frequency at low amplitude | Reduce octaves, remap amplitude band |
| Dissolve edge jagged | `discard` aliasing at DPR < 2 | Sampled threshold / dither; mobile column spec |
| Colors "wrong" vs. page UI | Color space mismatch (sRGB vs. linear) | Token colors set once via output color-space config; never per-material guesses |
| Crisp object on 2× screens glows when rim added | Fresnel width exceeds 1 pixel at DPR 1 | Increase `uPower` or rim alpha falloff; know what renders on the cheap screen |
| Canvas freezes after tab switch | Time accumulation (`uTime += fixed delta` with pause missing) | Time as accumulated `delta` with exposure; pause handling in scene |

## Debugging dialogue for handoff

When a rendered proof fails, name the class before re-render:

1. **Composition wrong** (frame/scale) → scene fundamentals topic.
2. **Material/edge wrong** (rim width/color/color-space) → materials + fresnel topics.
3. **Field wrong** (pattern scale, flow direction, octave count) → noise/gradient topics.
4. **Motion wrong** (timing, easing, driver conflicts) → scene animation topic.
5. **Frame-rate wrong** → this page (pause off-screen, DPR, octave counting).

The handover block names which class failed and what the fix altered, with
before/after stills for any still-relevant finding.

## When the shader stays but does less

Legitimate downgrades on the sheet (choosing one is a design decision):

- Drop octaves (4→2) and compensate with designed color ramps.
- Half-resolution render + upscale (fields with no text over them).
- Freeze ambient time into a 2-frame ping instead of full video-speed motion.
- Replace per-fragment rim with geometry-level fresnel via precomputed vertex
  colors (still designed, huge per-pixel savings).

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs/threejs-shaders, MIT); see [NOTICE.md](../../../../../NOTICE.md).
