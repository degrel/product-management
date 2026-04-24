# Heuristics — Nielsen's 10 + severity

> Source : Nielsen Norman Group.

Heuristic evaluation = audit expert basé sur principes (pas sur tests utilisateurs). 1-5 évaluateurs parcourent l'UI, catégorisent chaque violation par heuristique + sévérité.

## Les 10 heuristiques

| # | Nom | Question |
|---|---|---|
| 1 | **Visibility of system status** | L'utilisateur sait-il ce qui se passe ? Feedback visible ? |
| 2 | **Match between system and real world** | Langage, concepts, ordre familiers ? Pas de jargon interne ? |
| 3 | **User control and freedom** | Undo, back, escape, annulation ? |
| 4 | **Consistency and standards** | Cohérence avec le reste du produit + conventions web ? |
| 5 | **Error prevention** | Design qui empêche les erreurs avant qu'elles arrivent ? |
| 6 | **Recognition rather than recall** | Options visibles plutôt qu'à mémoriser ? |
| 7 | **Flexibility and efficiency of use** | Raccourcis, personalisation pour power users ? |
| 8 | **Aesthetic and minimalist design** | Chaque élément ajoute-t-il de la valeur ? |
| 9 | **Help users recognize, diagnose, recover from errors** | Messages clairs + solution actionnable ? |
| 10 | **Help and documentation** | Aide contextuelle accessible, concise ? |

## Détails par heuristique

### 1. Visibility of system status
- Loading states (feedback < 100 ms idéal, spinner > 1 s)
- Etat d'un bouton après click
- Progression dans un flow (step 2 of 5)
- Statut "sauvegardé" visible
- Pour les long-running : ETA + cancel

### 2. Match real world
- Termes métier (pas "Commit" → "Enregistrer")
- Icônes conventionnelles (loupe = recherche, pas "Θ")
- Ordre logique (lire de haut-gauche)
- Dates, nombres, devises au format local

### 3. User control & freedom
- Back button navigateur fonctionne
- Undo pour actions destructives
- Escape ferme les modals
- Pas de piège (impossible de sortir d'un flow sans le compléter)

### 4. Consistency
- Même mot = même action partout (pas "Delete" ici, "Supprimer" là, "Remove" ailleurs)
- Boutons primary toujours à la même position
- Icônes même style, même taille
- Adhérer aux standards plateforme (iOS HIG, Material, web)

### 5. Error prevention
- Validation inline (vs post-submit)
- Confirmation pour destructif ("Êtes-vous sûr ?")
- Auto-save
- Formats contraints (date picker, pas input libre)
- Disable action impossible avec raison

### 6. Recognition > recall
- Dropdown avec options visibles > input vide
- Recents, favorites, suggestions
- Breadcrumbs
- Preview avant action

### 7. Flexibility
- Keyboard shortcuts pour power users
- Batch actions
- Personalisation (tri, filtres persistants)
- Mode expert optionnel

### 8. Aesthetic & minimalist
- Enlever tout ce qui n'aide pas la tâche principale
- Ratio signal/bruit élevé
- Pas de décoration gratuite

### 9. Error recovery
- Langage naturel, pas de code ("Erreur 500" → "Problème technique")
- Explique le quoi + le comment-fixer
- Lien vers recovery ("Contacter le support", "Réessayer")
- Icon + couleur sémantique (red-500)

### 10. Help
- Help contextuel (tooltip, inline)
- Search dans la doc
- Exemples concrets > abstrait
- Video > texte pour flows complexes

## Severity scoring (Nielsen)

| Sev | Label | Effet | Action |
|---|---|---|---|
| 0 | Non-problème | Pas vraiment un problème | Ignorer |
| 1 | Cosmetic | Problème mineur, pas bloquant | Backlog, si temps |
| 2 | Minor | Problème réel mais pas bloquant | Sprint suivant |
| 3 | Major | Bloque ou dégrade fortement | **Fixer avant ship** |
| 4 | Catastrophic | Perte de données, impossible à utiliser | **Fixer immédiatement** |

Critères :
- **Fréquence** : combien d'users touchés ?
- **Impact** : sévérité pour l'user touché ?
- **Persistence** : user bloqué ou peut contourner ?

## Processus d'évaluation

1. **Préparation** : définir les écrans/flows à évaluer, le persona cible.
2. **1er passage** : évaluer globalement, noter les problèmes "qui sautent aux yeux".
3. **2e passage** : systématique, heuristique par heuristique.
4. **Scoring** : pour chaque issue, noter heuristique + sévérité + emplacement + fix proposé.
5. **Consolidation** (si plusieurs évaluateurs) : fusionner, déduplicater, négocier les severities.
6. **Report** : issues par severity décroissante, fix proposés prioritaires.

## Limites de l'heuristic eval

- Ne remplace PAS les tests utilisateurs (catch ~30-50% des problèmes réels)
- Meilleur combiné : heuristic eval + tests utilisateurs légers
- Biais d'évaluateur (expert ≠ user)
- Moins utile pour features très novatrices (heuristiques sont génériques)

## Quand l'utiliser

- Avant un premier test utilisateur (sortir les low-hanging fruits)
- Avant un merge important
- En audit post-launch pour trouver l'origine d'une baisse de conversion
- Quand le budget test utilisateur manque
