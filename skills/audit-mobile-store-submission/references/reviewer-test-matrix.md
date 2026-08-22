# Reviewer test matrix

Use this matrix in Review, Release, and Rejection Remediation modes. Mark each
row **Pass**, **Fail**, **Open**, or **Unknown** and attach the artifact,
device/OS, account, and evidence filename.

| Journey | Clean install | Cold launch | Denied/offline | Background/resume | Reviewer evidence |
| --- | --- | --- | --- | --- | --- |
| Launch and first value |  |  |  |  |  |
| Onboarding and navigation |  |  |  |  |  |
| Sign-up/sign-in/reset |  |  |  |  |  |
| MFA/OTP/QR/role access |  |  |  |  |  |
| Primary create/action/result |  |  |  |  |  |
| Search/filter/empty/no-results |  |  |  |  |  |
| Upload/share/deep link |  |  |  |  |  |
| Notifications and permission prompts |  |  |  |  |  |
| Subscription/purchase/restore |  |  |  |  |  |
| Account deletion/data deletion |  |  |  |  |  |
| UGC report/block/moderation |  |  |  |  |  |
| External provider failure |  |  |  |  |  |

## Environment discipline

- Use the exact TestFlight, Play track, or production install path under audit.
- Use a physical device for Apple review recordings; label simulator evidence
  separately and never substitute it silently.
- Test without a debugger, local server, seeded developer database, privileged
  feature flag, or unrecorded manual intervention.
- Record device model, OS, locale, timezone, region, network state, app build,
  account, and reset steps.
- Reset permission state, account state, subscription state, and app data before
  each relevant run. If reset is impossible, mark the path Open or Unknown.
- Include one slow-network/offline run and one force-quit/background-resume run
  for every journey that depends on remote data or background work.

## Review packet acceptance

A recording passes only when it starts from launch, shows the requested path,
contains no developer-only overlays or personal data, identifies build/device
provenance, and can be followed by a reviewer from the supplied notes. A
screenshot passes only when it shows the current binary, supported language and
device, real functionality, and no unshipped or misleading state.

## Coverage expansion

- Test the smallest supported phone, a representative current phone, and any
  tablet/foldable/wearable form factor promised in the listing.
- Test every shipped store localization for truncation, display-name drift,
  screenshots, permission copy, dates, currency, and reviewer instructions.
- Test storefront/region differences for availability, pricing, content,
  provider access, age gates, and legal links.
- Test narrow and large text/accessibility settings when they affect permission
  prompts, paywalls, reviewer notes, or core actions.
