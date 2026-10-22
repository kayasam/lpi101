# TP 14. Écrire un petit script de contrôle

> Durée estimée : 45 min

> Chapitres associés : [C03. Écrire un premier script Bash](https://kayasam.github.io/lpi101/complements/03-premiers-scripts/), [C04. Découvrir les conditions et les boucles](https://kayasam.github.io/lpi101/complements/04-conditions-boucles/), [C05. Lire des scripts utilitaires](https://kayasam.github.io/lpi101/complements/05-scripts-utilitaires/)

---

## Objectifs

- Créer un script exécutable avec un paramètre.
- Utiliser une condition et un code retour.
- Vérifier un résultat avant d’annoncer un succès.

## Avant de commencer

Cet atelier est un prolongement après l’initiation au shell. L’énoncé donne le comportement attendu ; plusieurs solutions sont possibles.

> [!info] Atelier optionnel
> À proposer après les bases, selon le rythme du groupe.

**Préparation fournie :**

```bash
mkdir -p ~/lpi101-tp/tp14
cd ~/lpi101-tp/tp14
```

---

## Partie A — Écrire et exécuter (15 min)

**A1.** Crée `bonjour.sh` : il affiche `Bonjour PRENOM`, en prenant le premier argument comme prénom et `stagiaire` si aucun argument n’est fourni.

**A2.** Vérifie sa syntaxe puis lance-le avec le prénom composé `Jean Paul`. Quelle différence entre `bash bonjour.sh` et `./bonjour.sh` ?

---

## Partie B — Contrôler une condition (20 min)

**B1.** Crée `controle.sh` : il reçoit un chemin, affiche `OK : chemin` si c’est un fichier ordinaire, sinon écrit `Absent : chemin` sur stderr et termine avec le code 1.

**B2.** Avec une boucle, lance le contrôle sur `bonjour.sh`, `controle.sh` et `fichier-absent.txt`, en signalant clairement les échecs.

---

## Partie C — Conserver une preuve (10 min)

**C1.** Archive les deux scripts dans `scripts.tar.gz`. N’affiche `Archive créée` que si tar a réussi, puis liste le contenu.
