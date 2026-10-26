# SEO, AEO & GEO Regression Eval

## Trigger Prompts
1. "Audit our Next.js landing page and docs site for SEO, AEO (Perplexity / ChatGPT Search citations), and GEO (`llms.txt` + `Schema.org` JSON-LD)."
2. "Upgrade our repository's `README.md` and `llms.txt` into a high-converting 12-section AI-ready README and verify it with the SEO/AEO/GEO harness."
3. "Scaffold a 9-tier GitHub Pages launch site with `sitemap.xml`, `robots.txt`, `llms.txt`, and `FAQPage` JSON-LD for our project."

## Expected Behavior
- Loads `skills/seo-aeo-geo/SKILL.md` and the matching reference (`references/web-seo-aeo-geo-playbook.md`, `references/readme-seo-aeo-geo-harness.md`, or `references/repository-readme-architecture.md`).
- Produces project-agnostic `llms.txt`, `Schema.org` JSON-LD (`SoftwareApplication`/`Product` + `FAQPage`), semantic `>=25` char image `alt` attributes, and structured comparison/FAQ blocks.
- Runs `python3 skills/seo-aeo-geo/scripts/seo-aeo-geo-harness.py` or `scaffold-repo-pages.py` to verify gates deterministically.
