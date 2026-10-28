---
title: "32. Comprendre les bibliothèques partagées"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/32-bibliotheques"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/32-bibliotheques/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/32-bibliotheques/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/32-bibliotheques/32-bibliotheques.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Identifier une dépendance partagée et reconnaître les outils de chargement.

**Repères LPI 101 :** 102.3.

**Commandes à connaître :** `ldd`, `ldconfig`.

**Fichiers et emplacements :** `/etc/ld.so.conf`, `/etc/ld.so.conf.d/`, `/etc/ld.so.cache`.

---

## Introduction

Sous Linux, les programmes utilisent souvent des **bibliothèques partagées** (fichiers `.so`) contenant du code commun (fonctions, outils…).
Cela permet de **réduire la taille des exécutables**, **partager la mémoire** entre plusieurs programmes et **mettre à jour le code partagé sans recompiler**.

Deux types principaux existent :

- **Bibliothèques statiques (.a)** → incluses directement dans le binaire au moment de la compilation.

- **Bibliothèques dynamiques / partagées (.so)** → chargées par le système au moment de l’exécution.

---

## Emplacements habituels

|Répertoire|Rôle|
|---|---|
|`/lib`, `/lib64`|Bibliothèques essentielles au démarrage du système|
|`/usr/lib`, `/usr/lib64`|Bibliothèques pour les programmes standards|
|`/usr/local/lib`|Bibliothèques installées manuellement|
|`/opt/.../lib`|Bibliothèques spécifiques à un logiciel tiers|

---

## Identifier les bibliothèques d’un programme

Pour connaître les bibliothèques utilisées par un exécutable :

```bash
ldd /usr/bin/ls
```

Exemple de sortie :

```text
linux-vdso.so.1 =>  (0x00007fffb7ffd000)
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f2f46a00000)
```

Chaque ligne indique le nom de la bibliothèque et son chemin réel sur le disque.

---

## Recherche et chargement des bibliothèques

Le **chargeur dynamique** (`ld.so` / `ld-linux.so`) trouve les bibliothèques nécessaires au lancement. Parmi les éléments qui interviennent : chemins enregistrés dans l’exécutable (RPATH/RUNPATH), variable `LD_LIBRARY_PATH`, cache `/etc/ld.so.cache` et répertoires standards.

`/etc/ld.so.conf` et `/etc/ld.so.conf.d/` sont lus par `ldconfig` pour construire le cache ; ce ne sont pas des fichiers relus de la même manière pour chaque lancement. L’ordre précis dépend notamment de RPATH/RUNPATH et du mode d’exécution sécurisé.

```bash
LD_LIBRARY_PATH=/opt/monapp/lib commande
ldconfig -p
```

La première forme ajuste l’environnement d’une seule commande. Elle illustre le mécanisme et suppose qu’un logiciel de ce nom est installé. Une bibliothèque manquante se résout d’abord en recherchant le paquet approprié.

Documentation : [manuel du chargeur dynamique](https://man7.org/linux/man-pages/man8/ld.so.8.html).

---

## Mettre à jour le cache des bibliothèques

Les gestionnaires de paquets exécutent normalement les opérations nécessaires. Après une installation manuelle dans les chemins configurés, l’administrateur peut actualiser le cache :

```bash
sudo ldconfig
```

Cette commande met à jour le fichier `/etc/ld.so.cache`, qui contient la liste des chemins valides pour les bibliothèques partagées.

Pour vérifier que tout est bien pris en compte :

```bash
sudo ldconfig -v | grep lib
```

---

## A retenir
> [!tip]
> - Les bibliothèques **statiques (.a)** sont intégrées dans le binaire.
>
> - Les bibliothèques **dynamiques (.so)** sont chargées à l’exécution.
>
> - `ldd` permet de lister les bibliothèques utilisées par un programme.
>
> - `ldconfig` met à jour le cache du système.
>
> - `LD_LIBRARY_PATH` permet d’ajouter temporairement un chemin personnalisé.
>
>

> [!note] Utilisation de ldd
> Utiliser `ldd` sur les programmes connus de la VM, comme `/usr/bin/ls`, plutôt que sur un exécutable inconnu.
