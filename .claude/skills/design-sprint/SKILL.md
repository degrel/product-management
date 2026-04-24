---
name: design-sprint
description: Cadrer et orchestrer plusieurs jours de design structurés — du problème flou au prototype testé. Use when framing a new product, planning design days, running a design sprint (GV-style), deciding between BMAD vs /ux vs manual design, choosing what to research before designing, structuring a discovery-to-delivery flow, or picking the right question for each day. Covers problem framing, Jobs-to-be-Done, Lean UX hypotheses, Opportunity Solution Trees, daily design agendas, and AI pipeline orchestration (BMAD + /ux). For IA/flow decisions inside a day, see design-ia. For visual craft on mockups, see design-craft.
---

# Design Sprint & Workflow Orchestration

## Purpose
Structurer les journées de design pour qu'elles produisent des décisions et pas du bruit. Ce skill répond à "par où commencer" et "quelle question on se pose aujourd'hui".

## Knowledge base (load on demand)

Fiches distillées dans `knowledge/design/`. Ouvrir uniquement celle nécessaire.

| Besoin | Fichier |
|---|---|
| Méthodes tests utilisateurs (5-sec, hallway, mining, JTBD interview, Mom Test) | `testing-methods.md` |
| Critique structurée, collaborative | `critique-templates.md` |
| Mental models, gulfs, framing du problème | `mental-models.md` |
| Psychology map (quels biais par scénario) | `psychology-map.md` |
| Hook Model complet (habit-forming, Fogg) | `hook-model.md` |

## Quand utiliser ce skill

Décide d'abord la nature du travail avant d'ouvrir Figma :

```
Décision réversible ?
├── OUI (libellé, couleur, composant isolé) → pas de sprint, aller direct en design-craft
└── NON (nouveau flow, IA, modèle mental)   → cadrer un mini-sprint
    │
    ├── Le problème est-il compris ?
    │   ├── NON → Jour Framing uniquement (voir Jour 1)
    │   └── OUI → Mini-sprint 2-3 jours (Framing léger + Diverge/Decide + Prototype)
    │
    └── Sprint complet 4-5 jours si :
        - Décision stratégique (nouveau produit, refonte nav)
        - Désaccord stakeholders
        - Coût de se tromper > coût de 5 jours bloqués
```

## Structure 5 jours (classique)

Adaptable en 3 ou 2 jours en compressant. Ne jamais sauter le Jour 1.

### Jour 1 — Understand / Frame the problem

**Question de la journée** : *Quel est le vrai problème, pour qui, et à quoi ressemble une victoire ?*

