---
title: "TP 13. Agrandir un volume logique de laboratoire"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="complements/02-lvm"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/complements/02-lvm/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/complements/02-lvm/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/complements/complements/c02-lvm/tp/tp-13-lvm.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://kayasam.github.io/lpi101/complements/02-lvm/tp" aria-current="page">Énoncé</a><a class="exercise-correction" href="https://kayasam.github.io/lpi101/complements/02-lvm/tp-corrigev2">Afficher les corrections</a></nav>

> Durée estimée : 55 min

> Chapitres associés : [C02. Comprendre et manipuler LVM](https://kayasam.github.io/lpi101/complements/02-lvm/)

---

## Objectifs

- Ajouter un disque à la VM et l’identifier sans risque.
- Relier PV, VG et LV.
- Agrandir séparément volume logique et système de fichiers.
- Démonter et retirer les ressources dans le bon ordre.

## Avant de commencer

Complément facultatif après le stockage (TP 08a). Le TP utilise un **nouveau disque NVMe de 2 Go**, entièrement consacré à LVM. Le groupe `lpi101_vg_tp13` doit être absent avant l’atelier.

> [!warning] Le système utilise déjà LVM
> L’installation Debian a créé son propre groupe de volumes (par exemple `debian13-vg`) qui porte `/` et le swap. Ne touche jamais à ses PV, VG ou LV : toutes les commandes de ce TP visent uniquement le nouveau disque et le groupe `lpi101_vg_tp13`.

> [!info] Atelier optionnel
> À proposer après les bases, selon le rythme du groupe.

---

## Partie A — Ajouter et identifier le disque (10 min)

**A1.** Éteins la VM, ajoute-lui un **nouveau disque dur NVMe de 2 Go**, puis redémarre-la. Installe ensuite le paquet `lvm2` s’il est absent.

**A2.** Identifie le nouveau disque et enregistre son chemin dans une variable `DISQUE`. Vérifie qu’il n’a ni partition, ni point de montage, ni signature. Quels PV et VG existent déjà sur la machine ?

> [!warning]
> La suite utilise `"$DISQUE"`. La variable disparaît à la fermeture du terminal : redéfinis-la si tu ouvres une nouvelle session.

---

## Partie B — Construire les trois niveaux (15 min)

**B1.** Initialise le nouveau disque comme volume physique, puis crée le groupe `lpi101_vg_tp13`. Affiche la taille et l’espace libre.

**B2.** Crée un LV nommé `donnees` de 256 Mio, formate-le en ext4 puis monte-le sous `/mnt/lpi101-lvm`. Écris un fichier `preuve.txt` dedans.

---

## Partie C — Agrandir sans perdre le fichier (20 min)

**C1.** Relève la taille du LV et celle du système de fichiers, puis agrandis seulement le LV de 128 Mio.

**C2.** Agrandis maintenant le système de fichiers ext4 et vérifie le contenu de `preuve.txt`.

**C3.** Donne au LV tout l’espace encore libre du groupe, en agrandissant le système de fichiers dans la même commande.

---

## Partie D — Nettoyer (10 min)

**D1.** Démonte puis retire le LV, le VG et le PV dans cet ordre. Vérifie que seul le LVM du système reste visible.

**D2.** *(Facultatif)* Éteins la VM et retire le disque de 2 Go dans VMware.
