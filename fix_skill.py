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

# Add When to Use section
when_to_use = """
## When to Use

When the user wants to run influencer, creator, or ambassador partnerships to promote their product — finding and vetting partners, structuring deals, briefing creators, disclosure compliance, and measuring ROI. Also use when the user mentions 'influencer marketing,' 'creator partnerships,' 'sponsorships,' 'YouTube sponsorships,' 'podcast sponsorships,' 'brand ambassador,' 'ambassador program,' 'creator program,' 'UGC creators,' 'B2B influencers,' 'thought leader ads,' 'gifting,' 'product seeding,' 'whitelisting creator content,' 'how much to pay an influencer,' or 'FTC disclosure.' For affiliate/referral payout mechanics, see referrals. For community-led advocacy, see community-marketing. For turning creator content into paid ads, see ad-creative.
"""

content = content.replace("# Influencer & Creator Marketing\n", f"# Influencer & Creator Marketing\n{when_to_use}")

# Fix dangling links
content = content.replace("the [tools registry](../../tools/REGISTRY.md)", "the tools registry (not included)")
content = content.replace("[sparktoro.md](../../tools/integrations/sparktoro.md)", "the sparktoro guide (not included)")

with open('skills/influencer-marketing/SKILL.md', 'w') as f:
    f.write(content)
