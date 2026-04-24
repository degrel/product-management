# DESIGN.md Format

> Format spec Google (2024) pour décrire une identité visuelle à des coding agents (Cursor, Claude Code, Copilot). Combine YAML front matter (machine-readable tokens) + markdown prose (human-readable rationale).

## Structure

```markdown
---
name: <Design System Name>
colors:
  <token-name>: "<hex>"
typography:
  <token-name>:
    fontFamily: <font>
    fontSize: <value>
    fontWeight: <value>
    lineHeight: <value>
spacing:
  <token-name>: <value>
radius:
  <token-name>: <value>
motion:
  <token-name>: <value>
---

## Overview
Prose expliquant la philosophie, le ton, le contexte.

## Colors
Prose expliquant le rôle de chaque couleur.

## Typography
Prose expliquant les choix typographiques.

## When to use what
Règles de composition.
```

## Exemple complet (Galigeo TM)

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
  heading-l:
    fontFamily: Inter
    fontSize: 1.5rem
    fontWeight: 600
    lineHeight: 1.2
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
stables, un seul accent pour les actions primaires.

## Colors
- **Primary (#1A4D7A)** : identité Galigeo, headers, focus ring.
- **Accent (#E6733A)** : UNIQUEMENT CTAs primaires et éléments actifs. Ne pas utiliser comme fond étendu.
- **Surface-alt (#F4F6F8)** : rangs alternés de tableau, fonds de sections secondaires.
- **Border (#E1E5EA)** : séparateurs subtils, cartes, inputs.
- **State colors** : utilisés uniquement pour le statut (badge, icône, message), jamais en fond large.

## Typography
Inter pour toute la UI. Pas de serif. Headings 600, body 400, labels 500.
Line-height généreux (1.5+) car beaucoup de data à lire.

## Spacing
Base 4 px. Rangs de tableau compacts (8-12 px padding vertical), cartes aérées (24 px).

## When to use what
- **Bouton primary** : couleur accent, 1 par écran (la décision principale).
- **Bouton secondary** : border primary, fond transparent.
- **Bouton ghost** : pas de fond, pas de border, texte primary.
- **Bouton destructive** : fond state-danger, réservé aux actions irréversibles.
- **Badge alerte** : state-warning pour "attention à vérifier", state-danger SEULEMENT pour blocage critique.
- **Card** : surface + border subtle, radius-md. Jamais shadow seule.
```

## Validation

```bash
npx @google/design.md lint DESIGN.md
```

Vérifie :
- Structure YAML valide
- Tokens référencés existent
- Contraste WCAG AA sur les paires text/background
- Cohérence inter-tokens

## Diff entre versions

```bash
npx @google/design.md diff DESIGN.md DESIGN-v2.md
```

Output : added / removed / modified pour chaque catégorie + flag `regression`.

## Usage avec coding agents

Dans `CLAUDE.md` ou équivalent :

```markdown
## Design system
La référence visuelle est dans `DESIGN.md` (YAML front matter + prose).
Tout composant créé doit :
- Utiliser uniquement les couleurs déclarées dans `colors`
- Respecter l'échelle `spacing`, `radius`, `typography`
- Suivre les règles "When to use what" de la section prose
- Ne jamais hardcoder une couleur ou taille hors des tokens
```

## Pourquoi ce format

- **Machine + humain** : les tokens sont machine-readable (YAML = structured), la prose est human-readable (markdown).
- **Versionnable** : un simple fichier dans git.
- **Sans tooling lourd** : pas besoin de Style Dictionary si on commence petit.
- **Portable vers tools** : compatible avec DTCG, conversion scripts vers CSS custom properties, iOS tokens, Android resources.

## Limites

- Pas de composants / variants (juste tokens).
- Pas d'interactions / micro-animations détaillées.
- Pas de grille / breakpoints responsive formalisés (à ajouter dans prose).
- Pour DS mature avec composants → compléter avec Figma + Storybook.

## Quand l'utiliser chez Galigeo

- Nouveau produit / prototype → créer un DESIGN.md dès le sprint 0.
- Handoff à un coding agent (Claude Code, Cursor) → pointer vers le fichier.
- Refonte UI → documenter l'état cible avant de coder.
- Système émergent, pas encore de DS formalisé.

Dès que le DS grossit : conserver DESIGN.md comme résumé d'intention, mais passer aux Figma Variables + Style Dictionary pour les composants.
