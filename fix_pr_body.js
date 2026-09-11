const body = `Modernize azure-storage-blob-ts skill

- Update the version string from 12.x to 12.33.0 in \`skills/azure-storage-blob-ts/SKILL.md\`
- Update \`data/maintenance/ledger.json\` to mark the skill as active, and then as reviewed
- Create a run log in \`docs/maintainers/agent-runs/2026-09-13-stale-skill-modernizer-azure-storage-blob-ts.md\`

## Change Classification

- [x] Skill PR
- [ ] Docs PR
- [ ] Infra PR

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
- [x] **Maintainer Edits**: I enabled **Allow edits from maintainers** on the PR.
`

function hasQualityChecklist(body) {
  const text = String(body || "");
  const heading = text.match(/##\s+quality bar checklist\b/i);
  if (!heading) return false;

  const section = text.slice(heading.index).split(/\n##\s+/i, 2)[0];
  console.log("Section", section)
  return /-\s+\[[xX]\]/.test(section) && !/-\s+\[\s\]/.test(section);
}

console.log(hasQualityChecklist(body))
