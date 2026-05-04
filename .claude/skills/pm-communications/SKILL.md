---
name: pm-communications
description: Meeting agendas, meeting summaries, status updates, release notes, stakeholder announcements, sprint reviews, monthly business reviews, project status reports, PM soft skills. Use when preparing meetings, writing updates, drafting release notes, or communicating with stakeholders.
---

# Communications Workflow

## Purpose
Streamline stakeholder communications with templates for meetings, updates, and releases.

## Meeting Templates

### Meeting Agenda Generator

```markdown
# [Meeting Type]: [Topic]
**Date**: [Date] | **Time**: [Time] | **Duration**: [Duration]
**Location/Link**: [Where]

## Attendees
| Name | Role | Required/Optional |
|------|------|-------------------|
| [Name] | [Role] | Required |

## Objective
[One sentence: What decision/outcome do we need?]

## Pre-read
- [Document link] (X min read)

## Agenda
| Time | Topic | Owner | Type |
|------|-------|-------|------|
| 5 min | Contexte et objectif | [Name] | Info |
| 15 min | [Topic] | [Name] | Discussion |
| 10 min | [Topic] | [Name] | Decision |
| 5 min | Next steps & owners | [Name] | Action |

## Questions to Address
1. [Question]

## Decisions Needed
- [ ] [Decision 1]

---
*Please review pre-read materials before the meeting*
```

### Meeting Types

**Roadmap Review**
```markdown
# Roadmap Review: [Quarter]
**Cadence**: Monthly

## Agenda (60 min)
| Time | Topic |
|------|-------|
| 10 min | Previous commitments status |
| 20 min | Current quarter progress |
| 20 min | Next quarter preview |
| 10 min | Risks & trade-offs |

## Preparation
- Update roadmap status
- Identify blockers
- Prepare trade-off scenarios
```

**Sprint Review/Demo**
```markdown
# Sprint Review: Sprint [N]
**Cadence**: Bi-weekly

## Agenda (45 min)
| Time | Topic |
|------|-------|
| 5 min | Sprint goal recap |
| 25 min | Demo of completed work |
| 10 min | Metrics & feedback |
| 5 min | Upcoming sprint preview |

## Demo Order
1. [Feature] - [Developer]
```

**Stakeholder Sync**
```markdown
# Stakeholder Sync: [Project/Area]
**Cadence**: Weekly

## Agenda (30 min)
| Time | Topic |
|------|-------|
| 5 min | Wins since last sync |
| 10 min | Current blockers |
| 10 min | Decisions needed |
| 5 min | Next steps |

## Standing Questions
- What's blocking you?
- What decisions do you need from me?
- What should I know about?
```

### Meeting Summary Template

```markdown
# Meeting Summary: [Topic]
**Date**: [Date] | **Attendees**: [Names]

## Key Decisions
| Decision | Rationale | Owner |
|----------|-----------|-------|
| [Decision] | [Why] | [Name] |

## Action Items
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [Action] | [Name] | [Date] | pending |

## Discussion Highlights
- [Key point discussed]

## Open Questions
- [Question] -> Follow-up with [Name]

## Next Meeting
- **Date**: [Date]
- **Focus**: [Topic]

---
*Summary by [PM Name] - Corrections welcome by [Date]*
```

## Stakeholder Updates

### Weekly Status Update

```markdown
# Product Update: Week [N]
**Period**: [Date] - [Date]
**Author**: [PM Name]

## Overview
[3 bullets max: What matters this week] - 
[French version] En bref

## Key Metrics
| Metric | This Week | Last Week | Trend |
|--------|-----------|-----------|-------|
| [Metric] | [Value] | [Value] | direction |

## Shipped This Week
- **[Feature]**: [One-line description + impact]

## In Progress
| Item | Status | ETA | Notes |
|------|--------|-----|-------|
| [Feature] | On track | [Date] | |
| [Feature] | At risk | [Date] | [Blocker] |
| [Feature] | Blocked | TBD | [Blocker] |

## Next Week Focus
1. [Priority 1]
2. [Priority 2]

## Risks & Blockers
| Issue | Impact | Action Needed | Owner |
|-------|--------|---------------|-------|
| [Issue] | [Impact] | [Ask] | [Name] |
```

### Monthly Business Review

```markdown
# Product Monthly Review: [Month Year]

## Executive Summary
[2-3 sentences: Key takeaways for leadership]

## Performance vs. Objectives
| Objective | Target | Actual | Status |
|-----------|--------|--------|--------|
| [OKR 1] | [Target] | [Actual] | status |

## Delivery Summary
### Shipped
| Feature | Impact | Adoption |
|---------|--------|----------|
| [Feature] | [Benefit] | [Usage data] |

### Delayed
| Feature | Original ETA | New ETA | Reason |
|---------|--------------|---------|--------|
| [Feature] | [Date] | [Date] | [Reason] |

## Customer Insights
- **NPS**: [Score] ([Change] vs last month)
- **Top request**: [Feature/improvement]
- **Key feedback**: "[Quote]"

## Next Month Priorities
1. [Priority with rationale]
2. [Priority with rationale]

## Decisions Requested
- [ ] [Decision needed] - Due [Date]
```

