# Agent Maintenance Run Log

**Date:** 2026-05-02
**Agent:** jules
**Target:** `sources/coreyhaines31/marketingskills/community-marketing`

## Why it was selected

- It is a highly relevant skill for community-led growth strategies, adding value to the curated collection.
- It was unclaimed and unreviewed in the ledger.
- It provides important instructions for creating community strategies across platforms like Discord, Slack, and Reddit.

## Evidence Reviewed

- Examined the upstream `SKILL.md` from `coreyhaines31/marketingskills`.
- Confirmed the file adhered to the English-first policy natively without requiring translation.
- Verified there were no active reverse shell payloads, unauthorized API execution endpoints, or potentially harmful configurations.

## Actions Taken

- Created `skills/community-marketing/SKILL.md` by importing the upstream version.
- Updated YAML frontmatter to include `risk: safe`, `source: coreyhaines31/marketingskills`, and `date_added: "2026-05-02"`.
- Shortened the description in the YAML frontmatter to comply with validation limits (under 200 characters) by moving the detailed prompt triggers into a new `## When to Use` section.
- Added the skill to `seo-core` bundle in `data/bundles.json`.
- Ran `npm run validate` and `npm run validate:references` to ensure the skill and bundles pass required checks.
- Created ledger entry for `sources/coreyhaines31/marketingskills/community-marketing`.

## Linked Issue or PR

- PR-jules-import-community-marketing

## Next Action

- Monitor the imported skill for upstream updates.
