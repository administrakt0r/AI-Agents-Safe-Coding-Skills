# Agent Run Log: stale-skill-modernizer

**Date:** 2026-04-11
**Target:** `skills/azure-monitor-opentelemetry-exporter-java`

## Why it was selected
The `azure-monitor-opentelemetry-exporter-java` skill explicitly states in a deprecation notice that the package is deprecated and instructs users to migrate to `azure-monitor-opentelemetry-autoconfigure`. The skill was unclaimed in `data/maintenance/ledger.json`.

## Evidence reviewed
- The `SKILL.md` file contained `> **⚠️ DEPRECATION NOTICE**: This package is deprecated. Migrate to azure-monitor-opentelemetry-autoconfigure.`
- The original file contained multiple sections referencing the deprecated installation and a migration guide that shouldn't be the primary focus of a modern skill.

## Files changed
- Renamed `skills/azure-monitor-opentelemetry-exporter-java` to `skills/azure-monitor-opentelemetry-autoconfigure-java`
- Modified `skills/azure-monitor-opentelemetry-autoconfigure-java/SKILL.md`:
  - Updated `name`, `description`, `risk`, and H1 in frontmatter/header.
  - Removed deprecation notices and deprecated installation instructions.
  - Refocused the skill exclusively on the recommended `autoconfigure` package.
  - Removed redundant migration steps.
  - Updated reference links to point to the `autoconfigure` package.
- Updated `data/maintenance/ledger.json` to reflect the claim and completion of the normalization.

## Linked PR or issue
`PR-modernize-azure-monitor-opentelemetry-autoconfigure-java`

## Next action
Review the updated SKILL.md for accuracy in real-world scenarios.
