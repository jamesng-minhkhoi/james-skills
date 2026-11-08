# Background textures: fixing flat surfaces

Use this router when a surface reads flat, empty, or generic and the fix is the
**background behind content**, not the layout or the copy. Typical requests:
"it feels flat", "give the hero some depth", "brainstorm backgrounds", or a
section that is a plain fill with nothing to hold the eye.

A background is only a candidate if it has a job. State the job in one sentence
first (separate a section, signal a category, add tactility, set mood, mark a
brand), then pick from the list. A texture with no job is decoration, and
[slop and consistency](slop-and-consistency.md) rejects it.

## Gates before any option

- **Legibility gate.** Measure text contrast against the texture's worst pixel,
  not its average. Body text needs 4.5:1; large display text needs 3:1. Any
  pattern that drops below that gets a scrim, a solid panel behind the copy, or
  is cut.
- **Frequency gate.** A background seen on every screen is part of the chrome,
  so it follows [motion and gesture](motion-and-gesture.md): subtle, static, and
  never competing with content. Animated backgrounds are reserved for rare
  moments.
- **Cost gate.** Prefer a static tile (CSS, a small SVG, or a small WebP/PNG)
  over a filter or canvas running on a large area. Any `feTurbulence` filter,
  blur over a large area, or per-frame canvas is a cost to measure, and each
  stays `unverified` until measured on a real build.
- **Honesty gate.** Photo-based options need a real, licensed asset. Do not
  present a generated image as a finished background without saying so.
- **Reduced motion.** Every animated option names its static fallback, per
  [motion and gesture](motion-and-gesture.md).

## The 22 techniques

Each entry gives the job it fits, a cheap implementation, and its main failure
mode. "Cheap" means the first thing to try before reaching for a heavy asset.

| # | Technique | Fits when | Cheap build | Main failure mode |
| --- | --- | --- | --- | --- |
| 1 | Felt texture | Warm, tactile, crafted, or editorial brands | Static noise tile or SVG `feTurbulence`, low opacity, tinted | Looks dirty on dark screens; hides small text |
| 2 | Fluted glass | Premium, architectural, or interior-brand sections | Repeating `linear-gradient` stripes with a light edge | Moiré on high-DPI screens; stripes fight with content edges |
| 3 | Thermal gradients | Data or climate, heat or intensity, scientific feel | Multi-stop `radial-gradient` or `conic-gradient` fields | Reads as a generic "AI gradient" if the stops are arbitrary; needs a meaning |
| 4 | Water ripples | Water, calm, wellness, or a reveal moment | Canvas or SVG rings; a static radial image as the fallback | Motion cost; animated by default fails reduced motion |
| 5 | Speckled graphite | Industrial, tools, dark UI, and serious product brands | Dark tint plus a sparse noise tile | Muddy on mid-grey; can look like a screen defect |
| 6 | Single-hue landscapes | Calm illustration, travel, and nature without busy detail | One hue in 3 or 4 tints, layered shapes, low contrast | Turns into a stock-vector look if the shapes are generic |
| 7 | Blueprint grids | Technical, dev-tool, architecture, and "plan" meaning | Repeating grid gradients, major and minor lines | Too strong, and the lines read as form fields |
| 8 | Halftone | Print, editorial, bold graphic, or retro pop | Radial-dot pattern at a fixed pitch, or a dithered image | Dots cut through text and fight with imagery |
| 9 | Grainy gradients | Modern brand fields and soft hero moods | Gradient plus noise tile at low opacity | Banding and blotchy grain on some displays |
| 10 | Grass texture | Outdoor, food, sustainability, and natural brands | Photographic tile or an organic SVG pattern | Usually needs a real photo; a fake one looks cheap |
| 11 | Dithered images | Retro, game, lo-fi, or a deliberate craft look | Pre-dither the asset offline, or a CSS `image-rendering: pixelated` scale | Hard to read small; can feel gimmicky if the whole page uses it |
| 12 | Paper texture | Editorial, writing, notes, warm trust | Paper-grain image tile, subtle shadow, off-white base | Muddies contrast; reads as skeuomorphic on app UI |
| 13 | Contour lines | Maps, topography, data density, or a "level" concept | SVG contour paths or a repeating radial gradient | Lines compete with text; generated contours look random |
| 14 | Cloud sky | Light, open, travel, or aspiration | Soft photo or layered blurred blobs | Stock-image feel; blobs read as the "AI glow" default |
| 15 | Pixel mosaics | Gaming, retro, mosaic tiling, or a grid brand | CSS grid of colored cells or a canvas tile | Busy at small sizes; pattern repeats are obvious |
| 16 | Lens distortion | Photography, optics, and a spatial or camera feel | SVG `feDisplacementMap` on a static image, or pre-warped asset | Heavy filter; warps faces and product shots |
| 17 | Stippled gradients | Vintage print, engraving, or soft tonal fields | Dot-noise tile over a gradient | Looks like dirt at small sizes |
| 18 | Square-dot grids | Dashboards, tech, workspace, and quiet structure | `radial-gradient` dot at a fixed grid | Cheap and useful, but pervasive; reads as a generic dev-tool look |
| 19 | Blurred photos | Hero depth with a real photo behind it | Photo with `filter: blur` and a darkening scrim | Blur on a large area costs; the photo must still be real and licensed |
| 20 | Iridescent shapes | Premium, fintech, or product-launch moments | Shader or layered gradient shapes with a sheen | Trend-driven; hard to justify without a brand reason; cost |
| 21 | Impressionist paintings | Culture, art, food, or hospitality | Licensed painted image, cropped and tinted | Rights and provenance; a stock painting reads as filler |
| 22 | ASCII and pixels | Terminal, developer, retro-tech, or a witty brand | Monospaced character field in a `pre`, or a canvas grid | Readability; forces the brand to read as a joke if overused |

## How to choose

1. Name the job in one sentence. If no job fits, pick none. Plain is valid.
2. Narrow to 2 or 3 options that fit the brand's tone, not the trend.
3. Build the cheapest version first (static CSS or SVG). Show it on the real
   content at real widths, not on an empty box.
4. Check legibility at the worst pixel, then the cost gate, then reduced motion.
5. Present the options with the job, the cost tier, and the legibility result.
   Mark any cost or contrast claim not measured on a real build as `unverified`.

## Tone rules

- One texture per surface. Two or more fight, and the page reads noisy.
- Texture belongs to a section or a moment, not every card. Do not stack a
  texture on a texture.
- A texture must not replace a missing layout decision. If the section is
  weak, fix the hierarchy first.
- Match the product's tokens: tint the texture from brand colours, do not add
  a new palette for it.
