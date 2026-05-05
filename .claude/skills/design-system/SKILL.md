---
name: design-system
description: Design system comme langage — tokens, composants, naming, thèmes, DESIGN.md format pour handoff. Use when defining design tokens, naming conventions, component specs, building a component library, setting up theming/dark mode, auditing token consistency, writing a DESIGN.md handoff file for coding agents, or preparing a design-to-dev handoff. Covers global/alias/component token tiers, component variants and states, accessibility baked in, DESIGN.md YAML+markdown spec, and versioning. For pure visual choices (palette, scale), see design-craft. For review of a single mockup, see design-review.
---

# Design System & Handoff

## Purpose
Transformer des décisions individuelles (un bouton, une couleur) en **langage partagé** réutilisable par designers, devs, et coding agents. Ce skill répond à "comment ça se réutilise", "comment on handoff", "comment on tient la cohérence dans la durée".

## Knowledge base (load on demand)

Fiches distillées dans `knowledge/design/`.

| Besoin | Fichier |
|---|---|
| Architecture tokens (global → alias → component) + naming | `design-tokens.md` |
| Format DESIGN.md (spec YAML + markdown pour coding agents) | `design-md-format.md` |
| Workflow DESIGN.md ↔ Claude ↔ Figma (CLI, briefing, ponts) | `design-md-workflow.md` |
| Spec normative + 3 patterns Google de référence | `design.md-main/` (vendorisé) |
| Color, contraste, palette, dark mode, data viz | `color-and-contrast.md` |
| Typography (échelle, weights, performance) | `typography.md` |
| Spacing & layout (échelle, grilles, densité) | `spacing-layout.md` |
| Accessibility (WCAG AA, ARIA) | `accessibility.md` |

## Architecture à 3 niveaux de tokens

**Règle d'or** : aucun composant ne référence une valeur brute. Tout passe par un alias sémantique.

```
┌─────────────────────────────────────────────┐
│ Component tokens                            │
│   button-color-primary-background           │
│   ↓                                         │
│ Alias (semantic) tokens                     │
│   color-action-primary                      │
│   ↓                                         │
│ Global (primitive) tokens                   │
│   blue-500: #3B82F6                         │
└─────────────────────────────────────────────┘
```

| Tier | Rôle | Exemple | Qui modifie |
|---|---|---|---|
| Global | Valeurs brutes, palette complète | `blue-500: #3B82F6` | Équipe DS uniquement |
| Alias | Sens métier | `color-action-primary` | Équipe DS |
| Component | Usage scopé | `button-primary-bg` | Équipe DS, parfois équipe produit |

Avantages :
- Thémer = changer uniquement les alias (light → dark), globals intacts
- Refonte de palette = modifier globals, les composants suivent
- Lecture du code composant = lisible sans connaître la palette

## Catégories de tokens

- **Color** : palette globale, alias (surface, text, border, action, state), tokens composants
- **Spacing** : base 4 px ou 8 px ; échelle `xs, sm, md, lg, xl, 2xl, 3xl`
- **Typography** : font families, sizes, weights, line heights, letter spacing
- **Radius** : `none, sm, md, lg, full`
- **Elevation** : `level-0` à `level-4`, z-index scale
- **Motion** : durations (`fast, normal, slow`), easings (`ease-out, ease-in-out`)
- **Border** : widths, styles

## Naming convention

Pattern général : `{category}-{property}-{variant}-{state}`

Exemples :
- `color-action-primary-default`
- `color-action-primary-hover`
- `color-surface-elevated`
- `spacing-inset-md`
- `typography-heading-xl`

Règles :
- **kebab-case** (évite le camelCase pour rester cross-platform)
- **Ordre général → spécifique** (gauche → droite)
- **Pas de valeurs dans le nom** (`color-blue-500` = global OK, `color-action-blue` = alias ambiguë, préférer `color-action-primary`)
- **États en dernier** : `default, hover, active, focus, disabled`

## Composant — spec template

