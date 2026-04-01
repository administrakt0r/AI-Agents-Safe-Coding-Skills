# Run Log: stale-skill-modernizer

- **Date:** 2026-03-31
- **Agent:** stale-skill-modernizer
- **Target:** `skills/azure-communication-callingserver-java`
- **Linked PR/Issue:** `PR-remove-azure-communication-callingserver-java`

## Why it was selected
The `azure-communication-callingserver-java` skill explicitly states it is deprecated. Specifically, the SDK has been renamed to Call Automation, and developers are instructed to use `azure-communication-callautomation` instead. Since the replacement skill already exists (`skills/azure-communication-callautomation-java`), this legacy/deprecated skill is obsolete.

## Evidence reviewed
- `skills/azure-communication-callingserver-java/SKILL.md` (checked for deprecation status and replacement SDK suggestions).
- `skills/azure-communication-callautomation-java/SKILL.md` (checked to ensure the modern replacement exists in the repository).
- `data/maintenance/ledger.json` (checked to ensure the skill was not already claimed or recently reviewed).

## Files changed
- Removed `skills/azure-communication-callingserver-java` entirely.
- Updated `data/maintenance/ledger.json` with the outcome of removing this obsolete skill.

## Next action
Review the PR to confirm the removal of the deprecated SDK skill.