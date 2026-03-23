# AI UX Workflow

## Purpose
Guide for PM to orchestrate AI-driven UX design using BMAD (v6.0.0-Beta.8) + Claude `/ux` skill.

## Decision Framework: When to Use What

### Task Suitability Matrix

| Task | Tool | Risk Level | Output Expected |
|------|------|------------|-----------------|
| New epic (full UX from scratch) | BMAD → /ux review | High | UX spec, personas, journeys, wireframes, reviewed mockups |
| Feature iteration (existing flow) | /ux topic + review | Medium | Guidance + review checklist |
| Component build (single element) | /ux topic | Low | Component specs, states, a11y |
| Mockup review (BMAD output) | /ux review | Medium | Issues list, fixes, a11y audit |
| Pre-merge (code review) | /ux review | High | Quality gate pass/fail |
| Quick experiment (throwaway) | Solo PM | Low | Sketch, no formal review needed |

### Decision Tree: Solo vs. Full Review

```
La décision est-elle réversible ?
├── OUI → PM solo ou /ux topic suffit
│   └── Exemples : couleur de bouton, libellé, espacement
└── NON → Pipeline complet (BMAD + /ux review)
    └── Exemples : nouveau flow, navigation, architecture d'info
        └── Coût de la mauvaise interprétation ?
            ├── FAIBLE → /ux review seul
            └── ÉLEVÉ → BMAD spec + /ux review + test utilisateur
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

## Problème
**[Persona]** rencontre **[problème]** quand **[contexte]**,
ce qui cause **[impact mesurable]**.

## Job to Be Done
**Quand** [situation]
**Je veux** [action]
**Pour pouvoir** [résultat attendu]

## Métriques de succès
| Métrique | Actuel | Cible |
|----------|--------|-------|
| [KPI]    | [val]  | [val] |

## Contraintes
- [ ] Mobile-first requis
- [ ] Accessibilité WCAG AA
- [ ] Cohérence avec le design system existant
- [ ] Performances (temps de chargement < X sec)

## Références
- PRD : [lien]
- Données discovery : [lien]
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

## Scope demandé
- [ ] Personas utilisateur
- [ ] User journeys
- [ ] Wireframes (desktop + mobile)
- [ ] Design tokens (couleurs, typo, espacements)
- [ ] Spécification d'interactions
- [ ] Architecture de l'information

## Contraintes design
- **Design system** : [référence au DS existant]
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

- [ ] **Accessibilité** : contraste, navigation clavier, lecteur d'écran, focus visible
- [ ] **Touch targets** : minimum 44×44px sur mobile, espacement suffisant
- [ ] **Contraste** : ratio 4.5:1 texte normal, 3:1 grand texte (WCAG AA)
- [ ] **États d'interaction** : hover, focus, active, disabled, loading, error, empty
- [ ] **Mobile** : viewport, clavier virtuel, orientation, safe areas
- [ ] **Formulaires** : labels, erreurs inline, autocomplete, validation timing
- [ ] **Feedback** : loading states, confirmations, messages d'erreur clairs
- [ ] **Cohérence** : alignement avec le design system et les patterns existants

#### Template: Review Request

```markdown
# Demande de review /ux

## Fichiers à reviewer
- `_bmad-output/design-mockups/[feature]/index.html`
- `_bmad-output/design-mockups/[feature]/mobile.html`

## Contexte
- Feature : [nom]
- PRD : [chemin]
- Spec BMAD : [chemin]

## Points d'attention spécifiques
- [Zone à risque identifiée]
- [Décision de design à valider]

## Commande
/ux review [chemin vers fichier]
```

### Phase 4: Implementation Guidance (/ux)

Use `/ux` topic mode for component-level guidance during development.

#### Topic Selection by Component Type

| Composant à construire | Commandes /ux | Guidance obtenue |
|------------------------|---------------|------------------|
| Login / signup | `/ux forms` + `/ux accessibility` | Timing validation, types d'input, autocomplete, placement erreurs |
| Dashboard | `/ux navigation` + `/ux components` | Patterns nav, wayfinding, états composants |
| Map viewer | `/ux interaction` + `/ux mobile` | Feedback interactions, gestes tactiles, viewport |
| Data tables | `/ux components` + `/ux accessibility` | Tri, pagination, responsive, lecteur d'écran |
| Formulaires complexes | `/ux forms` + `/ux interaction` | Multi-step, sauvegarde auto, undo |
| Notifications / alerts | `/ux interaction` + `/ux accessibility` | Timing, persistance, ARIA live regions |

#### Template: Implementation UX Request

```markdown
# Guidance UX pour implémentation

## Composant
**Type** : [formulaire / tableau / navigation / carte / ...]
**Feature** : [nom de la feature]
**Spec BMAD** : [chemin vers la spec]

## Questions UX spécifiques
1. [Question sur le comportement attendu]
2. [Question sur les états edge case]
3. [Question sur le responsive]

