# Lightweight User Testing Methods

Protocoles rapides (< 1h chacun) pour valider un design sans budget research. Complémentaires, pas exclusifs.

## 5-Second Test

**Ce qu'on teste** : la hiérarchie visuelle et le message principal.

**Protocole** :
1. Montrer le mockup pendant exactement 5 secondes.
2. Masquer.
3. Poser 3 questions :
   - Quel est l'objectif principal de cet écran ?
   - Quelle action ferais-tu en premier ?
   - Qu'as-tu remarqué en premier ?

**Critère de succès** : ≥ 4/5 participants identifient l'objectif → hiérarchie OK.

**Erreurs courantes** :
- Montrer plus longtemps (annule le test)
- Demander "ça te plaît" (subjectif, inutile)
- Sur un mockup hi-fi alors qu'on veut tester la structure (utiliser wireframe low-fi)

## Click Test (First Click)

**Ce qu'on teste** : les signifiers, l'affordance de la CTA.

**Protocole** :
1. Montrer le mockup statique.
2. Énoncer la tâche : "Imagine que tu veux [JTBD]. Où cliquerais-tu ?"
3. Capturer le premier clic (Useberry, Maze, Optimal Workshop).
4. Ne pas commenter.

**Critère de succès** : ≥ 70% cliquent sur la CTA prévue.

**Si < 70%** : problème de signifier (bouton pas assez évident), de mapping (mauvaise position), ou de conceptual model (user ne comprend pas la métaphore).

## Hallway Test

**Ce qu'on teste** : un flow complet avec un prototype cliquable.

**Protocole** :
1. Attraper 3-5 personnes disponibles (collègues non-designers, vrais users externes si possible).
2. Énoncer la tâche : "Imagine que tu veux [JTBD]. Montre-moi comment tu ferais."
3. **Se taire**. Observer 5-10 min.
4. Ne pas aider. Noter où elles hésitent, où elles échouent.
5. À la fin, demander ce qu'elles ont trouvé difficile.

**Ce qu'on note** :
| Participant | Réussite | Temps | Hésitations | Verbatim clé |
|---|---|---|---|---|
| P1 | Oui | 2 min | Step 2 | "Je ne savais pas où cliquer" |

**Patterns** à chercher :
- Même erreur ≥ 3/5 personnes → bug structurel, corriger
- Même hésitation ≥ 3/5 → signifier manquant
- Verbatim récurrent → mots à intégrer dans le copy

**Qualité ≠ collègues** : un collègue qui connaît le produit est biaisé. Sortir de la bulle (LinkedIn, client, personne aléatoire).

## Support Ticket Mining

**Ce qu'on teste** : les problèmes réels déjà signalés.

**Protocole** :
1. Exporter 30-50 tickets récents (30 derniers jours typiquement).
2. Catégoriser par type UX :
   - Navigation (où est X ?)
   - Formulaire (comment remplir Y ?)
   - Compréhension (que signifie Z ?)
   - Performance / bug UX
3. Compter et ranger.
4. Top 3 catégories → top 3 priorités UX.

**Output** :

```markdown
## Support UX mining — [période]

### Tickets analysés : 47

| Catégorie | Nb | % | Verbatims clés |
|---|---|---|---|
| Navigation | 14 | 30% | "je ne trouve pas X", "comment accéder à Y" |
| Formulaire zone | 11 | 23% | "le champ rayon ne marche pas" |
| Compréhension résultats | 9 | 19% | "c'est quoi le chiffre du pourcentage" |
| ... | | | |

### Top 3 priorités
1. Repenser nav (30% tickets) — owner: PM, date: sprint X
2. Améliorer form zone (23%) — owner: designer, date: sprint X+1
3. Ajouter explications aux métriques (19%) — copy + tooltips
```

## 1-1 Interview (Discovery)

Pour comprendre le JTBD, pas un design. Protocole type Mom Test :

**Règles** :
- Parler **du passé concret**, pas des hypothèses ("La dernière fois que tu as fait X...")
- Parler **de leur vie**, pas de ta solution
- **Écouter** 80% du temps

**Questions** :
- Raconte-moi la dernière fois que tu as [JTBD].
- Qu'est-ce qui était frustrant ?
- Qu'est-ce que tu as essayé ?
- Quels outils tu as utilisés ? Pourquoi ceux-là ?
- Qu'est-ce qui te ferait gagner une heure par jour ?

**Erreurs** :
- Pitcher sa solution
- Demander "est-ce que tu utiliserais X" (réponse = du politesse)
- Accepter des opinions ("ce serait bien si...") sans valider par un comportement

Voir aussi : *The Mom Test* de Rob Fitzpatrick.

## Usability Test (modérée)

Plus lourd (45-60 min, 5 participants). À faire une fois par sprint important.

**Protocole** :
1. Recruter 5 participants (représentatifs du persona cible).
2. Session 45 min :
   - 5 min warm-up (qui es-tu, contexte)
   - 30 min tâches (3-5 tâches concrètes avec le prototype)
   - 10 min debrief (questions ouvertes)
3. Enregistrer (avec consentement), transcrire les verbatims.
4. Synthèse par patterns (même problème ≥ 3/5).

**Règles Nielsen** : 5 participants détectent ~85% des problèmes d'usabilité. Au-delà, ROI décroissant.

## Matrice : quelle méthode pour quel moment

| Moment | Méthode | Durée | Output |
|---|---|---|---|
| Sketch / wireframe | 5-sec test | 10 min | Hiérarchie valide |
| Mockup hi-fi | Click test | 20 min | CTA reconnue |
| Prototype cliquable | Hallway test | 30 min | Flow fonctionne |
| Post-launch | Support mining + 1-1 | 2-3 h | Backlog UX priorisé |
| Pré-PRD / discovery | JTBD interview | 45 min × 5 | Problem validé |
| Feature centrale | Usability test | 5× 45 min | Issues + décisions |

## Erreurs transverses

| Erreur | Conséquence | Fix |
|---|---|---|
| Tester avec des collègues uniquement | Bias | Sortir — user externe |
| Poser des questions leading ("C'est clair hein ?") | Feedback poli inutile | Ouvert + silence |
| Changer le prototype entre deux users | Comparaison impossible | Freeze pour la session |
| Aider quand l'user bloque | Annule le test | Observer, aider à la fin |
| Ignorer un user isolé | "Anecdote" | Si ≥ 1/5 bloque, creuser |
| Tester trop tard | Refonte coûteuse | Tester tôt et souvent |

## Template de debrief de test

```markdown
# Debrief test — [feature]

## Méthode : [5-sec / hallway / usability]
## Participants : [n, profil]
## Date : [date]

## Observations clés
| Pattern | Fréquence | Sévérité | Fix proposé |
|---|---|---|---|
| [...] | 4/5 | Major | [...] |

## Surprises
- [Ce qui n'était pas prévu]

## Verbatims marquants
- "[quote]" — P3
- "[quote]" — P1

## Décisions
- [ ] Corriger [X] avant ship — owner, date
- [ ] Creuser [Y] — research supplémentaire
- [ ] Abandonner [Z]
```
