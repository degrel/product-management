# DESIGN.md — Workflow opérationnel

> Comment passer de "Claude improvise un DS à chaque session" à "Claude lit un fichier source-de-vérité et respecte les tokens". Le format spec est résumé dans `design-md-format.md` ; ici on couvre **l'usage**.

## TL;DR

```
                ┌─────────────┐
                │  Figma /    │
                │  intuition  │
                └──────┬──────┘
                       │ extract / draft
                       ▼
                ┌─────────────┐    lint     ┌──────────┐
                │  DESIGN.md  │ ──────────► │ findings │
                └──────┬──────┘             └──────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   coding agents   Tailwind       DTCG tokens
   (Claude,        theme.css      tokens.json
    Cursor,        @theme {}      (Style Dictionary,
    BMAD)                          Token Studio)
```

## Quand utiliser DESIGN.md

| Contexte | Outil |
|---|---|
| Prototype neuf, pas de DS encore | **DESIGN.md** seul, quelques jours |
| Coding agent (Claude / Cursor / BMAD) à briefer | **DESIGN.md** = brief portable |
| DS mature avec composants, variants, modes | **Figma Variables + Style Dictionary**, garder DESIGN.md comme résumé d'intention |
| Token swap entre tools (Figma ↔ code) | **DTCG** (export `--format dtcg`) |
| Audit de cohérence avant merge | **`lint`** comme quality gate |

Règle simple : DESIGN.md couvre "tokens + intent". Au-delà (composants documentés exhaustivement, modes light/dark complexes, breakpoints fins), Figma + Style Dictionary prennent le relais.

## Bootstrap d'un DESIGN.md

Template minimal viable, à compléter section par section. Voir `design.md-main/examples/` pour 3 patterns complets.

```yaml
---
version: alpha
name: <Product Name>
description: <1 phrase intent>
colors:
  primary: "#..."
  secondary: "#..."
  neutral: "#..."
  surface: "#..."
  on-surface: "#..."
  error: "#..."
typography:
  headline-lg:
    fontFamily: <font>
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
  body-md:
    fontFamily: <font>
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  label-sm:
    fontFamily: <font>
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
rounded:
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.md}"
    padding: 12px
---

## Overview
<Brand & Style — ton, audience, émotion visée. 3-5 lignes>

## Colors
<Pour chaque couleur clé : nom évocateur + rôle + quand l'utiliser>

## Typography
<Choix des familles + rôle de chaque niveau>

## Layout
<Grille, base spacing, densité>

## Shapes
<Philosophie des corners, icônes>

## Components
<Variants attendus, états>

## Do's and Don'ts
- Do ...
- Don't ...
```

### Checklist de complétude avant 1er lint

- [ ] `name` présent, `colors.primary` défini (sinon warning `missing-primary`).
- [ ] Au moins 1 entrée dans `typography` (sinon warning `missing-typography`).
- [ ] Si `components.*` référencent des tokens, vérifier les `{path.to.token}` (sinon error `broken-ref`).
- [ ] Au moins 4 sections prose (`Overview`, `Colors`, `Typography`, `Components`) — la prose donne le contexte que les tokens ne portent pas.

## Workflow CLI

Le CLI npm `@google/design.md` est l'outil de référence. Aucune install locale nécessaire — `npx` résout depuis le registry public.

### Lint — quality gate

```bash
npx -y @google/design.md lint DESIGN.md
```

Exit 0 si pas d'erreurs, 1 sinon. Format JSON par défaut. Les 7 règles :

| Règle | Sévérité | Détecte |
|---|---|---|
| `broken-ref` | error | `{colors.primary-60}` qui n'existe pas |
| `missing-primary` | warning | `colors` défini mais pas de `primary` |
| `contrast-ratio` | warning | Paires `backgroundColor`/`textColor` sous WCAG AA (4.5:1) |
| `orphaned-tokens` | warning | Tokens couleur définis mais jamais utilisés par un composant |
| `missing-typography` | warning | Couleurs définies mais pas de typo |
| `section-order` | warning | Sections dans le mauvais ordre canonique |
| `missing-sections` | info | `spacing` ou `rounded` absents quand d'autres tokens existent |
| `token-summary` | info | Récap du nombre de tokens par catégorie |

### Export — vers stack code

Formats publiés sur npm (v0.1.1) :

```bash
# Tailwind v3 (theme.extend JSON, à mettre dans tailwind.config.js)
npx -y @google/design.md export --format tailwind DESIGN.md > tailwind.theme.json

# DTCG (W3C Design Tokens) — interop Style Dictionary, Token Studio Figma, etc.
npx -y @google/design.md export --format dtcg DESIGN.md > tokens.json
```

> Le README du repo source documente aussi `css-tailwind` (Tailwind v4 `@theme {}`) et `json-tailwind` mais ces formats ne sont pas dans la version npm publiée à ce jour. Vérifier avec `npx -y @google/design.md export --help` avant de les utiliser. Pour générer un `theme.css` Tailwind v4, l'option pragmatique est de prendre la sortie `tailwind` JSON et de la transformer en CSS variables côté projet.

### Diff — régression check

```bash
npx -y @google/design.md diff DESIGN.md DESIGN-v2.md
```

Détecte tokens added/removed/modified et flag `regression: true` si la nouvelle version a plus d'errors/warnings que l'ancienne. À mettre dans un check CI avant merge sur la branche du DS.

### Spec — injecter dans un prompt agent

```bash
npx -y @google/design.md spec               # markdown
npx -y @google/design.md spec --format json # JSON
npx -y @google/design.md spec --rules-only  # juste les règles linter
```

