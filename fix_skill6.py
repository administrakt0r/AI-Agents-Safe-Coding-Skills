import re

with open('skills/influencer-marketing/SKILL.md', 'r') as f:
    content = f.read()

content = content.replace("---", "---\nname: influencer-marketing\ndescription: \"When the user wants to run influencer, creator, or ambassador partnerships to promote their product — finding and vetting partners, structuring deals, briefing creators, disclosure compliance, and measuring ROI.\"\nmetadata:\n  version: 1.0.0\n  risk: safe\n  source: community\n---", 1)


with open('skills/influencer-marketing/SKILL.md', 'w') as f:
    f.write(content)
