#!/usr/bin/env python3
"""
lint_post.py - deterministic anti-slop and format lint for social posts.

Implements the machine-checkable subset of the AI-tone gate
(skills/_shared/ai-tone.md owns the rules; this script is an implementation):

- AI-TONE-01: banned generic AI/marketing vocabulary and engagement bait
- AI-TONE-02: em/en dashes as sentence punctuation
- AI-TONE-03: "not X, it's Y" negative-parallelism templates
- AI-TONE-04: three-part rhythm lists (warn)

Plus deterministic platform format rules: character limits, hook-vs-fold
length, link-above-fold placement, hashtag walls and budgets, emoji budgets,
alt text for visual posts, wall-of-text detection, uniform sentence rhythm,
and unsourced numeric claims.

Usage:
    python3 lint_post.py <post.json>
    python3 lint_post.py --platform linkedin <draft.txt>
    python3 lint_post.py --self-test

Exit codes: 0 = pass, 1 = errors, 2 = bad input.
"""

import argparse
import json
import re
import statistics
import sys
from pathlib import Path

URL_LEN = 23
EMOJI_LEN = 2

# limit: post/caption cap. fold: chars visible before "more".
# hashtag_rec/max: recommended and hard max. emoji_max: hard max.
PLATFORMS = {
    "x":         {"limit": 280,   "fold": 280, "hashtag_rec": 1, "hashtag_max": 2,  "emoji_max": 2},
    "premium_x": {"limit": 25000, "fold": 280, "hashtag_rec": 1, "hashtag_max": 2,  "emoji_max": 2},
    "linkedin":  {"limit": 3000,  "fold": 210, "hashtag_rec": 3, "hashtag_max": 5,  "emoji_max": 2},
    "instagram": {"limit": 2200,  "fold": 125, "hashtag_rec": 5, "hashtag_max": 30, "emoji_max": 6},
    "tiktok":    {"limit": 4000,  "fold": 150, "hashtag_rec": 3, "hashtag_max": 10, "emoji_max": 4},
    "facebook":  {"limit": 63206, "fold": 477, "hashtag_rec": 3, "hashtag_max": 5,  "emoji_max": 4},
    "threads":   {"limit": 500,   "fold": 500, "hashtag_rec": 3, "hashtag_max": 10, "emoji_max": 2},
    "bluesky":   {"limit": 300,   "fold": 300, "hashtag_rec": 1, "hashtag_max": 3,  "emoji_max": 3},
    "youtube":   {"limit": 5000,  "fold": 157, "hashtag_rec": 3, "hashtag_max": 15, "emoji_max": 2},
}

# AI-TONE-01 judgment words: the owner file (ai-tone.md) mandates a rewrite,
# but context decides whether the word is doing generic work (travel posts do
# have journeys; apps really do navigate). Warn, never hard-fail.
JUDGMENT_WORDS = [
    (r"\binnovative\b", "innovative"),
    (r"\bjourneys?\b", "journey"),
    (r"\becosystems?\b", "ecosystem"),
    (r"\blandscape\b", "landscape"),
    (r"\bnavigat(e|es|ing)\b", "navigate"),
    (r"\bfoster(s|ed|ing)?\b", "foster"),
    (r"\bactionable\b", "actionable"),
    (r"\bscalable\b", "scalable"),
    (r"\bstreamlin(e|es|ed|ing)\b", "streamline"),
    (r"\bfrictionless\b", "frictionless"),
    (r"\bsmall but mighty\b", "small but mighty"),
    (r"\bmakes everything easier\b", "makes everything easier"),
]

# Site-echo check: flag any N-gram the draft shares with a polished source
# (e.g. the product's own marketing pages), which is the slop vector for
# founder posts (F-SC-8). Quoted, attributed text is carved out to a warning.
ECHO_NGRAM = 5