```markdown
# Component: [Nom]

## Overview
[Une phrase : rôle + quand l'utiliser]

## Variants
| Variant | Use case | Difference visuelle |
|---------|----------|---------------------|
| Primary | Action principale unique sur l'écran | Fond couleur accent |
| Secondary | Action alternative | Border, fond neutre |
| Ghost | Action tertiaire, faible proéminence | Pas de fond, pas de border |
| Danger | Action destructive | Fond red-500 |

## Sizes
| Size | Height | Padding | Font-size | Usage |
|------|--------|---------|-----------|-------|
| sm | 32px | 8x12 | 14 | Barres compactes, tableaux |
| md | 40px | 10x16 | 14 | Défaut |
| lg | 48px | 12x20 | 16 | CTA primaire, mobile |

## States
- default, hover, active (pressed), focus (keyboard), disabled, loading
- Pour chaque state, préciser : background, border, text color, shadow, cursor

## Props / Parameters
| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| variant | enum | no | primary | [primary, secondary, ghost, danger] |
| size | enum | no | md | [sm, md, lg] |
| loading | bool | no | false | Remplace le contenu par spinner, disable click |
| iconLeading | ReactNode | no | — | Icône avant le texte |

## Accessibility (obligatoire)
- [ ] Focus ring visible, contraste ≥ 3:1
- [ ] Touch target ≥ 44×44 px (sm OK si nested dans liste dense avec padding)
- [ ] `aria-busy` quand loading, `aria-disabled` quand disabled
- [ ] Label explicite (pas juste une icône sans `aria-label`)

## Content guidelines
- **Label** : 1-3 mots, verbe d'action ("Enregistrer", pas "Soumettre")
- **Pas de CAPS** sauf cas précis
- **Truncation** : jamais, préférer faire grandir le bouton ou passer à taille `lg`

## Do's and Don'ts
| Do | Don't |
|---|---|
| 1 bouton primary par écran | 3 boutons primary côte à côte |
| Icône ≤ taille du texte | Icône dominante |
| Ordre : primary à droite (web), en haut (mobile iOS) | Ordre arbitraire |

## Tokens utilisés
- `button-primary-bg: color-action-primary-default`
- `button-primary-text: color-on-primary`
- `button-primary-bg-hover: color-action-primary-hover`
- `button-radius: radius-md`
- `button-padding-md: spacing-inset-md`
```

## Format DESIGN.md — handoff à des coding agents

DESIGN.md est un format **Google** qui combine **YAML front matter** (tokens machine-readable) + **markdown prose** (pourquoi des choix). C'est le pivot quand on handoff à Cursor, Claude Code, Copilot, BMAD : un seul fichier portable, versionnable, lintable.

- **Spec normative** : `knowledge/design/design.md-main/docs/spec.md`
- **Primer rapide** : `knowledge/design/design-md-format.md`
- **Workflow opérationnel** (CLI, briefing, ponts Figma) : `knowledge/design/design-md-workflow.md`

Exemple minimal :

```markdown
---
name: Galigeo TM
colors:
  primary: "#1A4D7A"
  accent: "#E6733A"
  surface: "#FFFFFF"
  surface-alt: "#F4F6F8"
  text: "#1A1C1E"
  text-muted: "#6C7278"
  border: "#E1E5EA"
  state-success: "#1F8A4C"
  state-danger: "#C0392B"
  state-warning: "#D88A00"
typography:
  heading-xl:
    fontFamily: Inter
    fontSize: 2rem
    fontWeight: 600
    lineHeight: 1.15
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.55
  label-sm:
    fontFamily: Inter
    fontSize: 0.875rem
    fontWeight: 500
    lineHeight: 1.3
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
radius:
  sm: 4px
  md: 8px
  lg: 12px
motion:
  fast: 150ms
  normal: 200ms
  slow: 300ms
---

## Overview
Décision-cartographie sérieuse et lisible. La UI privilégie la densité
d'information (tableaux, cartes) sans sacrifier la respiration. Teintes
stables, un seul accent (#E6733A) pour les actions primaires.

## Colors
- **Primary (#1A4D7A)** : identité Galigeo, headers, focus ring.
- **Accent (#E6733A)** : UNIQUEMENT CTAs primaires. Ne pas utiliser comme fond étendu.
- **Surface-alt** : rangs alternés, fonds de sections secondaires.

## Typography
Inter pour tout. Pas de serif. Headings 600, body 400, labels 500.
Line-height généreux car beaucoup de data.

## When to use what
- Bouton primary → couleur accent, 1 par écran
- Bouton secondary → border primary, fond transparent
- Bouton destructive → fond state-danger
- Badge alerte → state-warning, jamais state-danger sauf blocage
```

### Workflow CLI

Outil de référence : `@google/design.md` (npm). Aucune install locale, `npx` résout depuis le registry.

```bash
# Quality gate : 7 règles, exit 1 si erreurs
npx -y @google/design.md lint DESIGN.md

# Export Tailwind v3 (theme.extend JSON pour tailwind.config.js)
npx -y @google/design.md export --format tailwind DESIGN.md > tailwind.theme.json

# Export DTCG (W3C, interop Style Dictionary, Token Studio Figma)
npx -y @google/design.md export --format dtcg DESIGN.md > tokens.json

# Régression check entre versions
npx -y @google/design.md diff DESIGN.md DESIGN-v2.md
```

7 règles linter (cf. `design-md-workflow.md` pour le détail) :
`broken-ref` (error), `missing-primary`, `contrast-ratio` (WCAG AA), `orphaned-tokens`, `missing-typography`, `section-order` (warnings), `missing-sections`, `token-summary` (info).

### Patterns de référence

3 DESIGN.md complets vendorisés depuis `@google/design.md` à copier/adapter :

