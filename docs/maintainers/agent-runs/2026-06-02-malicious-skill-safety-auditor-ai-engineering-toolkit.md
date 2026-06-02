# Malicious Skill Safety Auditor Run: ai-engineering-toolkit

**Target:** `skills/ai-engineering-toolkit`
**Date:** 2026-06-02
**Role:** malicious-skill-safety-auditor

## Selection Reasoning
The `ai-engineering-toolkit` skill was selected because it is marked as `risk: offensive` and did not contain the explicit user verification requirement per `docs/contributors/security-guardrails.md`.

## Evidence Reviewed
- `skills/ai-engineering-toolkit/SKILL.md` frontmatter has `risk: offensive`.
- The skill text lacked the exact required phrase: `Ask the user to verify the target URL/IP before running.`

## Action Taken
- Hardened `skills/ai-engineering-toolkit/SKILL.md` by inserting the mandatory user verification instruction under "Security & Safety Notes".

## Linked PR
- `PR-ai-engineering-toolkit-hardening`

## Next Action
- Monitor for re-introduction of active payloads.
