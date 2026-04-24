# Design Critique Templates

Critique ≠ feedback casual. Objectif : faire émerger de meilleures décisions, pas juger le designer.

## Règles de la critique

1. **Présenter le brief avant le design**. Le groupe doit comprendre le problème avant de juger la solution.
2. **Critiquer le choix, pas la personne.** "Ce choix sert-il le brief ?" ≠ "Je n'aime pas".
3. **Pas de "je ferais" ou "moi j'aime".** Reformuler : "Ce choix permet-il d'atteindre [objectif] ?"
4. **Observations avant suggestions.** Décrire, interpréter, puis proposer.
5. **Le designer écoute.** Questions de clarification OK. Pas de justification (c'est l'écouteur qui filtre).
6. **Time-box.** 30-45 min. Plus = fatigue et répétition.

## Format type (45 min, 4-6 participants)

| Phase | Durée | Activité |
|---|---|---|
| 1. Brief rappel | 5 min | Problème, persona, JTBD, success criteria |
| 2. Présentation silencieuse | 5 min | Designer présente, groupe regarde |
| 3. Observations | 10 min | "Je vois que...", "J'observe que..." (pas d'opinion encore) |
| 4. Critique constructive | 15 min | "Ce choix sert-il X ?", "Cette option répond-elle à Y ?" |
| 5. Open questions | 5 min | Ce qui manque d'info |
| 6. Décisions & actions | 5 min | Next steps, owner, date |

## Template feedback structuré

```markdown
# Design Critique — [feature]

**Date** : [date]
**Designer/PM** : [nom]
**Participants** : [n]

## Brief rappelé
- **Problème** : [...]
- **Persona** : [...]
- **JTBD** : [...]
- **Success criteria** : [...]
- **Contraintes** : [...]

## What works well
- [Observation] — [pourquoi ça sert le brief]
- [Observation] — [pourquoi ça sert le brief]

## What doesn't (yet) work

### Must fix (avant ship)
| # | Observation | Location | Rationale | Proposition |
|---|-------------|----------|-----------|-------------|
| 1 | [...]       | [...]    | [En quoi ça casse le brief] | [Option A / B] |
| 2 | [...]       | [...]    | [...] | [...] |

### Should consider
| Suggestion | Location | Bénéfice attendu |
|------------|----------|------------------|
| [...]      | [...]    | [...]            |

## Open questions
- [Question nécessitant plus d'info / research]

## Decisions & next steps
- [ ] [Action] — [owner] — [date]
- [ ] [Action] — [owner] — [date]
```

## Types de feedback à donner / refuser

### ✅ Bon feedback

- "Le CTA secondaire est plus visible que le primaire — est-ce intentionnel ?"
- "Je vois 3 actions possibles sur la card. Le persona doit-il choisir rapidement ?"
- "La hiérarchie m'amène d'abord au bouton de suppression. Est-ce l'action qu'on veut favoriser ?"
- "Ce copy est technique — match-il le vocabulaire du persona ?"
- "Cette icône évoque X pour moi. Est-ce le concept qu'on veut signaler ?"

### ❌ Feedback à refuser

- "Je n'aime pas le bleu." → pourquoi ? Lien avec le brief ?
- "Je ferais comme ça." → observation + rationale
- "On devrait faire comme [concurrent]." → quelle valeur ça apporte au persona ?
- "Peux-tu juste essayer X ?" → au designer de décider, après rationale
- "C'est moche." → 0 info, 100% agressif
- "Pourquoi tu n'as pas fait Y ?" → implique que Y est évident

## Designer en réception — protocole

1. **Ne pas se défendre.** Ecouter, prendre des notes.
2. **Questions de clarification uniquement.** ("Tu parles du CTA en haut ou du CTA inline ?")
3. **Ne jamais dire "oui mais...".** Remplacer par "Ok, noté, je te reviens avec une réponse".
4. **Après la critique**, prendre 24 h avant de décider quoi faire.

## Asynchrone (Slack / Figma comments)

Si la critique ne peut pas être en live, règles adaptées :

- Le designer poste : brief + mockup + questions spécifiques ("Est-ce que la hiérarchie marche ?").
- Les participants répondent dans un thread par question.
- Pas de dogpile : attendre 24 h avant de synthétiser.
- Decider final synthétise + tranche.

## Anti-patterns de critique

| Anti-pattern | Symptôme | Fix |
|---|---|---|
| Design par comité | "Essayons de plaire à tout le monde" | Decider unique, critique ≠ vote |
| Feedback en vrac | 40 commentaires sur Figma sans structure | Template structuré |
| Critique sans brief | On juge sans savoir le problème | Brief obligatoire en intro |
| Opinions personnelles | "Je préfère X" | Reformuler : "X sert mieux le brief parce que..." |
| Sandwich trop poli | "C'est super, mais... c'est super" | Observations factuelles + propositions |
| Designer qui justifie | Débat stérile | Écouter, noter, revenir à J+1 |

## Remote critique — bonnes pratiques

- **Partage d'écran** plutôt que lien Figma (tout le monde voit la même chose).
- **Un modérateur** qui time-box et coupe les dérapages.
- **Chat pour les observations** en parallèle (évite de couper la parole).
- **Enregistrer** si participants absents, transcrire les décisions.
- **Tools** : FigJam, Miro pour les annotations collectives.
