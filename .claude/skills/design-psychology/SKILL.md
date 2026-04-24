---
name: design-psychology
description: Psychologie appliquée au design — 106 biais cognitifs (Growth.design), Hook model, persuasion éthique, mental models, peak-end, goal gradient, Fogg behavior. Use when choosing persuasion levers, designing onboarding or pricing, debugging why users don't convert or don't return, picking between alternatives based on user psychology, adding ethical nudges, designing habit loops, or mapping biases by scenario (onboarding, pricing, forms, retention, trust). Covers 106 principles organized by category (information, meaning, time, memory), Hook Model (trigger/action/reward/investment), and Manipulation Matrix for ethics. For structural IA/flow, see design-ia. For visual craft, see design-craft.
---

# Design Psychology

## Purpose
Appliquer les principes de psychologie cognitive pour prendre des décisions de design motivées par **pourquoi les users font ce qu'ils font**, pas par le goût. Ce skill répond à "quel levier actionner" et "est-ce éthique".

## Knowledge base (load on demand)

Tout est dans `knowledge/design/`.

| Besoin | Fichier |
|---|---|
| **Mapping scénarios → biais (point d'entrée)** | `psychology-map.md` |
| **Index scénarios détaillés** (Growth.design) | `psychology/scenario-index.md` |
| Information biases (29) — Hick, Priming, Cognitive Load, Anchoring… | `psychology/information-biases.md` |
| Meaning biases (30) — Social Proof, Mental Model, Goal Gradient, Halo… | `psychology/meaning-biases.md` |
| Time biases (24) — Loss Aversion, Commitment, Default, Sunk Cost… | `psychology/time-biases.md` |
| Memory biases (23) — Peak-End, Zeigarnik, Chunking… | `psychology/memory-biases.md` |
| Hook Model complet (triggers, actions, rewards, investment) | `hook-model.md` |
| Mental models (Norman — 7 stages, gulfs) | `mental-models.md` |
| Progressive disclosure | `progressive-disclosure.md` |

## Workflow par scénario

Toujours commencer par **le scénario**, pas par le principe. Ouvrir `psychology/scenario-index.md`, trouver la ligne correspondante, charger 3-6 principes utiles.

### Scénarios couverts par l'index

| Scénario | Principes clés (extraits) |
|---|---|
| Onboarding | Progressive Disclosure, Cognitive Load, Aha moment, Zeigarnik, Priming |
| Pricing & Monetisation | Anchoring, Decoy Effect, Framing, Centre-Stage, Loss Aversion, Cashless |
| Checkout & Conversion | Hick, Fitts, Default Bias, Social Proof, Nudge, Spark Effect |
| Engagement & Retention | Variable Reward, Investment, Goal Gradient, Internal Trigger, Peak-End, Sunk Cost |
| Forms & Input | Cognitive Load, Chunking, Recognition>Recall, Tesler, Exit Points, Feedback |
| Navigation & IA | Mental Model, Signifiers, Proximity, Familiarity, Visual Hierarchy, Miller (7±2) |
| Trust & Credibility | Social Proof, Authority, Noble Edge, Halo |
| (+ autres : notifications, empty states, errors, pricing B2B, etc.) |

## Modèles fondateurs à maîtriser

### Hook Model (Nir Eyal)

Boucle d'habit-forming : `Trigger → Action → Variable Reward → Investment → (charge le prochain Trigger)`.

| Phase | Principe | Application |
|---|---|---|
| **Trigger** | Passer d'externes (notif, email) à internes (émotion) | Mapper produit à une émotion (ennui, FOMO, incertitude, solitude) |
| **Action** | Fogg : B = M × A × T, la motivation est volatile, l'ability est le levier | Réduire friction avant d'augmenter motivation |
| **Variable Reward** | Dopamine sur l'anticipation de l'incertain ; 3 types (Tribe, Hunt, Self) | Prévisibilité = perte d'engagement |
| **Investment** | IKEA effect + switching cost | Demander après reward, jamais avant |

Voir document complet dans `knowledge/design/SKILL.md`.

### Fogg Behavior Model — B = M × A × T

Un comportement n'arrive que si **les trois sont présents simultanément** :
- **Motivation** : veut-il le faire ? (plaisir/douleur, espoir/peur, acceptation/rejet)
- **Ability** : peut-il le faire facilement ? (temps, argent, effort physique, cycles cérébraux, déviance sociale, routine)
- **Trigger** : est-il invité au bon moment ?

Corollaire : *si un user ne fait pas X, une des trois manque*. Diagnostiquer avant de changer le design.

### 7 stages of action (Norman)

```
1. Goal (quoi je veux)
2. Plan (comment)
3. Specify (quelle action exacte)
4. Perform (faire)
─────── système ───────
5. Perceive (voir le résultat)
6. Interpret (sens)
7. Compare (conforme au goal ?)
```

Les deux gulfs à réduire :
- **Gulf of execution** : entre l'intention et ce qu'on peut faire dans l'UI (stages 1-4)
- **Gulf of evaluation** : entre le résultat et la compréhension de ce qui s'est passé (stages 5-7)

## Top principes transverses à appliquer systématiquement

### Cognitive Load (Sweller)

- **Intrinsic load** : complexité inhérente de la tâche. Irréductible mais décomposable.
- **Extraneous load** : complexité due à la présentation. **C'est ici qu'on travaille**.
- **Germane load** : effort productif pour apprendre. À préserver.

Règle : tout ce qui fait réfléchir sans ajouter de valeur = coupable.

### Hick's Law

Temps de décision ∝ log₂(nombre d'options).
- Réduire ≤ 7 choix par niveau.
- Regrouper, hiérarchiser, defaulter.
- Ne pas montrer 40 templates, en sélectionner 8 "recommended" + option "all".

### Fitts's Law

Temps pour cliquer ∝ distance × 1/taille.
- CTAs grands et proches de la zone de focus
- Mobile : FAB en bas (zone pouce)
- Desktop : primary en bas-droite d'un formulaire

### Miller's Law (7±2)

Mémoire de travail = 4-9 items. Concerne la mémoire active, pas le nombre de choix affichés.
- Chunker les informations (numéro tel : 06 12 34 56 78 > 0612345678)
- Tabs de nav ≤ 7
- Steps d'onboarding ≤ 5

### Peak-End Rule

Les gens retiennent : (a) le pic émotionnel et (b) la fin.
- Finir par un succès, un merci, une surprise positive
- Si le chemin est long, injecter des "peaks" positifs
- Corollaire : optimiser le dernier écran autant que le premier

### Goal Gradient

La motivation ↗ à mesure qu'on approche du but.
- Progress bar avec pas déjà complétés ("3/5 déjà fait, plus que 2")
- Stamp cards : commencer avec des cases pré-remplies
- Onboarding : afficher la progression dès la première étape

### Zeigarnik Effect

Les tâches inachevées restent en mémoire.
- Afficher les profils incomplets, les drafts non-finis
- Notifications "il te reste 1 étape" > "viens voir"
- Attention éthique : ne pas créer d'anxiété artificielle

### Anchoring

La première valeur perçue sert d'ancre.
- Pricing : afficher le plan le plus cher en premier
- Données : donner la référence ("moyenne du marché : 40 %") avant le chiffre individuel
- Biais pervers pour le user : être transparent

### Loss Aversion (Kahneman)

Perdre fait 2× plus mal que gagner.
- "Tu vas perdre ton historique" > "Sauvegarde ton historique"
- Trial : "Il te reste 3 jours" plutôt que "tu as eu X jours"
- Attention éthique : ne pas manufacturer une perte fictive

### Recognition Over Recall

Reconnaître est plus facile que se rappeler.
- Autocomplete > input vide
- Icons + labels > icons seuls
- Recents / favorites en plus du catalogue
- Dropdown avec search > typing exact

### Social Proof

Les actions des autres valident les nôtres.
- "12k utilisateurs ont choisi ce plan"
- Reviews, ratings, testimonials
- Usage : "34 personnes regardent ce produit" (si vrai)
- Attention : jamais fabriquer de preuve sociale

## Persuasion éthique — Manipulation Matrix

Cadre pour évaluer un choix de persuasion :

|   | **Maker uses it** | **Maker doesn't** |
|---|---|---|
| **Améliore la vie** | **Facilitator** ✅ | **Peddler** ⚠️ |
| **N'améliore pas** | **Entertainer** 🟡 | **Dealer** 🔴 |

3 questions avant d'ajouter un pattern persuasif :
1. Est-ce que je l'utiliserais moi ?
2. Est-ce que ça aide l'utilisateur à atteindre SON but ?
3. Est-ce que j'exploite une vulnérabilité ou je sers un besoin ?

Si Dealer/Peddler → changer l'approche.

## Dark patterns à éviter (et leurs alternatives)

| Dark pattern | Problème | Alternative éthique |
|---|---|---|
| Roach motel (facile d'entrer, dur de sortir) | Abonnements difficiles à résilier | 1-click cancel obligatoire |
| Confirmshaming ("Non merci, je déteste économiser") | Honte manufacturée | Bouton neutre |
| Disguised ads | Confondre ads et contenu | Label clair |
| Forced continuity | Trial qui se transforme silencieusement | Rappel J-3, opt-in explicite |
| Hidden costs | Coûts révélés au dernier step | Total affiché dès le début |
| Privacy Zuckering | Options privacy cachées | Defaults privacy-friendly |
| Bait and switch | Click mène ailleurs | Action = ce qui est annoncé |
| Urgency manufacturée | Faux compteurs, faux stocks | Urgency uniquement si réelle |

## Application : template de décision

```markdown
# Décision de design — [feature]

## Scénario
[Onboarding / Pricing / Checkout / Retention / etc.]

## Principes retenus (3-6)
1. **[Nom du biais]** — `[catégorie].md`
   - Ce qu'il prédit : [...]
   - Comment je l'applique ici : [...]
2. [...]

## Hypothèses éthiques
- Manipulation Matrix : Facilitator / Peddler / Entertainer / Dealer
- Je l'utiliserais moi ? Oui / Non
- Vulnérabilité exploitée ? Oui / Non

## Alternative(s) envisagée(s)
| Option | Principe | Pros | Cons |
|--------|----------|------|------|
| A      | [...]    | [...]| [...]|
| B      | [...]    | [...]| [...]|

## Décision
[Option retenue] — rationale : [...]

## Mesure
Comment saura-t-on que ça marche ?
- Métrique : [...]
- Cible : [...]
- Sinon, rollback.
```

## Traps classiques du PM-qui-veut-appliquer-la-psycho

| Trap | Symptôme | Fix |
|---|---|---|
| Empiler les principes | "J'ai mis du FOMO, du social proof, du loss aversion partout" | 3-6 max, focalisé sur LA bonne décision |
| Dark pattern "léger" | "C'est pas grave, tout le monde le fait" | Manipulation Matrix, si Dealer → stop |
| Anchoring au mauvais endroit | On ancre après la décision au lieu d'avant | Ancre = premier stimulus |
| Social proof fake | "9 personnes regardent ce produit" (jamais vrai) | Uniquement si exact, sinon contre-productif |
| Gamification plaquée | Badges sans lien avec la valeur | Reward = proxy d'un vrai accomplishment |
| Zeigarnik qui stresse | "Il te reste 47 choses à faire" | Formuler positivement, afficher la progression |

## Checklist application

- [ ] Scénario identifié (via `psychology/scenario-index.md`)
- [ ] 3-6 principes sélectionnés et compris (pas empilés)
- [ ] Manipulation Matrix passée, c'est un Facilitator
- [ ] Dark patterns vérifiés (rien de la liste ci-dessus)
- [ ] Alternative testée mentalement (pre-mortem)
- [ ] Métrique de succès définie pour mesurer l'effet
- [ ] Plan de rollback si contre-productif
