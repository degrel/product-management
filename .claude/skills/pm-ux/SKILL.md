---
name: pm-ux
description: UX design, user flows, wireframe specs, UX copy, design review, cognitive biases, progressive disclosure, accessibility, component specs. Use when working on wireframes, UX copy, design critique, user flows, prototyping, or any UX/UI design task.
---

# UX & Prototyping Workflow

## Purpose
Bridge product vision and design execution through flows, wireframes, copy, and design critique — informed by cognitive psychology and UX research.

## Knowledge Base

For deeper UX knowledge, load on demand from `knowledge/ux-design/` - use it most of the times :
- **106 cognitive biases for UX** (Growth.design): `knowledge/ux-design/ux-psychology/skills/ux-psychology/references/` — Start with `scenario-index.md` to find relevant principles by scenario (onboarding, pricing, forms, etc.), then load the specific category file (information-biases.md, meaning-biases.md, time-biases.md, memory-biases.md)
- **Progressive disclosure patterns**: `knowledge/ux-design/Designing for Progressive Disclosure _ by G. L. _ Prototypr.html`

When designing or reviewing UX, systematically consider which cognitive biases apply to the current context. Use the scenario index to find relevant principles.

## User Flow Documentation

### Flow Diagram Template

```markdown
# User Flow: [Flow Name]
**User**: [Persona]
**Goal**: [What they want to achieve]
**Entry Point**: [Where they start]

## Happy Path

[Entry] -> [Step 1] -> [Step 2] -> [Step 3] -> [Success State]
              |             |
         [Error A]     [Error B]
              |             |
         [Recovery]    [Recovery]

## Step Details

### Step 1: [Action Name]
- **Screen**: [Screen name]
- **User Action**: [What they do]
- **System Response**: [What happens]
- **Success Criteria**: [How they know it worked]
- **Cognitive bias check**: [Which biases might affect user here — check scenario-index]
- **Edge Cases**:
  - [Edge case] -> [Handling]

### Step 2: [Action Name]
[Same structure]

## Decision Points
| Decision | Option A | Option B | Criteria |
|----------|----------|----------|----------|
| [Decision] | [Path] | [Path] | [How user decides] |

## Error States
| Error | Cause | User Message | Recovery |
|-------|-------|--------------|----------|
| [Error] | [Why] | [What to show] | [How to fix] |

## Analytics Events
| Event | Trigger | Properties |
|-------|---------|------------|
| [Event name] | [When fired] | [Data captured] |
```

### Flow Complexity Assessment

```markdown
## Flow Analysis: [Feature]

### Complexity Score
| Factor | Score (1-5) | Notes |
|--------|-------------|-------|
| Steps required | [n] | [Context] |
| Decision points | [n] | [Context] |
| Data inputs | [n] | [Context] |
| Integration points | [n] | [Context] |
| Error scenarios | [n] | [Context] |
| **Total** | **[Sum]** | |

### Recommendation
- Score 5-10: Simple flow, single iteration
- Score 11-20: Moderate, consider phased approach
- Score 21+: Complex, recommend user testing before dev
```

## Wireframe Specifications

### Wireframe Brief Template

```markdown
# Wireframe Brief: [Screen/Component]

## Context
- **Feature**: [Parent feature]
- **User Story**: As a [persona], I want to [action] so I can [outcome]
- **Priority**: [P0/P1/P2]

## Requirements

### Must Have
- [ ] [Requirement]

### Should Have
- [ ] [Requirement]

### Nice to Have
- [ ] [Requirement]

## Content Inventory
| Element | Content Type | Source | Editable? |
|---------|--------------|--------|-----------|
| [Title] | Text | System | No |
| [Field] | Input | User | Yes |
| [Data] | Dynamic | API | No |

## Interaction Notes
- **Primary CTA**: [Action] -> [Result]
- **Secondary actions**: [List]
- **Hover states**: [Description]
- **Loading states**: [Description]

## Progressive Disclosure
Consider what to show immediately vs. on demand:
- **Level 1 (always visible)**: [Core content needed for primary task]
- **Level 2 (on interaction)**: [Details revealed on hover/click/expand]
- **Level 3 (on demand)**: [Advanced options, settings, help]

## Responsive Behavior
| Breakpoint | Layout Change |
|------------|---------------|
| Desktop (>1024px) | [Description] |
| Tablet (768-1024px) | [Description] |
| Mobile (<768px) | [Description] |

## Accessibility Requirements
- [ ] Keyboard navigable
- [ ] Screen reader compatible
- [ ] Sufficient color contrast
- [ ] Focus states visible
```

