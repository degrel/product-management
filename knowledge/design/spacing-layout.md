# Spacing & Layout

> Sources : `skills-main/refactoring-ui/`, `designer-skills-main/ui-design/skills/{spacing-system,layout-grid}/`.

## Base unit

Choisir **4 px** (finesse, data tools comme Galigeo) ou **8 px** (generous, consumer).

Échelle recommandée (base 4) :
```
xs  = 4
sm  = 8
md  = 12
lg  = 16
xl  = 24
2xl = 32
3xl = 48
4xl = 64
5xl = 96
6xl = 128
```

**Tout** padding, margin, gap, position = multiple de cette échelle. `13px` est une dette visuelle.

## Loi de proximité (Gestalt)

> Les éléments proches sont perçus comme appartenant au même groupe.

Règle : **plus d'espace entre groupes qu'à l'intérieur d'un groupe**. Si un label est à 12 px de son input et à 12 px du label suivant, l'œil ne voit pas le groupe. Label à 4 px de l'input, 24 px avant le prochain label → hiérarchie claire.

## Rhythm vertical

- **Ligne de rythme** : toutes les marges verticales sont multiples de la line-height du body (souvent 24 px).
- **Alignement vertical** : le top d'un élément s'aligne sur le baseline grid.
- Simpler : tout est multiple de l'unité de base (4 ou 8).

## Grille 12 colonnes (desktop) / 4 (mobile)

| Breakpoint | Colonnes | Gutter | Margin |
|---|---|---|---|
| Mobile < 640 | 4 | 16 | 16 |
| Tablet 640-1024 | 8 | 20 | 24 |
| Desktop 1024-1440 | 12 | 24 | 32 |
| Wide ≥ 1440 | 12 | 32 | 48 (max-width 1280 + auto margins) |

## Container max-width

Pour contenus textuels longs, max-width ~640-720 px (measure lisible, ~70ch).
Pour data dashboards, laisser s'étendre mais `max-width: 1440px` avec `margin: 0 auto`.

## Densité

| Type d'app | Padding cards | Gaps | Exemples |
|---|---|---|---|
| Data tool (Galigeo TM) | 12-16 | 12-16 | Airtable, Linear |
| Productivity | 16-24 | 16-24 | Notion, Slack |
| Consumer / marketing | 24-48 | 24-32 | Stripe, Apple |

## White space

Règles :
- **La plupart des UIs ont trop peu d'espace, pas trop.**
- **Espace autour = importance**. Un CTA avec 48 px de marge frappe plus qu'un CTA collé aux autres.
- **Ne pas combler** les vides par esthétique.

## Anti-patterns

| Anti-pattern | Symptôme | Fix |
|---|---|---|
| Padding arbitraire | `padding: 13px 17px` | Échelle finie |
| Même espace partout | Pas de groupement perçu | Proximity : serrer dans, aérer entre |
| Trop dense | Fatigue visuelle, clic erroné | Passer à densité medium |
| Trop aéré sur data tool | Scroll infini, peu d'info visible | Densité haute pour dashboards |
| Marges incohérentes entre écrans | Sensation de ballottement | Grille globale stricte |

## Stack vs inset vs inline (spacing sémantique)

- **Inset** (padding interne) : `inset-md` = 16 px padding all sides.
- **Stack** (espace vertical entre éléments empilés) : `stack-lg` = 24 px margin-top.
- **Inline** (espace horizontal entre éléments en ligne) : `inline-sm` = 8 px gap.

Tokeniser par usage, pas par valeur :
```yaml
space-inset-sm: 8px
space-inset-md: 16px
space-stack-sm: 12px
space-stack-md: 24px
space-inline-sm: 8px
```

## Alignement optique

- Un cercle "aligné au pixel" paraît décalé à cause de sa forme → corriger à l'œil.
- Icônes dans boutons : souvent 1-2 px de décalage optique.
- Text dans bouton : line-height faux le padding → ajuster padding visuellement.
