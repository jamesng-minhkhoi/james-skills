# Uniforms and varyings

The two data paths every recipe below uses. Knowing *who owns each number*
avoids the most common review confusion: "why does the designer's token not
take effect?" (it was a shader constant) and "why is the motion frozen?"
(the uniform was never updated after mount).

## Uniforms: set from the CPU, shared by every pixel

| Uniform type | Design meaning | Token mapping |
| --- | --- | --- |
| `vec3 uColorA/uColorB/uColorC` | The surface's color ramp | Brand ramp tokens, no hand-picked hex |
| `float uProgress` | Where in the story the surface is (0→1) | Scroll/timeline driven |
| `float uTime` | Ambient motion phase | Only if idle motion is designed; frozen under reduced motion |
| `vec2 uResolution` | Composition relative to canvas size | Auto; affects gradient framing across breakpoints |
| `float uIntensity` / `uSpeed` | The look's dials on the option sheet | Named on the sheet as adjustable values |

Uniform names go on the sheet exactly as the design's *knobs*: "uIntensity
1.0 = brand glow, 0.4 = whisper". An option presentation that hides the dials
can't be tuned by review.

```tsx
// R3F: uniforms live as refs; never recreate the object per frame.
const uniforms = useMemo(() => ({
  uColorA: { value: new Color(theme.revenue.warm) },
  uColorB: { value: new Color(theme.revenue.cool) },
  uProgress: { value: 0 },
}), []);
```

## Varyings: computed per-vertex, interpolated across the face

The GPU interpolates varyings between vertices — this is why a gradient looks
smooth with almost no per-pixel math. Design takes:

- `vUv` (0–1 across the surface): position-of-UV effects, mostly 2D quads.
- `vPosition/vNormal` (world or view space): edges, lighting, radial patterns
  on real geometry.
- Custom curved coordinates (e.g. `vUvDistorted`) when the surface is bent and
  gradients must follow the bend.

## The two frequency classes (why some patterns "pulsed" wrongly)

1. **Per-vertex (or per-fragment-of-quad)** — gradients, UV effects: resolution
   of a 6-vertex plane is as smooth as a 5000-vertex one.
2. **Per-fragment** — noise, rim, dissolve masks: as heavy as pixel count ×
   pattern complexity. Budget and mobile pixel ratio caps (see
   [performance](07-performance-and-debugging.md)) apply to this class.

Placement decision is a design one: a subtle full-bleed field belongs in
flat-quad fragments (cheap, forgiving); a surface detail on curved product
geometry must be per-fragment to hug the form.

## Token Reminder

Shader constants (a `#define`-style color or a magic middle number) hide the
brand. During hand-off the scene's uniforms map to design tokens, and any
stripped-in constant needs its own line on the sheet. Undeclared constants are
`unverified` design claims — reviewers have no script to tune.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs/threejs-shaders, MIT); see [NOTICE.md](../../../../../NOTICE.md).
