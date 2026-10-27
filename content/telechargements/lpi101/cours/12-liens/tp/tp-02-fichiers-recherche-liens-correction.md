# TP 02. Gérer un petit dossier de projet — Correction

> Essaie chaque question avant d’ouvrir **Afficher la correction**. Chaque réponse se replie indépendamment.

> Durée estimée : 75 min

> Chapitres associés : [10. Créer, copier, déplacer et supprimer](https://cours.kaya.ovh/lpi101/lpi101/10-manipuler-fichiers/), [11. Utiliser les jokers et rechercher](https://cours.kaya.ovh/lpi101/lpi101/11-jokers-et-recherche/), [12. Comprendre les liens physiques et symboliques](https://cours.kaya.ovh/lpi101/lpi101/12-liens/)

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

> [!success]- Afficher la correction — A1
> ```bash
> mkdir -p ~/lpi101-tp/tp02/projet/{docs,src,tests}
> cd ~/lpi101-tp/tp02
> ```
>
> Les accolades génèrent les trois chemins ; `mkdir -p` crée les parents.

**A2.** Crée `notes.txt` contenant `Bonjour Linux` et un fichier vide nommé `vide.txt`. Identifie leur type.

> [!success]- Afficher la correction — A2
> ```bash
> printf 'Bonjour Linux\n' > notes.txt
> touch vide.txt
> file notes.txt vide.txt
> ```
>
> Un fichier vide n’est pas identifié de la même manière qu’un fichier contenant du texte. L’extension n’impose pas le type.

**A3.** Copie `notes.txt` dans `projet/docs`, puis renomme cette copie en `compte-rendu.txt`. Le fichier de départ existe-t-il encore ?

> [!success]- Afficher la correction — A3
> ```bash
> cp notes.txt projet/docs/
> mv projet/docs/notes.txt projet/docs/compte-rendu.txt
> ls notes.txt projet/docs/compte-rendu.txt
> ```
>
> La copie est indépendante ; `mv` renomme la copie et ne modifie pas le nom de départ.

**A4.** Copie tout `projet` dans `copie-projet`. Crée et supprime un dossier vide nommé `a-retirer`. Pourquoi `rmdir projet` échouerait-il ?

> [!success]- Afficher la correction — A4
> ```bash
> cp -r projet copie-projet
> mkdir a-retirer
> rmdir a-retirer
> ```
>
> `cp -r` parcourt les sous-dossiers ; `rmdir` ne supprime que les dossiers vides. Il n’est pas nécessaire de lancer une suppression récursive pour le constater.

---

## Partie B — Sélectionner et rechercher (25 min)

**B1.** Crée cinq fichiers de `rapport-1.txt` à `rapport-5.txt`. Affiche ce que le shell sélectionne avec `rapport-?.txt`, puis avec `rapport-[12].txt`.

> [!success]- Afficher la correction — B1
> ```bash
> touch rapport-{1..5}.txt
> printf '%s\n' rapport-?.txt
> printf '%s\n' rapport-[12].txt
> ```
>
> `?` remplace un caractère ; `[12]` choisit 1 ou 2. Le shell développe les motifs avant de lancer `printf`.

**B2.** Crée `.confidentiel.txt`. Compare `ls` et `ls -a`. Une absence dans `ls` signifie-t-elle que le fichier est protégé ?

> [!success]- Afficher la correction — B2
> ```bash
> touch .confidentiel.txt
> ls
> ls -a
> ```
>
> Non : le point est une convention d’affichage. Les autorisations d’accès reposent sur les permissions.

**B3.** Recherche tous les fichiers `.txt` du projet, puis uniquement les fichiers vides de ton dossier TP.

> [!success]- Afficher la correction — B3
> ```bash
> find projet -type f -name '*.txt'
> find . -type f -empty
> ```
>
> Protéger `*.txt` pour que `find` reçoive le motif intact. `-empty` concerne ici les fichiers sans contenu.

**B4.** Trouve comment le shell interprète `cd` et `ls`. Affiche les métadonnées de `notes.txt` : `ctime` est-il une date de création ?

> [!success]- Afficher la correction — B4
> ```bash
> type cd
> type ls
> stat notes.txt
> ```
>
> `cd` est une commande interne ; `ls` peut être un alias ou un exécutable. `ctime` concerne un changement des métadonnées de l’inode, pas sa création.

---

## Partie C — Copier ou créer un lien (30 min)

**C1.** Crée `copie.txt` comme copie de `notes.txt`, `physique.txt` comme lien physique et `symbole.txt` comme lien symbolique relatif. Compare les numéros d’inode.

> [!success]- Afficher la correction — C1
> ```bash
> cp notes.txt copie.txt
> ln notes.txt physique.txt
> ln -s notes.txt symbole.txt
> ls -li notes.txt copie.txt physique.txt symbole.txt
> ```
>
> `notes.txt` et `physique.txt` partagent le même inode. La copie et le lien symbolique ont leurs propres inodes.

**C2.** Ajoute `Deuxième ligne` par le nom `physique.txt`. Compare le contenu de `notes.txt` et de `copie.txt`.

> [!success]- Afficher la correction — C2
> ```bash
> printf 'Deuxième ligne\n' >> physique.txt
> cat notes.txt
> cat copie.txt
> ```
>
> Le contenu accessible par le lien physique est commun. La copie garde sa première version.

**C3.** Supprime seulement `notes.txt`. Vérifie que le lien physique reste lisible et observe le lien symbolique.

> [!success]- Afficher la correction — C3
> ```bash
> rm notes.txt
> cat physique.txt
> ls -l symbole.txt
> readlink symbole.txt
> ```
>
> Le lien physique conserve un nom vers les données. Le lien symbolique pointe maintenant vers un nom absent : il est cassé.

**C4.** Conserve les fichiers et fais un bilan : quelle opération utiliser pour une copie indépendante, un raccourci de dossier et un deuxième nom du même fichier ?

> [!success]- Afficher la correction — C4
> Respectivement `cp`, `ln -s` et `ln`. Un lien physique ne traverse pas les systèmes de fichiers ; le lien symbolique contient un chemin.
