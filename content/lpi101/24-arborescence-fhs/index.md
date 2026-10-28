---
title: "24. Se repérer dans l’arborescence Linux"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/24-arborescence-fhs"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/24-arborescence-fhs/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/24-arborescence-fhs/24-arborescence-fhs.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Associer les répertoires importants à leur rôle.

**Repères LPI 101 :** 104.7.

---

## Introduction
> [!info]
> Cette section s’inspire de l'exellent support de Hughes Bigo et présente la structure d’un système Linux selon le **FHS (Filesystem Hierarchy Standard)**.
> - https://hedgedoc.dawan.fr/wskoGbqwRcSkQBoC9RG_KA?both

Sous Linux, tout est fichier et l’arborescence unique part de la racine `/`. Le FHS décrit quels répertoires existent, ce qu’ils contiennent et à quoi ils servent.
Pour la référence locale : `man hier`.

---

## Structure FHS (Filesystem Hierarchy Standard)

---

Le FHS définit une arborescence standardisée afin de garantir la cohérence entre distributions.
![](https://kayasam.github.io/lpi101/assets/course-media/12fb835ad8955dbd.png)

## Répertoires principaux et leur rôle

* **/**
  Racine de l’arborescence. Tous les chemins en dépendent.

* **/bin**, **/sbin**, **/lib**, **/lib64**
  Binaires et bibliothèques essentiels (souvent redirigés via usrmerge vers `/usr/bin`, `/usr/sbin`, `/usr/lib`, etc.).
  Utilisés très tôt au démarrage.

* **/boot**
  Fichiers nécessaires au démarrage (noyaux, initrd, chargeur).

* **/dev**
  Fichiers de périphériques (caractère/bloc), gérés dynamiquement par `udev` (ex. `/dev/sda`, `/dev/null`).

* **/etc**
  Configuration système spécifique à l’hôte. Fichiers statiques de configuration (pas de binaires).

* **/home**
  Répertoires personnels des utilisateurs finaux (`/home/<user>`).

* **/root**
  Répertoire personnel de l’administrateur `root` (séparé de `/home`).

* **/proc**
  Pseudo-FS fournissant des vues dynamiques du noyau et des processus (ex. `/proc/cpuinfo`, `/proc/meminfo`, `/proc/<PID>`).

* **/sys**
  Pseudo-FS exposant le modèle des périphériques et aspects du noyau (ex. `/sys/class/net`, `/sys/block`).

* **/run**
  Données d’exécution (runtime) depuis le dernier boot. Volatile.

* **/tmp**
  Fichiers temporaires (souvent `tmpfs`, nettoyage fréquent). Droits généralement `1777` (sticky bit).

* **/var**
  Données variables : logs, caches, spool, bases d’état, etc.
  Sous-répertoires usuels :

  * `/var/log` : journaux
  * `/var/lib` : données persistantes d’applications
  * `/var/cache` : données régénérables
  * `/var/tmp` : temporaires conservés plus longtemps que `/tmp`

* **/usr**
  Hiérarchie “secondaire” (majorité des programmes, bibliothèques, données partagées) :

  * `/usr/bin`, `/usr/sbin` : binaires non essentiels
  * `/usr/lib` : bibliothèques
  * `/usr/share` : données indépendantes de l’architecture
  * `/usr/local` : installations locales spécifiques à l’hôte

* **/opt**
  Logiciels additionnels “autocontenants” installés par paquet hors gestionnaire natif.

* **/srv**
  Données servies par des services (HTTP, FTP, VCS…).

* **/media**
  Points de montage pour supports amovibles (clés USB, CD/DVD), souvent créés automatiquement.

* **/mnt**
  Point(s) de montage temporaires utilisés par l’admin pour des montages manuels.

* **/lost+found**
  Présent à la racine de chaque système de fichiers ext*, destiné à la récupération après `fsck`.

* (**Spécifiques distribution**) **/snap** (Ubuntu Snap), éventuellement d’autres répertoires propres à l’écosystème (Flatpak, etc.).

---
> [!info]
> Points clés modernes :
>
> * **usrmerge** : sur de nombreuses distributions, `/bin`, `/sbin`, `/lib`, `/lib64` sont des liens symboliques vers leurs équivalents sous `/usr` (ex. `/usr/bin`), afin de simplifier la maintenance.
> * **/run** : remplace `/var/run` pour les données d’exécution temporaires (vidées au démarrage).
> * **/proc** et **/sys** : systèmes de fichiers virtuels exposant respectivement des informations sur les processus/le noyau et sur les périphériques/driver model.
>

## Points de montage

Un **point de montage** est un répertoire auquel on rattache (monte) un système de fichiers. L’ensemble forme une seule arborescence à partir de `/`.
Usages typiques :

* Monter des partitions dédiées : `/boot`, `/home`, `/var` (isolation, sécurité, quotas, redimensionnement plus simple).
* Monter des supports amovibles sous `/media/<label>`.
* Utiliser `/mnt` pour des montages ponctuels.

Commandes d’observation usuelles (aperçu, sans détailler le paramétrage qui sera vu en 5.2) :

* `lsblk` : visualiser disques/partitions et leurs points de montage.
* `findmnt` : lister les systèmes de fichiers montés et leur hiérarchie.
* `df -h` : voir l’espace utilisé/disponible par système de fichiers.

> [!info]
> **Sources externes**
> - Page du manuel : `man hier`
> - wikipedia : https://fr.wikipedia.org/wiki/Filesystem_Hierarchy_Standard
> - Doc Ubuntu : https://doc.ubuntu-fr.org/fhs
>

---

## À retenir
> [!tip]
> * Le **FHS** normalise l’arborescence pour assurer cohérence et portabilité.
> * Des répertoires sont **virtuels** (`/proc`, `/sys`), d’autres **volatils** (`/run`, souvent `/tmp`).
> * Les binaires essentiels et bibliothèques sont accessibles très tôt au boot ; de plus en plus de systèmes utilisent **usrmerge** pour centraliser sous `/usr`.
> * Les données variables et journaux résident sous **`/var`**, les profils utilisateurs sous **`/home`**, la configuration sous **`/etc`**.
> * Un **point de montage** attache un système de fichiers à un répertoire dans l’unique arborescence qui part de `/`.
> * Pour explorer : `lsblk`, `findmnt`, `df -h` donnent une vue rapide des disques et montages.
