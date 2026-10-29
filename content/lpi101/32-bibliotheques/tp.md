---
title: "TP 09. Installer un outil et retrouver ses fichiers"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/32-bibliotheques"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/32-bibliotheques/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/32-bibliotheques/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/32-bibliotheques/tp/tp-09-paquets-bibliotheques.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://kayasam.github.io/lpi101/lpi101/32-bibliotheques/tp" aria-current="page">Énoncé</a><a class="exercise-correction" href="https://kayasam.github.io/lpi101/lpi101/32-bibliotheques/tp-corrigev2">Afficher les corrections</a></nav>

> Durée estimée : 50 min

> Chapitres associés : [30. Installer et gérer les paquets Debian](https://kayasam.github.io/lpi101/lpi101/30-paquets-debian/), [31. Reconnaître RPM, DNF, YUM et Zypper](https://kayasam.github.io/lpi101/lpi101/31-paquets-rpm/), [32. Comprendre les bibliothèques partagées](https://kayasam.github.io/lpi101/lpi101/32-bibliotheques/)

---

## Objectifs

- Distinguer index des dépôts et paquets installés.
- Installer, interroger et retirer un petit paquet.
- Observer une bibliothèque partagée et reconnaître les équivalents RPM.

## Avant de commencer

Une connexion Internet et les dépôts Debian configurés sont nécessaires. Le paquet hello sert de support jetable à cet atelier. Les commandes RPM/DNF sont uniquement à reconnaître sur cette VM Debian.

---

## Partie A — Chercher et installer (20 min)

**A1.** Actualise le catalogue des paquets, puis cherche le paquet hello et affiche ses informations.

**A2.** Installe hello, lance-le et vérifie l’endroit où le shell trouve sa commande.

**A3.** Affiche l’état du paquet, les fichiers qu’il fournit et le paquet propriétaire de `/usr/bin/hello`.

---

## Partie B — Comprendre les dépendances (15 min)

**B1.** Affiche la version installée et la version candidate, puis les dépendances du paquet.

**B2.** Affiche les bibliothèques de `/usr/bin/ls`, puis consulte le cache du chargeur. Pourquoi ne copie-t-on pas au hasard une bibliothèque trouvée sur Internet ?

---

## Partie C — Retirer et transposer (15 min)

**C1.** Retire le paquet hello, vérifie son absence puis demande sa purge. Distingue remove et purge.

**C2.** Sur une distribution RPM, quelles commandes serviraient à installer hello et à retrouver le paquet d’un fichier ? Ne les lance pas sur Debian.
