import json
with open('data/maintenance/ledger.json', 'r') as f:
    ledger = json.load(f)
ledger['entries']['sources/coreyhaines31/marketingskills/influencer-marketing'] = {
    "status": "monitoring",
    "lastReviewedAt": "2026-07-23",
    "reviewerAgent": "new-skill-import-curator",
    "outcome": "Imported the influencer-marketing skill after verifying it complies with the English-first policy and quality standards.",
    "linkedIssueOrPr": "PR-new-skill-import-curator-influencer-marketing",
    "nextAction": "Monitor the imported skill for upstream updates."
}
with open('data/maintenance/ledger.json', 'w') as f:
    json.dump(ledger, f, indent=2)
    f.write('\n')
