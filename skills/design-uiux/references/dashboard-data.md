# Dashboard data and information architecture

Use when deciding what belongs in a dashboard and how data should be shaped,
prioritized, grouped, compared, filtered, and revealed.

## Contents

- [Data-to-structure matrix](#data-to-structure-matrix)
- [Table craft](#table-craft)
- [Charts and data meaning](#charts-and-data-meaning)
- [Color architecture for data surfaces](#color-architecture-for-data-surfaces)
- [Navigation spine](#navigation-spine)
- [Scope and filtering](#scope-and-filtering)
- [Sources](#sources)

## Data-to-structure matrix

| User task | Prefer | Required checks |
| --- | --- | --- |
| Compare consistent fields | Table or structured rows | Numeric alignment, attribute priority, search/filter/sort, truncation |
| Scan and act on records | List or grouped list | Status, key attributes, row action, selection, empty/no-results |
| Understand event sequence | Timeline | Time zone, order, missing events, pagination, accessibility |
| See trend or range | Line/bar chart | Metric, unit, range, labels, aggregation, comparison, text summary |
| See a single status | KPI/status card | Definition, freshness, denominator, trend, next action |
| Compare related categories | Small multiples or focused chart/table | Consistent scale, labels, grouping, color meaning |
| Understand one object | Detail route, drawer, or side panel | Source context, edit/save, permissions, back, related records |

Never choose a chart or card because it is visually impressive. Name the
question the representation answers.

## Table craft

- Put the most decision-relevant attributes first.
- Right-align comparable numeric values and use consistent precision.
- Use labels or chips for bounded categorical states.
- Truncate long text only with full-value access and a reason.
- Keep row structure consistent so users can compare across records.
- Separate inactive, unavailable, stale, or archived records without making
  them look current.
- Support search, filter, sort, pagination, selection, bulk action, and detail
  when the task requires them.
- Define column priority and a responsive strategy before design handoff.

## Charts and data meaning

For every chart, document:

- user question and decision;
- metric, unit, denominator, aggregation, and source;
- time range, comparison, time zone, and freshness;
- labels, gridlines, legend, tooltip, range selector, and empty state;
- accessible text summary and table/data alternative;
- color semantics, contrast, dark mode, and export behavior.

Use a timeline when event sequence is the important dimension. Use a table when
precise comparison is more important than shape. Do not use a chart for data
that has no meaningful trend or comparison.

### Color architecture for data surfaces

Use color semantically and consistently:

- neutral surface layers establish hierarchy without competing with the data;
- functional accent ramps cover links, focus, selection, hover, and action;
- semantic ramps communicate success, warning, danger, info, and categories;
- light and dark themes adapt the ramps instead of inverting hex values.

The 60-30-10 rule is not a dashboard validation rule. Avoid rainbow palettes,
arbitrary saturation, and color-only status. Prefer perceptually consistent
ramps such as OKLCH when practical, then verify contrast, color-vision
differences, print/export, disabled states, and accessible text summaries.

## Navigation spine

The sidebar or top navigation should reduce cognitive load:

- group related links by user relevance;
- make the active location unmistakable;
- support collapsed state with labels or tooltips;
- keep search, profile, workspace, and role context understandable;
- place low-frequency settings/help where they do not compete with the core;
- preserve direct URLs, refresh, browser back, and return-from-detail.

## Scope and filtering

Treat scope, filters, sort, date range, pagination, and saved views as part of
the product state. Define whether they persist in the URL, session, user
preference, or nowhere. Show active filters, result count, stale state, clear
all, and empty/no-results recovery.

## Sources

Kole Jain:

- [Resources](https://www.kolejain.com/resources)
- [Dashboard UI flaws transcript](https://sozai.app/transcript/dashboard-ui-flaws-never-built-one/)
- [Dashboard UI guide transcript](https://sozai.app/transcript/build-dashboard-ui-beginner-guide/)
- [Vibe-coded SaaS mistakes transcript](https://sozai.app/transcript/saas-ui-ux-mistakes-vibe-code/)
- [Animated Dashboard Sidebar Tutorial](https://sozai.app/transcript/animated-dashboard-sidebar-tutorial-figma/)
- [7 UI/UX Mistakes](https://sozai.app/transcript/ui-ux-mistakes-beginner/)
- [How to Think Like a Genius UI/UX Designer](https://sozai.app/transcript/think-like-genius-ui-ux-designer/)
- [7 Color Mistakes](https://sozai.app/transcript/7-color-mistakes-ruin-ui-designs/)
- [Why 60-30-10 Is Ruining Product UI](https://sozai.app/transcript/60-30-10-rule-ruining-ui-designs/)

NN/G:

- [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/)
- [Recognition and Recall](https://www.nngroup.com/articles/recognition-and-recall/)
- [The Anatomy of a List Entry](https://www.nngroup.com/articles/list-entries/)
- [F-Shaped Reading Pattern](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)
