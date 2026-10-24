# Store submission regression cases

Use these fixtures when changing the store audit skill. Each one is a
submission that looks fine on the surface and fails on an external gate.

## Case 1: Rejection fixed in a newer build

Prompt/artifact: Apple rejected build 41 under 5.1.1. The repository is now at
build 44 and the diff appears to add the missing permission purpose string.
No build 44 install, TestFlight state, or portal record is supplied.

Expected behavior:

- treat build 41 as the reviewed artifact and build 44 as unproven;
- require an install or TestFlight observation of build 44 before closing the
  rejection finding;
- keep the verdict `NOT_READY` or `UNKNOWN` with the exact missing evidence,
  not `READY` because the source changed;
- give the finding an `F-store-<n>` ID and name the smallest next action.

## Case 2: Privacy declaration contradicts an SDK

Prompt/artifact: Google Play Data Safety says no data is shared with third
parties. The manifest and dependency list include an advertising SDK that
collects an advertising ID, and the privacy policy never mentions it.

Expected behavior:

- report a PRIVACY P1 blocker with the manifest path and SDK behavior as
  evidence;
- reconcile the form, the policy, and the observed behavior instead of
  averaging them;
- state that the Play form is wrong until the SDK is removed or declared;
- keep legal conclusions out of the report and name the owner who must confirm.

## Case 3: Reviewer access depends on a personal account

Prompt/artifact: The reviewer runbook says to log in with the founder's email,
which sends an OTP to the founder's phone. The demo account has no data.

Expected behavior:

- report an ACCESS P1 blocker: the reviewer cannot complete the journey;
- require a resettable demo account with seeded data, no personal device, and
  written reset steps;
- verify the reviewer path from a clean install, not from a privileged session;
- do not accept "the founder can approve it during review" as evidence.

## Case 4: Development artifact submitted

Prompt/artifact: An Expo app's internal track points at an APK built with the
`development` profile. The app launches to a dev-client screen and needs a
local Metro server.

Expected behavior:

- report an ARTIFACT P0 blocker: this is not the production binary;
- identify the build profile and the missing production configuration;
- require a production-profile artifact and a clean-install launch before any
  runtime claim;
- keep every runtime and portal gate `NOT_RUN` until that artifact exists.

## Case 5: Screenshots show an unshipped feature

Prompt/artifact: The listing screenshots show an AI symptom checker. The
feature is behind a flag that is off in the submitted build.

Expected behavior:

- report a METADATA/QUALITY finding: the screenshots do not show the current
  build;
- require screenshots regenerated from the submitted artifact;
- check the description and preview video for the same claim;
- do not treat a polished screenshot as proof that the feature ships.

## Must not have

A report fails if it contains any of these:

- `READY` when a required external gate was not observed;
- one verdict for both platforms when the scope is Apple and Google;
- a finding without a stable `F-store-<n>` ID;
- a guessed legal owner, privacy answer, age rating, or portal state;
- "submission complete" or "approved" without an observed portal state;
- a source-code change treated as proof that the reviewed build changed.
