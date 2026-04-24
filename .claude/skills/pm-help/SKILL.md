---
name: pm-help
description: List available PM skills and recommend which one to use. Use when the user asks for PM help, what PM tools are available, which skill to use, or says /pm-help.
---

# PM Toolkit — Guide

## PM Skills

| Commande | Quand l'utiliser |
|----------|-----------------|
| `/pm-discovery` | Interview, feedback utilisateur, JTBD, problem statement, hypothèses |
| `/pm-strategy` | Strategy doc, roadmap, ROI, PRD, one-pager, priorisation, KPIs |
| `/pm-execution` | Spec feature, acceptance criteria (Gherkin), user stories, edge cases, handoff engineering |
| `/pm-communications` | Réunion (agenda/summary), status update, release notes, annonce stakeholder |
| `/pm-data-analytics` | SQL, analyse de données, rapport, dashboard, qualité des données |
| `/pm-revenue` | Revenue architecture, PLG↔SLG, bowtie CR1-CR8, LTV/CAC/NRR, SPICED, stades croissance |

## Design Skills (nouveau produit + travail avec designer)

| Commande | Quand l'utiliser |
|----------|-----------------|
| `/design-sprint` | Cadrer plusieurs jours de design (framing → diverge → decide → prototype → test), orchestration BMAD + /ux |
| `/design-ia` | Information architecture, user flows, navigation, mental models, hiérarchie d'info, Nielsen heuristics |
| `/design-craft` | Visual craft : typo, color, spacing, hiérarchie visuelle, microinteractions, responsive, dark mode |
| `/design-system` | Tokens, composants, naming, DESIGN.md handoff, versioning du DS |
| `/design-review` | Critique structurée, heuristic evaluation, audit a11y, pre-merge quality gate, tests légers |
| `/design-psychology` | 106 biais cognitifs, Hook Model, Fogg, mental models, persuasion éthique |

## Comment choisir

```
Que fais-tu en ce moment ?
│
├── Feedback utilisateur, interviews, JTBD
│   → /pm-discovery
│
├── Stratégie, PRD, roadmap, priorisation
│   → /pm-strategy
│
├── Spec pour les devs
│   → /pm-execution
│
├── Réunion, update, release notes
│   → /pm-communications
│
├── SQL, rapport, dashboard
│   → /pm-data-analytics
│
├── Décision revenue (pricing, PLG/SLG, ICP, expansion)
│   → /pm-revenue
│
├── Je démarre un produit / une feature complexe → je dois cadrer les jours de design
│   → /design-sprint
│
├── Je travaille sur la STRUCTURE (flows, nav, hiérarchie d'info)
│   → /design-ia
│
├── Je travaille sur la QUALITÉ VISUELLE d'un mockup
│   → /design-craft
│
├── Je construis / fais évoluer le design system
│   → /design-system
│
├── Je review un design (critique, a11y, quality gate, pre-merge)
│   → /design-review
│
└── Je cherche les bons biais à actionner (onboarding, pricing, retention…)
    → /design-psychology
```

## Knowledge Base (chargée à la demande par les skills)

| Ressource | Contenu | Utilisé par |
|-----------|---------|-------------|
| `knowledge/design/` | 15 fiches distillées + 5 fiches biais Growth.design | design-* |
| `knowledge/pm-course/` | Modules PRD, data analysis, product strategy | pm-strategy, pm-data-analytics |
| `knowledge/revenue/` | Leadership du revenu — 5 sessions, 6 frameworks, bowtie WbD, PLG↔SLG | pm-revenue |

## BMAD (workflows structurés)

Pour des workflows plus lourds (brainstorming, review éditoriale, multi-agent), utilise les commandes BMAD : `/bmad-help` pour voir ce qui est disponible.
