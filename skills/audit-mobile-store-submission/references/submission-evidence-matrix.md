# Submission evidence matrix

Use this matrix to prevent a source-level audit from being mistaken for store
readiness. Record the exact artifact, version, device, portal, URL, and date for
each observed item.

## Evidence levels

| Level | Proves | Does not prove |
| --- | --- | --- |
| Source | Code/config/docs declare an intention | Artifact, runtime, portal, or legal truth |
| Build | Artifact exists with version, signing, IDs, and target settings | Install, review access, provider, or store processing |
| Runtime | Named artifact installed and behavior was observed on a device/emulator | Portal approval, production backend, or every device |
| Access | Reviewer can reach the gated journey with supplied instructions | Successful policy review or all accounts/regions |
| Public URL | A named URL loads and matches the app on the observed date | Legal sufficiency or future availability |
| Privacy/SDK | Data and permissions were traced to declarations and policies | Legal approval or undocumented provider behavior |
| Portal | App Store Connect/Play Console status was directly observed | Native behavior, policy approval, or production rollout |
| Provider/legal | A named provider, rights owner, or legal owner confirmed the gate | Any unconfirmed release surface |
| Unknown | Evidence is missing, contradictory, or not observed | Readiness |

## Core matrix

| Area | Evidence to collect | Ready condition |
| --- | --- | --- |
| Artifact identity | Bundle/package, version, build/version code, signing, target SDK, architecture, track | Exact intended artifact is identified and reproducible |
| Review snapshot | Submission ID, review date/device, reviewed version/build, rejection text, attachments, current resubmission build | Every finding is tied to the artifact and evidence Apple/Google actually reviewed |
| Reproducibility | Backend, feature flags, auth, test data, locale, timezone, region, network, reset steps | Another reviewer can repeat the observation without developer-only state |
| Install and launch | Clean install, upgrade, first launch, startup logs, device/OS, screenshots | Installs and reaches first value without dev-only dependencies |
| Core functionality | Route/action/result/recovery per platform | Core value works on the submitted build |
| Stability | Crash/ANR, blank screen, timeout, slow network, offline, background/resume | No known release-blocking instability; open issues are explicit |
| Reviewer access | Demo account, OTP/MFA/QR, reset, test data, geo/device setup, notes | Reviewer can inspect all promised features without guessing |
| Review packet | Physical-device recording, device/OS list, purpose/audience, setup, external services, regions, rights/regulatory material | Required review information is complete, build-specific, and attached or portal-confirmed |
| Journey coverage | Primary journey plus each promised, paid, permission-gated, account, UGC, and regulated feature | Every applicable promise has Pass, Fail, Open, or Unknown evidence |
| Metadata | Name, descriptions, keywords, categories, screenshots, previews, ads, ratings, audience | Listing describes the exact binary and supported scope |
| Installed identity | Store name, signed display name, launcher label, Settings/app-switcher label, native overrides | Users can find the installed app and names are sufficiently similar |
| Public URLs | Privacy, support, terms, deletion, marketing, contact | HTTPS links load publicly and match the app |
| Privacy/data | SDK inventory, permissions, network/data map, policy, Apple details, Play Data Safety | Declarations agree with observed behavior and retention/deletion |
| Permissions | Native manifest/entitlements, rationale, minimum scope, denied path, declarations | Only necessary permissions are requested and documented |
| Permission UX | Pre-alert copy/CTA, system-prompt sequence, dialog imitation/highlight, denial and Settings recovery | Permission context is honest and does not coach the user’s choice |
| Accounts | Sign-up, login, SSO, logout, deletion, data deletion, account recovery | Platform-specific account requirements are fulfilled |
| Payments | Product IDs, attachment, billing framework, restore, cancel, pending, failure, test account | All monetized paths are reviewable and policy-compatible |
| Content/rights | UGC moderation, age rating, content rating, licenses, claims, regulated docs | Rights, audience, and risk gates have owners and evidence |
| Claims | Store/app claim, route/result, provider, audience/region, recording, authorization | Every consequential claim is supportable on the exact artifact |
| Platform changes | SDK/API/page-size/verification/deadline checks | Current applicable requirements are checked for the release date |
| Portal | App/build/IAP or track state, processing, compliance, forms, agreements, screenshots, submission state | Exact portal state is observed or explicitly open |

## Finding template

| Field | Record |
| --- | --- |
| Priority/platform/tag | P0–P3; Apple/Google/Both; artifact/runtime/access/etc. |
| Exact scope | App ID/package, version/build, route, URL, portal field, device, or SDK |
| Observation | What was actually seen or measured |
| Evidence level | Source, build, runtime, access, URL, privacy/SDK, portal, provider/legal, or unknown |
| Policy/source | Official policy URL or forum signal with confidence note |
| Impact | Rejection, delay, removal, user harm, or confidence risk |
| Recommendation | Smallest useful corrective action |
| Verification | Exact rerun, device, portal check, provider, or legal confirmation |

## Verdict rules

- **Ready:** no P0/P1 blockers and all required evidence for the selected mode
  and platform is observed at its applicable evidence level; there is no
  unresolved official rejection and artifact/listing/portal identity agrees.
- **Ready with conditions:** no P0/P1 blocker, but named P2/open gates have
  owners, due dates, and do not invalidate the intended submission.
- **Not ready:** any P0/P1 blocker, contradictory privacy/metadata, broken core
  journey, inaccessible reviewer path, unresolved official rejection, identity
  mismatch, or missing required platform gate/evidence.
- **Unknown:** use only when the selected mode does not yet require the missing
  portal, provider, native, legal, or production evidence. In Review or Release,
  record Unknown as the reason for a Not ready gate when the evidence is
  required but unobserved.
