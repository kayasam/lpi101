# 32. Comprendre les bibliothèques partagées

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
|`/usr/lib`, `/usr/lib64`|Bibliothèques du système et des programmes installés par les paquets|
|`/usr/lib/x86_64-linux-gnu`|Sur Debian/Ubuntu : bibliothèques rangées par architecture|
|`/lib`, `/lib64`|Historiquement : bibliothèques essentielles au démarrage. Aujourd’hui : liens vers `/usr/lib` et `/usr/lib64`|
|`/usr/local/lib`|Bibliothèques installées manuellement|
|`/opt/.../lib`|Bibliothèques spécifiques à un logiciel tiers|

> [!info] Fusion de /usr (*usrmerge*)
> Autrefois, `/usr` pouvait être sur une partition séparée montée tardivement : `/lib` gardait sur la racine le minimum nécessaire au démarrage. Aujourd’hui, `/usr` est monté dès le début du démarrage. Les distributions récentes (Debian 12+, Ubuntu, Fedora, RHEL…) ont donc tout regroupé dans `/usr` et remplacé `/lib`, `/lib64`, `/bin` et `/sbin` par des liens symboliques :
>
> ```bash
> ls -l / | grep -- '->'
> ```
>
> ```text
> lrwxrwxrwx 1 root root  7 … bin -> usr/bin
> lrwxrwxrwx 1 root root  7 … lib -> usr/lib
> lrwxrwxrwx 1 root root  9 … lib64 -> usr/lib64
> lrwxrwxrwx 1 root root  8 … sbin -> usr/sbin
> ```
>
> Pour l’examen LPI, connaître les deux emplacements : `/lib` et `/usr/lib` restent cités dans les objectifs.

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
