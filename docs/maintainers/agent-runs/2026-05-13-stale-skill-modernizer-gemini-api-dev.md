# Run Log: 2026-05-13

**Target:** `skills/gemini-api-dev`
**Agent:** stale-skill-modernizer
**Status:** Normalized

## Why it was selected
The skill's documentation referenced `gemini-3-pro-preview`, which has been officially deprecated and shut down according to Google's primary model documentation. It also referenced `gemini-3-flash-preview` and `gemini-3-pro-image-preview`, which have been superseded by the `Gemini 3.1` model family.

## Evidence reviewed
- `skills/gemini-api-dev/SKILL.md` showed references to `gemini-3-pro-preview`, `gemini-3-flash-preview`, and `gemini-3-pro-image-preview`.
- Current Microsoft docs (`https://ai.google.dev/gemini-api/docs/models.md.txt`) state that `Gemini 3 Pro Preview` is deprecated and was shut down on March 9, 2026. The docs recommend migrating to `Gemini 3.1 Pro Preview`.
- The docs also list `Gemini 3.1 Flash-Lite` and `Nano Banana 2 Preview` (`gemini-3.1-flash-image-preview`) as the current, stable or active models for fast tasks and image generation.

## Files changed
- Updated `skills/gemini-api-dev/SKILL.md` to point to the `3.1` model family in the text and code snippets.
- Added entry to `data/maintenance/ledger.json` to track this skill.

## Linked PR or issue
PR-modernize-gemini-api-dev

## Next action
Review the updated SKILL.md for accuracy.