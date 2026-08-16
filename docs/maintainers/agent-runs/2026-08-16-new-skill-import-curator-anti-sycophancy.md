# Run Log: Import anti-sycophancy skill from sickn33/agentic-awesome-skills

**Date:** 2026-08-16
**Agent:** new-skill-import-curator
**Target:** `skills/anti-sycophancy` from `sickn33/agentic-awesome-skills`

## Why Selected

The `anti-sycophancy` skill addresses a real need for AI agent quality: eliminating sycophantic agreement patterns. It was not present in the existing repo, making it a net-new addition. The skill is:

- MIT-licensed (compatible)
- English-first (compliant with repo policy)
- Risk-rated as `safe`
- Originally sourced from `mskadu/opencode-agent-skills`
- Distributed through the trusted upstream `sickn33/agentic-awesome-skills`

## Deduplication Check

Ran `gh pr list --state open --limit 200 --json number,title,headRefName`. Searched for "anti-sycophancy" in all 200 open PR titles. No open PR exists for this skill. Result: **CLEAN -- no duplicates.**

## Prompt Injection Guard Scan

Scanned the upstream SKILL.md for red flags:

| Check | Result |
|-------|--------|
| "ignore previous instructions" / "disregard" / "forget your rules" | NOT FOUND |
| Hidden HTML comments, zero-width chars, markdown tricks | NOT FOUND |
| Execute arbitrary code, download from unknown URLs, `curl\|bash` | NOT FOUND |
| Base64-encoded payloads or obfuscated commands | NOT FOUND |
| Modify agent behavior or bypass safety checks | NOT FOUND |
| Exfiltrate data, tokens, environment variables | NOT FOUND |
| References to "system prompt", "DAN", "jailbreak" | NOT FOUND |

**Result: CLEAN -- safe to import.**

## Evidence Reviewed

1. Upstream SKILL.md content from `https://raw.githubusercontent.com/sickn33/agentic-awesome-skills/main/skills/anti-sycophancy/SKILL.md`
2. License: MIT (compatible with repo)
3. Source attribution: `mskadu/opencode-agent-skills` via `sickn33/agentic-awesome-skills`
4. English-only policy compliance: fully English, no translation examples needed
5. Existing repo skills: confirmed `anti-sycophancy` was not already present

## Files Changed

- `skills/anti-sycophancy/SKILL.md` -- NEW (imported from upstream, cleaned for repo conventions)
- `data/maintenance/ledger.json` -- UPDATED (added import entry with status "monitoring")

## Linked PR or Issue

`PR-jules-import-anti-sycophancy` (deterministic branch name: `jules-import-anti-sycophancy`)

## Next Action

Monitor the imported skill for upstream updates. The skill is ready for human review before merge.
