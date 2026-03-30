# Claude Model Modernization for AI Review

- **Date:** 2026-03-30
- **Agent:** jules
- **Target:** skills/code-review-ai-ai-review
- **Linked PR/Issue:** `local-jules-2026-03-30`

## Why This Run Happened

During a scheduled autonomous maintenance run, the agent identified that the skill `code-review-ai-ai-review` contained hardcoded references to a retired Claude model version, which is drifting behind current primary documentation and will fail in production.

## Evidence Reviewed

- `skills/claude-api/shared/models.md` lists `claude-3-5-sonnet-20241022` as "Retired (no longer available)". The same document lists `claude-sonnet-4-6` as the current recommended alias.
- `skills/code-review-ai-ai-review/SKILL.md` (line 395) contained a hardcoded reference to `claude-3-5-sonnet-20241022` in its internal Python helper script for processing the git diff via Anthropic's Python SDK.

## Actions Taken

- Updated `SKILL.md` to use the currently recommended `claude-sonnet-4-6` model alias.
- Verified no other non-English issues existed in the skill file.
- Updated the maintenance ledger to track this modernization, setting status to `normalized` and recording the issue link.

## Next Action

- Monitor for future upstream model deprecations and update remaining skills if necessary.