def token_spans(text: str) -> list[tuple[str, bool]]:
    """Words of the text, lowercase, plus whether each came from inside quotes."""
    tokens: list[tuple[str, bool]] = []
    pos = 0
    for m in re.finditer(r'"([^"]*)"', text):
        tokens.extend((t, False) for t in re.findall(r"[a-z0-9']+", text[pos:m.start()].lower()))
        tokens.extend((t, True) for t in re.findall(r"[a-z0-9']+", m.group(1).lower()))
        pos = m.end()
    tokens.extend((t, False) for t in re.findall(r"[a-z0-9']+", text[pos:].lower()))
    return tokens


def site_echo(full_text: str, source_text: str) -> tuple[list[str], list[str]]:
    """5-gram overlap with the banned source. Error outside quotes, warn inside."""
    errors: list[str] = []
    warnings: list[str] = []
    src_ngrams = set()
    src_tokens = [t for t, _ in token_spans(source_text)]
    for i in range(len(src_tokens) - ECHO_NGRAM + 1):
        src_ngrams.add(tuple(src_tokens[i:i + ECHO_NGRAM]))
    if not src_ngrams:
        return errors, warnings
    tokens = token_spans(full_text)
    quoted_hits: list[str] = []
    for i in range(len(tokens) - ECHO_NGRAM + 1):
        window = tokens[i:i + ECHO_NGRAM]
        gram = tuple(word for word, _ in window)
        if gram in src_ngrams:
            phrase = " ".join(gram)
            if all(q for _, q in window):
                quoted_hits.append(phrase)
            else:
                errors.append(
                    f"Site echo: the draft shares the phrase \"{phrase}\" with the "
                    f"marketing source; strike it and rewrite in the poster's own words (F-SC-8)"
                )
    if quoted_hits and not errors:
        warnings.append(
            f"Site echo inside quotes only ({len(quoted_hits)} phrase(s)); "
            f"keep only with attribution in the post"
        )
    return errors, warnings


VISUAL_FORMATS = {"image", "video", "gif", "carousel"}

