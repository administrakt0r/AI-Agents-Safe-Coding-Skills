# Run Log: azure-monitor-opentelemetry-exporter-java Modernization

- **Target:** `skills/azure-monitor-opentelemetry-exporter-java`
- **Why it was selected:** The skill documentation itself noted that the `azure-monitor-opentelemetry-exporter` package is deprecated and that users should migrate to `azure-monitor-opentelemetry-autoconfigure`.
- **Evidence reviewed:**
  - Deprecation notice within `skills/azure-monitor-opentelemetry-exporter-java/SKILL.md` recommending the `autoconfigure` package instead.
  - The content primarily described the older setup process, which contradicts current primary documentation and best practices.
- **Files changed or removal decision:**
  - Renamed the directory from `skills/azure-monitor-opentelemetry-exporter-java` to `skills/azure-monitor-opentelemetry-autoconfigure-java`.
  - Modified `SKILL.md` frontmatter to rename the skill to `azure-monitor-opentelemetry-autoconfigure-java`.
  - Updated the content of `SKILL.md` to remove references to the deprecated installation, simplified the focus around the `azure-monitor-opentelemetry-autoconfigure` module, and removed the migration guide section (since the document itself is now the correct reference).
  - Updated `data/maintenance/ledger.json` to mark the skill as `normalized` with corresponding outcome.
- **Linked PR or issue:** `PR-modernize-azure-monitor-opentelemetry-java`
- **Next action:** Review the updated `SKILL.md` for accuracy.
