# Compositor guide

The layer recipe, geometry math, and verification loop for the headless-Chrome
compositing technique. Adapted from the SnowMowBC generator
(`docs/store/screenshots/build/build-composites.mjs`, extraction provenance in
SKILL.md's footer).

## File layout in the product repo

```
<repo>/docs/store/screenshots/
├── README.md                     # per-slot upload mapping + regenerate cmd
├── ios-6.9/ ios-6.3/ ios-6.1/    # one dir per display-size slot
└── build/
    ├── build-composites.mjs      # the generator (one shot-story, one run)
    ├── photos/                   # full-bleed background stock photos, app icon
    └── raw/                      # real simulator captures, if any
```

Gitignore generator scratch output (`build/.build-*/`) — headless Chrome temp
HTML otherwise shows up as directory noise each run.

## The stage-scale trick

Design once, render to any slot. The page wraps all content in a stage sized
to the design canvas, scaled per output size:

```css
.stage{position:absolute;left:0;top:0;width:1284px;height:2778px;
       transform:scale(sx,sy);transform-origin:top left}
```

where `sx = W/1284`, `sy = H/2778` for the output canvas. The slight
non-uniformity (ratios differing under ~3%) is invisible; exact pixels are
not. Shot layout never changes with size — positions live in design
coordinates.

Render each size with headless Chrome:

```
chrome --headless=new --disable-gpu --hide-scrollbars \
  --allow-file-access-from-files --force-device-scale-factor=1 \
  --window-size=<W>,<H> --screenshot=<out.png> file://<page.html>
```

Write per-shot temp HTML into a `mkdtempSync` dir under `build/` and delete it
after. Use `file://` URLs for local photo/asset refs, not inline base64 —
keeps the generator diff-able.

## Layers (bottom to top)

1. `body` background (dark ink, for sub-photos or overscan).
2. Full-bleed photo: `object-fit:cover`, per-shot `object-position` chosen so
   the subject survives every aspect; a scrim overlay for dark-theme shots.
3. Device frame: upright, flush to canvas bottom (`position:absolute` anchored
   at the canvas bottom edge, shadowed). NEVER rotated; this is a hard
   user-preference correction from the underlying workflow. Corners, border,
   island, and shadow live in the frame layer.
4. Mock screen: fixed design width (430 works) scaled to the frame's interior
   width (`MS ≈ 1076/430 ≈ 2.5`). Draw the iOS status bar INSIDE the screen —
   `9:41`, island, signal/wifi/battery glyphs — so no raw simulator chrome
   survives (Guideline 2.3.10).
5. Pop-out cards, above all.

## Mock screens: faithful recreation

Recreate the app's real screens as small HTML surfaces keyed to the product's
own theme tokens (page colour, ink colour, accent, glass fill) and to the
actual screens' component structure. Preserve:

- labels and values exactly as the real screens render them;
- row, chip, and stepper geometry measured off the real screen;
- status/navigation/plumbing chrome (nav back, titles, tab bar or footer).

The store copy and imagery live in the generator; the app's feel lives in
tokens. Never introduce a feature, price, or state that no real screen has.

Status bar readability: on photo-backed screens give the status layer its own
ink or scrim; on light app screens stick to system black.

## Pop-out cards

A pop is a white card at a chosen spot, containing a component scaled around
the screen scale (`POP_S ≈ 1.6–2.4`; the pops slightly rebel against the
in-screen scale so they read as foreground):

```
box width  = mockW × POP_S + P × 2     # P = 40 uniform padding; P = 0 bare
box height = mockH × POP_S + P × 2
```

Rules that cost real time getting right:

- `mockH` must match the content's natural height; a wrong value leaves a
  whitespace gap under the content or clips it — measure by rendering once
  and crop-reading the box.
- With `bare=true` (no padding box, e.g. a translucent push banner or a photo
  tile) the content carries its own background; shadow still applies.
- Keep `left + boxWidth ≤ canvas width` unless the design intends a deliberate
  edge crop.
- Twin rule: a pop must not duplicate content readable in the screen. Acceptable
  pop content: a component whose in-screen twin is cropped off the canvas; a
  component from another screen; a real footer/button whose in-screen twin is
  out of view. The usual fix for a twin is dropping the pop for that element
  pair, keeping one CTA card only.
- Rotate slowly, sparingly: tilt of −7°…+5° reads intentional; beyond that,
  drop the rotation.

Positioning spellbook (design-canvas coords): pops live near the phone sides
at varied heights, so each shot's collage is distinct; reuse the same pop
grammar sets across the 8–10 shots instead of per-shot invention.

## Surfaces with cross-screen elements

Components appearing in more than one surface (rows, chips, steppers) are
shared CSS, and a style bug there propagates to both. The lesson this
workflow hit: a progress rail was hardcoded and misaligned in an in-screen
step AND in a pop; positions must be derived from the measured
content width (dot centers = rail endpoints), never eyeballed.

Escape entities in code, not markup: editor tooling may unescape `&`
literals when it rewrites a file, silently breaking the entity. Compose from
`String.fromCharCode(38)` at runtime when building HTML in JS.

## Verification loop

1. After every generator run, verify pixel dimensions of every PNG in every
   size dir (`sips -g pixelWidth -g pixelHeight`). Exact equality against the
   slot's supported sizes — no "close enough".
2. Crop-read trouble regions: `sips --cropOffset <y> <x> -c <h> <w> --out
   /tmp/crop.png <file>.png`, then open and visually judge. Regions to check:
   anything overlapping (pops over phone, cards over canvas edges) and any
   measured geometry (rails, chip rows, alignment baselines).
3. Iterate on the generator, never the PNG. Re-render all sizes from one
   run; a per-size hotfix reinstates drift.
4. Do a final full-res read of every shot. Judgement calls (photo choice,
   pop grammar, copy tone) go back to the user as an edit list, not silent
   re-choices.

## Sources

- Background photos: fresh stock photography per project (downloaded into
  `build/photos/`); do not reuse app imagery, icons in contexts that
  confuse, or the simulator's own wallpaper. Record the source per asset so
  the licences stay traceable.
- In-app icons/SVG glyphs: hand-write small SVG paths and store them
  inline; they render crisply at both display scales.
