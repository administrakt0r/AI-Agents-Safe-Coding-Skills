# Run Log: stale-skill-modernizer

- **Date:** 2026-03-30
- **Agent:** stale-skill-modernizer
- **Target:** `skills/azure-monitor-query-java`
- **Linked PR/Issue:** `PR-modernize-azure-monitor-query-java`

## Why it was selected
The `azure-monitor-query-java` skill was explicitly marked with a `DEPRECATION NOTICE` stating that the legacy `azure-monitor-query` package should be migrated to `azure-monitor-query-logs` and `azure-monitor-query-metrics`. As the stale-skill modernizer, identifying obsolete and deprecated instructions is a core directive.

## Evidence reviewed
- `skills/azure-monitor-query-java/SKILL.md` (Checked for deprecation warnings)
- `data/maintenance/ledger.json` (Checked to ensure the skill wasn't already claimed)
- `https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/monitor/azure-monitor-query-logs/migration-guide.md` (Consulted for migration details to the new APIs)

## Files changed
- `skills/azure-monitor-query-java/SKILL.md`: Completely rewritten to instruct agents to use `azure-monitor-query-logs` and `azure-monitor-query-metrics`. Old, deprecated imports and syntax have been swapped with the latest syntax as indicated in the migration guide.
- `data/maintenance/ledger.json`: Updated status to `normalized` and detailed the outcome of the modernization task.

## Next action
Review the updated SKILL.md for accuracy in real-world scenarios.