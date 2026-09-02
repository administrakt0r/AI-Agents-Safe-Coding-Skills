# Agent Run: Modernize azure-resource-manager-postgresql-dotnet

- **Target**: skills/azure-resource-manager-postgresql-dotnet
- **Why it was selected**: The skill contains obsolete deprecation notices regarding Single Server, and the SDK version was stale compared to the latest release (v1.4.2).
- **Evidence reviewed**: Verified current SDK versions on NuGet (https://api.nuget.org/v3-flatcontainer/azure.resourcemanager.postgresql/index.json).
- **Files changed**: `skills/azure-resource-manager-postgresql-dotnet/SKILL.md`, `data/maintenance/ledger.json`
- **Linked PR/Issue**: PR-modernize-azure-resource-manager-postgresql-dotnet
- **Next action**: Review updated SKILL.md to ensure no other deprecated references remain.
