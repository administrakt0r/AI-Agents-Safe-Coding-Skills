# Run Log: stale-skill-modernizer (2026-07-16)

## Target
`skills/azure-resource-manager-postgresql-dotnet`

## Review Summary
Selected `skills/azure-resource-manager-postgresql-dotnet` for modernization.
The skill's stated "Current Version" for the `Azure.ResourceManager.PostgreSql` SDK was `v1.2.0 (GA)`.

Checked against current primary documentation via NuGet registration API (`https://api.nuget.org/v3/registration5-semver1/azure.resourcemanager.postgresql/index.json`) and verified the current GA version is actually `2.0.0`.

No changes needed to remove non-English strings, as the skill adheres to the English-only policy.

## Changes Made
- Modernized `skills/azure-resource-manager-postgresql-dotnet/SKILL.md` by replacing `**Current Version**: v1.2.0 (GA)` with `**Current Version**: v2.0.0 (GA)`.
- Added ledger entry to track the modernization of this skill.

## Next Actions
- Human review and approval via the linked PR.
- Monitor `Azure.ResourceManager.PostgreSql` SDK for future releases.
