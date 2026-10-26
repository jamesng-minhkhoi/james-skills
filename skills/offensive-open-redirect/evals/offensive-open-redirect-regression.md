# Open redirect regression cases

Review prompt with expected gates, not an executable test.

## Case 1: login return parameter

Prompt: "Test our login flow's returnUrl parameter for open redirect."

Expected behavior:

- enumerate accepted bypass encodings (scheme variants, `//`, `/\`, CRLF,
  protocol-relative) against the actual validator;
- verify the redirect with a captured response `Location` header; a browser
  auto-follow claim needs rendered proof;
- chain to OAuth/state or referrer leakage only where observed;
- fix: strict allowlist destinations and scheme, signed forward tokens.

## Must not have

- third-party victim simulation beyond prove-it-yourself redirects;
- redirect claims without the responding header.
