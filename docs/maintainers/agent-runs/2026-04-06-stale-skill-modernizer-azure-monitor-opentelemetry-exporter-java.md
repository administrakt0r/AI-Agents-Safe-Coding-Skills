# Run Log: azure-monitor-opentelemetry-exporter-java

- **Target:** `skills/azure-monitor-opentelemetry-exporter-java`
- **Why it was selected:** The skill was marked as deprecated and directed users to migrate to `azure-monitor-opentelemetry-autoconfigure`.
- **Evidence reviewed:** `SKILL.md` contained a deprecation notice and a migration section pointing to `azure-monitor-opentelemetry-autoconfigure` as the recommended approach. Additionally, primary documentation at https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=java was reviewed, confirming that the legacy exporter approach is no longer recommended and autoconfigure is the standard.
- **Files changed:**
  - Updated `skills/azure-monitor-opentelemetry-exporter-java/SKILL.md` to remove deprecated instructions and exclusively focus on the new autoconfigure approach. Preserved the folder name to prevent reference breaks in downstream derived files.
  - Updated `data/maintenance/ledger.json` to mark the skill as resolved.
- **Linked PR or issue:** PR-modernize-azure-monitor-opentelemetry-exporter-java
- **Next action:** Review the updated SKILL.md for accuracy.
