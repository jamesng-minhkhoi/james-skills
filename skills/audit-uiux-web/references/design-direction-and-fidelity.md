# Design direction and fidelity

Use for a visual reference review, redesign, landing page, or portfolio audit.
Adapted from the user-supplied `design-taste-frontend` guidance, with evidence
and user impact taking precedence over style bans or numerical presets.

## Establish the design contract

Record page kind, audience, primary decision, intended character, existing
brand rules, and scope: new work, preservation, or overhaul. Infer from the
brief and available evidence; mark uncertainty without inventing requirements.
For a redesign, compare before/after identity, content, navigation, CTA paths,
forms, accessibility, and relevant analytics/SEO dependencies. Do not treat a
new visual language as authorization to change those contracts silently.

## Compare references with evidence

Inspect supplied reference material. Record source, viewport, theme, and state
for both reference and reviewed artifact. Compare:

- composition: width, column ratio, alignment, focal point, section rhythm;
- type and space: hierarchy, line breaks, leading, measure, gaps, clipping;
- color and shape: accent roles, surfaces, borders, radii, shadows, icons;
- media: relevance, crop, aspect ratio, focal point, and provenance;
- restraint: whether added cards, labels, effects, or badges dilute emphasis;
- interaction: observed feedback, focus, scroll, timing, and alternatives.

Label values **measured**, **estimated**, or **proposed**, including measurement
method when relevant. Screenshot pixels do not establish CSS dimensions
without scale information. Font identity, mobile breakpoints, and animation
timing stay unknown unless independently evidenced.

For each material mismatch, state the contract, observation, consequence, and
the check that would verify a correction. Compare matching widths and states;
do not report a breakpoint difference as a fidelity defect. If a reference is
unavailable, disclose that limit instead of claiming it was matched.

## Inspect the whole page, not only its hero

Check first-viewport comprehension, CTA reachability, section transitions,
navigation fit, heading/CTA wrapping, image crops, and token consistency down
to the footer. Review long content, mobile, zoom, and missing assets. Use
interaction evidence for sticky headers, focus visibility, motion, and forms.

Repeated eyebrows, empty tiles, generic copy, or identical section grids can
indicate weak hierarchy. Explain where they obscure the message or conflict
with the brief. Do not count them against arbitrary quotas. Repetition may
support comparison; whitespace may support reading; text can be the main
visual. A headline wrapping at zoom is not automatically a defect.

Check that testimonials, logos, metrics, screenshots, and product images have
appropriate provenance. An attractive generated preview is not proof of a
shipped feature. A mock disclosure only in source is not visible to visitors.
Do not infer conversion or performance improvement from appearance.

## Classify before prioritizing

| Class | Example | Treatment |
| --- | --- | --- |
| Usability or trust defect | Sticky decoration covers the CTA at the observed mobile width | Prioritize by impact with reproduction and verification |
| Design-contract deviation | Explicit brief preserves purple; the redesign replaces it with green | Record the violated requirement and scope; prioritize by consequence |
| Style opportunity | An alternative hero alignment might better express the brand | Label optional with rationale; do not invent a failure or block sign-off |

Fonts, purple or warm palettes, multiple semantic colors, different radii by
role, common icon families, native lists, and repeated layouts are not defects
on their own. Additional themes, images, libraries, or cinematic motion are
not universal requirements. Validate supplied requirements and supported states.

Use the main audit finding schema and proof levels. Static evidence can
support visual observations but cannot establish working controls, keyboard
behavior, reduced motion, performance, or provider outcomes. Keep those gates
Unknown when they were not observed.
