# Textures and assets

Assets are the bridge between the design sheet and the rendered scene. Design
decides *what asset types exist, their aspect/roles, and their loading
behavior* — never the pixel-level production.

## Asset categories and their design decisions

| Asset | Design owns | Engineering owns |
| --- | --- | --- |
| Image textures (surface, logo decal, gradient plates) | What it depicts, aspect ratio, tonal role | `TextureLoader`/`useTexture`, color space, mipmaps |
| Environment map (for reflections/IBL) | Mood plate: neutral studio, dusk window, custom brand gradient | Generation/HDRI choice, resolution cap |
| Models (GLTF/GLB of product, UI glyph 3D set) | Source of truth (real asset vs sketch), orientation, units | `useGLTF` + draco/basis/compression pipeline |
| Data (particle seeds, time-series driving the scene) | The real numbers narrative | Buffer/attribute encoding, update cadence |
| Fonts for canvas text (rare) | Whether text belongs in the scene at all | SDF/mask layouts |

## Loading states are a designed surface, not a spinner

Every scene names its loading design *before* the heavy method appears on the
sheet:

1. **The plate arrives first:** page renders with the 2D fallback or gradient
   plate occupying the same layout block. No layout shift on scene mount.
2. **The scene fades/escalates in:** a 200–300 ms opacity step from plate to
   scene; per-asset suspense boundaries keep text from waiting on heavy models.
3. **Failure renders the plate, permanently:** WebGL unavailable / asset 404 /
   decode error all end in the same resting fallback. An error state that is a
   gray box is an undesigned deliverable, not an edge case.

## Realism cost tiers (state on the sheet)

| Tier | What it costs | Use |
| --- | --- | --- |
| Plate + primitives + env | ~No assets | Abstract moments, fastest builds |
| + Compressed textures (~2 texture maps) | +0.5–2 MB, decode pass | Product material truth, brand decal |
| + GLB models | +0.2–5 MB each, decode + GPU memory | Real product geometry |
| + HDRI env | +1–4 MB baked | Convincing reflections |
| + Post-processing chain | GPU time every frame per feature | Only for named dramatic moments |

The estimate lines go on the option sheet with the honesty gate's measured
numbers. An approximation is a declared assumption, not a claimed fact (see
[ontology](../../../_shared/ontology.md)); values in the sheet remain
`declared` until measured against the actual bundle.

## The `three-canvas` asset honesty check

- Text promised in 3D must come from real glyph/mesh licences already
  confirmed; never sketch typography as geometry placeholders.
- A "photo surface" without its provided map is fabricating the product's
  materiality; keep untextured changes as explicit placeholders worth labeling.
- Data-fed scenes must bind to real fixtures/demo formulas from the project,
  never invented arrays (particles of "revenue" need revenue data).

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
