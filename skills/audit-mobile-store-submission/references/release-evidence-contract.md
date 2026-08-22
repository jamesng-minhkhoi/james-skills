# Release evidence contract

Use this contract to prevent a source audit from being mistaken for store
readiness. Create one ledger for the exact release under review.

## Required release manifest

| Field | Required evidence | Status |
| --- | --- | --- |
| Platform/storefront | Apple/Google, countries, languages, form factors |  |
| Artifact identity | IPA/APK/AAB/app bundle, SHA-256, bundle/package ID, version/build, signing |  |
| Identity reconciliation | Portal item row, review environment, selected build, installed label, attached evidence |  |
| Review snapshot | Submission ID, reviewed build, review date/device, rejection text |  |
| Resubmission | New build, changed files/features, attached evidence |  |
| Runtime environment | Backend, feature flags, auth, test data, provider dependencies |  |
| Portal state | App version, build processing, IAP/subscription or track status |  |
| Access | Demo accounts, MFA/OTP/QR, reset path, sample data |  |
| Public surfaces | Privacy, support, terms, deletion, contact, marketing URLs |  |
| Policy/legal | Privacy forms, permissions, age/audience, rights, regulated authorization |  |
| Checked at | Date/time, operator, commands/devices/portal surfaces |  |

## Evidence levels

- **Source:** code/config/docs indicate intent or create a risk.
- **Build:** the exact artifact exists and its identity was inspected.
- **Runtime:** the named artifact behaved that way on a named device/OS.
- **Access:** a reviewer can reach the path using supplied instructions.
- **Portal:** the exact store state or field was directly observed.
- **Public URL:** the named URL loaded and matched on the checked date.
- **Provider/legal:** the responsible provider or rights owner confirmed it.
- **Unknown:** evidence is missing, contradictory, stale, or not reproducible.

## Conflict rules

1. Use the signed artifact and runtime for shipped behavior.
2. Use App Store Connect or Play Console for listing, processing, and submission
   state.
3. Use source/configuration for intent, provenance, and risk discovery only.
4. Use provider/legal confirmation for claims outside the repository.
5. If two surfaces disagree, create a finding for the mismatch; do not choose
   the more favorable statement.

## Verdict gates

- **Ready:** no P0/P1 findings, no unresolved official rejection, every required
  item for the selected mode has its applicable evidence level observed
  (including Runtime, Access, Public URL, Portal, or Provider/legal), and the
  artifact/listing/portal identity agrees.
- **Ready with conditions:** no blocker remains, and named P2 items have owners,
  due dates, and no effect on the selected submission scope.
- **Not ready:** any P0/P1, unresolved rejection, required evidence missing in
  Review/Release, inaccessible reviewer path, or identity/policy mismatch.
- **Unknown:** use only when the audit mode or platform scope does not require
  the missing evidence yet. In Release mode, missing required evidence is Not
  ready, with Unknown recorded as the reason.

## Finding row

| Priority | Surface | Observation | Evidence | Owner | Verification |
| --- | --- | --- | --- | --- | --- |
| P0–P3 | Source/build/runtime/access/portal/provider/legal | Exact fact | Level + artifact/device/date |  | Exact rerun or confirmation |