### Project Status Report

```markdown
# Project Status: [Project Name]
**Date**: [Date] | **PM**: [Name] | **Status**: [health]

## Health Dashboard
| Dimension | Status | Notes |
|-----------|--------|-------|
| Schedule | [health] | [Note] |
| Scope | [health] | [Note] |
| Resources | [health] | [Note] |
| Quality | [health] | [Note] |

## Milestones
| Milestone | Planned | Actual | Status |
|-----------|---------|--------|--------|
| [Milestone] | [Date] | [Date] | [status] |

## This Period Accomplishments
- [Accomplishment]

## Next Period Plan
- [Planned work]

## Risks & Issues
| Item | Type | Severity | Mitigation | Owner |
|------|------|----------|------------|-------|
| [Item] | Risk/Issue | H/M/L | [Action] | [Name] |
```

## Release Communications

### Internal Release Notes

```markdown
# Release Notes: v[X.X.X]
**Release Date**: [Date]
**Release Manager**: [Name]

## What's New

### [Feature Name]
**For**: [Persona]
**What**: [Description]
**Why**: [Business value]
**How to use**: [Quick guide or link]

## Improvements
- **[Area]**: [Improvement description]

## Bug Fixes
- Fixed: [Bug description] ([Ticket #])

## Known Issues
- [Issue]: [Workaround if any]

## Technical Notes
- **Database migrations**: [Yes/No - details]
- **Breaking changes**: [Yes/No - details]
- **Rollback plan**: [Summary]
```

### Customer Release Notes

```markdown
# Nouveautes [Product] - [Month Year]

## Ce qui change pour vous

### [Feature Name] - Nouveau
[2-3 sentences in customer-friendly language explaining the benefit]

**Comment l'utiliser**:
1. [Step]
2. [Step]

---

### Ameliorations
- **[Feature]**: [What's better now]

### Corrections
- [Issue that was affecting customers]: Resolu

---

## A venir
Apercu des prochaines fonctionnalites :
- [Upcoming feature] - [Expected timeframe]

## Besoin d'aide ?
- Documentation: [Link]
- Support: [Contact]
```

### Stakeholder Announcement

```markdown
# Announcement: [Topic]
**To**: [Distribution list]
**From**: [PM Name]
**Date**: [Date]

## What's Happening
[Clear, concise explanation - 2-3 sentences]

## Why This Matters
[Impact on their work/goals]

## Timeline
| Event | Date |
|-------|------|
| [Milestone] | [Date] |

## What You Need to Do
- [ ] [Action] by [Date]

## Questions?
Contact [Name] at [Email/Slack]
```

## Communication Best Practices

### Audience Adaptation

| Audience | Focus | Length | Tone |
|----------|-------|--------|------|
| Executives | Business impact, decisions | 1 page max | Strategic |
| Sales/CS | Customer value, talking points | Bullet points | Enthusiastic |
| Engineering | Technical details, scope | Comprehensive | Precise |
| Customers | Benefits, how-to | Short, visual | Friendly |

### Writing Principles

1. **Lead with the ask**: What do you need from the reader?
2. **Front-load value**: Most important info first
3. **Be specific**: Dates, numbers, names
4. **Make it scannable**: Headers, bullets, bold key points
5. **Include next steps**: Who does what by when

## Soft Skills PM

### Leadership
- **Prendre la responsabilite** des decisions produit, meme sans autorite hierarchique
- **Guider les decisions** en apportant contexte, donnees et cadre d'analyse
- **Creer de la clarte** quand tout est flou

### Negociation
- **Avec les stakeholders** : Ecouter le besoin derriere la demande
- **Avec l'engineering** : Proposer des trade-offs (scope vs. timeline), pas des ultimatums
- **Avec soi-meme** : Accepter que la roadmap parfaite n'existe pas

### Problem-Solving
- **Decomposer** : Separer le probleme en sous-problemes independants
- **Prioriser** : Identifier ce qui debloque le plus de valeur
- **Proposer** : Arriver avec des options, pas juste le probleme
- **Iterer** : Premiere solution != meilleure solution

### Communication
La moitie du role PM est de la traduction :
- **Vision -> taches** : Transformer une direction strategique en items de backlog actionnables
- **Pain client -> roadmap** : Convertir les retours terrain en opportunites produit priorisees
- **Objectifs leadership -> metriques** : Traduire "on veut croitre" en KPIs mesurables
