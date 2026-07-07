# Run Log: stale-skill-modernizer - azure-cosmos-db-py (2026-06-08)

## Target
skills/azure-cosmos-db-py

## Selection Reason
Selected an unclaimed stale skill to verify obsolescence against current primary documentation and modernize it if necessary.

## Evidence Reviewed
Checked the azure-cosmos-db changelog which lists a new feature in version 4.16.0 adding `aio` extras and native async client support (`azure.cosmos.aio.CosmosClient`). The previous `SKILL.md` used `starlette.concurrency.run_in_threadpool` with the synchronous client.

## Files Changed
- `skills/azure-cosmos-db-py/SKILL.md`
- `data/maintenance/ledger.json`

## Linked PR
PR-modernize-azure-cosmos-db-py

## Next Action
Review updated SKILL.md for accuracy.
