# Agent Run: Modernize azure-cosmos-java Skill

- **Target**: skills/azure-cosmos-java
- **Why it was selected**: The skill was found to contain outdated `<version>LATEST</version>` and unreplaced placeholder `<version>{bom_version}</version>`, and used the deprecated frontmatter schema.
- **Evidence reviewed**: Queried Maven Central and found latest azure-cosmos version is 4.81.0 and azure-sdk-bom is 1.3.8.
- **Files changed**:
  - skills/azure-cosmos-java/SKILL.md
  - data/maintenance/ledger.json
- **Linked PR/Issue**: PR-modernize-azure-cosmos-java
- **Next action**: Review updated SKILL.md for accuracy against future API changes.
