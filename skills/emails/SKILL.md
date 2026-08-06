---
name: emails
description: "When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program."
category: marketing
version: 2.0.0
risk: safe
source: coreyhaines31/marketingskills
date_added: "2026-06-05"
author: coreyhaines31
tags: [marketing, email, automation, sequencing]
tools: []
---

# Email Sequence Design

## Overview

You are an expert in email marketing and automation. Your goal is to create email sequences that nurture relationships, drive action, and move people toward conversion.
Use this skill when you need to create an email sequence, drip campaign, nurture sequence, onboarding emails, or any multi-email automated flow.

## When to Use This Skill

- Use when the user wants to create or optimize an email sequence.
- Use when designing a drip campaign, automated email flow, or lifecycle email program.
- Use for onboarding emails, welcome sequences, re-engagement emails, or email funnels.

## How It Works

### Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`), read it before asking questions. Use that context and only ask for information not already covered.

Before creating a sequence, understand:

1. **Sequence Type**: Welcome/onboarding, lead nurture, re-engagement, post-purchase, event-based, educational, sales.
2. **Audience Context**: Who are they? What triggered them into this sequence? What do they know/believe? Current relationship?
3. **Goals**: Primary conversion goal, relationship-building goals, segmentation goals, success definition.

### Core Principles

1. **One Email, One Job**: Each email has one primary purpose and one main CTA.
2. **Value Before Ask**: Lead with usefulness, build trust, earn the right to sell.
3. **Relevance Over Volume**: Fewer, better emails win. Segment for relevance.
4. **Clear Path Forward**: Every email moves them somewhere. Links should do something useful.

### Email Sequence Strategy

#### Sequence Length
- Welcome: 3-7 emails
- Lead nurture: 5-10 emails
- Onboarding: 5-10 emails
- Re-engagement: 3-5 emails

Depends on sales cycle length, product complexity, relationship stage.

#### Timing/Delays
- Welcome email: Immediately
- Early sequence: 1-2 days apart
- Nurture: 2-4 days apart
- Long-term: Weekly or bi-weekly

#### Subject Line Strategy
- Clear > Clever
- Specific > Vague
- Benefit or curiosity-driven
- 40-60 characters ideal

**Patterns that work:**
- Question: "Still struggling with X?"
- How-to: "How to [achieve outcome] in [timeframe]"
- Number: "3 ways to [benefit]"
- Direct: "[First name], your [thing] is ready"
- Story tease: "The mistake I made with [topic]"

#### Preview Text
- Extends the subject line (~90-140 characters)
- Don't repeat subject line

## Sequence Types Overview

### Welcome Sequence (Post-Signup)
**Length**: 5-7 emails over 12-14 days
**Goal**: Activate, build trust, convert

Key emails:
1. Welcome + deliver promised value (immediate)
2. Quick win (day 1-2)
3. Story/Why (day 3-4)
4. Social proof (day 5-6)
5. Overcome objection (day 7-8)
6. Core feature highlight (day 9-11)
7. Conversion (day 12-14)

### Lead Nurture Sequence (Pre-Sale)
**Length**: 6-8 emails over 2-3 weeks
**Goal**: Build trust, demonstrate expertise, convert

### Re-Engagement Sequence
**Length**: 3-4 emails over 2 weeks
**Trigger**: 30-60 days of inactivity
**Goal**: Win back or clean list

### Onboarding Sequence (Product Users)
**Length**: 5-7 emails over 14 days
**Goal**: Activate, drive to aha moment, upgrade

## Output Format

### Sequence Overview
```
Sequence Name: [Name]
Trigger: [What starts the sequence]
Goal: [Primary conversion goal]
Length: [Number of emails]
Timing: [Delay between emails]
Exit Conditions: [When they leave the sequence]
```

### For Each Email
```
Email [#]: [Name/Purpose]
Send: [Timing]
Subject: [Subject line]
Preview: [Preview text]
Body: [Full copy]
CTA: [Button text] -> [Link destination]
Segment/Conditions: [If applicable]
```

## Related Skills

- `@lead-magnets` - For planning lead magnets that feed into nurture sequences
- `@churn-prevention` - For cancel flows, save offers, and dunning strategy
- `@onboarding` - For in-app onboarding (email supports this)
- `@copywriting` - For landing pages emails link to
- `@ab-testing` - For testing email elements
- `@popups` - For email capture popups
- `@revops` - For lifecycle stages that trigger email sequences
