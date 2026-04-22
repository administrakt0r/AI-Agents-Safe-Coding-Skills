# Run Log: azure-ai-anomalydetector-java

## Target
`skills/azure-ai-anomalydetector-java`

## Why it was selected
The skill uses the Azure AI Anomaly Detector service, which is being retired. We need to verify obsolescence and either update or remove the skill.

## Evidence reviewed
According to the primary Azure documentation for Anomaly Detector (https://learn.microsoft.com/en-us/azure/ai-services/anomaly-detector/overview):
"Starting 20 September 2023 you won’t be able to create new Anomaly Detector resources. The Anomaly Detector service is being retired 1 October 2026."

## Files changed or removal decision
The skill `skills/azure-ai-anomalydetector-java` has been removed because it is entirely obsolete and resources cannot be created for new users. The skill was also removed from `data/bundles.json`. The ledger `data/maintenance/ledger.json` was updated to reflect this removal.

## Linked PR or issue
PR-remove-azure-ai-anomalydetector-java

## Next action
None.
