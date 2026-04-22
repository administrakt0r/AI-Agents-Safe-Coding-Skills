# Run Log: stale-skill-modernizer

- **Date:** 2026-04-12
- **Agent:** stale-skill-modernizer
- **Target:** `skills/azure-ai-formrecognizer-java`
- **Linked PR/Issue:** `PR-modernize-azure-ai-document-intelligence-java`

## Why it was selected
The `azure-ai-formrecognizer-java` skill was using the deprecated Form Recognizer SDK. Microsoft has renamed and modernized the service to Document Intelligence, and the latest Java SDK is `azure-ai-documentintelligence`.

## Evidence reviewed
- `skills/azure-ai-formrecognizer-java/SKILL.md` (checked for references to deprecated `azure-ai-formrecognizer`).
- Maven Central repository (confirmed `azure-ai-documentintelligence` is the new and active SDK with latest version `1.0.1`).
- `data/maintenance/ledger.json` (checked to ensure the skill was not already claimed or recently reviewed).

## Files changed
- Renamed `skills/azure-ai-formrecognizer-java` to `skills/azure-ai-document-intelligence-java`.
- Modernized `skills/azure-ai-document-intelligence-java/SKILL.md` (updated package names, class names, artifact ID, versions, and terminology from Form Recognizer to Document Intelligence).
- Updated `data/bundles.json` references.
- Updated `data/maintenance/ledger.json` with the normalized status.

## Next action
Review the updated SKILL.md for accuracy in real-world scenarios.
