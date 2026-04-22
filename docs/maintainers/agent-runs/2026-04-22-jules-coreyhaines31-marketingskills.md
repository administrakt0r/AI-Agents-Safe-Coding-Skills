# Run Log: Import Marketing Skill from coreyhaines31/marketingskills

**Date:** 2026-04-22
**Agent:** jules
**Target:** `sources/coreyhaines31/marketingskills`

## Summary

The upstream repository `coreyhaines31/marketingskills` was listed in the ledger as a trusted upstream source for curated English-language marketing and growth skills with the status `monitoring`. This repository contains high-quality, safe marketing skills. I selected `community-marketing` as a high-value skill to import, to augment the marketing and growth bundles.

## Actions Taken

- Cloned the `coreyhaines31/marketingskills` repository locally.
- Verified the `community-marketing` skill adheres to the English-only policy.
- Imported `community-marketing` from the upstream source to `skills/community-marketing/SKILL.md`.
- Updated `skills/community-marketing/SKILL.md` to add required frontmatter fields (`risk: safe`, `source: "coreyhaines31/marketingskills"`, `date_added: "2026-04-22"`) and ensured it passes validation. Included a 'When to Use' section.
- Added `community-marketing` to the `seo-core` bundle in `data/bundles.json`.
- Validated skills using `npm run validate` and `npm run validate:references`.
- Updated `data/maintenance/ledger.json` to change the outcome for `sources/coreyhaines31/marketingskills` and updated the `lastReviewedAt` date, setting the outcome appropriately and updating the linked issue (`PR-jules-import-community-marketing`).

## Next Actions

Monitor the imported `community-marketing` skill for any future upstream updates. Use `sources/coreyhaines31/marketingskills` as a source for future single-skill import runs.
