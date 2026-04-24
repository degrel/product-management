# Hook Model (Nir Eyal)

Boucle habit-forming qui connecte le problème de l'user à ton produit assez fréquemment pour créer une habitude.

```
Trigger → Action → Variable Reward → Investment ─╮
   ↑                                              │
   ╰──────────────────────────────────────────────╯
```

## 1. Trigger

Le déclencheur. Deux formes :
- **External** : notif, email, bouton, bouche-à-oreille. Rôle : amorcer les premiers cycles.
- **Internal** : émotion (ennui, solitude, FOMO, incertitude). Goal : passer de external → internal en < 30 jours.

**Mapper le produit à une émotion précise** :
- Instagram ↔ ennui
- Google ↔ incertitude
- WhatsApp ↔ solitude
- Facebook ↔ loneliness + FOMO

**Application** :
- Onboarding : external trigger avec 1 action claire
- Retention : identifier l'émotion résolue, la nommer
- Re-engagement : external triggers jusqu'à ce que internal se forme
- Ethique : ne pas exploiter détresse (deuil, addiction, dépression)

## 2. Action (Fogg Behavior Model)

**B = M × A × T**

Un comportement arrive SEULEMENT si motivation + ability + trigger sont présents simultanément.

**Les 6 éléments d'ability (simplicité)** :
1. Temps
2. Argent
3. Effort physique
4. Brain cycles
5. Déviance sociale
6. Non-routine

**Règle** : augmenter ability (réduire friction) est presque toujours plus efficace qu'augmenter motivation.

**Applications** :
- Signup : 1-click Google/Apple > form long
- Core action : < 60 s pour compléter
- Progressive disclosure : demander peu, révéler plus après reward
- Defaults intelligents > questions

## 3. Variable Reward

La phase qui garde les users. **L'anticipation d'un reward incertain** déclenche la dopamine — pas le reward lui-même.

**3 types** (souvent combinés) :
- **Tribe** : validation sociale (likes, commentaires, partages). Ex : Instagram.
- **Hunt** : chasse d'info ou de ressources. Ex : feed Twitter, scroll Pinterest.
- **Self** : accomplissement personnel (mastery, progression). Ex : Duolingo streak.

**Règles** :
- Predictable rewards = lose power over time
- Finite variability (catalogue fini) finit par devenir prévisible → aim for infinite variability
- Autonomy critique — forced engagement backfires

**Application** :
- Notifications variées ("3 likes" vs "Sarah a commenté")
- Feed algo varié
- Unexpected badges / achievements
- Pour B2B : "new insight", "benchmark comparison"

## 4. Investment

La phase qui augmente la probabilité du prochain cycle. User investit quelque chose — temps, data, réputation, contenu — qui **améliore le prochain cycle** et **augmente le switching cost**.

**Types d'investment** :
- **Data** : préférences, historique → personnalisation
- **Content** : posts, notes, projets créés
- **Reputation** : reviews, rating, followers
- **Skill** : expertise sur l'interface (vim, Photoshop)
- **Social** : connexions, groupes

**Règles** :
- Investment APRÈS reward, jamais avant
- Chaque investment doit **charger le prochain trigger** (ex : poster → notif quand qqn répond)
- IKEA effect : on valorise ce qu'on a construit, même irrationnellement
- Small investments compound

## Habit Zone

Produit entre en habit zone si :
- **Fréquence** d'usage élevée (daily / weekly)
- **Valeur perçue** élevée à chaque usage

|  | Low frequency | High frequency |
|---|---|---|
| **High value** | Vitamine (needs marketing) | **Habit zone** ✅ |
| **Low value** | Failure | Failure |

## Habit testing — la règle des 5%

Un produit a formé une habitude quand ≥ 5% des users montrent un usage spontané, non-prompté.

**3 questions** :
1. **Qui** sont les habituels ? (segment, usage)
2. **Que** font-ils ? (habit path = sequence d'actions)
3. **Pourquoi** ? (émotion, internal trigger)

## Manipulation Matrix — éthique

|  | Maker uses | Maker doesn't |
|---|---|---|
| **Improves life** | Facilitator ✅ | Peddler ⚠️ |
| **Doesn't improve** | Entertainer 🟡 | Dealer 🔴 |

**3 questions avant d'ajouter un hook** :
1. L'utiliserais-je moi ?
2. Aide-t-il vraiment l'user à atteindre SON but ?
3. Exploite-t-il une vulnérabilité ?

Si Dealer/Peddler → changer l'approche.

## Ne PAS utiliser le Hook Model si

- Produit n'améliore pas vraiment la vie
- Users vulnérables (enfants, addictifs)
- Business model dépend du regret user
- Engagement s'oppose au wellbeing

## Checklist onboarding pour habit formation

### First trigger
- [ ] 1re action claire et facile
- [ ] Valeur proposition visible avant demande d'investment
- [ ] External trigger approprié

### First action
- [ ] Core action < 60 s
- [ ] Friction minimum
- [ ] UI familière

### First reward
- [ ] Feedback immédiat
- [ ] Élément variable / surprise
- [ ] Connexion à internal trigger

### First investment
- [ ] Investment APRÈS reward
- [ ] Petit mais significatif
- [ ] Charge le prochain trigger

### Loop completion
- [ ] Chemin clair vers le prochain trigger
- [ ] Triggers envoyés au bon moment
- [ ] Mesure de progression dans le Hook

## Erreurs courantes

| Erreur | Effet | Fix |
|---|---|---|
| External triggers indéfiniment | Pas de formation d'internal trigger | Mapper émotion, transition en < 30 jours |
| Action trop complexe | Drop-off avant reward | Simplifier au minimum viable |
| Predictable rewards | Engagement dropoff | Variabilité tribe/hunt/self |
| Investment avant reward | Rejet | Toujours : trigger → action → reward → investment |
| Ignorer l'éthique | Regret user, churn, réputation | Manipulation Matrix |

Source complète : *Hooked* de Nir Eyal (ISBN 978-1591847786).
