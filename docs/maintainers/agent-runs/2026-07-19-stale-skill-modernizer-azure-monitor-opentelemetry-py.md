# Run Log: 2026-07-19

**Target:** `skills/azure-monitor-opentelemetry-py`
**Agent:** stale-skill-modernizer
**Status:** normalized

## Why it was selected
The skill's documentation was stale and drifting behind the current official primary documentation for `azure-monitor-opentelemetry` distro.

## Evidence reviewed
Current Microsoft docs for `azure-monitor-opentelemetry` indicate that `enable_live_metrics` defaults to True, the list of officially supported instrumentations has changed, and configuration for disabling instrumentations uses `instrumentation_options` (a nested dict) instead of a list.

## Files changed
- Updated `skills/azure-monitor-opentelemetry-py/SKILL.md`.

## Linked PR or issue
PR-modernize-azure-monitor-opentelemetry-py

## Next action
Review updated SKILL.md for accuracy.
