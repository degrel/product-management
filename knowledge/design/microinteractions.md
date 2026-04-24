# Microinteractions (Saffer)

> Source : `skills-main/microinteractions/SKILL.md`.

Une microinteraction = un moment où l'utilisateur fait UNE chose et le produit répond. Désactiver une notif, liker, refresh, toggle dark mode.

## Les 4 éléments à toujours spécifier

### 1. Trigger
Ce qui déclenche.
- **Manuel** : click, tap, hover, focus, keyboard shortcut
- **Système** : data arrive, erreur, seuil atteint, time-based
- **Ambient** : sensor (GPS, microphone), position du scroll

Règle : le trigger doit être **évident** (Norman : affordance + signifier). Hover ≠ évident sur mobile.

### 2. Rules
Ce qui détermine ce qui se passe.
- Input requis : quoi faut-il pour déclencher ?
- Manipulations possibles : undo, cancel, abort ?
- État final : que se passe-t-il après ?
- Erreurs possibles et comportement : retry ? fallback ?

### 3. Feedback
Le retour visuel / sonore / haptique.
- **Optique** : couleur, shape, position, animation
- **Auditif** : beep, swoosh, voice
- **Haptique** : vibration (mobile)

**Timing** :
- < 100 ms : instantané (click feedback, toggle)
- 100-300 ms : perception de réactivité (hover, state change)
- 300-1000 ms : acceptable si feedback progressif (loading bar)
- > 1 s : afficher progression explicite + estimated time

### 4. Loops & modes
- **Loop** : la microinteraction se répète-t-elle ? Varie-t-elle avec le temps (gamification, évolution UX) ?
- **Mode** : y a-t-il des états différents (editing vs viewing, online vs offline) ?

## Timing par type d'action

| Action | Timing | Easing |
|---|---|---|
| Button press | 100-150 ms | ease-out |
| Hover | 100-200 ms | ease-out |
| Toggle state | 150-200 ms | ease-in-out |
| Dropdown open | 200-250 ms | ease-out |
| Modal enter | 250-300 ms | ease-out |
| Modal exit | 200 ms | ease-in |
| Page transition | 300-400 ms | ease-in-out |
| Celebratory (success) | 400-600 ms | ease-out + bounce |

## Principes de motion

- **Purposeful** : chaque animation doit servir une compréhension (où vient l'élément, où il va, hiérarchie).
- **Natural** : ease-out pour entrées (ralentit comme dans la réalité), ease-in pour sorties.
- **Reversible** : l'animation d'ouverture + l'animation de fermeture doivent s'inverser visuellement.
- **Respect `prefers-reduced-motion`** : réduire à 0.01 ms (pas zéro, pour garder les events).

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

## Patterns communs

### Button press
Click → bouton descend de 1 px + background légèrement plus foncé + cursor reste, 150 ms.

### Input focus
Focus → border accent color + subtle shadow (ring), 150 ms.

### Toggle
Click → thumb slide + track color change, 200 ms, ease-in-out. Feedback haptique sur mobile.

### Toast notification
Enter : slide in + fade, 250 ms, ease-out. Reste 4-5 s. Exit : fade out + slide, 200 ms.

### Form validation
Inline : apparaît 500 ms après blur du champ (évite l'anxiété pendant la saisie). Erreur = red-500 + icône + message sous le champ.

### Loading
- < 300 ms : rien (flash inutile)
- 300 ms - 1 s : skeleton de la forme finale
- 1 s - 10 s : spinner + message contextualisé ("Calcul des zones...")
- > 10 s : progress bar explicite + cancel possible

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Animation > 500 ms sur action fréquente | Raccourcir à 200-300 ms |
| Spinner pour tout | Skeleton quand forme connue |
| Bounce/elastic partout | Réserver aux moments célébratoires |
| Hover-only interactions (mobile) | Toujours une alternative tap |
| Shake violent sur erreur | Subtle shake + message clair |
| Pas de feedback sur action | Minimum 100 ms visuel |
