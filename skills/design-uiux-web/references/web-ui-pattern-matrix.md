# Web UI pattern matrix

Choose the least disruptive surface that gives the user enough context and
control to complete the task.

| Need | Prefer | Audit or build checks |
| --- | --- | --- |
| Top-level destinations | Visible header or application sidebar | Current location, labels, keyboard access, responsive collapse |
| Nearby related destinations | Local nav, tabs, or breadcrumbs | Stable naming, back path, deep-link and refresh behavior |
| Short choice list | Select, menu, or combobox | Current value, keyboard, search when long, escape behavior |
| Contextual work | Popover or dialog | Focus trap, close/escape, return focus, mobile adaptation |
| Complex or durable work | Route or full-page flow | URL, browser back, unsaved changes, deep link, completion landing |
| Scan and act on records | List or grouped list | Attribute priority, comparison, long values, empty/no-results |
| Compare structured fields | Table | Alignment, search/filter/sort, responsive strategy, selection |
| Understand change over time | Timeline or chart | Time zone, units, labels, range, accessible summary |
| Edit one object | Detail route, side panel, or sheet | Context, save/cancel, pending, error, rollback |
| Brief non-blocking status | Inline status or toast | Consequence, persistence, next step, accessible announcement |
| Persistent system/network state | Banner or durable status row | Impact, recovery, dismiss rules |

## Web-specific checks

- Use links for navigation and buttons for actions.
- Preserve URL state for shareable filters, search, sort, pagination, and tabs
  when the product benefits from deep links or browser history.
- Keep browser back, refresh, open-in-new-tab, and direct-entry behavior
  coherent.
- Provide visible labels or accessible names for icon buttons, tooltips, and
  menus.
- Prefer inline validation beside the affected field; preserve entered data.
- Use dialogs for interruptions that truly need interruption; prefer a route or
  contextual surface when durable context matters.
- Recompose desktop patterns for narrow widths instead of shrinking controls
  below usable sizes or forcing horizontal overflow.
