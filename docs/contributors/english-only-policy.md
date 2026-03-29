# English-Only Policy

This repository is curated for English-first usage.

For skills, workflows, and other operational task assets:

- The primary instructional language must be English.
- Fully non-English assets must be removed instead of carried forward.
- Materially mixed-language assets whose core instructions are not English must be removed.
- Otherwise English assets should be normalized by replacing non-English examples, prompts, headings, or outputs with English equivalents where practical.

Allowed narrow exceptions:

- Proper nouns, product names, standards terms, and locale codes.
- Translation or localization reference material where non-English examples are necessary to describe the tool accurately.
- Domain examples that mention another language only as data, not as the language of the operating instructions.

Maintainer rules:

- Apply this policy before deeper modernization or security review work.
- If an asset fails the policy and cannot be normalized quickly, remove it or mark it for removal.
- Record removals and normalizations in `data/maintenance/ledger.json` and `data/maintenance/english-only-candidates.json`.
- Route all agent-made changes through human review before merge.
