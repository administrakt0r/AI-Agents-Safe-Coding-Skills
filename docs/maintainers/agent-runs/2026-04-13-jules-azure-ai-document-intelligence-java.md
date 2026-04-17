# Agent Run Log: Modernize azure-ai-formrecognizer-java

**Date:** 2026-04-13
**Agent:** jules
**Target:** skills/azure-ai-formrecognizer-java (now skills/azure-ai-document-intelligence-java)
**Outcome:** normalized

## Summary
The Azure Document Intelligence SDK for Java was formerly known as Form Recognizer. The SDK package has moved from `azure-ai-formrecognizer` to `azure-ai-documentintelligence`. I have modernized this skill by renaming the folder and updating the SKILL.md to use the new names and dependencies.

## Evidence
- https://raw.githubusercontent.com/Azure/azure-sdk-for-java/main/sdk/documentintelligence/azure-ai-documentintelligence/README.md indicates the name change and new dependency package.
- `azure-ai-documentintelligence` is the updated client library.

## Files Changed
- Renamed `skills/azure-ai-formrecognizer-java/` to `skills/azure-ai-document-intelligence-java/`
- Updated `skills/azure-ai-document-intelligence-java/SKILL.md` to reflect new class names and maven dependencies.
- Updated `data/bundles.json` references.
- Updated `data/maintenance/ledger.json`.

## Linked PR
- PR-modernize-azure-ai-document-intelligence-java

## Next Action
- Review the updated SKILL.md for accuracy.
