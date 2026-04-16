---
name: pm-help
description: List available PM skills and recommend which one to use. Use when the user asks for PM help, what PM tools are available, which skill to use, or says /pm-help.
---

# PM Toolkit — Guide

## Available Skills

| Commande | Quand l'utiliser |
|----------|-----------------|
| `/pm-discovery` | Interview, feedback utilisateur, JTBD, problem statement, hypotheses |
| `/pm-strategy` | Strategy doc, roadmap, ROI, PRD, one-pager, prioritisation, KPIs |
| `/pm-execution` | Spec feature, acceptance criteria (Gherkin), user stories, edge cases, handoff engineering |
| `/pm-ux` | User flow, wireframe, UX copy, design review, biais cognitifs, accessibilite |
| `/pm-communications` | Reunion (agenda/summary), status update, release notes, annonce stakeholder |
| `/pm-data-analytics` | SQL, analyse de donnees, rapport, dashboard, qualite des donnees |
| `/pm-ai-ux` | Pipeline UX avec BMAD + /ux, decision framework, quality gate pre-merge |

## Comment choisir

```
Que fais-tu en ce moment ?
|
+-- J'analyse du feedback / des interviews
|   -> /pm-discovery
|
+-- Je redige une strategie, un PRD, ou je priorise
|   -> /pm-strategy
|
+-- Je prepare une spec pour les devs
|   -> /pm-execution
|
+-- Je travaille sur un ecran, un flow, du copy UX
|   -> /pm-ux
|
+-- Je prepare une reunion ou un update
|   -> /pm-communications
|
+-- Je fais du SQL, un rapport, un dashboard
|   -> /pm-data-analytics
|
+-- Je lance un design UX complet avec l'IA
|   -> /pm-ai-ux
```

## Knowledge Base (chargee a la demande par les skills)

| Ressource | Contenu | Utilise par |
|-----------|---------|-------------|
| `knowledge/ux-design/ux-psychology/` | 106 biais cognitifs UX (Growth.design) | pm-ux |
| `knowledge/ux-design/` | Progressive disclosure, articles UX | pm-ux |
| `knowledge/pm-course/` | Modules PRD, data analysis, product strategy | pm-strategy, pm-data-analytics, pm-ai-ux |

## References rapides

| Fichier | Contenu |
|---------|---------|
| `references/pm-fundamentals.md` | Glossaire PM, tech stack, career paths |
| `references/claude-power-user-checklist.md` | Checklist power user Claude Code |

## BMAD (workflows structures)

Pour des workflows plus lourds (brainstorming, review editoriale, multi-agent), utilise les commandes BMAD : `/bmad-help` pour voir ce qui est disponible.
