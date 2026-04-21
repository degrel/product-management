---
name: Challenge prompts
type: prompts
---

# Challenge Prompts — Pour faire challenger ton travail PM

Bibliothèque de prompts prêts à l'emploi, adossés au contenu "Leadership du revenu". À coller tels quels ou à adapter. Chaque prompt indique les fichiers de knowledge à charger en priorité.

---

## 1. Challenge mon ICP / ma segmentation

> **Contexte Galigeo** : Territory Manager sert à la fois des Directeurs Développement (SLG), des analystes data (potentiel PLG), et des Network Managers. On hésite à mettre tout le monde dans le même ICP.

**Prompt** :
```
Charge knowledge/revenue/frameworks/icp-segmentation-spiced.md et knowledge/revenue/frameworks/plg-vs-slg-decision.md. 

Challenge mon ICP actuel avec SPICED. Spécifiquement :
- Est-ce que je mélange des personas qui ont des Pains et des Critical Events différents ?
- Mes Tier 1/2/3 sont-ils définis par des critères SPICED explicites ou par intuition ?
- Est-ce que j'utilise l'Impact émotionnel du décideur (pas juste le rationnel entreprise) ?
- La "salle de décision" chez mes cibles Tier 1 est-elle documentée (7 rôles) ?

Pose-moi les questions qui me forceront à expliciter et à faire remonter les contradictions.
```

---

## 2. Challenge ma roadmap sur l'arbitrage PLG ↔ SLG

> **Contexte Galigeo** : On a des features qui servent les deux motions, d'autres qui ne servent qu'une seule. Quelle proportion de la roadmap allouer à quoi ?

**Prompt** :
```
Charge knowledge/revenue/frameworks/plg-vs-slg-decision.md et knowledge/revenue/sessions/03-plg-to-slg.md.

Challenge ma roadmap trimestrielle :
- Quelle proportion sert explicitement le PLG (self-serve, activation rapide, onboarding produit) ?
- Quelle proportion sert explicitement le SLG (features "paillettes", certifications, sécurité, reporting C-level) ?
- Quelle proportion est "neutre" — et est-ce que "neutre" ne veut pas dire "ne sert bien aucune des deux motions" ?
- Avec ~[X M€ d'ARR], est-ce qu'on est en état de tenir les deux motions ou est-ce qu'on se disperse ?

Pour chaque feature de ma roadmap, note-la sur les 3 critères : Impact New Business / Impact Rétention / Faisabilité. Signale les features faibles sur les 3 axes.
```

---

## 3. Challenge mes KPIs produit

> **Contexte** : On a un dashboard NSM + NPS + retention mais rien sur le funnel bowtie.

**Prompt** :
```
Charge knowledge/revenue/frameworks/bowtie-winning-by-design.md.

Mes KPIs produit actuels sont : [liste]. 

Challenge-moi sur :
- Quels CR (1-8) du bowtie je ne mesure pas et qui expliqueraient mieux mes problèmes ?
- Quel couple d'indicateurs pourrait révéler un problème caché (ex : CR4 élevé + CR5 élevé = survente) ?
- Est-ce que je mélange des métriques "pilotables produit" avec des métriques "business" sans savoir quel levier je tire ?
- À quel niveau de benchmark suis-je (sectoriel, pairs, concurrent, soi-même) ? Quels outils utiliser pour progresser (benchsights.com/wbd) ?
```

---

## 4. Challenge mon onboarding

> **Contexte** : On a un onboarding "tour guidé" pour les petits comptes et un onboarding "accompagné CSM" pour les gros. CR5 pas tracké clairement.

**Prompt** :
```
Charge knowledge/revenue/frameworks/bowtie-winning-by-design.md et knowledge/revenue/sessions/02-mesurer-analyser-performance.md.

Mon onboarding actuel : [description].

Challenge :
- Je mesure T5 (durée onboarding) ? Je le mesure différemment pour PLG vs SLG ?
- Mon CR5 (onboarding churn) est quoi ? Dans quelle fourchette benchmark ?
- Est-ce que T5 court + CR6 élevé révèle un onboarding expédié ? OU T5 long + CR6 élevé révèle un onboarding poussif qui décourage ?
- Est-ce que mes activations PLG mesurent une adoption RÉELLE ou juste "l'utilisateur a cliqué sur X" ?
- Quels "aha moments" sont atteints / pas atteints par persona ?
```

---

## 5. Challenge ma stratégie Expansion (upsell/crossell/resell)

> **Contexte** : On sait faire des upsells (+seats). Les crossells entre modules fonctionnent mal. Le resell (champion qui change de boîte) est inexploré.

**Prompt** :
```
Charge knowledge/revenue/frameworks/icp-segmentation-spiced.md (matrice d'expansion 2×2) et knowledge/revenue/sessions/02-mesurer-analyser-performance.md.

Sur la matrice 2×2 (Acheteur × Impact) :
- Renouvellement : même acheteur, même impact → mes processus ?
- Upsell : même acheteur, autre impact → mes leviers ?
- Crossell : autre acheteur, même impact → comment j'identifie l'autre acheteur chez mon client existant ?
- **Resell** : autre acheteur (champion parti), autre/même impact → ai-je un process pour suivre les champions qui changent de boîte ? C'est "le grand oublié".

Challenge-moi sur les leviers que je ne mobilise pas. Donne-moi les 3 actions à tester en priorité.
```

