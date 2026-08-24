# Web accessibility and performance

Use this reference for release-sensitive changes and any route with forms,
tables, dialogs, navigation, complex data, or custom interaction.

## Accessibility review

Check the journey, not just the DOM score:

- landmarks and one useful page heading;
- logical heading order and meaningful link/button names;
- native controls before custom ARIA widgets;
- labels, descriptions, constraints, validation, and error association;
- keyboard reachability, visible focus, logical order, and focus return;
- dialog/menu focus containment, escape policy, outside-click policy, and
  scroll behavior;
- selected, expanded, pressed, disabled, pending, and invalid states exposed
  semantically;
- status updates announced without stealing focus;
- contrast, non-color meaning, zoom, large text, forced colors where supported;
- reduced motion and no-hover alternatives;
- tables, charts, images, icons, and decorative content have appropriate
  names, summaries, headers, or hiding behavior.

Automated checks find classes of defects; they do not prove task comprehension,
keyboard order, focus recovery, or useful error copy.

## Performance review

Look for:

- unnecessary client JavaScript and route-wide providers;
- render waterfalls, duplicate fetches, unbounded lists, and expensive state
  subscriptions;
- image dimensions, responsive loading, lazy boundaries, font loading, and
  layout shift;
- expensive blur, shadow, paint, or animation work;
- input latency and long tasks during typing, scrolling, filtering, and submit;
- caching, revalidation, stale data, and error behavior that match freshness
  requirements;
- bundle growth, dependency cost, and tree-shaking regressions.

Measure before claiming improvement. Separate local development behavior from
production-build and deployed observations.

## Acceptance rule

An accessibility or performance concern is not resolved by adding an audit
package or suppressing a warning. Show the user-visible behavior, relevant
measurement, scope, and regression check.
