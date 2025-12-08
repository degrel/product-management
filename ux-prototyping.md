# UX & Prototyping Workflow

## Purpose
Bridge product vision and design execution through flows, wireframes, copy, and design critique.

## User Flow Documentation

### Flow Diagram Template

```markdown
# User Flow: [Flow Name]
**User**: [Persona]
**Goal**: [What they want to achieve]
**Entry Point**: [Where they start]

## Happy Path

```
[Entry] → [Step 1] → [Step 2] → [Step 3] → [Success State]
              ↓           ↓
         [Error A]   [Error B]
              ↓           ↓
         [Recovery]  [Recovery]
```

## Step Details

### Step 1: [Action Name]
- **Screen**: [Screen name]
- **User Action**: [What they do]
- **System Response**: [What happens]
- **Success Criteria**: [How they know it worked]
- **Edge Cases**:
  - [Edge case] → [Handling]

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
- **Primary CTA**: [Action] → [Result]
- **Secondary actions**: [List]
- **Hover states**: [Description]
- **Loading states**: [Description]

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

## Reference
- **Similar patterns**: [Internal/external examples]
- **Constraints**: [Technical/brand limitations]
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
| ✅ Do | ❌ Don't |
|-------|---------|
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

### Body Copy
| Location | Copy (FR) | Purpose |
|----------|-----------|---------|
| [Description] | [Text] | [What it explains] |

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

When reviewing UX copy:
- [ ] **Clarity**: Is it immediately understandable?
- [ ] **Brevity**: Can any words be removed?
- [ ] **Action-oriented**: Does user know what to do?
- [ ] **Consistent**: Matches terminology elsewhere?
- [ ] **Localization-ready**: Avoids idioms, allows expansion?
- [ ] **Accessible**: Works for screen readers?
- [ ] **On-brand**: Matches Galigeo voice?

## Design Review Framework

### Review Request Template

```markdown
# Design Review Request

## Context
- **Feature**: [Name]
- **Stage**: [Wireframe/Mockup/Prototype]
- **Designer**: [Name]
- **Review deadline**: [Date]

## Links
- **Design file**: [URL]
- **Prototype**: [URL]
- **PRD**: [URL]

## Specific Feedback Needed
1. [Question/area of concern]
2. [Question/area of concern]

## Constraints to Consider
- [Technical constraint]
- [Business constraint]
- [Timeline constraint]
```

### Review Feedback Template

```markdown
# Design Review: [Feature Name]

## Summary
- **Overall Assessment**: 🟢 Approve / 🟡 Minor changes / 🔴 Major revision
- **Reviewed by**: [Name]
- **Date**: [Date]

## Feedback by Category

### ✅ What Works Well
- [Positive observation]
- [Positive observation]

### 🔄 Suggested Changes

#### Must Fix (Blocking)
| Issue | Location | Suggestion | Rationale |
|-------|----------|------------|-----------|
| [Issue] | [Where] | [How to fix] | [Why it matters] |

#### Should Consider
| Suggestion | Location | Benefit |
|------------|----------|---------|
| [Suggestion] | [Where] | [Why it's better] |

#### Nice to Have
- [Minor enhancement]

### ❓ Questions
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

**Context**
- Does it fit the user's mental model?
- Is there enough context for decision-making?
- Are error states and edge cases handled?

**Data**
- What happens with 0 items? 1 item? 1000 items?
- How does it look with very long text?
- What about different data formats?
