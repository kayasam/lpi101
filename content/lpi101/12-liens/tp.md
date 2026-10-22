---
title: "TP 02 — Gérer un petit dossier de projet"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/12-liens"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/12-liens/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/12-liens/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/tp/12-liens.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


> Durée estimée : 75 min

> Chapitres associés : [10 — Créer, copier, déplacer et supprimer](https://kayasam.github.io/lpi101/lpi101/10-manipuler-fichiers/), [11 — Utiliser les jokers et rechercher](https://kayasam.github.io/lpi101/lpi101/11-jokers-et-recherche/), [12 — Comprendre les liens physiques et symboliques](https://kayasam.github.io/lpi101/lpi101/12-liens/)

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
