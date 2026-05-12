# Run Log: 2026-05-12

**Target:** `skills/azure-ai-transcription-py`
**Agent:** stale-skill-modernizer
**Status:** Removed

## Selected skill
`skills/azure-ai-transcription-py`

## Why it was selected
The skill uses a fictional/non-existent package `azure-ai-transcription` for Python, which drifts behind the current primary documentation and actual pip repositories where `azure-cognitiveservices-speech` is the real official SDK.

## Risk evidence reviewed
- `pip index versions azure-ai-transcription` returned no results.
- Checked Microsoft docs and `pypi.org` for Cognitive Services Speech, which confirms `azure-cognitiveservices-speech` is the required dependency for speech transcription via Python.

## Files changed
- Removed directory `skills/azure-ai-transcription-py/`.
- Updated `data/bundles.json` to remove references.
- Updated `data/maintenance/ledger.json` to mark as removed.

## Linked PR/issue
PR-remove-azure-ai-transcription-py

## Next action
None
