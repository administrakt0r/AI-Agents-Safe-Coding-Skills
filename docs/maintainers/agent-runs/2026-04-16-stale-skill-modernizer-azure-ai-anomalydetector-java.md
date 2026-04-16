# Stale Skill Modernizer Run Log: azure-ai-anomalydetector-java

**Date:** 2026-04-16
**Agent:** stale-skill-modernizer
**Target:** `skills/azure-ai-anomalydetector-java`

## Selection Reason
The skill was selected for review to verify its freshness against current primary documentation. It was unclaimed in the ledger.

## Evidence Reviewed
Consulted Microsoft Azure documentation regarding the Anomaly Detector service:
`https://learn.microsoft.com/en-us/azure/ai-services/anomaly-detector/overview`

Found the following deprecation notice:
> Starting 20 September 2023 you won’t be able to create new Anomaly Detector resources. The Anomaly Detector service is being retired 1 October 2026.

This makes the skill obsolete for building new applications.

## Action Taken
- **Files Changed / Removed:**
  - `skills/azure-ai-anomalydetector-java/SKILL.md` (Removed)
  - `skills/azure-ai-anomalydetector-java` directory (Removed)
- **Ledger Status Update:** Updated `data/maintenance/ledger.json` entry to status `removed`.

## Linked Handoff
**PR:** `PR-remove-azure-ai-anomalydetector-java`

## Next Action
None. The service is being retired and the skill has been removed.