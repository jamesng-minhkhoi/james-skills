# Visual QA checklist

Look at the rendered surface, not only its source. Mark each item pass, fail,
not applicable, or not observed.

## Composition

- One focal point wins through at least two of scale, weight, color, depth, or
  space.
- The primary action is obvious and has visible press feedback.
- Negative space has rhythm rather than identical gaps everywhere.
- The composition feels specific to the product, not like a generic template.
- Every decorative element has a stated job.
- Each card earns its border, shadow, padding, and visual separation.

## Fidelity and system use

- The closest shipped screen or visual reference was compared when available.
- Typography, spacing, radii, icon sizes, shadows, and colors use project tokens.
- Icons belong to one coherent family and optical weight.
- Existing primitives are reused where their contract fits.
- No accidental one-off style or hardcoded value bypasses an existing token.

## Interaction

- Tappable surfaces show feedback within one interaction frame.
- Interactive targets are at least 44pt or use a documented compensating hit
  area.
- Focus is visible and keyboard content remains reachable.
- Disabled controls look unavailable and cannot be activated.
- Loading does not shift the surrounding layout.
- Sheets/modals close, cancel, and resolve predictably; back navigation does not
  strand the caller.
- Destructive actions are separated, labeled clearly, and recoverable when the
  product allows it.

## Motion and native surfaces

- Motion explains what entered, left, changed, or moved.
- No decorative or ambient loop distracts from the task.
- Reduced-motion preferences are honored for decorative, looping, large-travel,
  and first-mount animation.
- Blur, masks, glass, gradients, and other native surfaces are checked for
  clipping, flattening, zero-frame, and transform-ancestor failures.

## State coverage

- Loading uses the final content footprint and avoids a layout jump.
- Empty state explains what to do next and offers an action when one exists.
- Errors are specific, translated, reported through the app's observability
  path, and recoverable where possible.
- Offline or provider failure has a deliberate response when relevant.
- Loaded state works with zero, one, typical, and many records.
- Long names, long descriptions, missing media, and unexpected values remain
  legible.

## Accessibility and localization

- Every control has an appropriate role, useful label, and state for selected,
  expanded, disabled, busy, or checked behavior.
- Labels are unique enough for a screen reader to distinguish controls.
- Decorative imagery is hidden from assistive technology.
- Dynamic type or large text does not clip or hide the primary action.
- Copy uses the project's localization mechanism and exists in every supported
  locale.
- At least one long-copy locale and one narrow viewport were rendered.

## Acceptance

- Run the one-second test and name the focal point and primary action.
- Compare against the approved reference or document why no reference exists.
- Capture representative screenshots for the primary journey and non-happy
  states.
- Record what was actually observed and leave unobserved native, provider,
  production, store, or review gates open.
