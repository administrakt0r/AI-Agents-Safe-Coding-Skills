# Agent Run: Import marketing-plan skill

- **Target**: `sources/coreyhaines31/marketingskills/marketing-plan`
- **Why it was selected**: Selected as an unclaimed, high-value trusted upstream skill from coreyhaines31/marketingskills that was not yet imported or marked active/blocked in the ledger.
- **Evidence reviewed**: Checked `data/maintenance/ledger.json` to ensure the skill was unclaimed. Reviewed `docs/contributors/english-only-policy.md` and verified the upstream `SKILL.md` is in English. Validated the skill using `npm run validate` to ensure quality. Checked the upstream repository contents for `SKILL.md`, `evals/`, and `references/` files.
- **Files changed**:
  - Downloaded `SKILL.md`, `evals/evals.json`, and 13 reference files from `coreyhaines31/marketingskills/skills/marketing-plan`.
  - Updated `SKILL.md` frontmatter with `metadata` (version, risk, source) and truncated the description to under 300 characters.
  - Updated `data/maintenance/ledger.json` to track the import.
  - Created this run log in `docs/maintainers/agent-runs/`.
- **Linked PR/Issue**: `PR-new-skill-import-curator-marketing-plan`
- **Next action**: Monitor the imported skill for upstream updates.