# (regex, rule label). Case-insensitive.
BANNED_PHRASES = [
    # AI-TONE-01 lexicon (skills/_shared/ai-tone.md is the rule owner)
    (r"\bdelve\b|\bdelves\b|\bdelving\b", "AI-TONE-01 lexicon"),
    (r"\bleverag(e|es|ed|ing)\b", "AI-TONE-01 lexicon"),
    (r"\butiliz(e|es|ed|ing)\b", "AI-TONE-01 lexicon"),
    (r"\bfacilitat(e|es|ed|ing)\b", "AI-TONE-01 lexicon"),
    (r"\bseamless(ly)?\b", "AI-TONE-01 lexicon"),
    (r"\brobust\b", "AI-TONE-01 lexicon"),
    (r"\bunleash(es|ed|ing)?\b", "AI-TONE-01 lexicon"),
    (r"\bunlock(s|ed|ing)? (the )?(power|potential|full|value)\b", "AI-TONE-01 lexicon"),
    (r"\bempower(ing|s)?\b", "AI-TONE-01 lexicon"),
    (r"\belevat(e|es|ing)\b", "AI-TONE-01 lexicon"),
    (r"\bgame[- ]?changer\b", "AI-TONE-01 lexicon"),
    (r"\brevolution(ize|izes|izing|ary)\b", "AI-TONE-01 lexicon"),
    (r"\btransformative\b", "AI-TONE-01 lexicon"),
    (r"\btapestry\b", "AI-TONE-01 lexicon"),
    (r"\bparadigm\b", "AI-TONE-01 lexicon"),
    (r"\bsynergy|synergies\b", "AI-TONE-01 lexicon"),
    (r"\bholistic\b", "AI-TONE-01 lexicon"),
    (r"\bcutting[- ]edge\b", "AI-TONE-01 lexicon"),
    (r"\bit'?s worth noting\b", "AI-TONE-01 lexicon"),
    (r"\bhere'?s the thing\b", "AI-TONE-01 lexicon"),
    (r"\bin today'?s (fast[- ]paced |digital |ever[- ]changing |modern )?world\b", "AI-TONE-01 lexicon"),
    (r"\bat the end of the day\b", "AI-TONE-01 lexicon"),
    (r"\ba testament to\b", "AI-TONE-01 lexicon"),
    (r"\bthe (quiet parts|little details)\b", "AI-TONE-01 lexicon"),
    (r"\bin a world where\b", "AI-TONE-01 lexicon"),
    (r"\bthrilled to (announce|share|launch)\b", "sycophancy opener"),
    (r"\bexcited to (share|announce|launch)\b", "sycophancy opener"),
    (r"\b(i'?m|we'?re|i am|we are) (humbled|honored)\b", "sycophancy opener"),
    (r"\b(hope this|hope that) helps\b", "AI-TONE-01 lexicon"),
    (r"\blet'?s dive (in|deep)\b|\bdive deep into\b|\bdiv(ing|ed) deep\b", "AI-TONE-01 lexicon"),
    (r"\blet that sink in\b", "engagement bait"),
    (r"\bbuckle up\b", "engagement bait"),
    # Engagement bait (extends social-carousel BANNED_PHRASES)
    (r"wait (un)?til(l)? (the )?(end|slide)", "engagement bait"),
    (r"\byou won'?t believe\b", "engagement bait"),
    (r"\bsecret trick\b", "engagement bait"),
    (r"\bcomment [\"']?.{1,25}[\"']? (to get|to receive|and i'?ll)\b", "engagement bait"),
    (r"\bsave this (post|right now|before)\b", "engagement bait"),
    (r"\bsend (this|it) to (someone|a friend|three people)\b", "engagement bait"),
    (r"\b\d{1,2}x your\b", "engagement bait"),
    (r"\breplace all (programmers|designers|workers|engineers)\b", "engagement bait"),
    (r"\bnobody (is |will )?talk(ing)? about\b", "engagement bait"),
    (r"\bmost people (don'?t|do not) know\b", "engagement bait"),
    (r"\b99% of (people|developers|engineers)\b", "engagement bait"),
    (r"\bstop scrolling\b", "engagement bait"),
    (r"\bfollow for (more|daily)\b", "engagement bait"),
]

# AI-TONE-03 negative parallelism ("not just X, it's Y" / "it's not X, but Y").
NOT_BUT_PATTERNS = [
    r"(?i)\bnot (just|only|merely|simply)\b[^.!?\n]{2,80}?(but|it'?s)\b",
    r"(?i)\bit'?s not\b[^.!?\n]{3,80}?\b(but|it'?s)\b",
]

# Equivocation seesaw opener (warn; an AI tell, but sometimes legitimate).
SEESAW_PATTERN = r"(?i)\bwhile\b[^.!?\n]{5,70}?\b(may|might|can) (seem|be)\b"

# Three-part rhythm list (warn; AI-TONE-04).
TRIAD_PATTERN = r"\b\w[\w'-]*\s*,\s*\w[\w'-]*\s*,\s*and\s+\w[\w'-]*\b"

# Curiosity-gap question openers (warn; rewrite to name the subject).
OPENER_PATTERN = r"(?i)^(have you ever|did you know|what if i told you|can we talk about)"

EMOJI_RE = re.compile(
    "["
    "\U0001F1E6-\U0001F1FF"
    "\U0001F300-\U0001F5FF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA70-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U00002B00-\U00002BFF"
    "\U0001FA00-\U0001FA6F"
    "]"
)

URL_RE = re.compile(r"https?://\S+")
HASHTAG_RE = re.compile(r"#\w+")
PERCENT_RE = re.compile(r"\b\d{1,3}(\.\d+)?%")
DOLLAR_RE = re.compile(r"\$\d[\d,.]*\s*[kKmMbB]?\b")
MULT_RE = re.compile(r"\b\d{1,3}x\b")

MAX_BANNED_REPORTS = 12


