# Run Log: 2026-04-07

**Target**: `skills/gemini-api-dev`

**Why**: Selected because it referenced obsolete and deprecated models. Specifically, Gemini 3 Pro Preview is deprecated according to current documentation.

**Evidence**: The official API specification (`https://ai.google.dev/gemini-api/docs/models.md.txt`) explicitly states `Gemini 3 Pro Preview is deprecated`. It also introduced the Gemini 3.1 models (`gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-image-preview`, `gemini-3.1-flash-live-preview`).

**Files changed**:
- `skills/gemini-api-dev/SKILL.md`: Updated the "Current Gemini Models" section and added the deprecated warning for `gemini-3-pro-preview`.

**Linked PR**: PR-modernize-gemini-api-dev

**Next action**: Review the updated SKILL.md for accuracy.
