# Run Log: azure-monitor-opentelemetry-exporter-java

- **Target:** `skills/azure-monitor-opentelemetry-exporter-java`
- **Why it was selected:** Unclaimed skill that was explicitly marked as deprecated and advised migration to `azure-monitor-opentelemetry-autoconfigure`.
- **Evidence reviewed:** The `SKILL.md` explicitly contained a `> **⚠️ DEPRECATION NOTICE**: This package is deprecated. Migrate to azure-monitor-opentelemetry-autoconfigure.`
- **Files changed or removal decision:**
  - Renamed directory `skills/azure-monitor-opentelemetry-exporter-java` to `skills/azure-monitor-opentelemetry-autoconfigure-java`
  - `skills/azure-monitor-opentelemetry-autoconfigure-java/SKILL.md`:
    - Changed title and frontmatter to `azure-monitor-opentelemetry-autoconfigure-java`.
    - Removed deprecation notices.
    - Removed legacy dependency.
    - Promoted autoconfigure to the primary installation and basic setup steps.
    - Updated reference links to point to the correct autoconfigure paths.
- **Linked PR or issue:** PR-modernize-azure-monitor-opentelemetry-java
- **Next action:** Review the updated SKILL.md for accuracy in real-world scenarios.