def weighted_length(text: str) -> int:
    """Platform-visible length: every URL counts as 23, every emoji as 2."""
    remainder = URL_RE.sub(" " * URL_LEN, text)
    return len(remainder) + len(EMOJI_RE.findall(text)) * EMOJI_LEN


def sentences(text: str) -> list[str]:
    body_lines = [
        line for line in text.splitlines()
        if not HASHTAG_RE.search(line) or len(HASHTAG_RE.sub("", line).strip()) > 3
    ]
    clean = " ".join(line.strip() for line in body_lines)
    clean = URL_RE.sub("", clean)
    parts = re.split(r"(?<=[.!?])\s+", clean)
    out = []
    for s in parts:
        words = s.split()
        if 1 <= len(words) <= 60:
            out.append(words)
    return out


def lint(manifest: dict, plain_text: bool = False,
         site_source: str | None = None) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    platform = str(manifest.get("platform", "")).lower()
    if platform not in PLATFORMS:
        errors.append(f"Unknown platform '{platform}'. Known: {', '.join(sorted(PLATFORMS))}")
        return errors, warnings
    rules = PLATFORMS[platform]

    posts = manifest.get("posts") or [manifest]
    texts = []
    for post in posts:
        hook = str(post.get("hook", "") or "").strip()
        body = str(post.get("body", "") or "").strip()
        explicit_hook = bool(hook)
        if not hook and body:
            hook = body.splitlines()[0]
        if explicit_hook and body:
            # explicit hook is separate from body; count it once
            full = f"{hook}\n{body}"
        else:
            # hook defaults to body's first line; the body is the whole text
            full = body
        texts.append((hook, body, full))

    for i, (hook, body, full) in enumerate(texts, start=1):
        where = f"Post {i}: " if len(texts) > 1 else ""

        # Character limit
        limit = rules["limit"]
        length = weighted_length(full)
        if length > limit:
            errors.append(f"{where}Length {length} exceeds the {platform} limit of {limit} characters")

        # Hook vs fold
        fold = rules["fold"]
        if not hook:
            errors.append(f"{where}Empty hook: first line must name the subject")
        elif weighted_length(hook) > fold:
            warnings.append(
                f"{where}Hook runs past the {fold}-character fold; the payoff may truncate mid-line"
            )

        # Link placement (links above the fold suppress reach on LinkedIn)
        if platform in ("linkedin", "instagram", "tiktok", "facebook") and fold < rules["limit"]:
            m = URL_RE.search(body)
            if m and m.start() < fold:
                errors.append(
                    f"{where}Link appears within the first {fold} characters; "
                    f"on {platform} links above the fold suppress reach. Move it below the fold or to a comment"
                )

        # Hashtags
        hashtags = HASHTAG_RE.findall(full)
        explicit = manifest.get("hashtags") or []
        total_tags = len(set(h.lower() for h in hashtags)) + len(
            set(t.lower().lstrip('#') for t in explicit) - set(h.lower().lstrip('#') for h in hashtags)
        )
        for line in full.splitlines():
            if len(HASHTAG_RE.findall(line)) >= 4:
                errors.append(
                    f"{where}Hashtag wall: a line carries {len(HASHTAG_RE.findall(line))} hashtags; "
                    f"move them to the first comment or trim"
                )
                break
        if total_tags > rules["hashtag_max"]:
            errors.append(f"{where}Hashtag count {total_tags} exceeds the {platform} maximum of {rules['hashtag_max']}")
        elif total_tags > rules["hashtag_rec"]:
            warnings.append(f"{where}Hashtag count {total_tags} is above the {platform} recommended {rules['hashtag_rec']}")

        # Emoji budget
        emoji_count = len(EMOJI_RE.findall(full))
        if emoji_count > rules["emoji_max"]:
            errors.append(f"{where}Emoji count {emoji_count} exceeds the {platform} maximum of {rules['emoji_max']}")

        # Banned phrases
        banned_hits = 0
        for pattern, label in BANNED_PHRASES:
            m = re.search(pattern, full, re.IGNORECASE)
            if m:
                banned_hits += 1
                if banned_hits <= MAX_BANNED_REPORTS:
                    errors.append(
                        f"{where}Banned phrase ({label}): \"{m.group(0)}\". "
                        f"Rewrite from a specific observation (AI-TONE-01)"
                    )
        if banned_hits > MAX_BANNED_REPORTS:
            errors.append(f"{where}Banned-phrase hits ({banned_hits}) exceed the report cap")

        # AI-TONE-03: negative parallelism
        claimed: list[tuple[int, int]] = []
        for pattern in NOT_BUT_PATTERNS:
            m = re.search(pattern, full)
            if m and not any(s <= m.start() < e for s, e in claimed):
                claimed.append((m.start(), m.end()))
                errors.append(
                    f"{where}\"{m.group(0)[:60]}...\" is the negative-parallelism template "
                    f"(AI-TONE-03). Replace with a direct claim"
                )

        # AI-TONE-01 judgment words: warn, keep only with a stated reason
        for pattern, word in JUDGMENT_WORDS:
            m = re.search(pattern, full, re.IGNORECASE)
            if m:
                warnings.append(
                    f"{where}AI-TONE-01 judgment word: \"{m.group(0)}\"; rewrite unless it is doing specific work here"
                )

        # AI-TONE-02: dashes as sentence punctuation
        for dash in "—–":
            for m in re.finditer(re.escape(dash), full):
                if dash == "–" and m.start() > 0 and m.end() < len(full) \
                        and full[m.start() - 1].isdigit() and full[m.end()].isdigit():
                    continue  # numeric range like 5–10
                errors.append(
                    f"{where}Em/en dash used as sentence punctuation (AI-TONE-02). "
                    f"Use a period, comma, colon, or parentheses"
                )
                break
        if re.search(r"\s--\s", full):
            errors.append(f"{where}Double-hyphen used as an em-dash substitute (AI-TONE-02)")
        for m in re.finditer(r"\S\s-\s\S", full):
            errors.append(
                f"{where}Hyphen used as a sentence separator around \"{full[m.start():m.end()]}\": "
                f"use a period, comma, colon, or parentheses (AI-TONE-02)"
            )
            break

        # AI-TONE-04: triads
        m = re.search(TRIAD_PATTERN, full)
        if m:
            warnings.append(f"{where}Three-part list \"{m.group(0)[:50]}...\" reads as rhythm (AI-TONE-04); keep only if it carries meaning")

        # Equivocation seesaw
        m = re.search(SEESAW_PATTERN, full)
        if m:
            warnings.append(f"{where}Balanced hedge \"{m.group(0)[:50]}...\" leans on 'however' logic; make the sentence spiky")

        # Curiosity-gap opener
        m = re.search(OPENER_PATTERN, hook)
        if m:
            warnings.append(f"{where}Generic question opener \"{m.group(0)}\"; name the subject instead")

        # Wall of text
        words = len(full.split())
        if words > 350 and "\n\n" not in body:
            errors.append(f"{where}Wall of text: {words} words with no paragraph breaks (AI wall-of-text risk)")

        # Uniform sentence rhythm (a top AI tell after the em dash)
        sents = sentences(full)
        if len(sents) >= 4:
            lengths = [len(s) for s in sents]
            stdev = statistics.pstdev(lengths)
            mean = statistics.mean(lengths)
            if stdev < 1.5 and mean >= 8:
                errors.append(
                    f"{where}Uniform sentence rhythm: {len(sents)} sentences, mean {mean:.0f} words, "
                    f"stdev {stdev:.1f}. Vary sentence length; combine or split"
                )
            elif stdev < 2.5 and mean >= 10 and len(sents) >= 5:
                warnings.append(f"{where}Sentence rhythm is tight (stdev {stdev:.1f}); consider one longer and one shorter beat")

        # Sourced numbers
        has_numbers = bool(PERCENT_RE.search(full) or DOLLAR_RE.search(full) or MULT_RE.search(full))
        if has_numbers:
            sources = manifest.get("sources") or []
            if not any(str(s).strip() for s in sources):
                msg = (f"{where}Numeric claim without a source; attach the origin or delete the number")
                if plain_text:
                    warnings.append(msg)
                else:
                    errors.append(msg)

        # First-person check (F-SC-7): text/story/link posts read as brand
        # voice when the whole post is third person.
        fmt = str(manifest.get("format", "text") or "text").lower()
        if fmt in ("text", "story", "link"):
            combined = " ".join(full for _, _, full in texts)
            if not re.search(
                r"\b(i|i'm|i've|i'd|me|my|we|we're|we've|we'd|us|our)\b",
                combined,
                re.IGNORECASE,
            ):
                warnings.append(
                    "No first-person pronouns in a text/story/link post; "
                    "reads as brand voice rather than a person (F-SC-7)"
                )

    # Site-echo check (F-SC-8)
    if site_source:
        combined = "\n".join(full for _, _, full in texts)
        echo_errors, echo_warnings = site_echo(combined, site_source)
        errors.extend(echo_errors)
        warnings.extend(echo_warnings)

    # Visual format requirements
    visual = str(manifest.get("visual", "none") or "none").lower()
    if visual in VISUAL_FORMATS:
        alt = str(manifest.get("alt_text", "") or "").strip()
        if len(alt) < 20:
            errors.append(
                f"Visual post ({visual}) is missing alt text (>= 20 chars) describing the actual image"
            )
        if visual == "carousel":
            warnings.append("Multi-slide visual decks belong to social-carousel; this lint covers the caption only")

    if str(manifest.get("format", "text") or "text").lower() == "link":
        if not URL_RE.search(full):
            errors.append("Link format requires a URL in the post")

    return errors, warnings


