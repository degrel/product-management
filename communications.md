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
2. [Question]

## Decisions Needed
- [ ] [Decision 1]
- [ ] [Decision 2]

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
2. [Feature] - [Developer]
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
| [Action] | [Name] | [Date] | ⏳ |

## Discussion Highlights
- [Key point discussed]
- [Key point discussed]

## Open Questions
- [Question] → Follow-up with [Name]

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

## 🎯 TL;DR
[3 bullets max: What matters this week]

## 📊 Key Metrics
| Metric | This Week | Last Week | Trend |
|--------|-----------|-----------|-------|
| [Metric] | [Value] | [Value] | ↑/↓/→ |

## ✅ Shipped This Week
- **[Feature]**: [One-line description + impact]

## 🚧 In Progress
| Item | Status | ETA | Notes |
|------|--------|-----|-------|
| [Feature] | On track 🟢 | [Date] | |
| [Feature] | At risk 🟡 | [Date] | [Blocker] |
| [Feature] | Blocked 🔴 | TBD | [Blocker] |

## 🎯 Next Week Focus
1. [Priority 1]
2. [Priority 2]

## ⚠️ Risks & Blockers
| Issue | Impact | Action Needed | Owner |
|-------|--------|---------------|-------|
| [Issue] | [Impact] | [Ask] | [Name] |

## 💬 Feedback & Questions
[Office hours: Time/Link]
```

### Monthly Business Review

```markdown
# Product Monthly Review: [Month Year]

## Executive Summary
[2-3 sentences: Key takeaways for leadership]

## Performance vs. Objectives
| Objective | Target | Actual | Status |
|-----------|--------|--------|--------|
| [OKR 1] | [Target] | [Actual] | 🟢/🟡/🔴 |

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

## Competitive Landscape
- [Competitor move worth noting]

## Resource & Budget
| Category | Budget | Spent | Variance |
|----------|--------|-------|----------|
| [Category] | [€] | [€] | [€] |

## Next Month Priorities
1. [Priority with rationale]
2. [Priority with rationale]

## Decisions Requested
- [ ] [Decision needed] - Due [Date]
```

### Project Status Report

```markdown
# Project Status: [Project Name]
**Date**: [Date] | **PM**: [Name] | **Status**: 🟢🟡🔴

## Health Dashboard
| Dimension | Status | Notes |
|-----------|--------|-------|
| Schedule | 🟢🟡🔴 | [Note] |
| Scope | 🟢🟡🔴 | [Note] |
| Resources | 🟢🟡🔴 | [Note] |
| Quality | 🟢🟡🔴 | [Note] |

## Progress
[Visual: Gantt/timeline or percentage]

### Milestones
| Milestone | Planned | Actual | Status |
|-----------|---------|--------|--------|
| [Milestone] | [Date] | [Date] | ✅/⏳/❌ |

## This Period Accomplishments
- [Accomplishment]

## Next Period Plan
- [Planned work]

## Risks & Issues
| Item | Type | Severity | Mitigation | Owner |
|------|------|----------|------------|-------|
| [Item] | Risk/Issue | H/M/L | [Action] | [Name] |

## Budget Tracking
- **Planned**: [€]
- **Actual**: [€]
- **Forecast**: [€]
```

## Release Communications

### Internal Release Notes

```markdown
# Release Notes: v[X.X.X]
**Release Date**: [Date]
**Release Manager**: [Name]

## 🎉 What's New

### [Feature Name]
**For**: [Persona]
**What**: [Description]
**Why**: [Business value]
**How to use**: [Quick guide or link]

### [Feature Name]
[Same structure]

## 🔧 Improvements
- **[Area]**: [Improvement description]

