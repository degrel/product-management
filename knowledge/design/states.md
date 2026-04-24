# Les 7 états à toujours dessiner

Pour chaque écran avec des données, dessiner ces 7 états. Oublier un état = bug en prod.

## 1. Empty first-use (jamais rien eu)

Le user ouvre pour la première fois. L'écran est vide **parce que normal**.

Objectif : pédagogie + première action.

Template :
- Illustration légère (ou absence d'illustration — acceptable si design dense)
- Headline : "Aucune zone pour l'instant" (ou équivalent métier)
- Body : 1 phrase expliquant la valeur. "Crée ta première zone pour analyser un territoire."
- CTA primary unique : "Créer une zone"
- Parfois : lien doc / vidéo "Voir un exemple"

## 2. Empty post-action (tout supprimé)

Différent du first-use : le user SAIT déjà à quoi sert l'écran, il a juste tout vidé.

- Pas d'illustration lourde
- Body court : "Aucune zone active"
- CTA : "Créer une zone" OU "Restaurer depuis la corbeille"

## 3. Loading

- **< 300 ms** : rien (n'afficher aucun état de chargement, l'humain ne le perçoit pas)
- **300 ms - 1 s** : skeleton de la forme finale (cartes grises aux bonnes dimensions)
- **1-10 s** : skeleton + message contextualisé ("Calcul en cours...")
- **> 10 s** : progress bar explicite + cancel button

Don't : spinner générique au centre de l'écran quand on connaît la forme finale.

## 4. Partial (chargement progressif)

Data arrive par morceaux (streaming, pagination).

- Éléments chargés = normaux
- Éléments en attente = skeleton à leur position future
- Pas de "saut" visuel quand la data arrive

## 5. Error

Types d'erreurs :
- **Réseau** : connexion perdue → "Connexion perdue. [Réessayer]"
- **Permission** : 403 → "Tu n'as pas accès à cette zone. [Demander l'accès]"
- **Serveur** : 500 → "Un problème technique. On enquête. [Réessayer]"
- **Validation** : 400 → inline sur le champ fautif
- **Not found** : 404 → "Cette zone n'existe pas ou a été supprimée. [Retour à la liste]"

Règles :
- Message **expliquant le quoi + le fix** ("Le champ téléphone est invalide. Format : 06 12 34 56 78.")
- CTA de recovery (retry, back, contact support)
- Jamais de message "Error 500" à un end user

## 6. Single item (1 item seul)

Piège : mockup dessiné avec 5 items, en prod avec 1 item = écran 90% vide.

- Card/item garde sa taille
- Padding généreux autour OK
- Ajouter un CTA "Créer un autre" ou "Voir un exemple"

## 7. Many items (N très grand)

- **≥ 100 items** : virtualisation (ne render que les visibles, ex. react-window)
- **≥ 20 items** : pagination OU filtres OU search
- **Scroll infini** : uniquement si le user scrolle vers du contenu nouveau (feed, pas pour un settings)
- **Top/sticky header** : filtres, search, total

## Edge cases data à considérer

Pour chaque champ affiché, vérifier :

- [ ] Texte très long → truncation avec tooltip / expand
- [ ] Texte vide → placeholder ou "—"
- [ ] Date invalide / null → "N/A"
- [ ] Nombre très grand / négatif → formatage, unités
- [ ] Devise multiples → localisation
- [ ] Emoji / RTL / caractères spéciaux → fonctionne
- [ ] URL trop longue → truncation intelligente

## Template inventaire état

```markdown
## États — [écran]

| État | Trigger | Visuel | Copy | CTA |
|------|---------|--------|------|-----|
| Empty first | 1re visite, 0 data | [ref Figma] | [...] | Créer |
| Empty post | Post-suppression | [ref] | [...] | Créer |
| Loading | Fetch initial | Skeleton | — | — |
| Partial | Data streaming | Mix skeleton/data | — | — |
| Error réseau | Fetch fail | Banner | Connexion perdue | Retry |
| Error 403 | Forbidden | Full screen | Accès refusé | Demander |
| 1 item | | | | |
| N items | | | | |
```
