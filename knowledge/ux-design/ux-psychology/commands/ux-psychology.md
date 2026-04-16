---
name: ux-psychology
description: Look up UX psychology principles and cognitive biases for your design scenario
argument-hint: "[scenario or principle name]"
---

You have access to 106 cognitive biases and UX psychology principles organized in the `ux-psychology` skill references.

## Behavior based on input

### No argument provided
Display a summary of available categories and scenarios:

**Categories:**
- Information (29 principles) — how users filter information
- Meaning (32 principles) — how users interpret meaning
- Time (28 principles) — how users make quick decisions
- Memory (17 principles) — how users remember things

**Scenarios available:** Onboarding, Pricing & Monetisation, Checkout & Conversion, Engagement & Retention, Forms & Input, Navigation & IA, Trust & Credibility, Notifications & Re-engagement, Empty States & Errors, Dashboard & Data Viz

Tell the user they can run `/ux-psychology [scenario]` or `/ux-psychology [principle name]` for details.

### Argument is a scenario name (e.g., "onboarding", "pricing", "checkout")
1. Read `skills/ux-psychology/references/scenario-index.md`
2. Find the matching scenario section
3. For each recommended principle (3-6), read the detailed entry from the corresponding category file
4. Present max 5 principles with:
   - Name and emoji
   - One-liner description
   - Contextualised tip for the user's specific scenario
   - One product example if available

### Argument is a principle name (e.g., "anchoring bias", "hick's law")
1. Search across the 4 category files in `skills/ux-psychology/references/` for the matching principle
2. Present the full entry: definition, product example, tip, and sources

### Argument is a general UX question or design context
1. Read `skills/ux-psychology/references/scenario-index.md` to identify relevant scenarios
2. Select the 3-5 most relevant principles
3. Read their full entries from the category files
4. Present them with contextualised application tips

## Output format
- Keep responses concise — max 5 principles per response
- Each principle: emoji + name, one-liner, contextualised tip
- End with: "Use `/ux-psychology [principle]` to dive deeper into any specific principle."