Utile pour briefer un agent qui ne connaît pas le format.

## Briefer Claude (ou tout coding agent) avec un DS

### Pattern 1 — DESIGN.md à la racine, instruction dans CLAUDE.md

Dans `CLAUDE.md` du projet, ajouter une section :

```markdown
## Design system

La référence visuelle est dans `DESIGN.md` (YAML front matter + prose, format
Google `@google/design.md`).

Tout composant créé ou modifié doit :
- Utiliser uniquement les couleurs déclarées dans `colors`
- Respecter l'échelle `spacing`, `rounded`, `typography`
- Suivre les règles "Do's and Don'ts" et "When to use what" de la prose
- Ne jamais hardcoder une valeur (couleur hex, taille px) hors des tokens

Avant de livrer un mockup ou un composant, valider :
`npx -y @google/design.md lint DESIGN.md`
```

### Pattern 2 — Prompt one-shot

Si pas de CLAUDE.md, charger explicitement :

```
Lis DESIGN.md (en racine du projet) puis applique strictement ses tokens et
règles pour ce qui suit. Refuse de hardcoder une valeur hors de l'échelle.
Si tu sens un manque (couleur d'état, taille intermédiaire), propose un
ajout au DESIGN.md plutôt que d'improviser.

[demande]
```

### Pattern 3 — Inclure la spec en contexte (agent qui n'a jamais vu DESIGN.md)

```bash
npx -y @google/design.md spec | pbcopy
# Coller en début de session avant le DESIGN.md du projet.
```

## Pont Figma → DESIGN.md (manuel guidé)

Le `figma-bridge/ds-extractor/` (déjà présent dans le repo) extrait variables Figma + styles + composants en markdown. Aujourd'hui ça produit `knowledge-base/<file>-ds.md`, pas un DESIGN.md valide directement. Workflow manuel :

### 1. Extraction depuis Figma

```bash
cd figma-bridge/ds-extractor
# Configure FIGMA_PAT et FILE_KEY dans .env (cf. README ds-extractor)
npx tsx extract.ts
```

Output : un markdown listant collections de variables, text styles, composants.

### 2. Mapping Figma → DESIGN.md (à la main, ou via Claude)

Convention de mapping recommandée :

| Figma | DESIGN.md token |
|---|---|
| Variable `color/primary/500` | `colors.primary` (ou `colors.primary-50` si scale numérotée) |
| Variable `color/surface/base` | `colors.surface` |
| Variable `color/text/default` | `colors.on-surface` |
| Text style `heading/large` | `typography.headline-lg` |
| Text style `body/medium` | `typography.body-md` |
| Variable `space/4` (16px) | `spacing.md` |
| Variable `radius/medium` | `rounded.md` |
| Component `Button/Primary/Default` | `components.button-primary` |
| Component `Button/Primary/Hover` | `components.button-primary-hover` |

### 3. Demander à Claude la conversion

Prompt type :

```
Voici l'extraction Figma (markdown ci-dessous). Convertis ça en DESIGN.md
valide selon la spec @google/design.md (YAML front matter + prose). Suis le
mapping de conventions habituelles : color/primary/500 → primary, etc.

Pour les sections prose (Overview, Colors, Typography, ...), laisse des
placeholders <à compléter> que je remplirai avec l'intent du produit.

[coller le markdown]
```

Puis valider : `npx -y @google/design.md lint`.

## Pont DESIGN.md → Figma (round-trip, optionnel)

```bash
npx -y @google/design.md export --format dtcg DESIGN.md > tokens.json
```

Le fichier `tokens.json` est conforme au W3C Design Tokens Format Module (DTCG) et peut être importé dans Figma via le plugin **Token Studio for Figma** (ex Figma Tokens). Permet de partir d'un DESIGN.md écrit côté code/agent et de pousser les variables dans Figma pour que les designers travaillent dans la même grille.

Stretch (pas v1) : étendre `figma-bridge/ds-extractor/` avec un mode `--format design-md` qui écrit directement le YAML conforme. Hors scope tant qu'il n'y a pas de DS Galigeo formalisé.

## Anti-patterns du workflow

| Anti-pattern | Pourquoi c'est cassé | Fix |
|---|---|---|
| DESIGN.md écrit, jamais linté | On découvre les broken refs au pire moment | `lint` à chaque commit qui touche le fichier |
| Tokens définis mais pas utilisés dans `components.*` | Warning `orphaned-tokens` ; les agents ne savent pas où s'en servir | Soit utiliser, soit supprimer |
| Couleurs primary/accent mais pas de `on-primary` | Contraste impossible à valider | Toujours déclarer la paire bg + on-bg |
| Prose absente | L'agent improvise sur le "quand" et le "pourquoi" | Au moins Overview + Do's and Don'ts |
| DESIGN.md vit en dehors du repo | Drift inévitable, pas versionné | À la racine du repo, à côté de README.md |
| Plusieurs DESIGN.md sans `diff` entre versions | Régression visuelle invisible en review | `diff` dans la PR du DS |

## Checklist avant handoff à un coding agent

- [ ] `npx -y @google/design.md lint DESIGN.md` → exit 0 (pas d'errors)
- [ ] Warnings restants documentés ou résolus
- [ ] Section `Components` couvre au minimum : button-primary (+ hover, disabled), input-field, card
- [ ] Section `Do's and Don'ts` présente (au moins 5 règles)
- [ ] CLAUDE.md (ou équivalent) référence DESIGN.md
- [ ] Export Tailwind testé sur 1 composant réel pour vérifier que le mapping marche
