# Visual Hierarchy — Refactoring UI distillé

> Source : `skills-main/refactoring-ui/SKILL.md`. Ouvrir pour les exemples complets.

## Principe central
La hiérarchie visuelle guide l'œil vers ce qui compte. Un bon design a toujours **un élément dominant**, des éléments secondaires, du bruit visuel minimal.

## Checklist Grayscale-First
1. Désactiver la couleur (Figma → passer tout en niveaux de gris).
2. L'élément principal ressort-il ?
3. L'ordre d'importance est-il lisible sans couleur ?
4. Si oui → remettre la couleur, elle renforcera la hiérarchie.
5. Si non → **retravailler la hiérarchie avant d'ajouter la couleur**.

## Leviers de hiérarchie (jamais tous en même temps)
- **Taille** : 1 élément clairement plus grand que les autres
- **Poids** : 400 body, 500 label, 600 heading
- **Couleur** : contraste avec le fond, pas deux éléments "importants" en couleur pleine
- **Espacement** : plus d'air autour = plus d'importance perçue
- **Position** : haut-gauche (web Z-pattern), centre (focus)
- **Contraste** : texte 4.5:1, UI 3:1

## Contraintes (Refactoring UI)

### Échelles finies
- Typo : 12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72 (pas 17, pas 23)
- Spacing : 4, 8, 12, 16, 24, 32, 48, 64, 96 (multiples de 4)
- Radius : 2-3 valeurs (`sm`, `md`, `lg`)
- Shadow : 4-5 niveaux d'élévation

### Une seule accent color
- Primary = couleur de marque + quelques variations
- Accent = 1 couleur pour la CTA primaire
- Sémantiques : success, warning, danger, info (figées)

## Don't / Do rapides

| Don't | Do |
|---|---|
| Centrer un texte > 2 lignes | Align left |
| Utiliser `font-weight: 300` sur fond clair | Min 400, idéal 500+ |
| Shadow `0 0 10px black` | Shadow réaliste : décalé + blur fort + opacity 0.05-0.15 |
| Border partout | Proximité + white space d'abord |
| Gray-on-gray | Contraste ≥ 4.5:1 toujours |
| Tout en couleur primary | 1 accent, reste neutre |
| Icônes multiples styles | 1 pack, 1 weight, 1 taille |

## Le "squint test"
Loucher ou flouter le mockup (Figma : plugin ou screenshot + blur CSS).
- Un élément domine clairement ? OK
- Tout se vaut ? Retravailler la hiérarchie.
- Le mauvais élément domine ? Retravailler.

## Le "design from the back" trick
Commencer par le fond (surface), puis les éléments de bas niveau (cartes, inputs), puis les éléments actifs (boutons, liens), puis la couleur accent. Dans cet ordre. L'œil s'habitue au neutre et l'accent porte.