BAD_FIXTURE = {
    "platform": "linkedin",
    "format": "text",
    "body": (
        "Thrilled to announce our new analytics dashboard, live here https://example.com/dashboard\n"
        "It's not just faster, it's smarter. We leveraged a seamless pipeline to unlock the "
        "full potential of your data.\n"
        "Our team worked tirelessly to build a robust platform that empowers teams to elevate "
        "their decision making — and transform their workflow into a tapestry of insight.\n"
        "#data #analytics #saas #startup #ai #buildinpublic #devtools #launch"
    ),
}

GOOD_FIXTURE = {
    "platform": "linkedin",
    "format": "text",
    "body": (
        "Shipped the migration tool on Tuesday.\n"
        "It cut our nightly deploy from 38 minutes to 9. The fix was batching ALTERs in "
        "dependency order instead of alphabetically.\n"
        "Numbers and the schema diff are in the repo README.\n"
        "Happy to answer questions about the edge cases."
    ),
    "sources": ["repo README, 2026-10-27"],
}


ECHO_SOURCE = (
    "Everything your pet needs, in one place. Profile, documents, and memories, "
    "all in one place, so Peti's answers start from your pet. "
    "Scanned the bag I always buy and it flagged chicken fat straight away, "
    "which is exactly what our vet had told us to avoid."
)

