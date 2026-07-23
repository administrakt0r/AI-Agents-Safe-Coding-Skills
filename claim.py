import json
with open('data/maintenance/ledger.json', 'r') as f:
    ledger = json.load(f)
ledger['entries']['sources/coreyhaines31/marketingskills/influencer-marketing'] = {
    "status": "active",
    "lastReviewedAt": "2026-07-23",
    "reviewerAgent": "new-skill-import-curator",
    "outcome": "Claimed for import",
    "linkedIssueOrPr": "TBD",
    "nextAction": "TBD"
}
with open('data/maintenance/ledger.json', 'w') as f:
    json.dump(ledger, f, indent=2)
    f.write('\n')
