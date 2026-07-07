# 2026-06-22-new-skill-import-curator-cro

**Target**: `sources/coreyhaines31/marketingskills/cro`

**Why it was selected**:
Selected as part of the ongoing mission to import English-safe, high-value skills from the trusted `coreyhaines31/marketingskills` repository. A gap analysis showed that the `cro` (Conversion Rate Optimization) skill was missing locally.

**Evidence reviewed**:
- Verified the upstream skill `SKILL.md` file from `coreyhaines31/marketingskills`.
- Reviewed for English-first compliance (no Spanish or non-English text found).
- Validated that the skill description provided detailed guidance for conversion rate optimization scenarios.
- Identified that the upstream skill lacked a `## When to Use` section and used an outdated metadata schema.
- Identified missing references `experiments.md` and `form.md` causing broken links.

**Files changed**:
- Downloaded `skills/cro/SKILL.md` from upstream.
- Modified `skills/cro/SKILL.md` to:
  - Add a dedicated `## When to Use` section containing triggers from the original description.
  - Shorten the frontmatter description to pass length checks.
  - Update the metadata block to include `version: 2.0.0`, `risk: safe`, and `source: coreyhaines31/marketingskills`.
- Downloaded `skills/cro/references/experiments.md` and `skills/cro/references/form.md` from upstream to resolve dangling links.
- Updated `data/maintenance/ledger.json` to record the new entry under `sources/coreyhaines31/marketingskills/cro` with status `monitoring`.
- Verified changes by running `npm install`, `npm run validate` and `npm run test`, which completed successfully with zero critical errors.

**Linked PR or issue**:
`PR-new-skill-import-curator-cro`

**Next action**:
Monitor the imported skill for upstream updates.
