---
name: design-ia
description: Décisions de structure — information architecture, user flows, navigation, mental models, hiérarchie d'information. Use when deciding where a feature lives in the nav, designing a user flow, debating menu structure vs. contextual actions, resolving "users are confused" issues, applying Nielsen heuristics, or mapping mental models. Covers Norman's principles (affordances, signifiers, feedback, mapping), Nielsen's 10 heuristics, flow diagrams, progressive disclosure, and error-path design. For visual hierarchy on screen, see design-craft. For multi-day framing, see design-sprint.
---

# Information Architecture & Flow Decisions

## Purpose
Prendre les bonnes décisions **structurelles** avant d'ouvrir Figma : où vit une feature dans la nav, quel est le flow minimal, quels états l'utilisateur traverse, pourquoi il se perd.

## Knowledge base (load on demand)

Fiches distillées dans `knowledge/design/`.

| Besoin | Fichier |
|---|---|
| Nielsen 10 heuristics + severity scoring | `heuristics.md` |
| Norman (affordances, signifiers, gulfs, 7 stages) | `mental-models.md` |
| Microinteractions (triggers, rules, feedback, loops) | `microinteractions.md` |
| Les 7 états à dessiner (empty, loading, error…) | `states.md` |
| Progressive disclosure (P0/P1/P2) | `progressive-disclosure.md` |
| Psychology map (biais par scénario) | `psychology-map.md` |
| 106 biais détaillés par catégorie | `psychology/{information,meaning,time,memory}-biases.md` |

Démarrer par `psychology-map.md` + `psychology/scenario-index.md` pour mapper le contexte aux biais.

## Les 5 décisions structurelles

Avant tout écran, trancher ces 5 questions :

