# Geometry, particles, instancing

This topic covers the *density decisions* behind shape choices: when to model
vs. buy vs. generate, how many particles earn a moment, and where instancing
is mandatory.

## Geometry source decisions

| Source | Use when | Caveat |
| --- | --- | --- |
| Parametric primitives (`<Sphere>`, `<Torus>`, grids) | Abstract or data-shape moments | Primitives read as "3D demo" unless material and lighting carry the craft |
| Provided product/CAD/GLTF asset | Brand owns real geometry; brand accuracy matters | Design must reference the actual asset; sketch geometry misleads (never fabricate) |
| Procedural (shader/vertex) | Organic noise-driven form (mountains, fields, cloth-ish) | See [shader recipes · vertex displacement](../shader-recipes/06-vertex-displacement.md) |
| Purchased/marketplace asset | No provided asset and abstract won't land | Note license in the plan |

## Particle fields: count as a design decision

Particles are choreography *units of meaning*, not texture: their count and
motion must encode the metaphor stated in the prompt.

| Metaphor | Behavior |
| --- | --- |
| Many inputs → one output (users → consensus) | Particles individually slow, converging on a point with a confirmed arrival ease |
| Scale/grandeur (investors → markets) | Depth: near particles big and rare, far ones dense and faint; the density gradient gives the size cue |
| Activity (live process) | Velocity variance, not count; a sparse field with pulse beats dense chaos |
| Time-lapse skimming | Particles as short-lived streaks rather than persistent points |

- Count guidance: 5–200 units reads legibly and animates with per-unit nuance;
  300–5 000 when instanced on the GPU; tens of thousands need instancing +
  vertex-shader morphs, never per-object React overhead.
- Never implement a field as N React components: `InstancedMesh`/`Points`
  sacrifice nothing conceptually and cost orders of magnitude less.

## Instancing is a design constraint, not an optimization detail

On the sheet, the instancing decision appears as the count line: "≈2 400
particles, one instanced draw call". That line is checkable — prototypes that
hand-build thousands of meshes should sound obvious in review, and the honest
design time inscription: any count proposed must render on the target machine
before it is presented as [rendered proof](../../rendered-proof.md).

## What not to draw

- Text as geometry (except logo monograms): crisp typography belongs to the DOM
  layer; 3D text in the scene competes with the headline body.
- Human characters/avatars: uncanny valley risk + lighting budgets; use the
  illustrative layer instead unless the product IS characters.
- Rounded-cube "3D tiles" repeating a 2D grid: adds weight, subtracts meaning —
  the slop tell of template 3D.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
