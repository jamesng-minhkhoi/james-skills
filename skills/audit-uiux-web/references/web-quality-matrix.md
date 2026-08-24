# Web quality matrix

Use this matrix to prevent an audit from becoming a review of one ideal
screenshot. Mark unobserved cells Unknown.

## Audit-mode coverage

| Dimension | Quick | Deep | Release |
| --- | --- | --- | --- |
| Primary route and job | Required | Required | Required |
| Representative secondary routes | One if relevant | Required | Required |
| Typical, long, empty, no-results, error data | Risk-based | Required | Required |
| Narrow mobile, large mobile, tablet, desktop | Target state | Required | Required |
| Direct URL, refresh, back/forward, new tab | Risk-based | Core routes | All supported routes |
| Pointer, keyboard, touch, no-hover path | Core control | Required | Required |
| Focus, modal return, menu escape, validation | Risk-based | Required | Required |
| Loading, slow, partial, retry, offline | Risk-based | When supported | Required when supported |
| Browser support, theme, zoom, large text | Target browser | Representative set | Full support set |
| Accessibility and performance checks | Risk-based | Required when relevant | Required |

## Route and state matrix

For each in-scope route, record the following rows when applicable:

| Route | Entry | Primary action | Typical | Empty | Long/dense | Loading/partial | Error/retry | Permission/session | Back/refresh/deep link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |

Do not mark a state covered because a component exists in source. Record the
fixture, trigger, visible result, recovery, and proof level.

## Browser-behavior matrix

| Behavior | Evidence to capture |
| --- | --- |
| Direct URL/deep link | Route loads correctly without prior navigation |
| Refresh | State, query, authentication, and unsaved work behave as intended |
| Back/forward | Browser history preserves orientation and does not duplicate or lose actions |
| New tab/share | URL includes the necessary route/filter/context and handles expiry |
| Query/filter/sort/pagination | URL, results, empty state, reset, and back behavior agree |
| Session/permission | Expiry or denied access explains next step without unsafe exposure |
| Multi-step form | Cancel, resume, validation, duplicate submit, and recovery are clear |
| Overlay | Escape, outside click policy, focus trap/return, scroll lock, and deep link behavior work |

## Responsive matrix

Use project breakpoints plus representative CSS widths. A practical baseline is
320/375/390/414, 768, 1024, 1280, and 1440 where supported.

| Check | Narrow | Intermediate | Desktop |
| --- | --- | --- | --- |
| Navigation and orientation |  |  |  |
| Reading order and primary action |  |  |  |
| Tables/lists/forms |  |  |  |
| Long content and localization |  |  |  |
| Fixed/sticky/overlay behavior |  |  |  |
| Keyboard/touch/hover equivalent |  |  |  |
| Focus, zoom, large text, contrast |  |  |  |

## Interaction-state matrix

For every high-value control:

| Control | Intent | Trigger | Default | Focus/hover/pressed | Pending | Success | Error/retry | Cancel/undo | Accessibility/motion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |

Hover is never the only proof path. A screenshot cannot prove timing, focus
return, keyboard behavior, delayed feedback, or reduced motion.

## Visual and performance matrix

Check:

- neutral foundation, dominant accent, semantic status color, contrast, and
  non-color meaning;
- typography roles, loaded font, wrapping, line length, and hierarchy;
- card/container density, border/radius/elevation consistency, and raw color
  drift;
- image/font loading, layout shift, expensive blur/shadow, long tasks, input
  latency, animation frame stability, and content stability;
- light/dark theme, reduced motion, zoom, and high-contrast or forced-colors
  behavior where supported.

## Evidence confidence

Use the highest level actually observed:

| Level | Meaning |
| --- | --- |
| Source-declared | Found in source, route config, or documentation |
| Rendered-static | Seen in a screenshot or rendered DOM state |
| Interactive-local | Triggered locally and observed |
| Data-connected | Observed with real or connected data |
| Failure-observed | Failure, retry, rollback, or recovery triggered |
| Production-observed | Verified in deployed provider/runtime state |

Never infer production, browser compatibility, performance, or accessibility
from a lower evidence level.
