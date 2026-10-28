# Shader recipes

Use this module when the desired look is a *material or field*, not an object:
liquid or gradient surfaces, noise-scrolled atmospheres, dissolve transitions,
displaced geometry, glow rims. Shaders live either behind material extensions
(see [three canvas](../three-canvas/index.md)) or inside a standalone WebGL
canvas; the recipe code is environment-neutral GLSL adapted to R3F use.

Before a shader: name the look in one sentence and its moment job. "Gradient
shader" is not a design; "a light field that rises as shipments reconcile,
ending still" is.

| Topic | Use for |
| --- | --- |
| [Uniforms and varyings](01-uniforms-and-varyings.md) | The data plumbing: what the CPU controls, what the GPU computes |
| [Gradient fields](02-gradient-fields.md) | Linear/radial/curved gradients, brand-tied surfaces |
| [Noise](03-noise.md) | Organic motion: value noise, flow, aurora, grain |
| [Fresnel and rim](04-fresnel-and-rim.md) | Edge glow, silhouette emphasis, "hologram" reads |
| [Dissolve](05-dissolve.md) | Transition: state swap with a designed edge |
| [Vertex displacement](06-vertex-displacement.md) | Geometry shaped by fields: mountains, cloth, liquid |
| [Performance and debugging](07-performance-and-debugging.md) | Frame budget, common visual bugs, reduced motion |

The GLSL snippets follow the [stack translation](../../creative-catalog.md#adapting-source-material)
rules: technique over environment, tokens over hardcoded colors, and reduced
motion is a uniform (`uReduced`) the scene sets, not an optional nicety.

---

Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs/the threejs-shaders pack, MIT); see [NOTICE.md](../../../../../NOTICE.md).
