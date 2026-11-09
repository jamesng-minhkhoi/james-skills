# Display-size reference

The portal slot's supported-sizes line is the authority; this table only
primes the guess before that text is on screen. Slots and devices change; the
last row each submission re-verified is what it says.

## App Store Connect, iPhone screenshots (portrait/landscape)

| Slot | Supported portrait | Supported landscape |
| --- | --- | --- |
| iPhone 6.1" / 6.3" (Dynamic Island, medium display) | 1179 × 2556 / 1206 × 2622 | 2556 × 1179 / 2622 × 1206 |
| iPhone 6.7" / 6.9" (large display) | 1284 × 2778 / 1320 × 2868 | 2778 × 1284 / 2868 × 1320 |

Status: `attributed` — observed in the App Store Connect upload UI on
2026-10-31 while remediating this workflow's "File dimensions are invalid"
rejection. Legacy slots (5.5", older iPad sizes) disappear over time; expect
sizes to shift per season and always re-read the slot.

## Practical rules

- A slot accepts its listed sizes only; a near-miss (a 6.9" file in a 6.1/6.3
  slot) fails the whole batch upload — "1 or more errors occurred".
- Uploading a dual-size set into a single-size slot is fine; the portal picks
  the matching size. Keep one folder per size anyway: it ties each file to
  its slot unambiguously.
- Apple screenshots must be PNG/JPEG without alpha; render with opaque
  backgrounds.
- Design canvas: 1284 × 2778 covers the 6.7" slot natively and scales to
  6.9/6.3/6.1 by CSS transform (ratios stay within a few percent of
  uniform). Render every size from the same canvas; never rescale PNGs
  after the fact.

## Google Play screenshots

- Phone screenshots: portrait up to 1080 × 2400 class devices; Play requires
  PNG/JPEG, min dimension 320px, max 3840px. Keep the same design canvas
  scaled; Play does not demand per-device slots.
- Feature graphic 1024 × 500 is a separate deliverable, not a screenshot.

Status: `attributed` to Play Console documentation as commonly cited;
`unverified` for this submission — re-check Play Console's current limits
before generating a Play set.
