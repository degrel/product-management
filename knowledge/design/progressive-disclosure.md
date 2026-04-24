# Progressive Disclosure

> Principe fondateur : ne montrer QUE ce qui est nécessaire **maintenant**. Tout le reste reste masqué, accessible à la demande.

## Pourquoi

- Réduit la charge cognitive (Sweller) — l'user ne traite que ce qui est visible.
- Augmente le taux de complétion (moins de champs visibles = moins de décisions = plus de finition).
- Permet de supporter débutants ET experts sur le même écran.

## Les 3 niveaux

| Niveau | Contenu | Fréquence attendue | Comment y accéder |
|---|---|---|---|
| **P0 — Always visible** | Ce dont 80 % des users ont besoin 80 % du temps | Chaque session | Par défaut |
| **P1 — On interaction** | Détails, config légère | 20-60 % des sessions | Hover, click, expand, tab |
| **P2 — On demand** | Rare, power user, settings | < 20 % des sessions | Menu, settings, modal, keyboard shortcut |

**Règle** : si un élément est P2, il ne doit **pas** apparaître visuellement comme P0. Sinon pollution.

## Patterns courants

### Tabs
- Plusieurs "modes" sur un même écran (overview / details / history).
- P0 = tab active, P1 = autres tabs (1 click), P2 = "..." overflow.

### Expand / Accordion
- Sections secondaires masquées par défaut.
- Titre clique → révèle le contenu.
- Attention : si 5 sections expandables par défaut, le user les ouvre toutes → c'est P0 déguisé.

### Disclosure button ("Show more")
- Liste partiellement affichée (5 items).
- "Show all" / "More" révèle le reste.
- Indique un compte pour calibrer l'attente ("5 sur 23").

### Overflow menu (···)
- Actions rares sur un item (archive, pin, report).
- Icônes visibles = P0, overflow = P1 (click) ou P2 (settings).

### Tooltip / Popover
- Info explicative, pas critique pour la décision.
- Attention : contenu de tooltip = P1 sur desktop (hover), mais doit être accessible tap sur mobile.

### Modal / Side panel
- Workflow isolé qui ne nécessite pas d'être en contexte permanent.
- Entre-modes (filter builder, settings avancés).

### Wizards / Multi-step
- Remplace un long formulaire.
- Chaque step = P0 à ce moment, le reste est P1 (step précédents) ou P2 (futurs).

### Progressive forms
- Demander 1 champ à la fois selon les réponses.
- Ex : signup Duolingo demande un premier intérêt, puis skill level, puis objectif.

## Audit progressive disclosure

Sur un écran :

```markdown
## Audit PD — [écran]

| Élément | Niveau actuel | Niveau idéal | Justification |
|---------|---------------|--------------|---------------|
| Title | P0 | P0 | Répond à "où suis-je" |
| Primary action | P0 | P0 | JTBD principal |
| Date filter | P0 | P1 (dropdown) | 30% des users l'utilisent |
| Export CSV | P0 | P2 (menu) | 5% des users |
| Settings panel inline | P0 | P2 (/settings) | 2% des users |
```

Si 5+ éléments sont P0 → l'écran est surchargé. Downgrade quelque chose.

## Anti-patterns

| Anti-pattern | Symptôme | Fix |
|---|---|---|
| "Just in case" UI | Stakeholder a demandé un bouton, ajouté "au cas où" | Auditer fréquence d'usage, couper |
| P2 déguisé en P0 | 40 options dans la nav | Power user → keyboard shortcut, settings |
| 5 accordions fermés par défaut | User les ouvre tous | Passer en P0 ou reorganiser |
| Tooltip critique | Info essentielle cachée derrière hover | Doit être visible (P0) ou texte explicite |
| Wizard pour 3 champs | Friction inutile | Formulaire simple |
| Overflow menu pour l'action principale | User ne trouve pas | Primary CTA doit être P0 |

## Règles de pouce

- **> 3 clics pour atteindre un besoin fréquent** → reconsidérer la hiérarchie.
- **< 10 éléments visibles simultanément** sur un écran principal (hors data table).
- **Chaque masque = possibilité d'erreur** : le user peut oublier où est X. Compenser avec search, breadcrumbs, ou ne pas masquer.
- **Power users existent** : permettre de tout révéler (mode expert), mais ne pas imposer aux débutants.

## Measure

Après design :
- Taux de clic sur les éléments P1 / P2 → si élevé, peut-être P0.
- Temps pour atteindre la core action → devrait diminuer avec PD bien fait.
- Completion rate sur les formulaires progressifs vs one-shot.

Si clics sur "expand" > 80 % → remonter le contenu en P0. Si clics < 5 % → ok, c'est bien P2.
