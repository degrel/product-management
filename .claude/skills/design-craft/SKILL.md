---
name: design-craft
description: Qualité visuelle sur les mockups — typography, spacing, color, visual hierarchy, microinteractions, responsive, dark mode. Use when a mockup "looks off", producing production-grade visuals, picking a typeface, building a spacing scale, choosing a color palette, adding microinteractions, fixing visual hierarchy, polishing before review, or applying Refactoring UI principles. Covers grayscale-first, constrained design scales, shadows/depth, motion, data visualization. For IA/flow decisions, see design-ia. For tokenizing & reusing, see design-system.
---

# Visual Design Craft

## Purpose
Transformer un mockup "brouillon" en mockup "production-grade". Ce skill répond à "pourquoi ça rend pas bien" et "comment rendre ça précis et poli".

## Knowledge base (load on demand)

Fiches distillées dans `knowledge/design/`. Charger **une** fiche à la fois, pas toutes.

| Besoin | Fichier |
|---|---|
| Hiérarchie visuelle, grayscale-first, contraintes | `visual-hierarchy.md` |
| Typographie web (scale, pairing, performance) | `typography.md` |
| Color, contraste, WCAG, dark mode, data viz palettes | `color-and-contrast.md` |
| Spacing, rhythm, grille, densité | `spacing-layout.md` |
| Microinteractions (triggers, rules, feedback, motion) | `microinteractions.md` |
| Les 7 états à dessiner (empty, loading, error…) | `states.md` |
| Progressive disclosure (P0/P1/P2) | `progressive-disclosure.md` |

## Mindset : contraintes > options

Le craft progresse quand on **réduit** le nombre de choix. Trois règles fondatrices :

1. **Grayscale-first** : commencer sans couleur. Si la hiérarchie marche en niveaux de gris, la couleur la renforce. Sinon, la couleur cache un problème de hiérarchie.
2. **Échelle contrainte** : choisir une échelle finie (6-8 tailles typo, 8-10 espacements) et s'y tenir. Valeurs custom = dette visuelle.
3. **Optique avant arithmétique** : un cercle "aligné en pixel" paraît décalé. Corriger à l'œil, pas au chiffre.

## Les 6 leviers du craft

Dans l'ordre à auditer sur tout mockup :

### 1. Hierarchy (ce que l'œil voit en premier)

| Question | Réponse OK si… |
|---|---|
| Quel est l'élément dominant ? | Un seul, et c'est le plus important |
| Y a-t-il 3+ niveaux perceptibles ? | Oui (primary, secondary, tertiary) |
| Le regard suit-il un chemin (Z ou F) ? | Oui, cohérent avec l'objectif |
| Le plus important est-il aussi le plus visible ? | Oui |

Leviers disponibles : taille, poids, couleur, contraste, espacement, position. **Jamais** tous en même temps.

### 2. Typography

- **2 typefaces max** (souvent 1 suffit). Combiner un sans-serif UI + un serif éditorial seulement si justifié.
- **Échelle typographique** : 12, 14, 16, 18, 20, 24, 30, 36, 48 (exemple). Pas de 17px.
- **Line-height** : 1.4-1.6 pour du body text, 1.1-1.2 pour des titres.
- **Measure** (largeur de ligne) : 45-75 caractères.
- **Weight** : éviter < 400 sur fond clair, < 500 sur fond sombre.
- **Performance** : `font-display: swap`, subsetter, WOFF2, limiter à 2 weights par font.

### 3. Color

- **Construire la palette à partir du neutre**. Une échelle de 9-10 gris (50, 100, 200…, 900) résout 80% des besoins.
- **1 primary, 1 accent max**. Les autres couleurs sont sémantiques : success (green), warning (amber), danger (red), info (blue).
- **Contraste WCAG AA** : 4.5:1 pour body, 3:1 pour texte large (≥ 18pt ou 14pt bold).
- **Dark mode** : ne pas inverser — refaire la hiérarchie. Fonds : #0F172A (slate-900), jamais #000. Réduire contraste des éléments non-essentiels.
- **Éviter le noir pur sur blanc pur**. #111 sur #FAFAFA = plus reposant.

### 4. Spacing & layout

- **Base unit 4px ou 8px**. Toutes les valeurs sont des multiples : 4, 8, 12, 16, 24, 32, 48, 64, 96.
- **Loi de proximité** : ce qui est proche appartient ensemble. Plus d'espace entre groupes qu'à l'intérieur d'un groupe.
- **Grille à 12 colonnes** pour desktop, **à 4 colonnes** pour mobile. Gouttières multiples de la base.
- **Densité** : haute pour data tools, basse pour consumer. Galigeo penche densité moyenne (10-12 px padding + aération sélective sur data).
- **Respirer** : la plupart des UIs ont trop peu d'espace, pas trop.

### 5. Depth & shadow

- **Hiérarchie d'élévation** : 5 niveaux max. 0 (fond), 1 (carte), 2 (flottant), 3 (dropdown), 4 (modal).
- **Shadow réaliste** : lumière d'en haut, ombre sous-décalée, opacity faible, blur fort. Jamais `1px 1px 1px black`.
- **Border** alternative à shadow : un `border: 1px solid rgba(0,0,0,0.08)` suffit souvent pour séparer.

