#!/usr/bin/env python3
"""
validate_carousel.py - Anti-slop and structural validator for social carousels.

Checks slide manifests against house standards:
- Slide count bounds (3 to 10 slides)
- Word count budget per slide (preventing AI wall-of-text slop)
- Banned clickbait / engagement-bait phrases
- Safe-zone and aspect ratio specification
- Source citations for statistical/factual claims
"""

import argparse
import json
import re
import sys
from pathlib import Path

BANNED_PHRASES = [
    r"wait (un)?til(l)? (the )?end",
    r"wait (un)?til(l)? slide",
    r"you won'?t believe",
    r"game[- ]?changer",
    r"secret trick",
    r"comment [\"'].*[\"'] to get",
    r"comment [a-z0-9]+ to receive",
    r"save this (right now|post before it'?s deleted)",
    r"mind[- ]?blowing",
    r"10x your (productivity|growth|revenue)",
    r"replace all (programmers|designers|workers)",
]

MAX_WORDS_PER_SLIDE = 45
MAX_HEADLINE_WORDS = 14
MIN_SLIDES = 3
MAX_SLIDES = 10

def validate_carousel(data: dict) -> list[str]:
    errors = []
    warnings = []

    slides = data.get("slides", [])
    if not isinstance(slides, list) or len(slides) < MIN_SLIDES:
        errors.append(f"Slide count ({len(slides)}) below minimum threshold ({MIN_SLIDES})")
    elif len(slides) > MAX_SLIDES:
        errors.append(f"Slide count ({len(slides)}) exceeds recommended maximum ({MAX_SLIDES})")

    platform = data.get("platform", "instagram").lower()
    dimensions = data.get("dimensions", {})
    width = dimensions.get("width")
    height = dimensions.get("height")

    if platform == "tiktok" and (width != 1080 or height != 1920):
        warnings.append(f"TikTok format recommended at 1080x1920 (9:16), found {width}x{height}")
    elif platform in ("instagram", "linkedin") and (width != 1080 or height not in (1080, 1350)):
        warnings.append(f"Instagram/LinkedIn format recommended at 1080x1350 (4:5) or 1080x1080 (1:1), found {width}x{height}")

    for idx, slide in enumerate(slides, start=1):
        headline = slide.get("headline", "")
        body = slide.get("body", "")
        full_text = f"{headline} {body}"
        
        # Word counts
        body_words = len(body.split())
        headline_words = len(headline.split())
        
        if headline_words > MAX_HEADLINE_WORDS:
            errors.append(f"Slide {idx}: Headline has {headline_words} words (max {MAX_HEADLINE_WORDS})")
        
        if body_words > MAX_WORDS_PER_SLIDE:
            errors.append(f"Slide {idx}: Body has {body_words} words (AI wall-of-text risk, max {MAX_WORDS_PER_SLIDE})")

        # Banned phrases
        for pattern in BANNED_PHRASES:
            if re.search(pattern, full_text, re.IGNORECASE):
                errors.append(f"Slide {idx}: Contains banned engagement-bait/clickbait phrase matching '{pattern}'")

        # Visual artifact check
        artifact = slide.get("visual_artifact", {})
        artifact_type = artifact.get("type", "none")
        if artifact_type in ("none", "decorative_ai", "generic_stock"):
            errors.append(f"Slide {idx}: Violates Anti-Slop Gate 1. Lacks concrete proof artifact (found: '{artifact_type}')")

        # Check for unsourced stats in body
        if re.search(r"\b\d+([.,]\d+)?%\b|\b\$[0-9]+[a-zA-Z]?\b", body):
            source = slide.get("source", "").strip()
            if not source:
                errors.append(f"Slide {idx}: Mentions quantitative metric without explicit 'source' citation")

    return errors, warnings

def main():
    parser = argparse.ArgumentParser(description="Validate social carousel for anti-slop compliance")
    parser.add_argument("manifest", type=str, help="Path to carousel manifest JSON")
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    if not manifest_path.exists():
        print(f"Error: Manifest file '{manifest_path}' does not exist.", file=sys.stderr)
        sys.exit(2)

    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON manifest: {e}", file=sys.stderr)
        sys.exit(2)

    errors, warnings = validate_carousel(data)

    for w in warnings:
        print(f"  WARN: {w}")

    if errors:
        for err in errors:
            print(f"  FAIL: {err}", file=sys.stderr)
        print(f"\nVerification FAILED with {len(errors)} error(s).", file=sys.stderr)
        sys.exit(1)

    print("  PASS: Carousel passed all anti-slop and structure gates.")
    sys.exit(0)

if __name__ == "__main__":
    main()
