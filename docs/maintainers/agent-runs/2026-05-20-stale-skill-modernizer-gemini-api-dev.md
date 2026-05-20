# Run Log: gemini-api-dev

- **Selected skill**: `skills/gemini-api-dev`
- **Why it was selected**: The skill contains obsolete models like `gemini-3-pro-preview` which has been shut down, and it claims certain models are deprecated when they have newer primary versions.
- **Risk evidence reviewed**: Checked `https://ai.google.dev/gemini-api/docs/models.md.txt` which confirmed `gemini-3-pro-preview` is deprecated/shut down. Current recommended models include `gemini-3.1-pro-preview`, `gemini-3.5-flash`, `gemini-3.1-flash-lite`, and `gemini-3.1-flash-image-preview`.
- **Files changed**: `skills/gemini-api-dev/SKILL.md` (Updated model lists and code snippets to `gemini-3.5-flash`), `data/maintenance/ledger.json` (Updated tracking entry).
- **Linked PR/issue**: PR-modernize-gemini-api-dev
- **Next action**: Review updated SKILL.md for accuracy against future API changes.
