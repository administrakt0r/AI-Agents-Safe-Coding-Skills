# Run Log: stale-skill-modernizer

- **Date:** 2026-04-14
- **Agent:** stale-skill-modernizer
- **Target:** `skills/azure-ai-anomalydetector-java`
- **Linked PR/Issue:** `PR-remove-azure-ai-anomalydetector-java`

## Why it was selected
The `azure-ai-anomalydetector-java` skill uses the Azure Anomaly Detector service, which is being retired on 1 October 2026. Microsoft documentation confirms that the service is deprecated and no new resources can be created. Therefore, the skill is obsolete and must be removed.

## Evidence reviewed
- `skills/azure-ai-anomalydetector-java/SKILL.md` (checked the skill's purpose and service usage).
- Microsoft Azure Anomaly Detector documentation at `https://learn.microsoft.com/en-us/azure/ai-services/anomaly-detector/overview` (confirmed the service retirement date of 1 October 2026).
- `data/maintenance/ledger.json` (checked to ensure the skill was not already claimed or recently reviewed).

## Files changed
- Removed `skills/azure-ai-anomalydetector-java` entirely.
- Updated `data/maintenance/ledger.json` with the outcome of removing this obsolete skill.

## Next action
Review the PR to confirm the removal of the deprecated SDK skill.
