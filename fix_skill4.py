import re

with open('skills/influencer-marketing/SKILL.md', 'r') as f:
    content = f.read()

content = content.replace("  version: 1.0.0", "  version: 1.0.0\n  risk: unknown\n  source: community")

with open('skills/influencer-marketing/SKILL.md', 'w') as f:
    f.write(content)