### 6. Microinteractions

Les 5 éléments de Saffer à spécifier :

1. **Trigger** : quoi déclenche (click, hover, scroll, temps, données) ?
2. **Rules** : quoi se passe (logique, contraintes) ?
3. **Feedback** : quel retour visuel / sonore / haptique ?
4. **Loop & mode** : répétition, évolution dans le temps, variations ?

Timing par défaut :
- Hover : 100-150 ms
- State change (toggle, button press) : 150-200 ms
- Layout transition : 200-300 ms
- Full page / modal : 300-400 ms
- Au-delà : l'utilisateur trouve lent

Easing : `ease-out` pour l'apparition, `ease-in` pour la disparition, `ease-in-out` pour les mouvements continus.

Respecter `prefers-reduced-motion` : transitions 0.01 ms (quasi-instantanées) pour ces utilisateurs.

## Les 7 états à dessiner (rappel)

Voir `design-ia` pour la logique. Ici, le **visuel** de chaque état :

| État | Traitement visuel |
|---|---|
| Empty first-use | Illustration légère + copy pédagogique + 1 CTA primary |
| Empty post-action | Copy courte, pas d'illustration, 1 CTA |
| Loading | Skeleton (pas spinner si possible), taille exacte du contenu final |
| Partial | Skeleton ciblé sur ce qui manque, reste normal |
| Error | Couleur sémantique (red-500), icône, message clair, CTA recovery |
| 1 item | Ne pas laisser un item seul avec 90% de vide, ajuster layout |
| N items | Virtualisation ≥ 100 items, pagination ≥ 500 |

## Responsive — mobile first

- **Breakpoints** : 320, 640, 768, 1024, 1280, 1536 (exemple Tailwind).
- **Touch target** : 44×44 px minimum (iOS HIG), 48×48 px (Material).
- **Safe areas** : iPhone notch, barre home, clavier virtuel — laisser 16 px padding sur les bords critiques.
- **Typographie fluide** : `clamp(1rem, 0.9rem + 0.5vw, 1.25rem)` plutôt que media queries.
- **Tester sur vrai device** avant de livrer.

## Data visualization (contexte Galigeo : cartes, zones, dashboards)

- **Couleur** : éviter arc-en-ciel, préférer des palettes séquentielles (clair → sombre) pour données ordonnées, divergentes (red ↔ blue) pour écarts autour d'une médiane, catégorielles (ColorBrewer) pour catégories ≤ 8.
- **Accessibilité** : vérifier daltonisme (Sim Daltonism, contraste-finder), jamais rouge-vert seuls.
- **Labels > legend** : labeliser directement quand possible.
- **Zéro chart junk** : pas de 3D, pas d'ombre, pas de gradient gratuit.
- **Annotations** : faire parler la donnée ("pic de ventes", "zone sous-performante") plutôt que laisser l'utilisateur deviner.

Référence : `designer-skills-main/ui-design/skills/data-visualization/`.

## Anti-patterns courants

| Anti-pattern | Symptôme | Fix |
|---|---|---|
| Too many weights of the same font | Visuel flou, pas de hiérarchie | Max 2 weights |
| Gray-on-gray labels | Illisible, WCAG fail | Contraste ≥ 4.5:1 |
| Shadow monotone | "Cartes qui flottent dans le vide" | Hiérarchie d'élévation (voir §5) |
| Border partout | Sensation de grille Excel | Proximité + white space d'abord |
| Animations longues | Sentiment de lenteur | ≤ 300 ms, `ease-out` |
| Icônes inconsistantes | Feel amateur | 1 pack d'icônes, 1 poids, 1 taille |
| Corners inconsistants | Cartes 8px + boutons 12px + modal 4px | 2-3 rayons max, tokenisés |
| Centered body text long | Illisible | Align left pour > 2 lignes |

## Workflow recommandé sur un mockup

1. **Grayscale pass** : désactiver la couleur (Figma → palette → N&B). La hiérarchie tient ?
2. **Squint test** : loucher / flouter. Quel élément domine ? C'est le bon ?
3. **Vérifier l'échelle** : toutes les tailles/espacements sont dans l'échelle ? Lister les exceptions.
4. **Contrast pass** : tous les textes ≥ 4.5:1 ?
5. **States pass** : 7 états dessinés ?
6. **Motion pass** : transitions ≤ 300 ms, `prefers-reduced-motion` OK ?
7. **Responsive pass** : mobile, tablette, desktop, très grand écran ?
8. **Cross-check** : cohérent avec le design system (`design-system`) ?

## Checklist craft avant livraison

- [ ] Échelle typo, spacing, color respectée (tokenisé)
- [ ] 3+ niveaux de hiérarchie perceptibles
- [ ] Grayscale-first test passé
- [ ] Contraste WCAG AA partout
- [ ] 7 états dessinés
- [ ] Microinteractions spécifiées (triggers, timing, feedback)
- [ ] Responsive vérifié sur 3 breakpoints minimum
- [ ] Motion ≤ 300 ms, respect `prefers-reduced-motion`
- [ ] Aucune couleur, aucune taille, aucun espacement hors échelle
- [ ] Revue `design-review` programmée avant handoff
