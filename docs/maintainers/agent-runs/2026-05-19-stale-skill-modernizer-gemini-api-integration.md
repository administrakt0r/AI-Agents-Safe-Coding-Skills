# Run Log: 2026-05-19

**Target:** `skills/gemini-api-integration`
**Agent:** stale-skill-modernizer
**Status:** Removed

## Why it was selected
The skill `gemini-api-integration` was found to be instructing the use of legacy models (`gemini-1.5`, `gemini-2.0`) and deprecated SDKs (`@google/generative-ai`, `google-generativeai`).

## Evidence reviewed
- `skills/gemini-api-integration/SKILL.md` contains instructions for using `gemini-1.5` and `gemini-2.0` models.
- `skills/gemini-api-dev/SKILL.md` indicates that models like `gemini-1.5-*`, `gemini-2.0-*` and SDKs like `google-generativeai` and `@google/generative-ai` are legacy and deprecated, replaced by `gemini-3-*` and `@google/genai` / `google-genai`. Since the exact new syntax for the integration skill's complex examples (multimodal, streaming, function calling) is not fully documented in the reference, it is removed.

## Files changed
- Removed directory `skills/gemini-api-integration/`.
- Updated `data/bundles.json` to remove references to `gemini-api-integration`.
- Updated `data/maintenance/ledger.json` to mark as removed.

## Linked PR or issue
PR-remove-gemini-api-integration

## Next action
None