ECHO_FIXTURE = {
    "platform": "linkedin",
    "format": "text",
    "body": (
        "Everything your pet needs, in one place. Try the food scan today.\n\n"
        "The free app covers one pet profile and unlimited on Plus."
    ),
}

ECHO_QUOTED_FIXTURE = {
    "platform": "linkedin",
    "format": "text",
    "body": (
        "One reviewer put it best: \"scanned the bag I always buy and it flagged "
        "chicken fat straight away.\" That is the whole pitch."
    ),
}


def self_test() -> int:
    bad_errors, _ = lint(BAD_FIXTURE)
    bad_categories = set()
    for err in bad_errors:
        if "dash" in err:
            bad_categories.add("dash")
        if "Banned phrase" in err:
            bad_categories.add("banned")
        if "negative-parallelism" in err:
            bad_categories.add("not-but")
        if "Link appears" in err:
            bad_categories.add("link-fold")
        if "Hashtag" in err:
            bad_categories.add("hashtag")
    good_errors, good_warnings = lint(GOOD_FIXTURE)
    echo_errors, echo_warnings = lint(ECHO_FIXTURE, site_source=ECHO_SOURCE)
    echo_quoted_errors, echo_quoted_warnings = lint(ECHO_QUOTED_FIXTURE, site_source=ECHO_SOURCE)
    expected = {"dash", "banned", "not-but", "link-fold", "hashtag"}
    ok = True
    print("  SELF-TEST bad fixture:")
    for err in bad_errors:
        print(f"    FAIL: {err}")
    if not expected <= bad_categories:
        missing = expected - bad_categories
        print(f"    SELF-TEST FAILED: bad fixture missed gate categories {sorted(missing)}", file=sys.stderr)
        ok = False
    if not any("Site echo" in e for e in echo_errors):
        print("    SELF-TEST FAILED: echo fixture produced no site-echo error", file=sys.stderr)
        ok = False
    else:
        print(f"    echo fixture: {len(echo_errors)} site-echo error(s) (failing input confirmed)")
    if echo_quoted_errors:
        print("    SELF-TEST FAILED: quoted echo produced errors instead of a warning", file=sys.stderr)
        ok = False
    elif not any("Site echo" in w for w in echo_quoted_warnings):
        print("    SELF-TEST FAILED: quoted echo produced no warning", file=sys.stderr)
        ok = False
    else:
        print("    quoted echo: warn only (attribution carve-out confirmed)")
    if good_errors:
        print("  SELF-TEST good fixture:")
        for err in good_errors:
            print(f"    FAIL: {err}")
        print("    SELF-TEST FAILED: good fixture produced errors", file=sys.stderr)
        ok = False
    else:
        print(f"  SELF-TEST good fixture: PASS ({len(good_warnings)} warnings)")
    if ok:
        print("  PASS: self-test. Every gate category has a known failing input.")
        return 0
    return 1


