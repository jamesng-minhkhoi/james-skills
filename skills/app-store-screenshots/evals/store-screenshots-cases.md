# App Store Screenshot Behavior Cases

Rejection-audit fixtures for the `app-store-screenshots` skill: dimension-slot
failures, guideline traps, and boundary routing. All from real passes at the
SnowMowBC resubmission workflow this skill was extracted from
(provenance: 2026-10-31, `home_service_mvp`).

---

## Case 1: Dimension-slot rejection (the motivating failure)

**Prompt:**
"App Store Connect rejected the upload batch: 'File dimensions are invalid'
for `01-…`, `02-…`, `03-…` in the iPhone medium display slot (Dynamic
Island). The supported sizes line reads 2556 × 1179px, 1179 × 2556px, 2622 ×
1206px and 1206 × 2622px. Our files are 1284 × 2778 and 1320 × 2868. Fix the
set."

**Expected behavior:**
- Reads the slot's supported-sizes text as authority before generating.
- Produces a dedicated 6.1"/6.3" set at 1179 × 2556 (or 1206 × 2622) by
  scaling the existing design canvas, not by resizing existing PNGs.
- Keeps the 6.9"/6.7" sets for their own slots; explains slot-to-folder
  mapping in the hand-over block.
- Re-verifies rendered PNG pixel dimensions exactly (`rendered` rung).

**Must not have:**
- Instruction to hand-resize crop pad one PNG per slot.
- Claimed portal uploads or changed store state not authorized in session.

## Case 2: Guideline 2.3.10 status bar rejection

**Prompt:**
"Our build got rejected under Guideline 2.3.10 — 'the app status bar is not
consistent with the iOS design'. Regenerate the store set."

**Expected behavior:**
- Rebuilds every shot's phone screen with a native-look iOS status bar drawn
  inside the mock (time, island, signal glyphs), or crops the bars out of a
  real capture and repaints them.
- Explains the guideline in one line and names G2 as the now-passing gate.

**Must not have:**
- Fabricated marketing content to "make the app look official".

## Case 3: Pop-out duplication (twin rule)

**Prompt:**
"Shot 2 looks cluttered: the screen shows a provider tile on the phone AND
the same tile floating as a card next to it. Both the credit-card number and
the names match."

**Expected behavior:**
- Applies the twin rule: removes the duplicate pair; keeps one element or
  swaps the pop for content cropped off-canvas or unseen in-screen.
- Names G4 and the accepted pattern (a pop may exist only when its in-screen
  twin is cropped away, different-screen, or unseen).

**Must not have:**
- Slight cosmetic tweak (moving the card a few pixels) presented as the fix.

## Case 4: Boundary — routes elsewhere

**Prompt:**
"Can you make a 30-second app preview video for the App Store too?"

**Expected behavior:**
- Routes to `product-video` and stops screenshot work on that ask.

**Must not have:**
- Scripting or rendering a video from this skill.

## Case 5: Status content and abstraction-recreation mismatch

**Prompt:**
"Our app has no provider side yet, but the store shots look richer if we
show a 'provider dashboard' with earnings. Include it."

**Expected behavior:**
- Declines to invent a surface: screenshots must primarily depict real, in
  the build, app UX; an unshipped dashboard is an App Review rectangle.
- Offers real alternatives: market the shipped screens only.

**Must not have:**
- Any suggestion to fabricate, watermark over, or annotate unshipped
  functionality into the set.
