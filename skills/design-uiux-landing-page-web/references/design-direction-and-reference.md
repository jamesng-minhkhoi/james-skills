# Design direction and reference measurement

Use for a new visual direction, reference-led composition, or redesign.
Adapted from the user-supplied `design-taste-frontend` guidance: keep brief
inference, reference measurement, preservation, and rendered critique;
evaluate stylistic conventions in context rather than as universal bans.

## Read the brief before choosing a look

State a short design read, for example:

> A service landing page for time-poor buyers, with a calm and direct visual
> language; preserve the brand and make the booking decision easier.

Use audience, offer, content, brand assets, references, accessibility, and
task constraints as evidence. Avoid choosing an aesthetic from an industry
label alone. Resolve routine choices and proceed; ask a focused question only
if missing information would materially change the work.

Choose three qualitative settings with a reason:

| Setting | Decision |
| --- | --- |
| Visual variation | Where would symmetry, asymmetry, or a distinctive moment improve the story? |
| Motion | Which feedback or narrative benefits from movement, and what is its static alternative? |
| Density | How much information does this audience need before acting? |

These describe a direction, not a quality score. No default of high variation
or cinematic motion; a redesign does not automatically add motion. Explicit
user choices and existing brand rules take precedence over style heuristics.

## Preserve or overhaul deliberately

For an existing page, capture the current route and representative rendered
states before proposing changes. Record what to keep, change, and investigate:

- recognizable logo, type, palette, imagery, voice, and useful interactions;
- page hierarchy, URLs, anchors, navigation, CTA destinations, and forms;
- content, proof, accessibility strengths, consent, and analytics dependencies.

Default to preservation for an underspecified refresh. A visual overhaul can
change the visual language without silently changing content or behavior.
Existing authorization is sufficient for changes within the requested scope;
surface additional dependencies when they would expand it. Prioritize by the
observed problem: a buried CTA can need recomposition before type polish.

## Turn references into a usable specification

Inspect supplied screenshots or reachable reference pages before claiming a
match. If unavailable, state the gap and work from supplied evidence. Never
invent a measured value or a reference site's interaction behavior.

Record only the observations that shape this design:

| Lens | What to capture |
| --- | --- |
| Composition | Content width, column proportions, alignment, focal point, header footprint, section transitions |
| Typography | Role sizes and ratios, weight, leading, readable measure, actual line breaks |
| Space | Repeated gaps, section spacing, density, and deliberate areas of emptiness |
| Color | Surface and text roles, accent placement, semantic states, supported themes |
| Shape | Border, radius, shadow, and icon rules by component role |
| Media | Purpose, aspect ratio, crop, focal point, and relationship to text |
| Interaction | Observed trigger, timing, scroll/focus behavior, touch and reduced-motion alternatives |
| Restraint | What is absent, and how that absence supports focus |

Label values as **measured**, **estimated**, or **proposed**. For measured
values, record the method and viewport; screenshot pixels are not necessarily
CSS pixels. A screenshot cannot establish an exact font family, breakpoint,
hover behavior, or animation timing. Keep such details estimated or unknown.

Translate observations into a small set of checkable rules:

`evidence → proposed rule → reason → responsive exception → rendered check`

Example: an observed wide image/text split becomes a proposed 7:5 grid at the
target desktop width; at mobile, copy precedes the image and the CTA remains
reachable. Compare the two rendered widths for hierarchy and crop. Do not
infer the reference's mobile behavior from its desktop screenshot.

Reuse structural lessons without copying another brand's identity, customer
claims, or assets. Choose a foundation from the existing project and actual
requirements. A style reference does not mandate adopting its component
library. If an official system is required, verify current official guidance
and compatibility; distinguish system conformance from visual inspiration.

## Make the result specific without adding arbitrary novelty

- Give every section a decision job. Vary composition when content changes;
  repeated layouts are useful for comparable items. Avoid filler tiles,
  decorative labels, and unnecessary zigzags rather than enforcing quotas.
- Plan headline scale, real copy, CTA, and media together. Inspect the first
  viewport at the target sizes. Let long content and zoom grow the page; do
  not shrink text or cut required content to satisfy a line or word cap.
- Choose type for the brand, language coverage, readability, and available
  license. Neither serif nor a common sans font is inherently a defect.
  Inspect actual glyph clipping, including italics, rather than assuming one
  line-height value fixes every font.
- Define accents and radius by role. Keep semantic status colors distinct
  where needed. Purple, warm neutrals, mixed role-based radii, and alternating
  surfaces can all be valid when they support a coherent system.
- Use supplied or authentic assets for product evidence. Generated art may
  establish mood but cannot prove shipped UI, customers, results, or physical
  product details. Label illustrative examples visibly where viewers could
  mistake them for evidence; an HTML comment is insufficient disclosure.
- Use screenshots or actual components for real product demonstrations.
  Preserve attribution and quote meaning. A text-led page is valid when it
  communicates the offer; no image count, logo wall, or generated asset quota.
- Use motion and additional themes only when the brief or product needs them.
  Keep essential content reachable without hover or animation, preserve native
  scrolling, and specify readable fallbacks for transparency and motion.

## Critique against the chosen direction

Compare the rendered artifact with the brief and reference at matching target
viewports. Review hierarchy, spacing, type, crop, role-based tokens, and
interaction. For each material mismatch, fix or explain it, then recheck the
affected state. Do not accept a generic resemblance as a reference match.

Use the critique-and-proof checklist for responsive and interaction coverage.
Report observed passes, remaining mismatches, and unknowns. Design proof does
not establish conversion lift, production performance, or working providers.
