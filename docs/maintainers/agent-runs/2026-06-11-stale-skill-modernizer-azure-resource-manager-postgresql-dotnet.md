# Maintenance Run: azure-resource-manager-postgresql-dotnet

- **Date:** 2026-06-11
- **Agent:** stale-skill-modernizer
- **Target:** skills/azure-resource-manager-postgresql-dotnet

## Why Selected
The skill was unclaimed in the ledger and its stated Current Version (v1.2.0) was stale compared to the latest version available on NuGet.

## Evidence Reviewed
- `curl -s "https://api.nuget.org/v3-flatcontainer/azure.resourcemanager.postgresql/index.json"` confirmed v2.0.0 is available.
- Inspected `skills/azure-resource-manager-postgresql-dotnet/SKILL.md` to identify the old version.

## Files Changed
- `skills/azure-resource-manager-postgresql-dotnet/SKILL.md`
- `data/maintenance/ledger.json`

## Linked PR/Issue
PR-modernize-azure-resource-manager-postgresql-dotnet

## Next Action
Review the updated SKILL.md for any required API changes between v1 and v2.
