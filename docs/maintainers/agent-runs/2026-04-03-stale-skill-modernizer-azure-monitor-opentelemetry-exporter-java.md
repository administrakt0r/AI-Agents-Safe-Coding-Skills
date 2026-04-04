# Run Log: azure-monitor-opentelemetry-exporter-java

- **Target:** `skills/azure-monitor-opentelemetry-exporter-java`
- **Why it was selected:** Selected by `stale-skill-modernizer` because it was unclaimed and outdated.
- **Evidence reviewed:** The SKILL.md file contained an explicit deprecation notice: `> **⚠️ DEPRECATION NOTICE**: This package is deprecated. Migrate to azure-monitor-opentelemetry-autoconfigure.`
- **Files changed or removal decision:**
    - Renamed directory `skills/azure-monitor-opentelemetry-exporter-java` to `skills/azure-monitor-opentelemetry-autoconfigure-java`.
    - Rewrote `SKILL.md` to focus on the autoconfigure package setup, removing deprecated content and updating metadata (`risk: safe`, `name: azure-monitor-opentelemetry-autoconfigure-java`).
    - Updated `data/maintenance/ledger.json`.
- **Linked PR or issue:** `PR-modernize-azure-monitor-opentelemetry-autoconfigure-java`
- **Next action:** Review the updated SKILL.md for accuracy.