# Landing page critique and proof

Use after rendering the design artifact or prototype at representative widths
and states. This is a design critique, not product QA. Source inspection and
tests can support the review but cannot replace rendered and interactive design
evidence.

## Review order

Fix the earliest failed layer:

1. **Intent:** Is the audience, job, promise, and primary conversion clear?
2. **Message:** Can the visitor understand what this is, for whom, and why it
   matters without reconstructing the meaning?
3. **Narrative:** Does each section move the visitor toward an informed decision?
4. **Proof:** Are claims credible, specific, attributable, and placed near the
   claim?
5. **Hierarchy:** Is the first viewport and scan order clear?
6. **Content:** Do real strings, prices, translations, legal copy, and media fit?
7. **Responsive:** Does the composition adapt across widths and input methods?
8. **Interaction:** Do links, forms, accordions, tabs, navigation, focus, and
   recovery work?
9. **Accessibility:** Do semantics, keyboard, screen readers, contrast, zoom,
   reduced motion, and focus behavior preserve the task?
10. **Handoff dependencies:** Are loading, layout shift, metadata, indexing,
    structured data, consent, and analytics requirements explicit for the next
    owner?
11. **Polish:** Do visual details add comprehension, trust, or personality?
12. **Proof:** Were important claims, states, widths, and outcomes actually
    observed?

## Rendered-state matrix

| Dimension | Evidence |
| --- | --- |
| Message | First viewport, headline wrapping, CTA, post-click expectation |
| Content | Typical, longest realistic, translated, missing, legal, and dense copy |
| Media | Loading, loaded, slow, missing, reduced-motion, dark-mode, alt behavior |
| Interaction | Hover, focus-visible, pressed, disabled, accordion/tab, form pending/success/error |
| Responsive | Narrow mobile, large mobile, intermediate/tablet, desktop, zoom |
| Accessibility | Keyboard traversal, focus order/return, screen reader names, contrast, large text |
| Performance | Image/font loading, layout shift, animation, long task, network condition |
| Handoff | Title, description, canonical, indexing, structured data, social preview, consent, event scope |
| Recovery | Retry, validation, provider failure, duplicate submit, interruption, back |

## Fast questions

- Can a new visitor explain the offer after the first viewport?
- Does the headline name an outcome rather than a mood?
- Is the primary CTA visible, specific, and honest about what happens next?
- Does every major claim have nearby credible proof?
- Is pricing, eligibility, privacy, or risk disclosed before commitment?
- Does the page still work with long copy, large text, zoom, keyboard, and a
  narrow viewport?
- Does focus remain visible and return logically after overlays or disclosure?
- Are forms honest about pending, success, failure, retry, and duplicate submit?
- Would the page still be credible if the logo and color were removed?
- Which visual effects could be removed without losing comprehension or trust?

## Finding shape

| Priority | Layer/tag | Route/viewport/state | Evidence + proof level | Impact | Recommendation | Verification |
| --- | --- | --- | --- | --- | --- | --- |
| P0–P3 | MESSAGE, PROOF, FLOW, CONTENT, RESPONSIVE, ACCESS, PERFORMANCE, SEO, SYSTEM |  |  |  |  |  |

Do not label a page “AI slop” as a finding. Name the observable generic
pattern, user impact, evidence, confidence, and exact verification method.

## Completion report

Report the design artifact, exact route, content fixture, viewport/input,
theme, network assumptions, screenshots or recordings reviewed, interaction
decisions, event/form/SEO dependencies, and unresolved engineering or
production gates. Distinguish design proof from real traffic, analytics,
search indexing, and production behavior.
