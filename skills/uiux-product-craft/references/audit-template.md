# UI/UX audit template

Use this as a working artifact. Replace placeholders with repository-specific
evidence; do not fill gaps with assumptions.

## Scope

- User and job:
- Entry route/surface:
- Desired outcome:
- UI/UX-only boundary:
- Explicitly out of scope:
- Visual source of truth:
- Required evidence:

## Evidence map

| Area | File/route/component | What it proves | Confidence | Gap |
| --- | --- | --- | --- | --- |
| Product/design rules |  |  | High/Medium/Low |  |
| Runtime composition |  |  | High/Medium/Low |  |
| Shared primitives/tokens |  |  | High/Medium/Low |  |
| Existing visual reference |  |  | High/Medium/Low |  |
| Automated checks |  |  | High/Medium/Low |  |
| Runtime/provider state |  |  | High/Medium/Low |  |

## Journey and state matrix

| Route or component | State/input | User action | Expected response | Recovery | Evidence |
| --- | --- | --- | --- | --- | --- |
|  | Loading |  |  |  |  |
|  | Empty |  |  |  |  |
|  | Loaded |  |  |  |  |
|  | Error/offline |  |  |  |  |
|  | Long copy/many items |  |  |  |  |
|  | Keyboard/focus/disabled |  |  |  |  |

## Findings

| Priority | Route/component | Finding and reproduction | User impact | Proposed fix | Status |
| --- | --- | --- | --- | --- | --- |
| P0/P1/P2/P3 |  |  |  |  | Open/Fixed/Deferred |

## Design decision record

For choices that materially change the user's mental model, record the options
before implementation.

| Option | Composition/interaction | Benefit | Trade-off | Decision |
| --- | --- | --- | --- | --- |
| A |  |  |  |  |
| B |  |  |  |  |
| C |  |  |  |  |

## Verification ledger

### Implementation

- Changed files:
- Preserved contracts:
- New or reused primitives:

### Automated

| Command | Result | Notes |
| --- | --- | --- |
|  | Pass/Fail/Not run |  |

### Visual/runtime

| Route/state | Viewport/device | Reference | Observed result | Screenshot |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### Open gates

- Native device:
- Provider/backend:
- Production/deployment:
- Dashboard/store/reviewer:

