# Run Log: 2026-04-20

**Target:** `skills/azure-ai-formrecognizer-java`
**Agent:** Jules
**Status:** Removed

## Why it was selected
The skill uses the deprecated `azure-ai-formrecognizer` package for Java. It needed modernization or removal in compliance with the stale-skill cleanup directive.

## Evidence reviewed
Read `skills/azure-ai-document-intelligence-dotnet/SKILL.md` which states:
`| Azure.AI.FormRecognizer | Legacy SDK (deprecated) | Use DocumentIntelligence instead |`
Checked maven central for `azure-ai-documentintelligence`, it is the current package. The entire `azure-ai-formrecognizer-java` skill is based on the deprecated package.

## Files changed
- Removed directory `skills/azure-ai-formrecognizer-java/`.
- Updated `data/bundles.json`.
- Updated `data/maintenance/ledger.json`.

## Linked PR or issue
PR-remove-azure-ai-formrecognizer-java

## Next action
None
