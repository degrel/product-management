---
name: design-review
description: Critique structurée et quality gate — heuristic evaluation, accessibility audit, design critique, pre-merge review, lightweight user testing. Use when reviewing mockups or implemented UI, running Nielsen heuristic eval, auditing WCAG compliance, writing constructive design critique, validating a design before dev handoff, gating a merge on UX quality, or running 5-second / hallway / support mining tests. Covers severity scoring, accessibility test plan, critique templates, quality gate, and lightweight test protocols. For making the design in the first place, see design-craft + design-ia.
---

# Design Review & Quality Gate

## Purpose
Décider si un design est **prêt à shipper**, avec un process répétable et non-biaisé. Ce skill répond à "qu'est-ce qui cloche" et "peut-on merger".

## Knowledge base (load on demand)

Fiches distillées dans `knowledge/design/`.

| Besoin | Fichier |
|---|---|
| Nielsen 10 heuristics + severity scoring | `heuristics.md` |
| WCAG AA pratique, keyboard, screen reader, outils | `accessibility.md` |
| Templates de critique structurée | `critique-templates.md` |
| Méthodes tests légers (5-sec, click, hallway, mining, usability) | `testing-methods.md` |
| Les 7 états à vérifier | `states.md` |
| Biais à surveiller dans la critique | `psychology-map.md` |
| Lint DESIGN.md (quality gate token-level) | `design-md-workflow.md` |

## Trois modes de review

Choisir en fonction du momentum :

| Mode | Quand | Durée | Output |
|---|---|---|---|
| **Heuristic eval** | Mockup solo ou prototype statique | 45-60 min | Issues list avec severity |
| **Design critique** | Entre designers/PMs, collaboratif | 30-45 min | Feedback structuré, décisions |
| **Pre-merge quality gate** | Feature implémentée, avant merge | 20-30 min | Pass / Fail avec fixes requis |

Tests utilisateurs légers (5-second, hallway, support mining) = *complémentaires*, ne remplacent pas les 3 ci-dessus.

## 1. Heuristic evaluation (Nielsen + Norman)

Méthode : 1-3 évaluateurs indépendants parcourent l'interface avec la checklist, notent chaque violation avec severity, puis consolident.

### Les 10 heuristiques — scoring

Pour chaque heuristique, noter **chaque écran** de 0 à 3 :
- 0 = violation grave
- 1 = partiellement problématique
- 2 = OK
- 3 = exemplaire

| # | Heuristique | Question |
|---|---|---|
| 1 | Visibility of system status | L'utilisateur sait-il ce qui se passe ? |
| 2 | Match real world | Termes et concepts familiers ? |
| 3 | User control & freedom | Undo, back, escape ? |
| 4 | Consistency & standards | Cohérent avec le reste du produit et les standards du web ? |
| 5 | Error prevention | Validation avant l'erreur ? |
| 6 | Recognition > recall | Options visibles plutôt que mémorisées ? |
| 7 | Flexibility & efficiency | Raccourcis pour power users ? |
| 8 | Aesthetic & minimalist | Chaque élément nécessaire ? |
| 9 | Recover from errors | Erreurs actionnables ? |
| 10 | Help & documentation | Aide contextuelle ? |

### Severity d'un problème

| Sev | Label | Exemple | Action |
|---|---|---|---|
| 0 | Non-problème | "Un peu moins joli ici" | Ignorer |
| 1 | Cosmetic | Bouton un peu trop petit | Backlog |
| 2 | Minor | Label pas assez clair | Sprint suivant |
| 3 | Major | Flow confus, 30% des users bloqués | **Bloque le ship** |
| 4 | Catastrophic | Perte de données, inaccessible | **Bloque le ship** |

### Template — Heuristic evaluation report

```markdown
# Heuristic Evaluation — [feature / screen]

**Évaluateur** : [nom] • **Date** : [date] • **Build** : [version / link]

## Scope
- Écrans évalués : [liste]
- Hors scope : [liste]
- Persona référence : [nom]

## Summary scoring
| Heuristique | Score global /3 | Principales violations |
|-------------|----------------|------------------------|
| 1. System status | 2 | Loading invisible au Step 2 |
| 2. Match real world | 3 | — |
| 3. User control | 1 | Impossible d'annuler la création |
| ...

## Issues
### 🔴 Sev 4 — Catastrophic (ship blockers)
| # | Description | Location | Fix proposé |
|---|-------------|----------|-------------|
| 1 | [...] | [...] | [...] |

### 🟠 Sev 3 — Major (ship blockers)
...

### 🟡 Sev 2 — Minor
...

### 🔵 Sev 1 — Cosmetic
...

## Recommandations prioritaires
1. [Sev 4 #1] → owner, deadline
2. [Sev 3 #1] → owner, deadline
3. [Sev 3 #2] → owner, deadline

## Pass criteria
- [ ] Aucun Sev 4
- [ ] 0 ou 1 Sev 3 (avec mitigation documentée)
- [ ] Sev 2 : plan d'itération dans la release suivante
```

## 2. Design critique (collaborative)