def main() -> None:
    parser = argparse.ArgumentParser(description="Deterministic anti-slop and format lint for social posts")
    parser.add_argument("artifact", nargs="?", help="post.json manifest or a plain-text draft")
    parser.add_argument("--platform", help="platform for plain-text mode")
    parser.add_argument("--against", help="path to a polished source (e.g. the product's marketing page text); flags shared phrases")
    parser.add_argument("--self-test", action="store_true", help="verify gates against known failing inputs")
    args = parser.parse_args()

    if args.self_test:
        sys.exit(self_test())

    if not args.artifact:
        parser.print_usage(sys.stderr)
        sys.exit(2)

    path = Path(args.artifact)
    if not path.exists():
        print(f"Error: artifact '{path}' does not exist.", file=sys.stderr)
        sys.exit(2)

    plain_text = path.suffix == ".txt"
    if plain_text:
        if not args.platform:
            print("Error: plain-text mode requires --platform <name>.", file=sys.stderr)
            sys.exit(2)
        manifest = {"platform": args.platform, "format": "text", "body": path.read_text(encoding="utf-8")}
    else:
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"Error reading post manifest: {e}", file=sys.stderr)
            sys.exit(2)

    site_source = None
    if args.against:
        against_path = Path(args.against)
        if not against_path.exists():
            print(f"Error: source file '{against_path}' does not exist.", file=sys.stderr)
            sys.exit(2)
        site_source = against_path.read_text(encoding="utf-8")

    errors, warnings = lint(manifest, plain_text=plain_text, site_source=site_source)

    for w in warnings:
        print(f"  WARN: {w}")

    if errors:
        for err in errors:
            print(f"  FAIL: {err}", file=sys.stderr)
        print(f"\nVerification FAILED with {len(errors)} error(s).", file=sys.stderr)
        sys.exit(1)

    print("  PASS: post passed all anti-slop and format gates.")
    sys.exit(0)


if __name__ == "__main__":
    main()