## 🐛 Bug Fixes
- Fixed: [Bug description] ([Ticket #])

## ⚠️ Known Issues
- [Issue]: [Workaround if any]

## 📊 Technical Notes
- **Database migrations**: [Yes/No - details]
- **Breaking changes**: [Yes/No - details]
- **Rollback plan**: [Summary]

## 📚 Documentation
- [Updated doc link]

## 🙏 Contributors
[Team members who contributed]
```

### Customer Release Notes

```markdown
# Nouveautés [Product] - [Month Year]

## Ce qui change pour vous

### [Feature Name] - Nouveau ✨
[2-3 sentences in customer-friendly language explaining the benefit]

**Comment l'utiliser**:
1. [Step]
2. [Step]

[Screenshot or GIF if applicable]

---

### Améliorations
- **[Feature]**: [What's better now]

### Corrections
- [Issue that was affecting customers]: Résolu

---

## À venir
Aperçu des prochaines fonctionnalités :
- [Upcoming feature] - [Expected timeframe]

## Besoin d'aide ?
- Documentation: [Link]
- Support: [Contact]
- Webinar de présentation: [Date/Link]
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

### Status Indicators

Use consistently:
- 🟢 On track / Good
- 🟡 At risk / Needs attention
- 🔴 Blocked / Critical
- ⏳ In progress
- ✅ Complete
- ❌ Cancelled/Blocked

### Writing Principles

1. **Lead with the ask**: What do you need from the reader?
2. **Front-load value**: Most important info first
3. **Be specific**: Dates, numbers, names
4. **Make it scannable**: Headers, bullets, bold key points
5. **Include next steps**: Who does what by when

---

## Soft Skills PM

Les compétences interpersonnelles qui font la différence au quotidien. Un PM passe plus de temps à négocier, convaincre et clarifier qu'à rédiger des PRDs.

### Leadership

Pas besoin d'être le plus visible. Le leadership PM, c'est :
- **Prendre la responsabilité** des décisions produit, même sans autorité hiérarchique
- **Guider les décisions** en apportant contexte, données et cadre d'analyse
- **Créer de la clarté** quand tout est flou — transformer l'ambiguïté en plan d'action

**En pratique chez Galigeo** : Quand un client retail demande 5 features en même temps, le PM structure la conversation autour de la valeur business et propose un séquencement argumenté.

### Négociation

Les PMs négocient en permanence — avec les stakeholders, les devs, et même avec eux-mêmes. C'est l'art d'équilibrer ce qu'on veut vs. ce qui est possible.

- **Avec les stakeholders** : Écouter le besoin derrière la demande. "Je veux un dashboard" signifie souvent "Je veux comprendre la performance de mon réseau"
- **Avec l'engineering** : Proposer des trade-offs (scope vs. timeline), pas des ultimatums
- **Avec soi-même** : Accepter que la roadmap parfaite n'existe pas — prioriser c'est renoncer

**En pratique chez Galigeo** : Arbitrer entre une demande C-Level (nouveau module stratégique) et un pain utilisateur terrain (UX d'export RetailFocus) en quantifiant l'impact de chaque option.

### Problem-Solving

Chaque jour amène un "ce n'était pas dans le plan". La rapidité à décomposer un problème et trouver un chemin praticable construit la confiance de l'équipe.

- **Décomposer** : Séparer le problème en sous-problèmes indépendants
- **Prioriser** : Identifier ce qui débloque le plus de valeur
- **Proposer** : Arriver avec des options, pas juste le problème
- **Itérer** : Première solution ≠ meilleure solution

**En pratique chez Galigeo** : Un bug critique sur le calcul d'isochrones avant une démo client → identifier l'impact, proposer un workaround immédiat, planifier le fix, communiquer au client.

### Communication

La moitié du rôle PM est de la traduction :
- **Vision → tâches** : Transformer une direction stratégique en items de backlog actionnables
- **Pain client → roadmap** : Convertir les retours terrain en opportunités produit priorisées
- **Objectifs leadership → métriques** : Traduire "on veut croître" en KPIs mesurables et actionnables

**Principes clés** :
- Adapter le niveau de détail à l'audience (cf. tableau Audience Adaptation ci-dessus)
- Une communication claire est ce qui permet de scaler l'alignement
- Préférer l'écrit pour les décisions, l'oral pour l'alignement émotionnel

**En pratique chez Galigeo** : Le même sujet (nouvelle feature de cannibalization analysis) se présente différemment au C-Level (impact sur le ROI réseau), au dev (spec technique + edge cases), et au client (bénéfice concret sur sa décision d'implantation).
