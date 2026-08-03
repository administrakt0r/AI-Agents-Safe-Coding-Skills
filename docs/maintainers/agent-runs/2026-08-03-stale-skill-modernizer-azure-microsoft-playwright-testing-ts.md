# Agent Run: Modernize azure-microsoft-playwright-testing-ts

- **Target**: skills/azure-microsoft-playwright-testing-ts
- **Why it was selected**: The skill contains an obsolete migration notice stating the package `@azure/microsoft-playwright-testing` is retired on March 8, 2026.
- **Evidence reviewed**: The skill file itself explicitly mentions the deprecation/retirement date and instructs to use `@azure/playwright`.
- **Files changed**: Renamed `skills/azure-microsoft-playwright-testing-ts` to `skills/azure-playwright-ts`, updated its SKILL.md to remove the notice and update the name, and updated `data/maintenance/ledger.json`.
- **Linked PR/Issue**: PR-modernize-azure-playwright-ts
- **Next action**: Review updated SKILL.md for accuracy.
