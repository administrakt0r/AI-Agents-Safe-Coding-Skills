import re

with open('skills/influencer-marketing/SKILL.md', 'r') as f:
    content = f.read()

# Fix frontmatter
new_frontmatter = """---
name: influencer-marketing
description: "When the user wants to run influencer, creator, or ambassador partnerships to promote their product — finding and vetting partners, structuring deals, briefing creators, disclosure compliance, and measuring ROI."
metadata:
  version: 1.0.0
  risk: safe
  source: community
---
"""

content = re.sub(r"^---.*?---\n", new_frontmatter, content, flags=re.DOTALL)


with open('skills/influencer-marketing/SKILL.md', 'w') as f:
    f.write(content)
