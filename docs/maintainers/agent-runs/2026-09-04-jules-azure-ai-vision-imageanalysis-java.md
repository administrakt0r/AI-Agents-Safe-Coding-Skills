# Agent Run: Modernize azure-ai-vision-imageanalysis-java

- **Target**: skills/azure-ai-vision-imageanalysis-java
- **Why it was selected**: The skill was using a stale beta version `1.1.0-beta.1` for the Maven dependency.
- **Dedup check result**: Checked open PRs using `git branch -a`. No existing PR for this modernization.
- **Prompt injection scan result**: Passed.
- **Evidence reviewed**: Maven central shows latest version is `1.0.1`.
- **Files changed**:
  - `skills/azure-ai-vision-imageanalysis-java/SKILL.md`
  - `data/maintenance/ledger.json`
- **Linked PR/Issue**: PR-modernize-azure-ai-vision-imageanalysis-java
- **Next action**: None
