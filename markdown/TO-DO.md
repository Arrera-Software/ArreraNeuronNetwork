# Liste des Améliorations et Corrections de Bugs

Ce document résume les points d'amélioration prioritaires pour fiabiliser le projet, réduire les risques de bugs et faciliter la maintenance future.

---

### 1. Fiabilisation des Appels Réseau et API

**Problème :** Les interactions avec les services externes (météo, actualités, etc.) sont fragiles et peuvent faire planter l'application en cas d'imprévu.

**Actions à entreprendre :**

-   **Gestion complète des erreurs réseau :**
    -   Dans les fonctions qui utilisent `requests.get` (ex: `fnc/fonctionMeteo.py`), ne vous contentez pas d'un simple `try...except`.
    -   Vérifiez systématiquement le code de statut de la réponse : `if response.status_code == 200:`.
    -   Gérez les autres cas (404, 500, etc.) en retournant une erreur explicite ou une valeur par défaut claire.

-   **Parsing JSON sécurisé :**
    -   Remplacez les accès directs aux dictionnaires comme `data["key"]` par la méthode `.get("key", "valeur_par_défaut")`.
    -   Cela évitera les plantages (`KeyError`) si l'API modifie sa structure de réponse.

-   **Centraliser la gestion des erreurs API :**
    -   Au lieu de retourner `True` ou `False`, propagez des exceptions personnalisées (ex: `class NetworkError(Exception): pass`) ou des objets de résultat plus riches pour que la fonction appelante sache précisément ce qui s'est mal passé.

**Fichiers concernés :** `fnc/fonctionMeteo.py`, `fnc/fonctionActu.py`, `neuron/API.py` et tout autre fichier faisant des appels réseau.

---

### 2. Simplification de l'Architecture et de la Gestion de l'État

**Problème :** L'architecture actuelle, très centralisée autour du `gestionnaire`, crée un couplage fort et des dépendances difficiles à suivre, ce qui rend les modifications risquées.

**Actions à entreprendre :**

-   **Réduire les responsabilités du `gestionnaire` (God Object) :**
    -   Déplacez la logique spécifique dans des classes plus petites et dédiées. Par exemple, la gestion de l'historique pourrait être entièrement contenue dans `gestHistorique` sans que le `gestionnaire` ait besoin de connaître les détails.

-   **Casser les dépendances circulaires :**
    -   Revoyez l'initialisation de `gestNeuron` et `gestionnaire` pour qu'ils ne dépendent pas l'un de l'autre de manière circulaire. Utilisez l'injection de dépendances de manière plus stricte.

-   **Rendre la gestion de l'état explicite :**
    -   Dans `neuron/API.py` pour le GPS, au lieu de stocker `__depart` et `__arriver` dans des variables de classe, passez-les en paramètres des fonctions qui en ont besoin. Cela rend le flux de données plus prévisible.

**Fichiers concernés :** `gestionnaire/gestion.py`, `gestionnaire/gestNeuron.py`, `neuron/API.py`.

---

### 3. Amélioration de la Réactivité de l'Interface Graphique (GUI)

**Problème :** L'interface utilisateur risque de se "figer" (freeze) à chaque appel réseau, car ces opérations sont synchrones et bloquantes.

**Actions à entreprendre :**

-   **Rendre les appels réseau asynchrones :**
    -   Utilisez le module `threading` pour exécuter les requêtes réseau (comme la récupération de la météo) dans un thread séparé.
    -   Une fois la donnée reçue, utilisez un mécanisme de file d'attente (`queue`) ou un événement pour mettre à jour l'interface graphique depuis le thread principal en toute sécurité.

**Fichiers concernés :** `main.py` (pour démarrer le thread), `fnc/fonctionMeteo.py` et les autres fonctions réseau.

---

### 4. Amélioration de la Qualité et de la Maintenabilité du Code

**Problème :** Certaines pratiques de code rendent le projet difficile à lire et augmentent le risque d'erreurs cachées.

**Actions à entreprendre :**

-   **Supprimer les imports "sauvages" (`*`) :**
    -   Remplacez tous les `from mon_module import *` par des imports explicites : `from mon_module import ma_fonction, ma_classe`.
    -   Cela clarifie d'où vient chaque fonction et évite les conflits de noms.

-   **Corriger le style de code (PEP 8) :**
    -   Utilisez un outil de formatage automatique (comme `autopep8` ou l'outil intégré à votre IDE) pour corriger les problèmes d'espacement, d'indentation et de longueur de ligne. Un code propre est plus facile à débugger.

**Fichiers concernés :** L'ensemble du projet, en commençant par `gestionnaire/gestion.py`.
