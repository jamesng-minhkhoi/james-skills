---
name: app-store-screenshots
description: Produce App Store and Google Play screenshot sets from real app surfaces — one design canvas composited in headless Chrome, scaled pixel-exact to every display-size slot (6.1, 6.3, 6.7, 6.9, iPad), with full-bleed stock backgrounds, an upright device frame, faithful mock screens, and pop-out cards. Use for store screenshot creation, "File dimensions are invalid" slot rejections, resubmission assets, and 2.3.x screenshot guideline fixes. Not for video previews (→ product-video) or submission audits (→ audit-mobile-store-submission).
---

# App Store Screenshots

Produce the store screenshot sets a submission needs: portrait marketing PNGs
in every display-size slot the portal requires for the current submission,
each derived from the same design canvas and each showing the real app's
surfaces. The artifact is a directory-per-display-size set of PNGs plus the
deterministic generator that rendered them, kept in the product repo.

Shared vocabulary: [ontology](../_shared/ontology.md). Every verification step
names its proof-ladder rung; the deliverable verdict uses
`READY | READY_WITH_CONDITIONS | NOT_READY | UNKNOWN`.

## When NOT to use

- App previews and demo video screens (→ `product-video`).
- Deciding whether a submission is ready, parsing a full rejection letter
  beyond its screenshot/dimension lines (→ `audit-mobile-store-submission`).
- Designing the screens themselves from scratch (→ `design-uiux`). This skill
  recreates existing, shipped surfaces.
- In-app UI implementation (→ `frontend-mobile-engineering`).

## Operating rules

- The store slot's own supported-sizes line is the authority for dimensions.
  The table in [display sizes](references/display-sizes.md) is a fast guess,
  not authority; slots change and per-slot text overrides it.
