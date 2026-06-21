# Run Log: 2026-06-13

**Target:** `sources/coreyhaines31/marketingskills/ads`
**Role:** new-skill-import-curator

## Why Selected
The `ads` skill is a high-value marketing skill from a trusted upstream source (`coreyhaines31/marketingskills`). It was unclaimed and did not exist locally.

## Evidence Reviewed
- Verified local `skills/ads` directory did not exist.
- Read `docs/contributors/english-only-policy.md` and confirmed the skill contained Portuguese instructions (`pt-BR`) related to medical compliance.

## Actions Taken
- Downloaded `SKILL.md` for `ads`.
- Normalized the skill to adhere to the English-only policy by removing the `Medical / CFM compliance` section and related self-check items.
- Logged the normalization in `data/maintenance/english-only-candidates.json`.
- Updated `data/maintenance/ledger.json` with status `monitoring`.

## Next Action
Monitor the imported skill for upstream updates.

## Linked PR/Issue
PR-new-skill-import-curator-ads
