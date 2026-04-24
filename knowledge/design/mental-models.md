# Mental Models — Norman distillé

> Source : *The Design of Everyday Things*, Don Norman.

Un mental model = la représentation interne qu'a l'utilisateur du fonctionnement d'un système. **Un bon design réduit l'écart entre son modèle mental et la réalité du système.**

## Les 6 principes fondamentaux

### 1. Affordance
Propriété d'un objet qui indique **comment** il peut être utilisé.
- Bouton qui ressemble à un bouton (relief, couleur, shape) → se clique
- Slider qui ressemble à un slider → se glisse
- Lien souligné → se clique

Règle : chaque élément interactif **signale** sa fonction sans devoir être expliqué.

### 2. Signifier
Indice perceptible de l'affordance.
- Curseur qui change sur hover
- Underline sur un lien
- Icon "pencil" à côté d'un champ éditable
- Texte "Cliquez pour éditer"

Difference : affordance = la possibilité, signifier = le signal de cette possibilité.

### 3. Constraint
Limitation qui empêche les mauvaises actions.
- **Physique** : impossible de taper une lettre dans un champ "number"
- **Culturel** : une croix rouge = supprimer (convention)
- **Logique** : bouton "Enregistrer" désactivé tant que le formulaire est invalide
- **Sémantique** : un champ "email" refuse ce qui n'est pas un email

### 4. Feedback
Retour visible de chaque action.
- Click → button press visible
- Save → confirmation + état persisté
- Error → message explicite
- Long-running → progression

Règle : **feedback < 100 ms** pour le sentiment de réactivité.

### 5. Mapping
Correspondance entre contrôles et effets.
- Curseur "volume" à droite = plus fort
- Flèche haut = scroll haut
- Ordre des boutons = ordre de workflow (Next à droite, Back à gauche en LTR)

Règle : **arrangement spatial = logique du système**.

### 6. Conceptual model
La métaphore générale que le design évoque.
- Desktop OS = "bureau avec dossiers et fichiers"
- Slack = "pièces de discussion"
- Spotify = "bibliothèque musicale"

Règle : choisir une métaphore familière. Inventer un modèle coûte 10× le temps d'apprentissage.

## Les 7 stages of action

```
╭─ GOAL : quoi je veux ?
│
├─ PLAN : comment ?
├─ SPECIFY : quelle action exacte ?
├─ PERFORM : faire
│
══════════════ système ══════════════
│
├─ PERCEIVE : voir le résultat
├─ INTERPRET : quel sens ?
╰─ COMPARE : ça correspond au goal ?
```

## Les 2 gulfs à réduire

### Gulf of execution
Écart entre **ce que l'utilisateur veut faire** et **ce que le système permet**.
- User veut "archiver ce mail" → doit faire glisser, mais pas de signifier pour ça = gulf élevé.
- Fix : affordances visibles, chemins courts, constraints qui empêchent les erreurs.

### Gulf of evaluation
Écart entre **ce qui se passe** et **ce que l'utilisateur comprend**.
- Mail disparaît → où est-il allé ? Archivé ? Supprimé ? Perdu ? = gulf élevé.
- Fix : feedback clair + état visible + undo.

## Application — diagnostic

Face à un design confus, diagnostiquer :

| Problème observé | Le plus probable : |
|---|---|
| "Je ne sais pas quoi faire" | Affordance / signifier manquant (gulf of execution) |
| "Je ne sais pas si ça a marché" | Feedback absent (gulf of evaluation) |
| "J'ai fait une mauvaise action" | Constraint absente |
| "Ça ne correspond pas à ce que je pensais" | Conceptual model incohérent |
| "Je ne trouve rien" | Mapping spatial faux |

## Métaphores : inventer vs réutiliser

| Critère | Réutiliser | Inventer |
|---|---|---|
| User l'a déjà vue ailleurs ? | Oui (Google, Apple, etc.) | Non |
| Coût d'apprentissage | Quasi-zéro | Élevé (tuto obligatoire) |
| Risque de mauvaise interprétation | Faible | Élevé |
| Contexte Galigeo (cartes, zones) | Google Maps, tableur, filtres | — |

Quand inventer justifiable : la métaphore existante crée des limites cognitives pires que le coût d'apprentissage (rare).

## Principes pratiques

- **Les 7 stages** : un mauvais design casse au moins un stage. Identifier lequel avant de redesigner.
- **Discoverability** : toutes les actions possibles doivent être visibles OU découvrables par exploration.
- **Forgiveness** : undo partout où les conséquences sont non-triviales. Double confirmation réservée à l'irréversible.
- **Consistency** : actions similaires → même comportement, même position, même mot.
