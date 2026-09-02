# Agent Run: new-skill-import-curator

**Target**: `sources/coreyhaines31/marketingskills/product-marketing`
**Date**: 2026-06-30

## Why it was selected
Selected the `product-marketing` skill from the trusted `coreyhaines31/marketingskills` source. It was an unclaimed, missing fundamental skill that creates the shared context `.agents/product-marketing.md` referenced by all other marketing skills. The skill was verified against the English-only policy and deemed safe.

## Evidence Reviewed
- Read `docs/contributors/english-only-policy.md` and `docs/maintainers/agent-maintenance-playbook.md`.
- Read the active ledger and `english-only-candidates.json` to verify it was unclaimed.
- Fetched `product-marketing/SKILL.md` from the upstream source.
- Verified English-only compliance and updated non-ASCII characters (e.g., `—`, `→`, `…`) to safe English-equivalent ASCII representations.

## Files Changed
- `skills/product-marketing/SKILL.md`: Created and updated to conform to the modernized v4 schema format (nested `metadata`, safe `risk` rating, missing `## When to Use` section added, and description shortened to under 300 characters).
- `data/maintenance/ledger.json`: Claimed and logged completion.

## Linked PR or Issue
`PR-new-skill-import-curator-product-marketing`

## Next Action
Monitor the imported skill for upstream updates.
