# SSR and bundle honesty

Three.js on Next.js is a client-bundle decision. This topic turns the honesty
gate into concrete, checkable requirements: what the option sheet carries at
design time, and what the handoff must measure before engineering builds.

## What the gate requires before a 3D option is presented

| Requirement | How it is checked |
| --- | --- |
| Client-only mount | Scene lives behind `next/dynamic` with `ssr: false`, loaded from the page's client boundary; no `<Canvas>` in server component paths |
| Named moment | One sentence: what the 3D shows that 2D cannot. "Depth of the product" counts; "looks cool" does not |
| Declared estimate | Rough route-chunk cost stated as `unverified` at option time; the real measurement is required before build handoff (below) |
| 2D twin option | A non-3D option on the sheet for the same moment — or the named concrete 2D constraint that defeats one |
| Fallback design | The quiet frame + no-WebGL fallback (see [textures · loading](04-textures-and-assets.md)) is designed |
| Render sanity | Scene renders and composes at 1440 AND 390 before it is shown (rendered proof, not declared) |

The option sheet carries rows 2–5 (named moment, declared estimate, 2D twin,
fallback design). Row 1 (client-only mounting) is engineering's wiring job,
and the render-sanity row is the rendered-proof duty before the option leaves
the sheet. The measured `next build` chunk size for the route (reported in KB,
never guessed) is the engineering gate checked before build handoff — design
does not present a measured number it cannot observe.

## Cost knowledge for the estimate (then measure)

- `three` core is on the order of half a megabyte minified; R3F + drei add
  tens-to-hundreds of KB depending on imports. Design assumption: a
  canvas-backed route roughly doubles its JS payload vs. a motion-only route.
  Then measure with `next build` and replace the estimate — the ontology makes
  an unmeasured number `unverified`.
- Assets layered per [textures · cost tiers](04-textures-and-assets.md) are
  separate from JS cost; a 2 MB HDRI can hurt more than the library itself.
- Dynamic import splits the scene chunk behind the route's initial payload; the
  *route-level* regression size is what the budget line reports.

## Never-block rules

- No synchronous three imports at module scope of non-canvas modules: barrel
  imports that pull three into the shared chunk are the classic accidental
  regression (`import { Canvas } from …` in a layout file does it).
- Canvas mount is below the fold-by-default unless the scene IS the hero; the
  hero case accepts the cost consciously with the moment sentence to prove it.
- `frameloop` must pause off-screen: an invisible canvas burning 60 fps is a
  defect regardless of design approval; interaction below the scene (forms,
  reading) must stay smooth (compare against the page's interaction lags).

## Cheap upgrades that pass review

Before accepting the library cost, name these as considered-and-rejected or
considered-and-chosen alternatives on the sheet:

- CSS 3D transforms (perspective card wall, device tilt) for shallow depth.
- Lottie/SVG for scripted-drawn moments.
- `<canvas>` 2D hand-drawn animation for particle-ish effects at fraction of
  cost (fits for glyph rain, star field, or confetti passes).
- Pre-rendered looping video (mp4/webm) for a one-off camera flight — static
  cost, no geometry parsing, works everywhere.

The 3D choice is only won by argument when a cheaper alternative is visibly on
the table. That is the honesty gate doing its job, not paperwork.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
