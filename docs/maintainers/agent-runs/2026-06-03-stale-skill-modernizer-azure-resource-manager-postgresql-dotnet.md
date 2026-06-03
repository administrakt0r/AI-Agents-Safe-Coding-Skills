# Skill Maintenance Run Log

- **Selected skill**: `skills/azure-resource-manager-postgresql-dotnet`
- **Why it was selected**: The skill was obsolete as it was claiming to use version v1.2.0.
- **Evidence reviewed**: Investigated NuGet API (`https://api.nuget.org/v3/registration5-gz-semver2/azure.resourcemanager.postgresql/index.json`) and discovered that the newest version is 2.0.0.
- **Files changed**: Updated `skills/azure-resource-manager-postgresql-dotnet/SKILL.md` to reflect `**Current Version**: v2.0.0`.
- **Linked PR/issue**: `PR-modernize-azure-resource-manager-postgresql-dotnet`
- **Next action**: Review updated SKILL.md for API changes.