1. **Mental model** : quelle est la métaphore ? (dossier/fichier, tableau, carte, feed, tableau de bord…)
2. **Hiérarchie d'info** : quelle info est P0 (toujours visible) vs P1 (disclosed) vs P2 (settings) ?
3. **Navigation** : où vit la feature ? (top nav, side nav, contextuelle, flottante, par URL)
4. **Flow** : quel est le chemin minimal ? (nb d'étapes, décisions, retours en arrière possibles)
5. **États** : quels états l'utilisateur peut voir ? (empty, loading, error, partial, success, 0/1/N items)

## 1. Mental model

**Règle** : s'aligner sur un modèle que l'utilisateur connaît déjà. Inventer un nouveau modèle coûte 10× plus cher à enseigner qu'à éviter.

Template — Mental model check :

```markdown
## Mental model: [feature]

### Métaphore envisagée
[Ex: "une carte avec des pins" / "un feed chronologique" / "un tableau Excel"]

### Utilisateurs connaissent déjà ?
- [ ] Oui, dans notre produit (où ?)
- [ ] Oui, dans un autre outil (lequel ? Google Maps, Excel…)
- [ ] Non — invention

### Si invention, coût pédagogique
- [ ] Tutoriel obligatoire ?
- [ ] Mauvaise hypothèse va créer quel type d'erreur ?
- [ ] Peut-on se rabattre sur un modèle connu ?

### Cohérence interne
- [ ] Cette métaphore est-elle déjà utilisée ailleurs dans le produit ?
- [ ] Si oui, le comportement ici est-il cohérent ?
```

## 2. Hiérarchie d'information — Progressive disclosure

**Règle** : ce qui n'est pas P0 doit être masqué par défaut. L'UI est vide jusqu'à preuve du contraire.

| Niveau | Contenu | Exemples |
|---|---|---|
| **P0 — Always visible** | Ce dont 80% des users ont besoin 80% du temps | Titre, data principale, 1 CTA primaire |
| **P1 — On interaction** | Détails, configuration légère | Hover, click-to-expand, tabs, drawer |
| **P2 — On demand** | Power user, rare, config avancée | Settings, keyboard shortcuts, modal |

Template — Audit hiérarchie :

```markdown
## Hiérarchie — [écran]

| Élément | Niveau | Justification | Coût si mal placé |
|---------|--------|---------------|-------------------|
| [titre] | P0 | Répond à "où suis-je ?" | Confusion immédiate |
| [filtre temps] | P1 | Utilisé par 40% | Clic en plus, OK |
| [export CSV] | P2 | 5% power users | 2 clics en plus, OK |
```

Anti-pattern : **"just in case" UI** — ajouter un bouton parce qu'un stakeholder l'a demandé, sans évaluer la fréquence d'usage. Couper.

## 3. Navigation — où vit la feature ?

Arbre de décision :

```
La feature est-elle consultée régulièrement (≥ 1×/semaine par un user actif) ?
├── OUI → Primary nav (top / side)
│   └── Est-ce un mode d'activité distinct ou un sous-ensemble ?
│       ├── Mode distinct → top-level (ex: Territory Manager / RetailFocus)
│       └── Sous-ensemble → nested (ex: TM > Zones)
└── NON → Contextuelle
    ├── Liée à un objet ? → action sur cet objet (menu ... ou barre d'actions)
    ├── Préférences user ? → Settings
    └── Admin ? → Admin section dédiée
```

Règle des 3 niveaux : jamais plus de 3 niveaux de nav avant d'arriver au contenu. Au-delà, l'utilisateur se perd (Hick + mémoire de travail).

## 4. Flow — chemin minimal

### Template flow

```markdown
# Flow: [nom]
**User**: [persona]
**Goal**: [JTBD]
**Entry point**: [où il démarre]

## Happy path
[Entry] → [Step 1] → [Step 2] → [Step 3] → [Success]
              │           │
         [Error A]   [Error B]
              │           │
         [Recovery]  [Recovery]

## Steps
### Step 1: [action]
- **Screen**: [nom]
- **User action**: [ce qu'il fait]
- **System response**: [ce qui se passe]
- **Success criteria**: [comment il sait que c'est OK]
- **Biais à vérifier**: [voir scenario-index]
- **Edge cases**:
  - [cas] → [handling]

## Decision points
| Décision | Option A | Option B | Critère utilisateur |
|----------|----------|----------|---------------------|
| [...]    | [path A] | [path B] | [comment il tranche] |

## Error states
| Erreur | Cause | Message | Recovery |
|--------|-------|---------|----------|
| [...]  | [...] | [...]   | [...]    |

## Analytics
| Event | Trigger | Props |
|-------|---------|-------|
| [...] | [...]   | [...] |
```

### Score de complexité flow

| Facteur | Score (1-5) |
|---------|------------|
| Nb d'étapes | |
| Decision points | |
| Inputs utilisateur | |
| Intégrations | |
| Scénarios d'erreur | |
| **Total** | |

- 5-10 : simple, 1 itération suffit
- 11-20 : modéré, phaser
- 21+ : complexe, user testing obligatoire avant dev

## 5. États — les 7 à toujours dessiner

Pour chaque écran contenant des données :

- [ ] **Empty first-use** (jamais rien eu) — contenu pédagogique + 1 CTA
- [ ] **Empty post-action** (tout supprimé) — différent de first-use
- [ ] **Loading** (skeleton ou spinner) — retour < 1 s = instant, 1-10 s = feedback explicite
- [ ] **Partial** (data arrive par morceaux) — skeleton ciblé
- [ ] **Error** (réseau, permission, serveur) — message clair + recovery
- [ ] **1 item** (souvent moche si mal pensé)
- [ ] **N items** (overflow, pagination, virtualization, scroll)

Voir `knowledge/design/skills-main/microinteractions/` pour le timing et le feedback.

## Principes de Norman à vérifier

Checklist à passer sur tout flow :

- [ ] **Affordance** : chaque élément interactif signale sa fonction ? (pas de div-qui-se-clique invisible)
- [ ] **Signifier** : curseur, surlignage, label, icône — l'utilisateur sait ce qu'il peut faire ?
- [ ] **Feedback** : chaque action produit un retour visible en < 100 ms ?
- [ ] **Mapping** : la disposition spatiale reflète la logique ? (ex: bouton "valider" en bas-droite)
- [ ] **Constraint** : les actions impossibles sont-elles désactivées avec explication ?
- [ ] **Consistency** : deux actions similaires ont-elles le même comportement ?
- [ ] **Forgiveness** : undo, confirmation, validation inline, pas de destruction sans filet ?

## Nielsen — les 10 heuristiques appliquées

Pour audit rapide, noter chaque heuristique de 0 (violation grave) à 3 (exemplaire) :

| # | Heuristique | Question à se poser |
|---|-------------|---------------------|
| 1 | Visibility of system status | L'utilisateur sait-il ce qui se passe maintenant ? |
| 2 | Match real world | Termes et concepts familiers (pas de jargon interne) ? |
| 3 | User control & freedom | Undo, back, escape hatch ? |
| 4 | Consistency & standards | Même action = même mot = même emplacement ? |
| 5 | Error prevention | Validation avant l'erreur plutôt qu'après ? |
| 6 | Recognition > recall | Options visibles plutôt qu'à mémoriser ? |
| 7 | Flexibility & efficiency | Raccourcis pour power users ? |
| 8 | Aesthetic & minimalist | Chaque élément est-il nécessaire ? |
| 9 | Recover from errors | Erreurs claires + solution actionnable ? |
| 10 | Help & documentation | Aide contextuelle accessible sans bloquer ? |

Severity d'un problème : 0 = pas un problème / 1 = cosmetic / 2 = minor / 3 = major / 4 = catastrophic. Prioriser 3-4.

## Décisions contre le biais du PM

Quand on doute, se rappeler :

| Biais du PM | Contre-mesure |
|---|---|
| "C'est évident" (curse of knowledge) | Hallway test 5 s |
| "On rajoute juste un bouton" (feature creep) | Audit P0/P1/P2, couper |
| "L'utilisateur comprendra" (false consensus) | 3 users externes, pas des collègues |
| "C'est plus logique comme ça" (engineer-view) | Tester avec le mental model existant |

## Checklist de décision IA

Avant d'envoyer une structure à un designer/Figma :

- [ ] Mental model nommé explicitement
- [ ] Hiérarchie P0/P1/P2 documentée
- [ ] Emplacement dans la nav justifié
- [ ] Flow happy path + erreurs dessinés
- [ ] 7 états prévus
- [ ] Norman (feedback, affordance, mapping) vérifiés
- [ ] Nielsen 10 passés (noter severity)
- [ ] Biais cognitifs pertinents identifiés (via scenario-index)
