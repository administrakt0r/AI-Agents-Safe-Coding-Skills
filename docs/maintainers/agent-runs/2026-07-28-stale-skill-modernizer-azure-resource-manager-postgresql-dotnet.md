# Agent Run: Modernize azure-resource-manager-postgresql-dotnet

- **Target**: skills/azure-resource-manager-postgresql-dotnet
- **Why it was selected**: The skill is stale and references an older version (1.2.0) of the Azure.ResourceManager.PostgreSql NuGet package, while 2.0.0 is the latest GA version according to the NuGet API.
- **Evidence reviewed**: Checked the latest version of Azure.ResourceManager.PostgreSql on NuGet (https://api.nuget.org/v3-flatcontainer/azure.resourcemanager.postgresql/index.json), which shows 2.0.0 is available.
- **Files changed**:
  - `skills/azure-resource-manager-postgresql-dotnet/SKILL.md`
  - `data/maintenance/ledger.json`
- **Linked PR/Issue**: PR-modernize-azure-resource-manager-postgresql-dotnet
- **Next action**: Review updated SKILL.md for accuracy against future API changes.
