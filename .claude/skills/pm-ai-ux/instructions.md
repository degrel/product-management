---
name: pm-ai-ux
description: AI-driven UX design pipeline using BMAD and /ux skill. Decision framework for when to use BMAD vs /ux, hybrid pipeline phases, lightweight user testing, quality gates. Use when orchestrating AI-assisted UX design, running design reviews, or planning UX workflows.
---

# AI UX Workflow

## Purpose
Guide for PM to orchestrate AI-driven UX design using BMAD (v6.3.0) + Claude `/ux` skill.

## Knowledge Base

For deeper methodology on AI agents and custom subagents, load on demand:
- **Agents**: `knowledge/pm-course/course-materials/lesson-modules/1.4-agents/`
- **Custom subagents**: `knowledge/pm-course/course-materials/lesson-modules/1.5-custom-subagents/`

## Decision Framework: When to Use What

### Task Suitability Matrix

| Task | Tool | Risk Level | Output Expected |
|------|------|------------|-----------------|
| New epic (full UX from scratch) | BMAD -> /ux review | High | UX spec, personas, journeys, wireframes, reviewed mockups |
| Feature iteration (existing flow) | /ux topic + review | Medium | Guidance + review checklist |
| Component build (single element) | /ux topic | Low | Component specs, states, a11y |
| Mockup review (BMAD output) | /ux review | Medium | Issues list, fixes, a11y audit |
| Pre-merge (code review) | /ux review | High | Quality gate pass/fail |
| Quick experiment (throwaway) | Solo PM | Low | Sketch, no formal review needed |

### Decision Tree: Solo vs. Full Review

```
La decision est-elle reversible ?
+-- OUI -> PM solo ou /ux topic suffit
|   +-- Exemples : couleur de bouton, libelle, espacement
+-- NON -> Pipeline complet (BMAD + /ux review)
    +-- Exemples : nouveau flow, navigation, architecture d'info
        +-- Cout de la mauvaise interpretation ?
            +-- FAIBLE -> /ux review seul
            +-- ELEVE -> BMAD spec + /ux review + test utilisateur
```

## The Hybrid Pipeline

### Phase 1: Problem Definition (PM)

PRD first, always. The PM owns the problem — AI owns the exploration.

**Input**: Business need, user pain point, or opportunity
**Output**: PRD ready for BMAD consumption
**Tool**: `/bmad-bmm-create-prd` or manual brief

#### Template: Problem Brief for UX

```markdown
# Brief UX: [Nom de la feature]

## Probleme
**[Persona]** rencontre **[probleme]** quand **[contexte]**,
ce qui cause **[impact mesurable]**.

## Job to Be Done
**Quand** [situation]
**Je veux** [action]
**Pour pouvoir** [resultat attendu]

## Metriques de succes
| Metrique | Actuel | Cible |
|----------|--------|-------|
| [KPI]    | [val]  | [val] |

## Contraintes
- [ ] Mobile-first requis
- [ ] Accessibilite WCAG AA
- [ ] Coherence avec le design system existant
- [ ] Performances (temps de chargement < X sec)

## References
- PRD : [lien]
- Donnees discovery : [lien]
- Feedback utilisateur : [lien]
```

### Phase 2: UX Strategy (BMAD)

**Commands**: `/bmad-bmm-create-ux-design`, `/bmad-agent-bmm-ux-designer`
**Input**: PRD from Phase 1
**Output**: UX spec, personas, journeys, wireframes, design tokens

#### Template: BMAD UX Design Request

```markdown
# Demande UX BMAD

## PRD Source
Fichier : [chemin vers PRD]

## Scope demande
- [ ] Personas utilisateur
- [ ] User journeys
- [ ] Wireframes (desktop + mobile)
- [ ] Design tokens (couleurs, typo, espacements)
- [ ] Specification d'interactions
- [ ] Architecture de l'information

## Contraintes design
- **Design system** : [reference au DS existant]
- **Plateforme** : Web / Mobile / Les deux
- **Standards** : WCAG AA minimum

## Output attendu
Dossier : `_bmad-output/design-mockups/[feature-name]/`
```

### Phase 3: Design Review (/ux)

Run `/ux` in review mode on BMAD mockups.

**Input**: BMAD-generated mockups (HTML files in `_bmad-output/design-mockups/`)
**Output**: Issues list with severity, fixes, a11y audit

#### Review Checklist

- [ ] **Accessibilite** : contraste, navigation clavier, lecteur d'ecran, focus visible
- [ ] **Touch targets** : minimum 44x44px sur mobile, espacement suffisant
- [ ] **Contraste** : ratio 4.5:1 texte normal, 3:1 grand texte (WCAG AA)
- [ ] **Etats d'interaction** : hover, focus, active, disabled, loading, error, empty
- [ ] **Mobile** : viewport, clavier virtuel, orientation, safe areas
- [ ] **Formulaires** : labels, erreurs inline, autocomplete, validation timing
- [ ] **Feedback** : loading states, confirmations, messages d'erreur clairs
- [ ] **Coherence** : alignement avec le design system et les patterns existants

### Phase 4: Implementation Guidance (/ux)

Use `/ux` topic mode for component-level guidance during development.

#### Topic Selection by Component Type

