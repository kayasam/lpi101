# TP 02. Gérer un petit dossier de projet

> Durée estimée : 75 min

> Chapitres associés : [10. Créer, copier, déplacer et supprimer](https://kayasam.github.io/lpi101/lpi101/10-manipuler-fichiers/), [11. Utiliser les jokers et rechercher](https://kayasam.github.io/lpi101/lpi101/11-jokers-et-recherche/), [12. Comprendre les liens physiques et symboliques](https://kayasam.github.io/lpi101/lpi101/12-liens/)

---

## Objectifs

- Créer, copier, déplacer et supprimer dans un espace de travail.
- Utiliser les jokers et trouver des fichiers.
- Distinguer copie, lien physique et lien symbolique.

## Avant de commencer

Les manipulations restent dans `~/lpi101-tp/tp02`. Les parties s’enchaînent : conserve les fichiers jusqu’au bilan.

---

## Partie A — Construire le projet (20 min)

**A1.** Crée les dossiers `projet/docs`, `projet/src` et `projet/tests` dans `~/lpi101-tp/tp02`. Place-toi dans ce dernier dossier.

**A2.** Crée `notes.txt` contenant `Bonjour Linux` et un fichier vide nommé `vide.txt`. Identifie leur type.

**A3.** Copie `notes.txt` dans `projet/docs`, puis renomme cette copie en `compte-rendu.txt`. Le fichier de départ existe-t-il encore ?

**A4.** Copie tout `projet` dans `copie-projet`. Crée et supprime un dossier vide nommé `a-retirer`. Pourquoi `rmdir projet` échouerait-il ?

---

## Partie B — Sélectionner et rechercher (25 min)

**B1.** Crée cinq fichiers de `rapport-1.txt` à `rapport-5.txt`. Affiche ce que le shell sélectionne avec `rapport-?.txt`, puis avec `rapport-[12].txt`.

**B2.** Crée `.confidentiel.txt`. Compare `ls` et `ls -a`. Une absence dans `ls` signifie-t-elle que le fichier est protégé ?

**B3.** Recherche tous les fichiers `.txt` du projet, puis uniquement les fichiers vides de ton dossier TP.

**B4.** Trouve comment le shell interprète `cd` et `ls`. Affiche les métadonnées de `notes.txt` : `ctime` est-il une date de création ?

---

## Partie C — Copier ou créer un lien (30 min)

**C1.** Crée `copie.txt` comme copie de `notes.txt`, `physique.txt` comme lien physique et `symbole.txt` comme lien symbolique relatif. Compare les numéros d’inode.

**C2.** Ajoute `Deuxième ligne` par le nom `physique.txt`. Compare le contenu de `notes.txt` et de `copie.txt`.

**C3.** Supprime seulement `notes.txt`. Vérifie que le lien physique reste lisible et observe le lien symbolique.

**C4.** Conserve les fichiers et fais un bilan : quelle opération utiliser pour une copie indépendante, un raccourci de dossier et un deuxième nom du même fichier ?