---

## 6. Challenge mon pricing / packaging

> **Contexte** : On a 3 plans Territory Manager (Starter / Pro / Enterprise). Le Starter cannibalise parfois le Pro.

**Prompt** :
```
Charge knowledge/revenue/frameworks/business-models-saas.md.

Mon pricing actuel : [description 3 plans + ACV moyen par plan].

Challenge :
- Sur l'arc Propriété/Abonnement/Consommation, où se situent mes plans ? Sont-ils cohérents entre eux ?
- Ratio LTV/CAC par plan : lesquels financent leur propre acquisition (>3) ?
- CAC payback par plan : sous ou au-dessus de 24 mois ?
- Est-ce que le Starter sous-service les petits clients qui ne sont pas mon ICP, ou sert vraiment de porte d'entrée PLG ?
- Les "features paillettes" du plan Enterprise : déclenchent-elles vraiment l'achat ? Ou c'est du coût porté ?
```

---

## 7. Challenge ma décision de lancer une nouvelle motion GTM

> **Contexte** : On pense ouvrir un 2e GTM (par ex. PLG pour TM sur un segment SMB, alors qu'on est SLG aujourd'hui).

**Prompt** :
```
Charge knowledge/revenue/frameworks/plg-vs-slg-decision.md et knowledge/revenue/sessions/03-plg-to-slg.md.

On pense ouvrir un 2e GTM : [description].

Challenge-moi sur les conditions préalables :
- Mon GTM actuel génère-t-il au moins 5 M€ d'ARR solide avant de se disperser (seuil empirique français) ?
- Si je veux tenir 2 GTM en parallèle, ai-je au moins 20 M€ d'ARR ? Sinon, est-ce que j'ouvre temporairement ou définitivement ?
- Ma cible du 2e GTM achète-t-elle vraiment autre chose (produit vs service) ? Ou c'est la même chose empaquetée autrement ?
- Qui va diriger ce 2e GTM ? Si c'est "le même manager", c'est un signal de faiblesse (les 2 GTM ont des logiques de croissance différentes : bouche à oreille vs thought leadership vs marque).
- Risque de cannibalisation : mes Grands Comptes actuels voient le self-serve comme un signal de baisse de service ?
```

---

## 8. Challenge mon alignement Product / Marketing / Sales / CS

> **Contexte** : Le produit est critiqué par Sales ("manque telle feature"), tandis que le CS demande autre chose.

**Prompt** :
```
Charge knowledge/revenue/frameworks/icp-segmentation-spiced.md et knowledge/revenue/sessions/03-plg-to-slg.md.

Nos 4 fonctions (Marketing, Sales, CS, Product) sont-elles alignées sur SPICED ?

- Même définition du Pain client ? Même Impact (rationnel + émotionnel) ?
- Les features demandées par Sales servent l'Impact du décideur ou juste le confort de l'utilisateur ?
- Les demandes CS sont-elles des problèmes de Pain (produit) ou de Service (organisation) ?
- Ai-je un Critical Event commun qui structure le cycle de vente ?

Identifie les 3 désalignements les plus coûteux et propose une résolution.
```

---

## 9. Challenge mes choix de stade de croissance

> **Contexte** : On est à X M€ d'ARR, on veut accélérer / lever / restructurer.

**Prompt** :
```
Charge knowledge/revenue/frameworks/growth-stages-gtm.md et knowledge/revenue/sessions/04-stades-de-croissance.md.

Nous sommes à [X M€ ARR, Y % croissance, Z % EBITDA].

Challenge :
- Sur la courbe en S, où suis-je ? Phase 1 (démarrage lent), 2 (accélération), 3 (saturation) ?
- Camp de base validé ? BM aligné valeur ? Founder Sales Led dépassé ? Modèle de données en place ? Organisation GTM ?
- Rule of 40 respectée ? Trajectoire T2D3 tenue ?
- Quel est LE point de passage critique du stade actuel que je risque de manquer ?
- Risques de "mal des montagnes" : injecter trop de cash avant GTM Fit ?
```

---

## 10. Challenge ma décision sur une hire commerciale / product

> **Contexte** : On va recruter notre premier Head of Product ou un CSM Lead.

**Prompt** :
```
Charge knowledge/revenue/frameworks/coaching-performance-culture.md.

Le rôle à recruter : [description].

Challenge :
- Est-ce que je recrute une "superstar" (hero fragile) ou un "process builder" (construira le système) ? Pyramide Deming 85/15.
- Ai-je les 4 fondamentaux en place (process, tech, enablement, skills) pour que cette personne réussisse ?
- Mes scorecards pour ce rôle sont-elles explicites (pas "débrouillez-vous") ?
- Mon gap actuel : compétence ou système ? RESA dit quoi ?
- Si la personne sous-performe dans 6 mois, serai-je capable de dire si c'est coaching / recrutement / système cassé ?
```

---

## Méta-prompt : laisser Claude choisir

Si tu ne sais pas quel angle attaquer :

```
Charge knowledge/revenue/README.md. 

Voici ma situation / ma décision / mon doc : [description].

Quel(s) framework(s) parmi ceux disponibles est le plus pertinent pour me challenger ? Charge-le et challenge-moi.
```