- Screenshots must primarily depict the app in use (App Review 2.3.3, observed
  in this session's portal text) and must carry an iOS-native status bar with
  the device's island or notch shaped in (2.3.10): no Android-style bars, no
  unpainted raw simulator chrome.
- In-screen content is always a recreation of a real screen: copy, states,
  hierarchy, colours, and ordering copied from those product screens. The mock
  is HTML with the product's own theme tokens; no invented copy claims.
- The device frame is upright, NEVER rotated, and flush to the canvas bottom
  (a user-visible hard preference from this workflow's history); floats and
  pop-out cards may crop at canvas edges, the frame may not.
- Pop-out cards never duplicate content already readable in the phone screen.
  A pop shows content cropped off-canvas in-screen, content genuinely off
  the canvas, or context the screen cannot show.
- Rebuild all sizes from one generator run; never hand-crop one PNG. A mixed
  resize set is what "File dimensions are invalid" rejections come from.

## Workflow

### 0. Read the slots, not memory

Open the store portal slot (or the user's paste of its supported-sizes text)
first; record target pixel dimensions per slot. If the slot text disagrees
with [display sizes](references/display-sizes.md), the slot text wins and the
reference gets dated. Output: the dimension list this run must hit.

### 1. Contract the surfaces

Pick 8–10 shots covering the whole journey (both customer and provider sides
if the product has them). For each shot name the real screen that backs it.
Copy arrives from the product repo, not imagination. Output: a shot table —
order, badge, headline, sub-headline, backing screen path.

### 2. Design one canvas

Design at one canonical size (the 6.9 or 6.7 geometry works: e.g. 1284×2778).
Every other output size is
the same HTML stage scaled by CSS transform; never redesign per size. Shot
copy stays identical across sizes. Output: the design
plan (per-shot theme, background photo, object-position, light or dark ink).

### 3. Build surfaces faithfully

Recreate the backing screens in HTML at the mock's native width, scaled into
the frame; status bar `9:41` with island; navigation bar, rows, chips, and
progress elements derived from measured content. Source work to generate:
[compositor guide](references/compositor-guide.md) has the layer recipe,
scale math, and the geometry patterns that broke in practice (pop whitespace,
stage hardcoding, off-canvas pops).

### 4. Compose backgrounds and pop-outs

Full-bleed stock photos per shot (`object-fit:cover`, per-shot
`object-position`) — fresh imagery, never reuse the app's own assets. Add
pop-out cards with the geometry formula in the guide and the twin rule from
Operating rules. Copy for a 3+ shot session: reuse the same collage grammar
(pop position, scale band) rather than re-inventing per shot.

### 5. Render every slot

One generator run renders one PNG per shot per slot size with headless Chrome
at `--window-size` equal to the target canvas. Keep the generator and its
photos in the product repo so the set regenerates deterministically.

### 6. Verify, then re-verify after any change

- Dimension gate: every PNG's pixel dimensions verified (`sips -g
  pixelWidth -g pixelHeight`) — `rendered` rung.
- Geometry gate: weird regions (overlapping floats, rails, off-canvas crops)
  crop-read at full resolution (`sips --cropOffset`) and eyeballed.
- Fidelity gate: in-screen copy checked against the backing screens —
  `declared` from source, surfaces `rendered`.

Iterate on the generator until clean; every rebuild re-runs all gates.

### 7. Hand over for upload

Print the set: folder per size, per-slot upload mapping,
pixel dimensions, and any judgement the user still owns (upload slot, store
copy). Hand over the generator command for future submission deltas.
Never upload or push portal state; that is the user's action.

## Gates

- **G1 dimensions exact** — every PNG `PASS`es its slot's supported sizes.
  Known failing input: a 1320×2868 PNG in the 6.1/6.3 slot (this project's
  observed "File dimensions are invalid" rejection, 2026-10-31).
- **G2 iOS status bar** — each frame's status bar is iOS-styled. Known
  failing input: black Android-style bar or raw simulator chrome behind
  content (the 2.3.10 rejection this workflow fixed).
- **G3 real-app fidelity** — every in-screen label maps to a real screen.
  Known failing input: a mock feature shipped nowhere.
- **G4 no twins** — no pop-out duplicating readable in-screen content.
  Known failing input: button + call-to-action card with identical copy.
- **G5 rendered proof** — each shot's trouble regions crop-verified.
  Known failing input: a card cropped mid-text by the canvas edge.

## Failure modes

- Scaling per shot by width only, "close enough" — the portal checks exact
  pixels. Renders must have exact per-slot window sizes.
- Reusing an existing app asset as background — reads as filler, loses the
  marketing read; pick fresh full-bleed photography.
- Rotating the device frame — a hard user rejection from this workflow,
  never re-do it.
- Hardcoding pop geometry per size — one canvas, one math; size is a scale.
- Editing entity markup with tools that unescape `&` — compose entities
  in code at runtime (e.g. `AMP = String.fromCharCode(38)`).
- Leaving generator scratch output (`build/.build-*` dirs) — gitignore it.
- Iterating a single size after review — rebuild propagates the fix to all
  sizes with the same run.

## Hand-over

Return this block, filled in:

```
## Store screenshot hand-over
Screenshots generated:
- <slot>: <folder>/ → <n> files, <size>, G1 PASS
Gates: G1 <result>, G2 <result>, G3 <result>, G4 <result>, G5 <result>
Regenerate: node <path to generate script>
Upload ownership: user (>= the exact slot mapping)
```

## Changing this skill

Start from a failure this workflow produced (a rejection, a re-accepted
resubmission, a user aesthetic correction in-session), add it as a case in
`evals/`, then edit. Read [the house standard](../_shared/authoring.md).

---

Provenance: method extracted from the SnowMowBC App Store resubmission work
(2026-10-31) in `home_service_mvp`; Apple portal slot text and Guideline
2.3.x wording observed there are `attributed` to that session and MUST be
re-verified against the live portal and live App Review Guidelines at the
next use.
