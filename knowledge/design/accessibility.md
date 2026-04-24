# Accessibility — WCAG AA pratique

Niveau cible : **WCAG 2.2 AA** (équivalent RGAA 4 en France pour produits B2B).

## Les 4 principes POUR

### Perceivable
Les informations doivent être perçues par tous.

- **Alt text** sur toutes images porteuses d'information. Image décorative = `alt=""`.
- **Captions** sur vidéos, **transcripts** sur audio.
- **Contraste** : 4.5:1 (texte normal) / 3:1 (texte large ≥ 18pt / 14pt bold) / 3:1 (UI et bordures porteuses d'info).
- **Info jamais véhiculée par la couleur seule** : rouge/vert pour succès/erreur → ajouter icône ou label.
- **Texte redimensionnable** à 200% sans perte d'info ni scroll horizontal.

### Operable
Tous les utilisateurs doivent pouvoir naviguer.

- **Tout doit être accessible au clavier** : Tab, Shift+Tab, Enter, Space, Arrow keys, Escape.
- **Pas de piège clavier** : on peut sortir d'un composant avec Tab ou Esc.
- **Focus visible** : ring ≥ 2px, contraste ≥ 3:1 avec l'arrière-plan. Ne jamais `outline: none` sans remplacement.
- **Skip links** pour sauter la nav ("Aller au contenu principal").
- **Timing ajustable** : session timeout > 20 s, possibilité de prolonger.
- **Pas de flash > 3× par seconde** (risque épilepsie).

### Understandable
L'interface et le contenu doivent être compréhensibles.

- **Langue de la page** : `<html lang="fr">`.
- **Focus prévisible** : pas de redirection automatique inattendue.
- **Labels et instructions** sur tous les inputs (`<label for="...">`).
- **Error identification** : champ en erreur clairement identifié (pas juste couleur).
- **Suggestion de correction** : "Format attendu : 06 12 34 56 78".

### Robust
Le contenu doit marcher avec les AT (assistive technologies) actuels et futurs.

- **HTML valide** : pas d'ID dupliqués, tags correctement imbriqués.
- **ARIA** utilisé correctement (rôles, états, propriétés) — seulement si HTML natif ne suffit pas.
- **Composants custom** exposent leur état (`aria-expanded`, `aria-selected`, `aria-pressed`).
- **Live regions** pour le contenu dynamique (`aria-live="polite"`, `role="status"`, `role="alert"`).

## Patterns courants

### Formulaires
- Label explicite (`<label for="email">Email</label>`), jamais placeholder-only.
- `aria-required="true"` ou `required` attribute.
- `aria-invalid="true"` sur champ en erreur + `aria-describedby` pointant vers le message.
- Erreur affichée sous le champ, pas au-dessus.
- Summary en haut si plusieurs erreurs.

### Boutons vs liens
- Bouton = action qui change l'état (save, delete, submit).
- Lien = navigation vers une URL.
- Pas de `<div onClick>` — jamais accessible au keyboard par défaut.

### Modals
- Focus trap pendant l'ouverture.
- Esc ferme.
- Focus revient à l'élément déclencheur après fermeture.
- `role="dialog"` + `aria-modal="true"` + `aria-labelledby`.

### Dropdowns et menus
- Open avec Space/Enter/Arrow.
- Arrow keys pour naviguer.
- Esc pour fermer.
- Tab pour sortir vers l'élément suivant.
- `aria-haspopup` + `aria-expanded`.

### Images
- `alt` = description de ce qu'elle véhicule (pas "image de X", juste "X").
- SVG informatif : `<title>` à l'intérieur + `role="img"`.
- Images purement décoratives : `alt=""` ou `role="presentation"`.

### Tables
- `<th scope="col">` ou `scope="row"`.
- `<caption>` pour résumer.
- Pas de `<table>` pour la mise en page.

### Focus management
- Focus ring natif ou custom ≥ 2px et contraste ≥ 3:1.
- Après action destructive, focus va à l'élément logique suivant.
- Pas de `tabindex > 0` (casse l'ordre naturel).

## Outils de test

### Automatiques (catch ~30% des problèmes)
- **axe DevTools** (Chrome extension) — rapide, précis
- **Lighthouse** → Accessibility score + issues
- **WAVE** (wave.webaim.org) — analyse visuelle

### Manuels (indispensables)
- **Keyboard-only** : 30 min sans souris. Toutes les fonctions accessibles ? Focus toujours visible ?
- **Screen reader** : VoiceOver (macOS : Cmd+F5), NVDA (Windows, gratuit). Tester le flow principal.
- **Zoom 200%** : lisible, pas de coupure, scroll vertical uniquement ?
- **Sim Daltonism** : fonctionne sans perception rouge-vert ?
- **Réduire le mouvement** (système macOS) : animations réduites, pas bloquantes ?

## Checklist pre-merge a11y

- [ ] Contraste vérifié sur tous textes et UI
- [ ] Navigation clavier complète testée
- [ ] Focus ring visible sur tous les interactifs
- [ ] Labels sur tous les inputs
- [ ] Messages d'erreur actionnables
- [ ] Alt text sur images (ou `alt=""` si décoratives)
- [ ] Couleur n'est pas le seul signal
- [ ] `lang` attribut correct
- [ ] Titres `<h1>` → `<h6>` hiérarchisés
- [ ] Landmarks ARIA (`<main>`, `<nav>`, `<header>`)
- [ ] Composants dynamiques ont `aria-live` si pertinent
- [ ] Test screen reader sur le flow principal (5 min min)

## Ressources

- WCAG 2.2 : w3.org/WAI/WCAG22/quickref/
- RGAA : accessibilite.numerique.gouv.fr
- ARIA Authoring Practices : w3.org/WAI/ARIA/apg/
- WebAIM : webaim.org