Livrables :
- [ ] Long-term goal (phrase unique : "Dans 2 ans, ...")
- [ ] Sprint questions (3-5 peurs formulées : "Peut-on... ?")
- [ ] User journey map haut niveau (persona → moment clé → système)
- [ ] Cible de sprint (1 persona + 1 étape du journey où on concentre l'effort)

Méthodes recommandées :
- **Expert interviews / HMW** : 15 min par expert interne, capture en "How Might We"
- **JTBD switch interview** si les utilisateurs existent (voir `skills-main/jobs-to-be-done`)
- **Opportunity tree** pour relier outcome → opportunités (voir `skills-main/continuous-discovery`)

Template — Brief de sprint :

```markdown
# Sprint brief: [nom]

## Long-term goal (2 ans)
[Phrase unique, ambitieuse mais plausible]

## Sprint questions (nos peurs)
1. Peut-on [résultat risqué] ?
2. Les utilisateurs vont-ils [comportement incertain] ?
3. Notre hypothèse [X] tient-elle ?

## Cible
- Persona : [une seule — le plus critique]
- Moment du journey : [une seule étape]
- JTBD : Quand [situation], je veux [action], pour [outcome]

## Success criteria
| Métrique | Aujourd'hui | Cible post-sprint |
|----------|-------------|-------------------|
| [KPI]    | [val]       | [val attendue]    |
```

### Jour 2 — Diverge / Sketch

**Question** : *Quelles sont les directions possibles, sans auto-censure ?*

- Lightning demos (15 min : 3-5 produits inspirants, pas forcément du même secteur)
- Notes individuelles (20 min, silence)
- Crazy 8s (8 croquis en 8 min, 1 par persona)
- Solution sketch (3 panneaux : contexte → moment clé → détail)

Règle : sketcher **seul** avant de parler. Le groupthink tue le jour 2.

### Jour 3 — Decide / Converge

**Question** : *Laquelle on teste ? Et pourquoi pas les autres ?*

- Art museum (sketches au mur, silence, heat map dots)
- Speed critique (3 min par sketch, la personne ne se défend pas)
- Straw poll → Decider vote (1 personne tranche)
- Storyboard 10-15 cases du flow à prototyper

Output : un storyboard unique, assez détaillé pour démarrer un prototype sans re-débat.

### Jour 4 — Prototype

**Question** : *Peut-on le tester demain ?*

Principe de la **façade réaliste** : seules les pages testées sont construites. Pas de back-end, pas de tous les états. Assez beau pour qu'un utilisateur y croie 10 minutes.

Répartition :
- Makers (Figma / HTML) : 2 personnes
- Stitcher : 1 personne qui relie les écrans
- Writer : microcopy
- Asset collector : logos, visuels

Voir `design-craft` pour la qualité visuelle et `design-system` pour les composants.

### Jour 5 — Test

**Question** : *Qu'est-ce qu'on a appris ?*

- 5 utilisateurs en 1-à-1, 45-60 min chacun
- Tâche non-dirigée : "Imagine que tu veux [JTBD], montre-moi"
- Le reste de l'équipe regarde dans une autre salle (ou Zoom) et note en silence
- Synthèse en fin de journée : patterns, surprises, décisions

Grille de synthèse :

```markdown
## Test résultats — [feature]

| Pattern observé | Nb users concernés | Décision |
|-----------------|--------------------|----|
| [Ex: bloquent sur écran de config] | 4/5 | Revoir IA avant dev |
| [Ex: passent direct en mode avancé] | 3/5 | Simplifier l'entrée |

### Décisions
- [ ] Build : [ce qu'on garde tel quel]
- [ ] Iterate : [ce qu'on modifie]
- [ ] Drop : [ce qu'on abandonne]
- [ ] Research more : [ce qu'on doit creuser]
```

## Variantes condensées

### Sprint 2 jours (itération sur existant)
- Jour 1 matin : Framing + Sprint question unique
- Jour 1 après-midi : Crazy 8s + décision
- Jour 2 matin : Prototype focus
- Jour 2 après-midi : 3 tests hallway + synthèse

### Sprint 3 jours (décision moyenne)
- J1 : Understand + Diverge
- J2 : Decide + Prototype
- J3 : Test + synthèse

## Orchestration AI : BMAD vs /ux vs solo

### Matrix de suitability

| Tâche | Outil | Sortie attendue |
|---|---|---|
| Nouveau epic (UX complet from scratch) | BMAD puis review `/ux` | Spec UX, personas, journeys, wireframes, mockups review |
| Itération feature (flow existant) | `/ux topic` + review | Guidance + checklist |
| Composant isolé | `/ux topic` | Specs composant, states, a11y |
| Review de mockups BMAD | `/ux review` | Issues list, fixes, audit a11y |
| Pre-merge (code) | `/ux review` | Quality gate pass/fail |
| Expérimentation jetable | Solo PM | Sketch, pas de review formelle |

### Pipeline complet (décision à fort enjeu)

```
Phase 1 — Problem definition (PM)
    └─> PRD ou brief (template ci-dessous)

Phase 2 — UX strategy (BMAD)
    └─> /bmad-bmm-create-ux-design
    └─> Output : spec + wireframes + tokens dans _bmad-output/

Phase 3 — Design review (/ux review)
    └─> Issues, a11y, fixes

Phase 4 — Implementation guidance (/ux topic)
    └─> /ux forms, /ux navigation, /ux interaction, /ux accessibility

Phase 5 — Pre-ship review (/ux review sur code)
    └─> Quality gate bloquant (voir design-review)
```

### Brief UX — template (Phase 1)

```markdown
# Brief UX : [nom feature]

## Problème
**[Persona]** rencontre **[problème]** quand **[contexte]**,
ce qui cause **[impact mesurable]**.

## Job to Be Done
Quand [situation], je veux [action], pour [outcome].

## Métriques de succès
| Métrique | Actuel | Cible |
|----------|--------|-------|
| [KPI]    | [val]  | [val] |

## Contraintes
- [ ] Mobile-first ?
- [ ] WCAG AA
- [ ] Cohérence design system
- [ ] Perf (< X s)

## Références
- PRD : [lien]
- Discovery : [lien]
- Feedback : [lien]
```

## Lightweight user testing (< 1h)

Intégrable dans n'importe quel sprint, même en solo.

### Test 5 secondes
- Montrer 5 s, masquer, demander : (1) objectif de l'écran ? (2) 1re action ? (3) qu'as-tu remarqué en premier ?
- ≥ 4/5 comprennent → hiérarchie OK, sinon retravailler.

### Hallway test
- 3-5 personnes × 5 min. Tâche : "Imagine que tu veux [JTBD], montre-moi."
- Noter : réussite oui/non, hésitations, verbatim.

### Support ticket mining
- Extraire 30-50 tickets récents, catégoriser par type UX (nav, form, compréhension, perf).
- Top 3 → recommandations.

## Framing anti-patterns

| Anti-pattern | Symptôme | Antidote |
|---|---|---|
| Sauter le Jour 1 | "On sait déjà le problème" mais 3 définitions coexistent | Forcer la HMW + la sprint question écrite |
| Commencer à dessiner en groupe | Une seule idée domine | Sketching silencieux obligatoire |
| Prototyper > 1 direction | Rien n'est assez fini pour tester | 1 storyboard, 1 prototype, 1 test |
| Tester sur des collègues | Biais, feedback poli | 5 vrais users externes minimum |
| Pas de décideur | Débat infini au Jour 3 | Nommer le Decider dès le Jour 1 |

## Checklist de clôture de sprint

- [ ] Sprint question répondue (oui/non/partiellement)
- [ ] Décisions listées : build / iterate / drop / research
- [ ] Prochaines actions assignées avec owner + date
- [ ] Artefacts archivés : brief, storyboard, prototype, notes de test
- [ ] Apprentissage documenté pour les prochains sprints