### Component Specification

```markdown
# Component: [Component Name]

## Overview
[One sentence description]

## Variants
| Variant | Use Case | Visual Difference |
|---------|----------|-------------------|
| Default | [When to use] | [How it looks] |
| Active | [When to use] | [How it looks] |
| Disabled | [When to use] | [How it looks] |
| Error | [When to use] | [How it looks] |

## Props/Parameters
| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| [prop] | [type] | [Y/N] | [value] | [What it does] |

## Behavior
- **On click**: [Action]
- **On hover**: [Action]
- **On focus**: [Action]

## Content Guidelines
- **Label**: [Character limit, tone]
- **Helper text**: [When to use, format]
- **Error message**: [Format, examples]

## Do's and Don'ts
| Do | Don't |
|---|---|
| [Good practice] | [Bad practice] |
```

## UX Copy Guidelines

### Microcopy Framework

```markdown
# UX Copy: [Feature/Screen]

## Voice & Tone
- **Brand voice**: Professionnel, accessible, expert
- **This context tone**: [Informative/Encouraging/Urgent/Neutral]
- **User emotional state**: [Likely feeling when seeing this]

## Copy Inventory

### Headlines
| Location | Copy (FR) | Character Limit | Notes |
|----------|-----------|-----------------|-------|
| [Screen title] | [Text] | [n] | [Context] |

### CTAs
| Button | Copy (FR) | Action | Alt Text |
|--------|-----------|--------|----------|
| Primary | [Text] | [What happens] | [For screen readers] |
| Secondary | [Text] | [What happens] | [For screen readers] |

### Form Labels & Helpers
| Field | Label | Placeholder | Helper | Error |
|-------|-------|-------------|--------|-------|
| [Field] | [Label] | [Placeholder] | [Help text] | [Error msg] |

### Empty States
| State | Headline | Body | CTA |
|-------|----------|------|-----|
| No data | [Text] | [Text] | [Text] |
| Error | [Text] | [Text] | [Text] |
| First use | [Text] | [Text] | [Text] |

### Success/Error Messages
| Scenario | Message | Duration | Action |
|----------|---------|----------|--------|
| [Success] | [Text] | [Seconds] | [Dismiss/Action] |
| [Error] | [Text] | [Seconds] | [Retry/Contact] |
```

### Copy Review Checklist

- [ ] **Clarity**: Is it immediately understandable?
- [ ] **Brevity**: Can any words be removed?
- [ ] **Action-oriented**: Does user know what to do?
- [ ] **Consistent**: Matches terminology elsewhere?
- [ ] **Localization-ready**: Avoids idioms, allows expansion?
- [ ] **Accessible**: Works for screen readers?
- [ ] **On-brand**: Matches company voice?

## Design Review Framework

### Review Feedback Template

```markdown
# Design Review: [Feature Name]

## Summary
- **Overall Assessment**: Approve / Minor changes / Major revision
- **Reviewed by**: [Name]
- **Date**: [Date]

## Feedback by Category

### What Works Well
- [Positive observation]

### Suggested Changes

#### Must Fix (Blocking)
| Issue | Location | Suggestion | Rationale |
|-------|----------|------------|-----------|
| [Issue] | [Where] | [How to fix] | [Why it matters] |

#### Should Consider
| Suggestion | Location | Benefit |
|------------|----------|---------|
| [Suggestion] | [Where] | [Why it's better] |

### Questions
- [Question needing clarification]

## Next Steps
1. [Action] - [Owner] - [Date]
```

### Critique Questions

When reviewing designs, consider:

**Usability**
- Can users complete their goal in <3 clicks?
- Are interactive elements obviously clickable?
- Is the information hierarchy clear?

**Consistency**
- Does it match existing patterns in the product?
- Are spacing, colors, typography consistent?
- Do similar actions look similar?

**Accessibility**
- Is there sufficient color contrast?
- Are touch targets large enough (44x44px mobile)?
- Does it work without color alone?

**Cognitive Load** (check ux-psychology references)
- Is progressive disclosure applied appropriately?
- Are defaults set to reduce decision fatigue?
- Does it leverage recognition over recall?

**Data**
- What happens with 0 items? 1 item? 1000 items?
- How does it look with very long text?
- What about different data formats?
