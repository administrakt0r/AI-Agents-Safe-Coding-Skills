# Skill Maintenance Run Log

- **Selected skill**: `skills/azure-ai-document-intelligence-dotnet`
- **Why it was selected**: The skill is stale as it contains references to the deprecated `Azure.AI.FormRecognizer` legacy SDK in its "Related SDKs" section.
- **Evidence reviewed**: `skills/azure-ai-document-intelligence-dotnet/SKILL.md` included `Azure.AI.FormRecognizer` under Related SDKs marked as "Legacy SDK (deprecated)".
- **Files changed**: Removed the "Related SDKs" section from `skills/azure-ai-document-intelligence-dotnet/SKILL.md`.
- **Linked PR/issue**: `PR-modernize-azure-ai-document-intelligence-dotnet`
- **Next action**: Review updated SKILL.md to ensure no other deprecated references remain.
