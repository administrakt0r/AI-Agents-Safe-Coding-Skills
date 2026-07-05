# 2026-07-05-new-skill-import-curator-product-marketing

- **Target**: `sources/coreyhaines31/marketingskills/product-marketing`
- **Why it was selected**: High-value marketing skill missing from the local skills registry, not claimed in the ledger.
- **Evidence reviewed**: Verified `SKILL.md` from upstream via `curl`. Confirmed compliance with the English-first policy. Checked `data/maintenance/ledger.json` for prior claims.
- **Files changed**:
  - Downloaded `skills/product-marketing/SKILL.md` and modernized its frontmatter (added `risk`, `source`, truncated `description`, and moved full description to a `## When to Use` section).
  - Updated `data/maintenance/ledger.json` to track the claim and outcome.
- **Linked PR or issue**: PR-new-skill-import-curator-product-marketing
- **Next action**: Monitor the imported skill for upstream updates.
