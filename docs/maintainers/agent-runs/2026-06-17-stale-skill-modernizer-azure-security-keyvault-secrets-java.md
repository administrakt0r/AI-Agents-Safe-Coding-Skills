# Maintenance Run Log: azure-security-keyvault-secrets-java

**Date:** 2026-06-17
**Agent Role:** stale-skill-modernizer
**Target:** skills/azure-security-keyvault-secrets-java

## Why it was selected
The skill was identified as an unclaimed candidate for modernization, to ensure the Java SDK versions are up-to-date with current upstream releases.

## Evidence reviewed
- Explored `skills/` and found `azure-security-keyvault-secrets-java`.
- Verified Maven Central `https://repo1.maven.org/maven2/com/azure/azure-security-keyvault-secrets/maven-metadata.xml` which showed version `4.11.0` as the latest release, superseding `4.9.0`.

## Files changed
- `skills/azure-security-keyvault-secrets-java/SKILL.md`: Updated `com.azure:azure-security-keyvault-secrets` from `4.9.0` to `4.11.0` and migrated the frontmatter `risk` and `source` tags into a `metadata` block.
- `data/maintenance/ledger.json`: Claimed the task and recorded the modernization outcome.

## Linked PR or issue
PR-modernize-azure-security-keyvault-secrets-java

## Next action
Review updated SKILL.md for accuracy.