Objectif : faire émerger des idées sans démolir la personne. Ne pas confondre critique et feedback non structuré.

### Règles de la critique

1. **Présentation silencieuse** (5 min) : le designer/PM présente le brief, pas encore le design. But : aligner le groupe sur le problème.
2. **Critique séparée du brief** : on ne critique pas "la couleur", on critique **est-ce que ce choix sert le brief**.
3. **Pas de "je ferais" / "moi j'aime"** : remplacer par "ce choix permet-il [objectif] ?"
4. **Observations avant suggestions** : noter ce qui se passe, puis pourquoi, puis quoi changer.
5. **Le designer écoute** — ne défend pas. Questions de clarification OK, pas de justification.

### Template — Critique feedback

```markdown
# Design Critique — [feature]
**Designer/PM** : [nom] • **Date** : [date] • **Participants** : [n personnes]

## Brief rappelé
- Problème : [...]
- Persona : [...]
- JTBD : [...]
- Success criteria : [...]

## What works well
- [Observation] : [Pourquoi ça sert le brief]
- ...

## What doesn't work (yet)
### Must fix (bloquants)
| Observation | Location | Rationale | Proposition |
|-------------|----------|-----------|-------------|
| [...] | [...] | [En quoi ça casse le brief] | [Option A / B] |

### Should consider
| Suggestion | Location | Bénéfice attendu |
|------------|----------|------------------|
| [...] | [...] | [...] |

## Open questions
- [Question pour laquelle on manque d'info] → [research à faire]

## Decisions & next steps
- [ ] [Action] — [owner] — [date]
- [ ] [Action] — [owner] — [date]
```

## 3. Pre-merge quality gate

Appliquer **avant chaque merge** d'un PR touchant l'UI. Bloquant.

### Quality gate automatisé : `lint` du DESIGN.md

Si le projet a un `DESIGN.md`, lancer le linter Google **avant** la review humaine. Il détecte des classes d'erreurs que l'œil rate.

```bash
npx -y @google/design.md lint DESIGN.md
```

Politique de gate :

| Sévérité linter | Politique |
|---|---|
| `error` (broken-ref) | **Bloque le merge** — référence cassée = composant impossible à styler. |
| `warning` (contrast-ratio) | **Bloque le merge** sauf justification écrite (texte décoratif, etc.). |
| `warning` (orphaned-tokens, missing-primary, missing-typography, section-order) | À traiter dans la review, pas bloquant en soi. |
| `info` (token-summary, missing-sections) | Information, pas d'action obligatoire. |

Les 7 règles couvertes : `broken-ref`, `missing-primary`, `contrast-ratio` (WCAG AA 4.5:1), `orphaned-tokens`, `missing-typography`, `section-order`, `missing-sections`, `token-summary`. Détail dans `knowledge/design/design-md-workflow.md`.

Bonus régression : si le PR modifie `DESIGN.md`, comparer avec la version `main` pour bloquer les régressions involontaires :

```bash
git show main:DESIGN.md > /tmp/DESIGN.before.md
npx -y @google/design.md diff /tmp/DESIGN.before.md DESIGN.md
```

Le flag `regression: true` dans la sortie = ship blocker.



```markdown
# Quality Gate UX — Pre-merge

**Feature** : [nom] • **PR** : [lien] • **Date** : [date] • **Reviewer** : [nom]

## Critères obligatoires (bloquants)

### Accessibilité
- [ ] Contraste WCAG AA sur tous les textes (4.5:1 / 3:1 pour large)
- [ ] Navigation clavier complète (tab, shift+tab, enter, esc)
- [ ] Focus ring visible, contraste ≥ 3:1
- [ ] Screen reader : chaque élément interactif a un label
- [ ] Pas de texte en image (SVG OK avec `<title>`)
- [ ] `aria-live` pour les contenus dynamiques importants

### Touch / Mobile
- [ ] Touch targets ≥ 44×44 px
- [ ] Viewport configuré, pas de zoom bloqué
- [ ] Fonctionne en portrait et paysage
- [ ] Safe areas respectées (notch, home bar)

### États
- [ ] Loading states pour chaque action async > 300 ms
- [ ] Error states : message clair + recovery
- [ ] Empty states : 1re utilisation vs post-suppression distincts
- [ ] Pas de texte tronqué sans indication (tooltip / expand)

### Microcopy
- [ ] Pas de terme technique interne visible
- [ ] CTAs sont des verbes d'action ("Enregistrer" pas "OK")
- [ ] Messages d'erreur expliquent le quoi + le comment-fixer
- [ ] Cohérence terminologique (pas "delete" ici, "supprimer" là)

### Data
- [ ] 0 items, 1 item, N items (N très grand) testés
- [ ] Noms longs, data manquante, erreur API — tous gérés
- [ ] Formats nombres, dates, devises — localisés

## Critères recommandés (non-bloquants, mais à tracker)
- [ ] `prefers-reduced-motion` respecté
- [ ] Feedback optimiste là où pertinent
- [ ] Undo pour les actions destructives
- [ ] Labels liés aux inputs (`for`/`id`)
- [ ] Test `tabindex` : pas de piège clavier
- [ ] Analytics events en place

## Résultat
- [ ] **Pass** — tous les critères obligatoires OK
- [ ] **Fail** — lister les critères manquants ci-dessous

### Si Fail : fixes requis
1. [...]
2. [...]

### Commentaire reviewer
[Notes libres]
```