| Composant a construire | Commandes /ux | Guidance obtenue |
|------------------------|---------------|------------------|
| Login / signup | `/ux forms` + `/ux accessibility` | Timing validation, types d'input, autocomplete, placement erreurs |
| Dashboard | `/ux navigation` + `/ux components` | Patterns nav, wayfinding, etats composants |
| Map viewer | `/ux interaction` + `/ux mobile` | Feedback interactions, gestes tactiles, viewport |
| Data tables | `/ux components` + `/ux accessibility` | Tri, pagination, responsive, lecteur d'ecran |
| Formulaires complexes | `/ux forms` + `/ux interaction` | Multi-step, sauvegarde auto, undo |
| Notifications / alerts | `/ux interaction` + `/ux accessibility` | Timing, persistance, ARIA live regions |

### Phase 5: Pre-Ship Review (/ux)

Run `/ux` review on changed files before merge. Quality gate — no merge without pass.

#### Quality Gate Checklist

```markdown
# Quality Gate UX — Pre-merge

## Feature : [nom]
## PR : [lien]
## Date : [date]

### Criteres obligatoires (bloquants)
- [ ] Contraste WCAG AA verifie sur tous les textes
- [ ] Navigation clavier fonctionnelle (tab, enter, escape)
- [ ] Touch targets >= 44px sur mobile
- [ ] Etats d'erreur presents et clairs
- [ ] Loading states pour toutes les actions async
- [ ] Pas de texte tronque sans indication (tooltip, expand)

### Criteres recommandes (non-bloquants)
- [ ] Animations respectent `prefers-reduced-motion`
- [ ] Empty states informatifs et actionnables
- [ ] Feedback optimiste la ou pertinent
- [ ] Undo disponible pour les actions destructives
- [ ] Labels de formulaires lies aux inputs (for/id)

### Resultat
- **Pass** : Tous les criteres obligatoires coches
- **Fail** : Critere(s) obligatoire(s) manquant(s) -> lister les fixes requis
```

## The "Cost of Misinterpretation" Test

### Template: Risk Assessment

```markdown
# Evaluation risque UX

## Decision : [description de la decision UX]

### 1. Reversibilite
- [ ] Facilement reversible (changement CSS, libelle) -> Risque faible
- [ ] Moderement reversible (nouveau composant, flow alternatif) -> Risque moyen
- [ ] Difficile a reverser (architecture info, modele mental, navigation) -> Risque eleve

### 2. Cout de la mauvaise interpretation
- **Si on se trompe, que se passe-t-il ?**
  - Impact utilisateur : [description]
  - Impact business : [description]
  - Cout de correction : [estimation T-shirt]

### 3. Decision
| Risque | Action |
|--------|--------|
| Faible | PM decide seul, /ux topic si besoin |
| Moyen  | /ux review obligatoire |
| Eleve  | Pipeline complet + test utilisateur |
```

## Lightweight User Testing (Under 1 Hour)

### 5-Second Test

```markdown
# Test 5 secondes

## Setup
- Montrer le mockup pendant 5 secondes
- Masquer
- Poser les questions

## Questions
1. Quel est l'objectif principal de cet ecran ?
2. Quelle action feriez-vous en premier ?
3. Qu'avez-vous remarque en premier ?

## Resultats
| Participant | Q1 (objectif compris ?) | Q2 (CTA identifie ?) | Q3 (hierarchie ok ?) |
|-------------|------------------------|----------------------|---------------------|
| P1          | Oui / Non              | Oui / Non            | [Element]           |

## Verdict
- >= 4/5 comprennent l'objectif -> OK
- < 4/5 -> Revoir la hierarchie visuelle
```

### Hallway Test

```markdown
# Test couloir

## Tache
"Imagine que tu veux [job to be done]. Montre-moi comment tu ferais."

## Observations (3-5 personnes, 5 min chacune)
| Participant | Reussite | Temps | Hesitations | Commentaires |
|-------------|----------|-------|-------------|-------------|
| P1          | Oui/Non  | Xs    | [Ou]        | "[Verbatim]"|

## Patterns identifies
- [Pattern recurrent]
- [Point de friction commun]
```

### Support Ticket Mining

```markdown
# Mining tickets support

## Periode : [dates]
## Feature analysee : [nom]

### Categorisation
| Categorie UX | Nb tickets | % total | Exemples verbatim |
|-------------|------------|---------|-------------------|
| Navigation  | n          | %       | "[quote]"         |
| Formulaire  | n          | %       | "[quote]"         |
| Comprehension | n       | %       | "[quote]"         |
| Performance | n          | %       | "[quote]"         |

### Top 3 problemes UX
1. [Probleme] -> [Recommandation]
2. [Probleme] -> [Recommandation]
3. [Probleme] -> [Recommandation]
```

## Quick Reference: /ux Topics

| Building this? | Run this | Gets you |
|---|---|---|
| Forms, inputs, validation | `/ux forms` | Timing, input types, autocomplete, error placement |
| Mobile screens | `/ux mobile` | iOS bugs, touch targets, viewport, keyboard |
| Visual design | `/ux visual` | Color, typography, spacing, animation rules |
| Components | `/ux components` | States, patterns, anti-patterns per component |
| Navigation/IA | `/ux navigation` | Patterns, wayfinding, deep linking |
| Loading/feedback/flows | `/ux interaction` | Feedback timing, optimistic UI, undo vs confirm |
| Accessibility | `/ux accessibility` | WCAG AA, keyboard nav, screen reader, focus |
| Product decisions | `/ux product` | JTBD, prioritization, metrics, MVP vs MLP |

## Validation Checklist

- [ ] Probleme defini avant le design (PRD existe)
- [ ] Spec UX generee par BMAD a partir du PRD
- [ ] Review /ux effectuee sur les mockups
- [ ] Guidance /ux `<topic>` fournie pour chaque composant
- [ ] Review /ux pre-merge sur le code final
- [ ] Test utilisateur leger realise (si decision irreversible)
