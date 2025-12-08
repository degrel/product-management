# Execution Workflow

## Purpose
Translate product requirements into engineering-ready specifications with clear acceptance criteria.

## Feature Specification Template

```markdown
# Feature Spec: [Feature Name]

## Metadata
| Field | Value |
|-------|-------|
| **Author** | [PM Name] |
| **Status** | Draft / Review / Approved / In Dev |
| **Version** | [X.X] |
| **Last Updated** | [Date] |
| **Epic** | [Link] |
| **Target Release** | [Version/Date] |

---

## Overview

### Problem Statement
[What problem are we solving? For whom?]

### Hypothesis
We believe that [this capability] for [these users] will result in [this outcome] because [evidence/rationale].

### Success Metrics
| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|
| [Metric] | [Value] | [Goal] | [How to measure] |

### Out of Scope
- [Explicitly excluded item]
- [Explicitly excluded item]

---

## User Stories

### US-001: [Story Title]
**As a** [persona]
**I want to** [action]
**So that** [benefit]

**Priority**: P0 / P1 / P2
**Estimate**: [T-shirt size or points]

---

## Functional Requirements

### FR-001: [Requirement Name]
**Description**: [Detailed description]

**Business Rules**:
- BR-001: [Rule]
- BR-002: [Rule]

**Acceptance Criteria**:
```gherkin
GIVEN [precondition]
WHEN [action]
THEN [expected result]
AND [additional result]
```

**Edge Cases**:
| Scenario | Expected Behavior |
|----------|-------------------|
| [Edge case] | [How system handles it] |

---

## Non-Functional Requirements

### Performance
- Page load: < [X] seconds
- API response: < [X] ms
- Concurrent users: [X]

### Security
- [ ] Authentication required: [Yes/No]
- [ ] Authorization level: [Roles]
- [ ] Data sensitivity: [Classification]

### Scalability
- Expected data volume: [X records]
- Growth projection: [% per year]

---

## Data Requirements

### Data Model Changes
| Entity | Field | Type | Constraints | Notes |
|--------|-------|------|-------------|-------|
| [Entity] | [Field] | [Type] | [Required/Unique/etc.] | [Notes] |

### API Contracts
```json
// Endpoint: [METHOD] /api/v1/[resource]
// Request
{
  "field": "type"
}

// Response (200 OK)
{
  "field": "type"
}

// Error Response (4XX/5XX)
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message"
  }
}
```

---

## UI/UX Requirements
- **Wireframes**: [Link]
- **Mockups**: [Link]
- **Prototype**: [Link]

### Key Interactions
1. [Interaction description]
2. [Interaction description]

---

## Dependencies

### Internal
| Dependency | Team | Status | Blocker? |
|------------|------|--------|----------|
| [Dependency] | [Team] | [Status] | [Y/N] |

### External
| Dependency | Provider | Risk Level |
|------------|----------|------------|
| [Dependency] | [Provider] | [H/M/L] |

---

## Rollout Plan

### Feature Flags
- Flag name: `[feature_name]_enabled`
- Default: `false`
- Rollout: [% per phase]

### Phases
| Phase | Audience | Duration | Success Criteria |
|-------|----------|----------|------------------|
| Alpha | Internal | 1 week | No P0 bugs |
| Beta | [X]% users | 2 weeks | [Metrics] |
| GA | 100% | - | [Metrics] |

---

## Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk] | H/M/L | H/M/L | [Action] |

---

## Open Questions
| # | Question | Owner | Due | Resolution |
|---|----------|-------|-----|------------|
| 1 | [Question] | [Name] | [Date] | [Answer] |

---

## Appendix
- [Link to research]
- [Link to competitive analysis]
- [Link to technical design]
```

## Acceptance Criteria Generator

### Gherkin Format

When generating acceptance criteria, use this structure:

```gherkin
Feature: [Feature Name]
  As a [persona]
  I want [capability]
  So that [benefit]

  Background:
    Given [common precondition]

  Scenario: [Happy path scenario name]
    Given [precondition]
    And [additional precondition]
    When [action]
    And [additional action]
    Then [expected outcome]
    And [additional outcome]

  Scenario: [Alternative path scenario name]
    Given [different precondition]
    When [action]
    Then [different outcome]

  Scenario: [Error scenario name]
    Given [precondition]
    When [invalid action]
    Then [error handling]
    And [user feedback]
```

### AC Checklist

For each user story, ensure AC covers:

- [ ] **Happy path**: Primary success scenario
- [ ] **Alternative paths**: Valid variations
- [ ] **Edge cases**: Boundary conditions
- [ ] **Error scenarios**: Invalid inputs, failures
- [ ] **Empty states**: No data, first-time use
- [ ] **Permissions**: Unauthorized access attempts
- [ ] **Performance**: Load time expectations
- [ ] **Accessibility**: Keyboard, screen reader support

### Common Patterns

**CRUD Operations**
```gherkin
# Create
Scenario: Successfully create [entity]
  Given user has [permission]
  When user submits valid [entity] data
  Then [entity] is created
  And user sees confirmation message

Scenario: Fail to create [entity] with invalid data
  Given user has [permission]
  When user submits invalid [field]
  Then [entity] is not created
  And user sees error message "[message]"

# Read
Scenario: View [entity] list
  Given user has [permission]
  And [n] [entities] exist
  When user navigates to [page]
  Then user sees list of [entities]
  And list shows [fields]

# Update
Scenario: Edit [entity] successfully
  Given user has [permission]
  And [entity] exists
  When user modifies [field]
  And user saves changes
  Then [entity] is updated
  And user sees confirmation

# Delete
Scenario: Delete [entity] with confirmation
  Given user has [permission]
  And [entity] exists
  When user clicks delete
  Then confirmation modal appears
  When user confirms deletion
  Then [entity] is removed
  And user sees confirmation
```

**Search & Filter**
```gherkin
Scenario: Search returns matching results
  Given [n] [entities] exist
  When user searches for "[term]"
  Then results show only [entities] matching "[term]"
  And result count is displayed

Scenario: Search returns no results
  Given [n] [entities] exist
  When user searches for "[non-matching term]"
  Then empty state is displayed
  And user sees message "Aucun résultat pour [term]"

Scenario: Filter by [criteria]
  Given [n] [entities] exist
  When user applies [criteria] filter
  Then only [entities] matching [criteria] are shown
  And filter is visually active
```

## Edge Cases & Test Cases

### Edge Case Categories

```markdown
## Edge Case Analysis: [Feature]

### Data Boundaries
| Case | Input | Expected Behavior |
|------|-------|-------------------|
| Empty | No data | [Behavior] |
| Minimum | 1 item | [Behavior] |
| Maximum | [Max] items | [Behavior] |
| Over limit | [Max+1] items | [Behavior] |
| Long text | [n] characters | [Behavior] |

### State Transitions
| From State | To State | Trigger | Valid? |
|------------|----------|---------|--------|
| [State A] | [State B] | [Action] | Yes/No |

### Concurrent Operations
| Scenario | Expected Behavior |
|----------|-------------------|
| Two users edit same [entity] | [Behavior] |
| User edits while [entity] deleted | [Behavior] |

### Network Conditions
| Condition | Expected Behavior |
|-----------|-------------------|
| Slow connection (>3s) | [Behavior] |
| Connection lost mid-operation | [Behavior] |
| Timeout | [Behavior] |

### Permission Edge Cases
| User Role | Action | Expected |
|-----------|--------|----------|
| No permission | [Action] | [Denied + message] |
| Permission revoked mid-session | [Action] | [Behavior] |
```

### Test Case Template

```markdown
## Test Case: TC-[ID]

**Feature**: [Feature name]
**Requirement**: [FR-XXX]
**Priority**: Critical / High / Medium / Low

### Preconditions
1. [Condition]
2. [Condition]

### Test Steps
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | [Action] | [Result] |
| 2 | [Action] | [Result] |
| 3 | [Action] | [Result] |

### Test Data
| Field | Value |
|-------|-------|
| [Field] | [Value] |

### Postconditions
- [State after test]

### Notes
- [Any special considerations]
```

## Engineering Translation

### Technical Handoff Checklist

Before handing off to engineering:

- [ ] All user stories have acceptance criteria
- [ ] Edge cases documented
- [ ] Data model changes specified
- [ ] API contracts defined
- [ ] UI mockups linked and approved
- [ ] Dependencies identified and communicated
- [ ] Performance requirements stated
- [ ] Feature flags defined
- [ ] Rollout plan agreed
- [ ] Open questions resolved

### Spec Review Questions

Engineers should be able to answer:
1. What exactly should I build?
2. What does "done" look like?
3. What are the constraints?
4. What can I defer?
5. Who do I ask if I have questions?

### Translation Tips

| PM Language | Engineering Language |
|-------------|---------------------|
| "Users should be able to..." | API endpoint + UI interaction |
| "It should be fast" | Response time < X ms, page load < Y s |
| "Secure access" | Authentication + authorization rules |
| "Handle errors gracefully" | Error codes, retry logic, user messages |
| "Scale for growth" | Pagination, indexing, caching strategy |