## 4. Accessibility audit dédié

Quand lancer un audit a11y complet :
- Première mise en prod d'une feature centrale
- Refonte majeure
- Demande d'accessibilité client
- Pré-audit externe (RGAA, WCAG)

### Checklist WCAG AA essentielle

```markdown
## Perceivable
- [ ] Alt text sur toutes images porteuses d'info
- [ ] Captions / transcript sur vidéos
- [ ] Contraste 4.5:1 (texte) / 3:1 (UI / texte large)
- [ ] Info pas véhiculée par couleur seule (icône + texte)

## Operable
- [ ] Tout le produit navigable au clavier
- [ ] Pas de piège clavier
- [ ] Skip links pour contenu principal
- [ ] Timing ajustable (session timeout, animations)
- [ ] Pas de flash > 3× / seconde

## Understandable
- [ ] Langue de la page déclarée (`<html lang="fr">`)
- [ ] Focus prévisible, pas de redirection inattendue
- [ ] Erreurs identifiées + suggestion de correction
- [ ] Labels et instructions sur les inputs

## Robust
- [ ] HTML valide, pas d'ID dupliqués
- [ ] ARIA utilisé correctement (rôles, états)
- [ ] Composants custom exposent leur état aux AT
```

Outils recommandés :
- **axe DevTools** (navigateur) — audit automatique, catch ~30% des problèmes
- **Lighthouse** — accessibility score + perf
- **VoiceOver (macOS) / NVDA (Windows)** — test screen reader manuel
- **Sim Daltonism** — vérifier palettes sous daltonisme
- **Keyboard-only** — débrancher la souris 30 min, tester le flow

## 5. Tests utilisateurs légers (< 1h)

### Test 5 secondes
- Montrer 5 s, masquer, questionner : (1) objectif ? (2) 1re action ? (3) vu en premier ?
- Critère : ≥ 4/5 comprennent l'objectif → hiérarchie OK.

### Click test (1re action)
- Montrer le mockup statique, demander "où cliqueriez-vous pour [tâche] ?"
- Capturer le 1er clic. Si > 30 % cliquent ailleurs que la CTA prévue → problème de signifier.

### Hallway test
- 3-5 personnes × 5 min. Tâche : "Imagine que tu veux [JTBD], montre-moi."
- Noter réussite, hésitations, verbatims. Patterns répétés ≥ 3/5 = à corriger.

### Support ticket mining
- 30-50 tickets récents catégorisés par type UX (nav, form, compréhension, perf).
- Top 3 catégories → top 3 priorités.

### Protocole rapide

```markdown
# Lightweight test — [feature]

**Type** : [5-sec / click / hallway / mining]
**Participants** : [n, profil]
**Date** : [date]

## Tâche / stimulus
[Ce qu'on leur présente, instructions]

## Observations
| P | Réussite | Temps | Hésitations | Verbatim clé |
|---|----------|-------|-------------|--------------|
| 1 | Oui | 15 s | Au step 2 | "[...]" |
| 2 | Non | — | Dès l'accueil | "[...]" |

## Patterns
- [Pattern récurrent] — n/N personnes
- [Pattern récurrent] — n/N personnes

## Décisions
- [ ] Corriger [problème] → [action]
- [ ] Creuser [flou] → [research à faire]
```

## Combinaison : quelle review pour quel moment

```
Idée → Sketch → Wireframe → Mockup HiFi → Prototype → Dev → Ship
             ▲            ▲             ▲           ▲
             │            │             │           │
         Hallway    Heuristic     Critique    Quality
         test       eval          collab      gate
         (5 min)    (45 min)      (30 min)    (20 min)
```

## Pitfalls du reviewer

| Pitfall | Symptôme | Fix |
|---|---|---|
| Design par comité | "On essaie de plaire à tout le monde" | Decider unique, critique ≠ vote |
| Subjectivité non avouée | "Je préfère le bleu" | Reformuler : "pourquoi le bleu sert mieux le brief ?" |
| Revue sans brief | On critique sans savoir le problème | Toujours rappeler le brief en intro |
| Sev inflation | Tout devient bloquant | Revenir à la grille Sev 0-4 objectivement |
| Ignorer l'a11y | "On verra plus tard" | Critère bloquant dès le Jour 1 |

## Checklist globale "prêt à ship"

- [ ] Heuristic eval passée, 0 Sev 4, ≤ 1 Sev 3 avec mitigation
- [ ] Design critique collaborative (≥ 1 pair)
- [ ] WCAG AA vérifié (axe + VoiceOver manuel)
- [ ] Quality gate pre-merge signée
- [ ] Au moins 1 test léger (5 s / hallway) ≥ 3 users
- [ ] Edge cases data (0, 1, N) vérifiés
- [ ] Analytics events en place
- [ ] Plan de mesure post-ship défini