## Commandes /ux à exécuter
- /ux [topic1] — pour [raison]
- /ux [topic2] — pour [raison]
```

### Phase 5: Pre-Ship Review (/ux)

Run `/ux` review on changed files before merge. Quality gate — no merge without pass.

#### Quality Gate Checklist

```markdown
# Quality Gate UX — Pré-merge

## Feature : [nom]
## PR : [lien]
## Date : [date]

### Critères obligatoires (bloquants)
- [ ] Contraste WCAG AA vérifié sur tous les textes
- [ ] Navigation clavier fonctionnelle (tab, enter, escape)
- [ ] Touch targets ≥ 44px sur mobile
- [ ] États d'erreur présents et clairs
- [ ] Loading states pour toutes les actions async
- [ ] Pas de texte tronqué sans indication (tooltip, expand)

### Critères recommandés (non-bloquants)
- [ ] Animations respectent `prefers-reduced-motion`
- [ ] Empty states informatifs et actionnables
- [ ] Feedback optimiste là où pertinent
- [ ] Undo disponible pour les actions destructives
- [ ] Labels de formulaires liés aux inputs (for/id)

### Résultat
- **Pass** : Tous les critères obligatoires cochés
- **Fail** : Critère(s) obligatoire(s) manquant(s) → lister les fixes requis
```

## The "Cost of Misinterpretation" Test

Before any UX decision, run this assessment.

### Template: Risk Assessment

```markdown
# Évaluation risque UX

## Décision : [description de la décision UX]

### 1. Réversibilité
- [ ] Facilement réversible (changement CSS, libellé) → Risque faible
- [ ] Modérément réversible (nouveau composant, flow alternatif) → Risque moyen
- [ ] Difficile à reverser (architecture info, modèle mental, navigation) → Risque élevé

### 2. Coût de la mauvaise interprétation
- **Si on se trompe, que se passe-t-il ?**
  - Impact utilisateur : [description]
  - Impact business : [description]
  - Coût de correction : [estimation T-shirt]

### 3. Décision
| Risque | Action |
|--------|--------|
| Faible | PM décide seul, /ux topic si besoin |
| Moyen  | /ux review obligatoire |
| Élevé  | Pipeline complet + test utilisateur |
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
1. Quel est l'objectif principal de cet écran ?
2. Quelle action feriez-vous en premier ?
3. Qu'avez-vous remarqué en premier ?

## Résultats
| Participant | Q1 (objectif compris ?) | Q2 (CTA identifié ?) | Q3 (hiérarchie ok ?) |
|-------------|------------------------|----------------------|---------------------|
| P1          | Oui / Non              | Oui / Non            | [Élément]           |

## Verdict
- ≥ 4/5 comprennent l'objectif → OK
- < 4/5 → Revoir la hiérarchie visuelle
```

### Hallway Test

```markdown
# Test couloir

## Tâche
"Imagine que tu veux [job to be done]. Montre-moi comment tu ferais."

## Observations (3-5 personnes, 5 min chacune)
| Participant | Réussite | Temps | Hésitations | Commentaires |
|-------------|----------|-------|-------------|-------------|
| P1          | Oui/Non  | Xs    | [Où]        | "[Verbatim]"|

## Patterns identifiés
- [Pattern récurrent]
- [Point de friction commun]
```

### Support Ticket Mining

```markdown
# Mining tickets support

## Période : [dates]
## Feature analysée : [nom]

### Catégorisation
| Catégorie UX | Nb tickets | % total | Exemples verbatim |
|-------------|------------|---------|-------------------|
| Navigation  | n          | %       | "[quote]"         |
| Formulaire  | n          | %       | "[quote]"         |
| Compréhension | n       | %       | "[quote]"         |
| Performance | n          | %       | "[quote]"         |

### Top 3 problèmes UX
1. [Problème] → [Recommandation]
2. [Problème] → [Recommandation]
3. [Problème] → [Recommandation]
```

### Session Recording Review

```markdown
# Review enregistrements sessions

## Outil : [Hotjar / FullStory / ...]
## Période : [dates]
## Écrans analysés : [liste]

### Observations
| Écran | Comportement observé | Fréquence | Problème UX suspecté |
|-------|---------------------|-----------|---------------------|
| [Écran] | [Comportement] | n/N sessions | [Hypothèse] |

### Heatmap Insights
- **Zones cliquées ignorées** : [éléments non-interactifs cliqués]
- **CTA ignorés** : [boutons non cliqués]
- **Scroll drop-off** : [% qui ne scrollent pas au-delà de X]

### Actions
- [ ] [Action corrective avec priorité]
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

- [ ] Problème défini avant le design (PRD existe)
- [ ] Spec UX générée par BMAD à partir du PRD
- [ ] Review /ux effectuée sur les mockups
- [ ] Guidance /ux `<topic>` fournie pour chaque composant
- [ ] Review /ux pré-merge sur le code final
- [ ] Test utilisateur léger réalisé (si décision irréversible)
