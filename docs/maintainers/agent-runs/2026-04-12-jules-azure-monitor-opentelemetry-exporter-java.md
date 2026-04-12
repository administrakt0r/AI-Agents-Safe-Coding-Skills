# Run Log: 2026-04-12

**Target:** `skills/azure-monitor-opentelemetry-exporter-java`
**Agent:** Jules
**Status:** Removed

## Why it was selected
The skill uses the deprecated `azure-monitor-opentelemetry-exporter` package for Java. It needed modernization or removal in compliance with the stale-skill cleanup directive.

## Evidence reviewed
Read `skills/azure-monitor-opentelemetry-exporter-java/SKILL.md`. The document itself contains a deprecation notice:
`> **⚠️ DEPRECATION NOTICE**: This package is deprecated. Migrate to azure-monitor-opentelemetry-autoconfigure.`
The entire skill is based on the deprecated package.

## Files changed
- Removed directory `skills/azure-monitor-opentelemetry-exporter-java/`.
- Updated `data/maintenance/ledger.json`.

## Linked PR or issue
PR-remove-azure-monitor-opentelemetry-exporter-java

## Next action
None
