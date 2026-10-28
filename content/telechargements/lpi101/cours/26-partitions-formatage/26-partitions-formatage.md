# 26. Créer des partitions et des systèmes de fichiers

> [!note] Objectif
> Distinguer disque, partition et système de fichiers avant de formater.

**Repères LPI 101 :** 104.1.

**Commandes à connaître :** `lsblk`, `blkid`, `fdisk`, `mkfs`, `mkswap`.

---

## Introduction

Sous Linux, le stockage repose sur la notion de **systèmes de fichiers montés dans une arborescence unique**.
Chaque disque ou partition doit être **formaté** avec un système de fichiers (ext4, xfs, btrfs, etc.) puis **monté** à un emplacement (point de montage).
Cette section explique les outils permettant de visualiser, créer, monter et gérer ces systèmes de fichiers.

---
![Les trois niveaux du stockage : disque, partitions et système de fichiers.](https://kayasam.github.io/lpi101/assets/course-media/2e6294cef35ed354.svg)

## Outils de gestion des disques

## `lsblk` — visualiser la structure des disques et partitions

Affiche l’arborescence des périphériques de stockage et leurs points de montage.

```bash
lsblk
```

Exemple de sortie :

```text
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0  100G  0 disk
├─sda1   8:1    0   96G  0 part /
└─sda2   8:2    0    4G  0 part [SWAP]
sdb      8:16   0   10G  0 disk
```

Options utiles :

* `-f` : affiche le type de FS, les labels et UUID
* `-p` : affiche les chemins complets (`/dev/sda1`, etc.)

---

## `blkid` — identifier les partitions et leurs métadonnées

Permet d’afficher le type de système de fichiers, les labels et les UUID.

```bash
sudo blkid
```

Exemple :

```text
/dev/sda1: UUID="a7b5d..." TYPE="ext4" PARTUUID="..."
/dev/sda2: UUID="e1a0a..." TYPE="swap"
```

Les **UUID** sont souvent utilisés dans `/etc/fstab` car ils restent stables même si le nom du périphérique change.

---

## `fdisk` — gérer la table de partitions (MBR ou GPT)

Permet de visualiser ou modifier la table des partitions d’un disque.

Lister la table de partitions :

```bash
sudo fdisk -l
```

Lancer le mode interactif sur un disque :

```bash
sudo fdisk /dev/sdb
```

Principales commandes (à taper dans l’interface fdisk) :

* `n` → nouvelle partition
* `d` → supprimer une partition
* `p` → afficher la table
* `w` → enregistrer et quitter
* `q` → quitter sans enregistrer

> ⚠️ **Attention** : ces opérations modifient la structure du disque, à manipuler uniquement sur un disque de test ou non critique.

---

## Création et formatage d’un système de fichiers

## `mkfs` — créer un système de fichiers

Formate une partition pour y créer un système de fichiers.

Exemples :

```bash
sudo mkfs.ext4 /dev/sdb1
sudo mkfs.xfs /dev/sdb2
```

Autres formats possibles :

* `ext4` (par défaut sur Debian/Ubuntu)
* `xfs` (performant pour gros fichiers)
* `vfat` / `exfat` (compatibles Windows)
* `btrfs` (système moderne à snapshots)

---

## `mkswap` — initialiser une partition de swap

Le swap est un espace disque utilisé comme mémoire d’appoint.

```bash
sudo mkswap /dev/sdb3
sudo swapon /dev/sdb3
sudo swapoff /dev/sdb3
```

---

## Introduction à LVM et Btrfs

* **LVM (Logical Volume Manager)** : permet de gérer l’espace disque de manière flexible (agrandir, réduire, regrouper des disques sans repartitionner).
  Commandes : `pvcreate`, `vgcreate`, `lvcreate`, `lvextend`, `lvreduce`.

* **Btrfs** : système de fichiers moderne avec gestion intégrée des snapshots, sous-volumes, compression et vérification automatique.

Ces sujets sont abordés en détail dans des formations d’administration avancée.

---

## Choisir une table de partitions et un système de fichiers

**GPT** est la table de partitions moderne ; **MBR** reste à reconnaître pour les systèmes plus anciens. La table décrit les partitions ; le système de fichiers organise les données à l’intérieur d’une partition ou d’un volume.

| Système de fichiers | Repère |
|---|---|
| ext2 / ext3 / ext4 | Famille Linux ; ext3 et ext4 proposent un journal. |
| XFS | Système journalisé fréquent sur les serveurs ; outils de maintenance propres. |
| FAT / VFAT | Compatibilité et partition système EFI. |
| exFAT | Échanges de fichiers, notamment sur supports amovibles. |
| Btrfs | Sous-volumes, compression et fonctions sur plusieurs périphériques. |

Les commandes correspondantes comprennent `mkfs.ext4`, `mkfs.xfs`, `mkfs.vfat` et `mkfs.exfat`, selon les outils installés. Pour débuter, se concentrer sur ext4.

## À retenir

> [!warning]
> Les exemples de création et formatage s’appliquent à un **disque supplémentaire de laboratoire vide**, identifié avant la commande. Le nom `/dev/sdb` est un exemple ; il peut être différent dans votre VM.
