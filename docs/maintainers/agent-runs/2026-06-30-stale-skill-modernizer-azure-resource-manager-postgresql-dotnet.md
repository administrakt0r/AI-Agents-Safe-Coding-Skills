# Agent Run: Modernize azure-resource-manager-postgresql-dotnet

- **Target**: `skills/azure-resource-manager-postgresql-dotnet`
- **Why it was selected**: The skill was obsolete and using an outdated version of the `Azure.ResourceManager.PostgreSql` SDK (v1.2.0) and API version (`2023-12-01-preview`).
- **Evidence reviewed**: Checked the latest Nuget version for `Azure.ResourceManager.PostgreSql` which is `2.0.0` and the current Azure PostgreSQL Flexible Server REST API which uses version `2024-08-01`.
- **Files changed**:
  - `skills/azure-resource-manager-postgresql-dotnet/SKILL.md`
  - `data/maintenance/ledger.json`
- **Linked PR/Issue**: PR-modernize-azure-resource-manager-postgresql-dotnet
- **Next action**: Review updated SKILL.md for accuracy against future API changes.
