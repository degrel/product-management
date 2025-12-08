# Discovery Workflow

## Purpose
Transform raw user research into structured, actionable insights for product decisions.

## Interview Synthesis

### Input Processing
When receiving interview transcripts or notes:

1. **Extract verbatim quotes** - Capture exact user language
2. **Identify themes** - Group related observations
3. **Note emotional signals** - Frustration, excitement, confusion markers
4. **Flag feature requests** - Distinguish needs from wants

### Output Template: Interview Synthesis

```markdown
# Interview Synthesis: [Persona/Segment]

## Participant Profile
- **Role**: [Job title]
- **Company**: [Size, sector]
- **Use case**: [Primary usage of Galigeo]

## Key Insights

### Pain Points
| Pain Point | Verbatim Quote | Frequency | Severity (1-5) |
|------------|----------------|-----------|----------------|
| [Issue]    | "[Quote]"      | [n users] | [score]        |

### Jobs to Be Done
| When I... | I want to... | So I can... |
|-----------|--------------|-------------|
| [Context] | [Action]     | [Outcome]   |

### Feature Requests
| Request | Underlying Need | Priority Signal |
|---------|-----------------|-----------------|
| [What they asked] | [What they actually need] | [How urgent] |

## Opportunities
1. [Opportunity statement]
2. [Opportunity statement]

## Questions for Follow-up
- [Question]
```

## Problem Statement Generator

### Framework
Use the format: **[User] experiences [problem] when [context], which causes [impact].**

### Validation Criteria
- [ ] Specific user segment identified
- [ ] Problem is observable/measurable
- [ ] Context is concrete
- [ ] Impact is quantifiable or clearly described
- [ ] No solution embedded in statement

### Example
```
Les Directeurs de Développement Retail expérimentent une perte de temps significative 
lors de l'analyse des zones de chalandise, car ils doivent croiser manuellement 
plusieurs sources de données, ce qui retarde leurs décisions d'implantation de 2-3 semaines.
```

## JTBD (Jobs to Be Done) Framework

### Structure
```markdown
## Job Statement
**When** [situation/trigger]
**I want to** [motivation/action]
**So I can** [expected outcome]

## Job Map
1. **Define** - How do they frame the job?
2. **Locate** - What inputs do they need?
3. **Prepare** - What setup is required?
4. **Confirm** - How do they validate readiness?
5. **Execute** - What's the core action?
6. **Monitor** - How do they track progress?
7. **Modify** - What adjustments are needed?
8. **Conclude** - How do they know it's done?

## Outcome Expectations
| Desired Outcome | Current Satisfaction | Importance |
|-----------------|---------------------|------------|
| [Outcome]       | [1-10]              | [1-10]     |
```

## Hypothesis Generator

### Template
```markdown
## Hypothesis: [Code/Name]

### Statement
**We believe that** [action/change]
**For** [user segment]
**Will result in** [expected outcome]
**Because** [rationale based on evidence]

### Evidence Supporting
- [Data point/quote]
- [Observation]

### Evidence Against
- [Counter-signal]

### Validation Approach
| Metric | Current | Target | Measurement Method |
|--------|---------|--------|-------------------|
| [KPI]  | [Value] | [Goal] | [How to measure]  |

### Risk Level
- **Confidence**: [High/Medium/Low]
- **Effort to validate**: [T-shirt size]
- **Impact if wrong**: [Description]
```

## Feedback Analysis

### Categorization Matrix

```markdown
## Feedback Triage: [Source/Period]

### By Category
| Category | Count | % | Trend vs Previous |
|----------|-------|---|-------------------|
| Bug      | n     | % | ↑/↓/→            |
| UX       | n     | % | ↑/↓/→            |
| Feature  | n     | % | ↑/↓/→            |
| Data     | n     | % | ↑/↓/→            |

### Priority Matrix
| Feedback | Frequency | Impact | Effort | Priority Score |
|----------|-----------|--------|--------|----------------|
| [Item]   | [1-5]     | [1-5]  | [1-5]  | [Formula]      |

### Actionable Insights
1. **Quick Win**: [Low effort, high impact item]
2. **Strategic**: [High effort, high impact item]
3. **Deprioritize**: [Low impact items]

### Verbatim Highlights
> "[Powerful quote representing common sentiment]" - [Persona type]
```

## Synthesis Patterns

### Affinity Mapping Output
```markdown
## Theme: [Theme Name]

### Sub-themes
- **[Sub-theme 1]**: [n observations]
  - [Observation]
  - [Observation]
- **[Sub-theme 2]**: [n observations]

### Insight
[One-sentence insight derived from theme]

### Opportunity
[How might we statement]
```

### Persona Update Trigger
When discovery reveals:
- New unserved segment → Create persona draft
- Behavior shift in existing segment → Update persona
- Segment no longer relevant → Archive persona
