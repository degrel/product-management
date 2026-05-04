---
name: bilme
description: "Bill me" — génère le suivi temps mensuel Payfit à partir d'Apple Calendar. Agrège les events en demi-journées (matinée/après-midi), infère l'activité PM dominante, mappe vers les projets Payfit officiels (R&D/Factory, R&D/RoadMap/ProductManagement, R&D/Retail/ZoneInsight, R&D/Power Bi, R&D/G4E&Cloud, Encadrement, CSM/CREDIT-MUT, etc.). Use when the user says "/bilme", "suivi temps", "remplir Payfit", "feuille de temps", "suivi mensuel", "saisie Payfit", or asks to declare time for a specific month.
---

# Suivi temps mensuel Payfit

## Purpose

Produire un tableau prêt à recopier dans Payfit pour un mois donné, à partir des events Apple Calendar du PM (Grégoire). Une ligne par demi-journée, projet Payfit officiel issu du CSV de référence.

## Inputs

- **Mois cible** : si non spécifié → mois précédent si on est avant le 5 du mois, sinon mois en cours.
- **Année cible** : par défaut, l'année du mois cible.

Demande à l'user uniquement si le mois est ambigu.

## Étape 1 — Extraire les events

Exécuter le script AppleScript de la skill, qui retourne un TSV `calendar / date / start / end / summary` pour les calendars `Calendrier` (events perso) et `Jours fériés - France` (fériés).

```bash
osascript /Users/gregoire/Dev/product-management/.claude/skills/bilme/extract-calendar.applescript <MONTH> <YEAR>
```

**Filtres importants** :
- Garder uniquement les events du calendar **`Calendrier`** pour la classification.
- Utiliser **`Jours fériés - France`** pour marquer les jours fériés (matinée + après-midi → vide, total 0j).
- **Ignorer** les calendars `Absences Payfit`, `Fêtes (France)` — ce sont les TT/absences des collègues, pas les miens.

## Étape 2 — Découpage en demi-journées

Pour chaque jour ouvré (lun-ven hors fériés) :

| Tranche | Règle |
|---|---|
| Matinée | events qui démarrent **< 13h00** |
| Après-midi | events qui démarrent **≥ 13h00** |
| Event journée entière (`00:00 → 23:59`) | marque les deux demi-journées |
| Event traversant 13h (ex. 11h-14h) | compte sur la demi-journée majoritaire en durée |
| Event court (≤ 30 min) sans contexte | poids faible — ignoré si une autre activité dominante existe sur la même demi-j |

**Cas particuliers** :
- Réunion qui dure une journée entière (ex. réunion annuelle 9h-18h) → projet appliqué matinée + après-midi.
- Mercredi/Vendredi avec « Télétravail » : ignorer ce label, ne pas l'utiliser comme projet — garder l'event de fond.
- Standup, points courts (< 30 min) sur fond de focus work : utilise l'event le plus long de la demi-j comme signal dominant.

## Étape 3 — Classification → projet Payfit

Charger `payfit-projects.csv` (même dossier que cette skill). Pour chaque demi-journée :

1. Concaténer en minuscules les titres d'events de la demi-j.
2. Tester chaque ligne du CSV dans l'**ordre de la colonne `priority`** (10 = testé en premier).
3. Pour chaque ligne, tester les regex de la colonne `keywords` (séparées par `|`) sur le texte agrégé.
4. Le **premier match** gagne → utilise `payfit_label` comme projet.
5. Si plusieurs events de la demi-j matchent des projets différents, choisir celui avec la **plus longue durée cumulée** (en minutes).
6. Aucun match → utiliser le **fallback** : la ligne du CSV avec `bucket_key=__fallback__` (par défaut `R&D/Factory`). Marquer la sortie d'un `*` pour indiquer que c'est un fallback (pas un match calendrier).
7. Pour changer le projet par défaut, éditer la première ligne du CSV (`__fallback__`).

### Heuristiques de tie-break (issues de retours user)

| Situation | Décision |
|---|---|
| Sprint mgmt (rétro/planning/prépa sprint) sans contexte projet explicite | `R&D/RoadMap/ProductManagement` |
| Sprint orienté Factory (« sprint Factory ») | `R&D/Factory` |
| Sprint orienté Étude de zone | `R&D/Retail/ZoneInsight` |
| Réunion annuelle CM/EI (toute la journée) | `CSM/CREDIT-MUT` (tout traverse) |
| Tests techniques recrutement, coaching, Naélys, Gabriel, EI/CM prépa, pilotage | `Encadrement` |
| Maquettes site v3 / GTM PowerBI / naming PowerBI | `R&D/Power Bi` (pas Encadrement, pas Factory) |
| Naming & packaging des offres → Encadrement (positioning), sauf si explicitement PowerBI | `Encadrement` |
| Import de données / nouvel éditeur de couches / releases on-prem | `R&D/G4E&Cloud` |
| Étude de zone, RetailFocus, Tryba, Refashion, RZI | `R&D/Retail/ZoneInsight` |
| Conception/Maquettes Factory ou Azimut | `R&D/Factory` |
| Lundi de Pâques, 1er & 8 mai, Ascension, lundi de Pentecôte, 14 juillet, 15 août, Toussaint, 11 nov, Noël | **férié — 0j** (même si event présent) |
| Vendredi saint, 26 décembre | ⚠️ férié **uniquement en Alsace-Moselle** — pour Galigeo (Paris), c'est un **jour ouvré normal**, ne pas marquer férié |

## Étape 4 — Format de sortie (strict)

Reproduire exactement la mise en page Payfit, semaine par semaine :

```
S<NN>  <Xj>

<Jour>
<Mois> <Numéro>
Matinée    <payfit_label>
Après-midi <payfit_label>
Total      <Xj>

(répéter pour chaque jour de la semaine, samedi et dimanche → vides, total 0j)
```

Exemple validé (avril 2026, S14) :

```
S14  3j

Mercredi
Avril 1
Matinée    R&D/Retail/ZoneInsight (GGO - R&D)
Après-midi R&D/Factory (GGO - R&D/Factory)
Total      1j

Jeudi
Avril 2
Matinée    R&D/RoadMap/ProductManagement (GGO - R&D)
Après-midi Encadrement (GGO - Encadrement)
Total      1j

Vendredi
Avril 3
Matinée    —
Après-midi —
Total      0j   (Jour férié — Vendredi saint)
```

À la fin du mois :

```
Total avril 2026 : <X>j travaillés / <Y> férié(s)
Répartition par projet :
- R&D/Factory ............ 6 demi-j  (3,0j)
- Encadrement ............ 8 demi-j  (4,0j)
- ...
```

## Anti-patterns

- ❌ Inventer un projet absent du CSV. Si une demi-j ne match rien → utiliser le fallback CSV (marqué d'un `*`), pas inventer.
- ❌ Remplir un projet sur un jour férié.
- ❌ Étiqueter « Télétravail » comme projet.
- ❌ Compter une demi-journée sans event comme `0j` automatiquement — c'est probablement du focus work non-calendarisé. Appliquer le fallback CSV (`*`).

## Sortie attendue

1. Tableau format Payfit (semaine par semaine).
2. Liste des `?` à confirmer avec l'user.
3. Récap mensuel (total + répartition par projet).
4. Pas de phrase d'intro, pas de conclusion — juste le tableau et le récap.

## Évolution du CSV

Si l'user corrige systématiquement un mapping (ex. « Naming → R&D/Power Bi » au lieu de `Encadrement`), proposer d'ajouter le mot-clé à la ligne correspondante du CSV. Ne pas modifier le CSV sans confirmation explicite.
