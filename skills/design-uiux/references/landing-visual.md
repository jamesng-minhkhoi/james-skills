# Responsive visual system

Use this reference when choosing visual direction, layout, type, imagery,
motion, breakpoints, or responsive behavior for a landing page.

## Composition before components

Design the page as a sequence of visual moments:

Orient → Focus → Explain → Prove → Resolve objections → Act

Use a grid, content measure, and section rhythm that support the message. A
new card, badge, gradient, illustration, or floating panel needs a job:
comprehension, grouping, affordance, trust, depth, or personality. Otherwise
subtract it.

Avoid generic AI patterns:

- identical card grids for unrelated content;
- oversized gradient text with vague claims;
- decorative blobs replacing product evidence;
- endless pill badges and icon-title-description rows;
- fake dashboards, fabricated charts, or invented testimonial walls;
- glass, glow, shadows, and animation with no semantic role;
- every section using the same centered heading and three columns.

Distinctiveness should come from the product's content, audience, proof,
typography, art direction, and composition—not random novelty.

## Typography and content fit

- Use a small set of semantic roles with a clear reading hierarchy.
- Protect readable line length and avoid headings whose line breaks change the
  promise at common widths.
- Test longest real headings, translated strings, dates, labels, prices,
  punctuation, and legal copy.
- Avoid shrinking body text to rescue a desktop composition.
- Make the CTA and supporting copy readable at zoom and large text settings.

## Imagery and media

Choose media by its job:

- product demonstration for mechanism;
- annotated screenshot for orientation;
- customer or context image for trust and relevance;
- diagram for explanation;
- illustration for tone or abstraction.

Check loading, aspect ratio, crop, focal point, alt text, dark mode, reduced
motion, and missing-media fallback. Do not use decorative media to imply proof.

## Responsive composition

Check at least:

| Width/state | Questions |
| --- | --- |
| Narrow mobile | Is the promise readable, CTA reachable, and order intentional? |
| Large mobile | Does whitespace, media crop, and line wrapping remain balanced? |
| Intermediate/tablet | Does the layout recompose instead of leaving awkward gaps? |
| Desktop | Is the page focused rather than over-wide or over-dense? |
| Zoom/large text | Do content and controls reflow without clipping or overlap? |
| Long or missing content | Do sections grow naturally and preserve the decision path? |

Change order, alignment, media treatment, or disclosure when the visitor's
decision requires it. Do not treat one DOM order and one desktop grid as a
universal answer.

## Interaction and motion

Use explicit states for links, buttons, navigation, forms, accordions, tabs,
pricing controls, and disclosure. Support hover where useful, but never make
meaning or a core action hover-only. Ensure focus-visible is as clear as hover.

Motion should clarify reveal, continuity, hierarchy, progress, or result. Check
reduced motion, interruption, scroll behavior, sticky elements, layout shift,
and whether animation delays reading or action. Do not use a web prototype's
motion literally when it harms content or performance.
