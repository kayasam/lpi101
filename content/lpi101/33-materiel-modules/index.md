---
title: "33 — Identifier le matériel et les modules du noyau"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/33-materiel-modules"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/33-materiel-modules/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/33-materiel-modules.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Observer les ressources de la VM et le rôle des pilotes.

**Repères LPI 101 :** 101.1.

**Commandes à connaître :** `lscpu`, `free`, `lspci`, `lsusb`, `lsmod`, `modinfo`, `modprobe`.

---

## Introduction

Sous Linux, le matériel (processeur, mémoire, disques, périphériques USB, cartes réseau…) est entièrement accessible depuis le **système de fichiers virtuel** `/proc` et via des **outils d’inspection**.
Comprendre ces commandes est essentiel pour diagnostiquer, surveiller et configurer un système.

Ce chapitre aborde :

- la **détection du matériel** ;

- la **vérification du processeur et de la mémoire** ;

- la **gestion des périphériques de stockage et USB** ;

- la **lecture des informations système via `/proc` et `/sys`**.

---

## Informations sur le processeur

## `lscpu` — afficher les informations CPU

```bash
lscpu
```

Affiche :

- modèle du processeur ;

- nombre de cœurs et de threads ;

- architecture (64 bits, ARM, etc.) ;

- hyper-threading, virtualisation, fréquences.

Exemple :

```text
Architecture :            x86_64
Processeur(s) :           4
Modèle :                  Intel(R) Core(TM) i7-8650U CPU @ 1.90 GHz
Thread(s) par cœur :      2
Cœur(s) par socket :      2
```

---

## Informations sur la mémoire

## `free` — afficher la mémoire utilisée et disponible

```bash
free -h
```

- `-h` : affiche les valeurs dans un format lisible (Mo/Go).

---

## `cat /proc/meminfo` — consulter le détail de la mémoire

```bash
cat /proc/meminfo | head
```

Donne des informations précises sur :

- la RAM totale et libre ;

- la mémoire tampon/cache ;

- la mémoire utilisée par le noyau.

---

## Détection des périphériques matériels

Les périphériques PCI et USB peuvent être listés avec les commandes suivantes. Pour les disques, voir le chapitre 26 ; pour l’espace disque, le chapitre 28.

---

## `lspci` — lister les périphériques PCI

```bash
lspci
```

Affiche les cartes réseau, contrôleurs SATA, GPU, etc.
Pour plus de détails :

```bash
lspci -v
```

---

## `lsusb` — lister les périphériques USB

```bash
lsusb
```

Affiche les clés USB, webcams, imprimantes, etc.
Pour un affichage détaillé :

```bash
lsusb -v | less
```

---

## `lsblk` — lister les périphériques de stockage (disques)

`lsblk` affiche les périphériques de stockage. Sa lecture détaillée, les partitions et les systèmes de fichiers sont traités dans le chapitre 26.

---

## `df` — afficher l’espace disque utilisé

Voir le chapitre 28 pour mesurer l’espace disponible avec `df -h`.

---

## `du` — mesurer l’espace occupé par un dossier

Voir le chapitre 28 pour mesurer la place occupée par un dossier avec `du -sh`.

---

## Gestion des modules du noyau

Les **pilotes matériels** sous Linux sont chargés sous forme de **modules**.

## `lsmod` — lister les modules chargés

```bash
lsmod
```

Affiche les modules du noyau actuellement en mémoire (pilotes actifs).

## `modinfo` — obtenir des détails sur un module

```bash
sudo modinfo e1000e
```

Affiche la version, le fournisseur et les dépendances du module `e1000e` (carte Intel).

---

## Arborescences virtuelles du système

## `/proc`

Ce dossier contient des **fichiers virtuels** reflétant l’état du système (CPU, mémoire, processus…).

```bash
ls /proc
cat /proc/cpuinfo
cat /proc/meminfo
```

## `/sys`

Ce dossier reflète la **hiérarchie des périphériques** détectés par le noyau (sysfs).

```bash
ls /sys/class/
ls /sys/block/
```

---
## Comprendre le chargement d’un module

```bash
lsmod
modinfo loop
```

`lsmod` liste les modules chargés et `modinfo` décrit un module disponible. Un pilote intégré directement dans le noyau n’apparaît pas dans `lsmod`.

`sudo modprobe nom_module` charge un module avec ses dépendances ; `sudo modprobe -r nom_module` tente de le retirer s’il n’est pas utilisé. Ces formes servent de repères : conserver les pilotes du disque et du réseau actifs pendant la formation.

## Périphériques et événements

`/dev` expose les nœuds de périphériques ; `/sys` décrit les objets du noyau ; `/proc` fournit des informations sur le système et les processus. **udev** gère les événements et noms de périphériques ; **D-Bus** est un mécanisme d’échange de messages entre composants de l’espace utilisateur.

Dans le firmware d’une machine physique, certains périphériques intégrés peuvent être activés ou désactivés. Dans une VM, les réglages du matériel virtuel sont effectués depuis l’hyperviseur. Reconnaître aussi les stockages SATA, SCSI, NVMe et USB ; leur nom dans `/dev` dépend du pilote et du type de matériel.

---

## À retenir
> [!tip]
> - Linux expose toutes les informations matérielles via **/proc** et **/sys**.
> - Le CPU et la mémoire peuvent être consultés facilement depuis le système.
> - Les périphériques PCI, USB et disques sont détectés automatiquement par le noyau.
> - Les pilotes matériels sont chargés sous forme de **modules du noyau**.
> - Les outils `lspci`, `lsusb`, `lsblk` et `df` permettent d’identifier rapidement le matériel présent.
> - Savoir interpréter la mémoire disponible, l’espace disque et les périphériques est essentiel pour diagnostiquer un système.
> - **/proc** et **/sys** sont des arborescences **virtuelles**, mises à jour en temps réel par le noyau.