| Pattern | Style | Quand s'en inspirer |
|---|---|---|
| `design.md-main/examples/atmospheric-glass/` | Glassmorphism, monochromatic blanc + alpha, gradients vifs | UI ambient, météo, dashboards créatifs |
| `design.md-main/examples/paws-and-paths/` | Warm consumer, orange + sky blue, sans-serif amical | Produit grand public, onboarding chaleureux |
| `design.md-main/examples/totality-festival/` | Dark editorial, obsidian + corona gold | Event, premium, lecture intensive |

Chaque dossier contient : `DESIGN.md` + `tailwind.config.js` (généré par export) + `design_tokens.json` (DTCG). À ouvrir avant de partir d'une page blanche.

### Briefer Claude (ou tout coding agent) avec ce DS

Une fois ton `DESIGN.md` à la racine du projet, ajoute dans `CLAUDE.md` :

```markdown
## Design system

La référence visuelle est dans `DESIGN.md` (format @google/design.md).
Tout composant créé doit :
- Utiliser uniquement les tokens déclarés (colors, typography, spacing, rounded)
- Respecter "Do's and Don'ts" et la prose des sections
- Ne jamais hardcoder une valeur hors échelle

Avant handoff : `npx -y @google/design.md lint DESIGN.md`.
```

Détails et patterns alternatifs (prompt one-shot, injection de spec) dans `knowledge/design/design-md-workflow.md`.

## Handoff design → dev

### Handoff checklist par composant

```markdown
# Handoff : [Nom composant]

## Figma
- [ ] Lien vers la frame source
- [ ] Variants visibles (primary/secondary/..., sm/md/lg, all states)
- [ ] Auto-layout activé si pertinent
- [ ] Component properties exposés dans le panneau

## Tokens
- [ ] Toutes les valeurs (couleur, spacing, radius) référencent des tokens
- [ ] Aucune valeur hardcodée (`#3B82F6` → `color-action-primary`)

## Spec
- [ ] Variants, sizes, states documentés
- [ ] Props avec type, default, requis
- [ ] A11y : focus ring, aria-*, keyboard nav
- [ ] Do's and Don'ts

## Exemples d'usage
- [ ] 2-3 screens réels intégrant le composant
- [ ] Edge cases (text long, icône seule, loading)

## Tests
- [ ] Visual regression baseline (Storybook + Chromatic / Playwright)
- [ ] Keyboard interaction (tab, enter, escape)
- [ ] Screen reader (test VoiceOver rapide)
```

## Audit de cohérence

Signes qu'un design system dérive :
- **Valeurs hors échelle** : `padding: 13px` quand l'échelle fait 12 ou 16. Auditer via script.
- **Composants dupliqués** : `ButtonPrimary`, `ActionButton`, `CTAButton`. Consolider.
- **Tokens non-utilisés** : un alias créé "au cas où" jamais référencé. Supprimer.
- **Patterns copié-collés** : carte produit redessinée sur 3 écrans. Extraire composant.
- **A11y disparate** : certains composants compliant, d'autres non. Rendre obligatoire via lint.

Audit minimal :

```markdown
# DS Audit — [date]

## Tokens
- Global utilisés / total : X/Y (Z % de morts à supprimer ?)
- Alias couvrant les cas métiers : oui/non (lister gaps)
- Composants référençant des valeurs brutes : lister (0 idéalement)

## Composants
- Total : n
- Avec doc complète : n (%)
- Avec tests a11y : n (%)
- Dupliqués / à consolider : lister

## Adoption
- % de screens utilisant le DS à 100 % : ?
- Composants les plus utilisés : top 5
- Composants jamais utilisés : lister
```

## Versioning & evolution

- **Semver** pour le DS : major = breaking (token renommé, composant supprimé), minor = ajout, patch = fix visuel non-breaking.
- **Deprecation** : marquer un token/composant deprecated avant suppression, avec warning dans le code et fenêtre de 1 release minimum.
- **Changelog explicite** à chaque release : qui migre, comment, avant quand.
- **Migration scripts** quand possible (regex codemod sur tokens renommés).

## Anti-patterns

| Anti-pattern | Symptôme | Fix |
|---|---|---|
| Tokens sémantiques absents | `#3B82F6` en dur partout | Ajouter alias `color-action-primary` |
| Composant pour tout | 40 composants, 6 utilisés | Consolider, supprimer |
| A11y "on verra plus tard" | Composants pas accessibles | Bloquer le merge sans tests a11y |
| Pas de doc | "Demande à [designer] comment c'est censé marcher" | Doc minimale obligatoire |
| DS forké par équipe | Chaque équipe a sa version | 1 DS, contributions centralisées |

## Checklist création / évolution DS

- [ ] Architecture 3 tiers de tokens en place
- [ ] Naming convention documentée et respectée
- [ ] Chaque composant a : variants, sizes, states, props, a11y, tokens, exemples
- [ ] DESIGN.md généré pour handoff aux coding agents
- [ ] Audit trimestriel planifié (tokens morts, doublons, adoption)
- [ ] Changelog à jour
- [ ] Ownership clair (qui valide les PRs DS ?)
