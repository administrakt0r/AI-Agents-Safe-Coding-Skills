# Agent Run: Modernize azure-resource-manager-postgresql-dotnet

- **Target**: `skills/azure-resource-manager-postgresql-dotnet`
- **Why it was selected**: The skill was obsolete, referring to version 1.2.0 (GA) while the latest version is 2.0.0. The note on Single Server deprecation was also updated for clarity.
- **Evidence reviewed**: Checked NuGet (`https://api.nuget.org/v3-flatcontainer/azure.resourcemanager.postgresql/index.json`) and saw version 2.0.0 is the latest.
- **Files changed**: `skills/azure-resource-manager-postgresql-dotnet/SKILL.md`, `data/maintenance/ledger.json`
- **Linked PR/Issue**: PR-modernize-azure-resource-manager-postgresql-dotnet
- **Next action**: Review updated SKILL.md for accuracy.
