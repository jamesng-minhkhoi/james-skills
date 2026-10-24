# Fix report

The builder returns this after acting on an audit. The auditor consumes it on
re-audit. One row per finding ID, in the order the audit reported them.

| Finding | Status | Proof rung | Evidence |
| --- | --- | --- | --- |
| `F-web-03` | `closed` | `failure-tested` | `src/checkout.ts:41`; command output |
| `F-web-05` | `partially-closed` | `interactive` | Remaining: keyboard trap in Safari |

Statuses: `closed`, `partially-closed`, `not-fixed`, `wont-fix`.
Proof rung: the highest rung reached on the shared ladder for this fix.

## Rules

- Never renumber, merge, or reuse an ID. New defects get new IDs from the
  auditor.
- `closed` requires evidence at or above the rung the finding demanded.
- `partially-closed` names exactly what remains and why.
- `wont-fix` needs a reason and the user's agreement, not the builder's
  preference.
- A finding absent from the report is still open.
- The builder does not mark its own fix above the rung it actually reached.
