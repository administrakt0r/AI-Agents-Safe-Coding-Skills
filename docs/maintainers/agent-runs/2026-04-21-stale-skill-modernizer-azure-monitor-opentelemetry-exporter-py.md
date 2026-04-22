# Run Log: 2026-04-21

**Target:** `skills/azure-monitor-opentelemetry-exporter-py`
**Agent:** stale-skill-modernizer
**Status:** Removed

## Why it was selected
The skill uses the `azure-monitor-opentelemetry-exporter` package for Python, which is part of an older API. The SDK documentation and search results indicate that `azure-monitor-opentelemetry` (distro) is the primary recommendation, and older exporter packages are being deprecated across languages (like the Java one removed on 2026-04-12). Although still present on PyPI, it is drifting behind the current primary documentation which recommends the distro approach. To keep the AI agent skills fresh and safe, obsolete paths should be removed.

## Evidence reviewed
- `skills/azure-monitor-opentelemetry-exporter-py/SKILL.md` showed it's for low-level configuration, but notes "Use the distro (`azure-monitor-opentelemetry`) unless you need custom pipelines".
- Similar skills in other languages (like `azure-monitor-opentelemetry-exporter-java`) were already deprecated and removed.
- Microsoft's Azure SDK deprecation lists and NuGet show older exporter packages (like `Microsoft.OpenTelemetry.Exporter.AzureMonitor`) are obsolete.
- Current Microsoft docs (`azure-monitor-opentelemetry` distro) emphasize a simpler, integrated approach.

## Files changed
- Removed directory `skills/azure-monitor-opentelemetry-exporter-py/`.
- Updated `data/bundles.json` to remove references to `azure-monitor-opentelemetry-exporter-py`.
- Updated `data/maintenance/ledger.json` to mark as removed.

## Linked PR or issue
PR-remove-azure-monitor-opentelemetry-exporter-py

## Next action
None
