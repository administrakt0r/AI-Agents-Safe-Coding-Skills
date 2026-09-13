const { hasQualityChecklist } = require("./tools/lib/workflow-contract.js");

const body1 = `Modernizes azure-ai-projects-dotnet by updating SDK versions to current versions based on NuGet API.

## Quality Bar Checklist ✅

**All items must be checked before merging.**

- [x] **Standards**: I have read docs/contributors/quality-bar.md and docs/contributors/security-guardrails.md.
- [x] **Metadata**: The SKILL.md frontmatter is valid (checked with npm run validate).
- [x] **Risk Label**: I have assigned the correct risk: tag (none, safe, critical, offensive, or unknown for legacy/unclassified content).
- [x] **Triggers**: The "When to use" section is clear and specific.
- [x] **Security**: If this is an _offensive_ skill, I included the "Authorized Use Only" disclaimer.
- [x] **Safety scan**: If this PR adds or modifies SKILL.md command guidance, remote/network examples, or token-like strings, I ran npm run security:docs (or equivalent hardening check) and addressed any findings.
- [x] **Automated Skill Review**: If this PR changes SKILL.md, I checked the skill-review GitHub Actions result and addressed any actionable feedback.
- [x] **Local Test**: I have verified the skill works locally.
- [x] **Repo Checks**: I ran npm run validate:references if my change affected docs, workflows, or infrastructure.
- [x] **Source-Only PR**: I did not manually include generated registry artifacts (CATALOG.md, skills_index.json, data/*.json) in this PR.
- [x] **Credits**: I have added the source credit in README.md (if applicable).
- [x] **Maintainer Edits**: I enabled Allow edits from maintainers on the PR.`;

const body2 = `Modernizes azure-ai-projects-dotnet by updating SDK versions to current versions based on NuGet API.

## Quality Bar Checklist ✅

**All items must be checked before merging.**

- [x] **Standards**: I have read \`docs/contributors/quality-bar.md\` and \`docs/contributors/security-guardrails.md\`.
- [x] **Metadata**: The \`SKILL.md\` frontmatter is valid (checked with \`npm run validate\`).
- [x] **Risk Label**: I have assigned the correct \`risk:\` tag (\`none\`, \`safe\`, \`critical\`, \`offensive\`, or \`unknown\` for legacy/unclassified content).
- [x] **Triggers**: The "When to use" section is clear and specific.
- [x] **Security**: If this is an _offensive_ skill, I included the "Authorized Use Only" disclaimer.
- [x] **Safety scan**: If this PR adds or modifies \`SKILL.md\` command guidance, remote/network examples, or token-like strings, I ran \`npm run security:docs\` (or equivalent hardening check) and addressed any findings.
- [x] **Automated Skill Review**: If this PR changes \`SKILL.md\`, I checked the \`skill-review\` GitHub Actions result and addressed any actionable feedback.
- [x] **Local Test**: I have verified the skill works locally.
- [x] **Repo Checks**: I ran \`npm run validate:references\` if my change affected docs, workflows, or infrastructure.
- [x] **Source-Only PR**: I did not manually include generated registry artifacts (\`CATALOG.md\`, \`skills_index.json\`, \`data/*.json\`) in this PR.
- [x] **Credits**: I have added the source credit in \`README.md\` (if applicable).
- [x] **Maintainer Edits**: I enabled **Allow edits from maintainers** on the PR.`;

const body3 = `Modernizes azure-ai-projects-dotnet by updating SDK versions to current versions based on NuGet API.

## Quality Bar Checklist ✅

**All items must be checked before merging.**

- [x] Standards
- [x] Metadata
- [x] Risk Label
- [x] Triggers
- [x] Security
- [x] Safety scan
- [x] Automated Skill Review
- [x] Local Test
- [x] Repo Checks
- [x] Source-Only PR
- [x] Credits
- [x] Maintainer Edits`;

console.log("Checklist valid 1:", hasQualityChecklist(body1));
console.log("Checklist valid 2:", hasQualityChecklist(body2));
console.log("Checklist valid 3:", hasQualityChecklist(body3));
