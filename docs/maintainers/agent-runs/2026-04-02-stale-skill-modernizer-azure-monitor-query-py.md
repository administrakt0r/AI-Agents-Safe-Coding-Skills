# Run Log: azure-monitor-query-py Modernization

- **Target:** `skills/azure-monitor-query-py`
- **Why it was selected:** The Python Azure Monitor Query SDK has split its functionality. The `azure-monitor-query` package is now exclusively for querying Log Analytics workspaces, while a new package, `azure-monitor-querymetrics`, handles querying Azure Monitor metrics. The existing skill documentation still instructed users to query metrics using the old `azure-monitor-query` package, rendering it obsolete.
- **Evidence reviewed:**
  - Microsoft documentation for `azure-monitor-query` and `azure-monitor-querymetrics`.
  - Package contents of `azure-monitor-query` (v2.0.0) show `MetricsQueryClient` is removed.
  - Package contents of `azure-monitor-querymetrics` (v1.0.0) show `MetricsClient` and `query_resources`.
- **Files changed or removal decision:**
  - Modified `skills/azure-monitor-query-py/SKILL.md` to update the Installation section to include `azure-monitor-querymetrics`.
  - Updated the code examples to use `azure.monitor.querymetrics.MetricsClient` instead of the removed `azure.monitor.query.MetricsQueryClient`.
  - Updated the method call from `query_resource` to `query_resources` with the correct arguments (e.g., `resource_ids`, `metric_namespace`).
  - Removed outdated APIs (`list_metric_definitions`, `list_metric_namespaces`).
  - Updated the `azure.monitor.querymetrics.aio` asynchronous import.
  - Updated the Client Types table.
  - Modified `data/maintenance/ledger.json` to reflect the active claim and subsequent normalized outcome.
- **Linked PR or issue:** `PR-modernize-azure-monitor-query-py`
- **Next action:** Review the updated `SKILL.md` for accuracy.
