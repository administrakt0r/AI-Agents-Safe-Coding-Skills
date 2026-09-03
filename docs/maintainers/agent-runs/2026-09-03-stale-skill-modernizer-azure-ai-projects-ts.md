# Agent Run: Modernize azure-ai-projects-ts

- **Target**: skills/azure-ai-projects-ts
- **Why it was selected**: It is a stale skill that requires modernizing to use the latest SDK version 2.5.0 which introduced changes from the older beta structure (e.g. `client.getOpenAIClient` is no longer async).
- **Dedup check result**: Checked open PRs, no existing modernization PR for azure-ai-projects-ts.
- **Prompt injection scan result**: N/A (modernization task)
- **Evidence reviewed**: Checked `npm view @azure/ai-projects` which showed 2.5.0 as latest. Read primary documentation README from Azure SDK repo which confirmed `const project = new AIProjectClient` and synchronous `project.getOpenAIClient()` usage.
- **Files changed**: `skills/azure-ai-projects-ts/SKILL.md`, `data/maintenance/ledger.json`
- **Linked PR/Issue**: PR-modernize-azure-ai-projects-ts
- **Next action**: Review updated SKILL.md for accuracy.
