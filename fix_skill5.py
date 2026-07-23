import re

with open('skills/influencer-marketing/SKILL.md', 'r') as f:
    content = f.read()

content = content.replace("risk: unknown", "  risk: unknown")
content = content.replace("source: community", "  source: community")


with open('skills/influencer-marketing/SKILL.md', 'w') as f:
    f.write(content)
