# Agent Run: Modernize Azure AI Document Intelligence Java

**Date:** 2026-04-03
**Agent:** stale-skill-modernizer
**Target:** `skills/azure-ai-formrecognizer-java` -> `skills/azure-ai-document-intelligence-java`

## Why it was selected
The `azure-ai-formrecognizer` Java SDK has been deprecated and superseded by `azure-ai-documentintelligence`. Microsoft renamed the service from "Azure Form Recognizer" to "Azure AI Document Intelligence" and released a new version of the client libraries with updated namespaces, classes, and artifacts.

## Evidence reviewed
- The Microsoft documentation confirms the name change and deprecation of the older SDK.
- Raw GitHub `azure-sdk-for-java` READMEs indicate the new artifact `com.azure:azure-ai-documentintelligence`.
- The main client class `DocumentAnalysisClient` was updated to `DocumentIntelligenceClient` and `DocumentModelAdministrationClient` was updated to `DocumentIntelligenceAdministrationClient`.
- The package namespace changed from `com.azure.ai.formrecognizer` to `com.azure.ai.documentintelligence`.

## Files changed or removal decision
- **Renamed:** Directory `skills/azure-ai-formrecognizer-java` -> `skills/azure-ai-document-intelligence-java`
- **Modified:** `skills/azure-ai-document-intelligence-java/SKILL.md`
  - Replaced `<artifactId>azure-ai-formrecognizer</artifactId>` with `<artifactId>azure-ai-documentintelligence</artifactId>`.
  - Replaced `<version>4.2.0-beta.1</version>` with `<version>1.1.0-beta.1</version>`.
  - Updated classes: `DocumentAnalysisClient` to `DocumentIntelligenceClient`, and `DocumentModelAdministrationClient` to `DocumentIntelligenceAdministrationClient`.
  - Added a note indicating the deprecation and renaming of the service.
- **Modified:** `data/maintenance/ledger.json`

## Linked PR or issue
`PR-modernize-azure-ai-document-intelligence-java`

## Next action
Review the updated `SKILL.md` for accuracy and test the new code samples.
