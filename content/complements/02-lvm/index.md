---
title: "C02 — Comprendre et manipuler LVM"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="complements/02-lvm"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/complements/02-lvm/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/complements/02-lvm/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/complements/cours/02-lvm.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Relier volumes physiques, groupes et volumes logiques.

**Repères LPI 101 :** 102.1.

> [!info] Complément
> À découvrir après les bases, selon le rythme du groupe.

---

## Introduction

Le **LVM (Logical Volume Manager)** est un système de gestion de volumes logiques.
Il permet d’allouer, redimensionner et gérer l’espace disque de manière **beaucoup plus souple** que les partitions classiques.

LVM est particulièrement utile sur les serveurs ou les environnements virtualisés, car il permet :

* d’**agrandir** des volumes et certains systèmes de fichiers à chaud ; une réduction nécessite une procédure propre au système de fichiers ;
* de **regrouper plusieurs disques** physiques dans un seul espace logique ;
* de **créer des snapshots** (états à un instant donné) qui peuvent aider à réaliser des sauvegardes.

---

## Structure logique du LVM

LVM repose sur trois couches principales :

```text
Disques physiques → Physical Volumes (PV)
         ↓
Groupes de volumes → Volume Groups (VG)
         ↓
Volumes logiques → Logical Volumes (LV)
```

| Élément                  | Description                                 | Exemple                  |
| ------------------------ | ------------------------------------------- | ------------------------ |
| **PV (Physical Volume)** | Disque ou partition utilisée par LVM        | `/dev/sdb1`              |
| **VG (Volume Group)**    | Ensemble de PV formant un “pool” d’espace   | `vg_data`                |
| **LV (Logical Volume)**  | Partition logique que l’on formate et monte | `/dev/vg_data/lv_backup` |

---

## Étapes de création d’un volume LVM
> [!danger]
> ⚠️ Réaliser ces commandes **sur un disque de test uniquement** (ex. `/dev/sdb` ajouté dans VirtualBox).

## Créer un volume physique (PV)

```bash
sudo pvcreate /dev/sdb1
```

Afficher les volumes physiques existants :

```bash
sudo pvs
sudo pvdisplay
```

---

## Créer un groupe de volumes (VG)

```bash
sudo vgcreate vg_data /dev/sdb1
```

Afficher les groupes de volumes :

```bash
sudo vgs
sudo vgdisplay
```

---

## Créer un volume logique (LV)

```bash
sudo lvcreate -L 1G -n lv_backup vg_data
```

* `-L 1G` → taille du volume logique
* `-n lv_backup` → nom du volume
* `vg_data` → nom du groupe de volumes

Lister les volumes logiques :

```bash
sudo lvs
sudo lvdisplay
```

---

## Formater et monter le volume

Formater en ext4 :

```bash
sudo mkfs.ext4 /dev/vg_data/lv_backup
```

Créer un point de montage et monter :

```bash
sudo mkdir /mnt/lvm
sudo mount /dev/vg_data/lv_backup /mnt/lvm
```

Vérifier :

```bash
lsblk
df -h /mnt/lvm
```

---

## Agrandir un volume logique (exemple)

Si le groupe contient encore de l’espace libre :

```bash
sudo lvextend -L +500M /dev/vg_data/lv_backup
sudo resize2fs /dev/vg_data/lv_backup
```

La première commande agrandit le volume logique ; la seconde agrandit explicitement son système de fichiers ext4. XFS utilise d’autres outils et ne permet pas la réduction de son système de fichiers.

---

## Supprimer proprement les volumes (pour test uniquement)

```bash
sudo umount /mnt/lvm
sudo lvremove /dev/vg_data/lv_backup
sudo vgremove vg_data
sudo pvremove /dev/sdb1
```

---

## Visualisation synthétique

```bash
sudo pvs   # liste les volumes physiques
sudo vgs   # liste les groupes de volumes
sudo lvs   # liste les volumes logiques
```

---

## Avantages de LVM

* Redimensionnement dynamique (agrandissement à chaud possible).
* Agrégation de plusieurs disques dans un seul espace.
* Création de **snapshots** pour sauvegardes rapides.
* Gestion simplifiée de l’espace de stockage dans le temps.

---

## À retenir
> [!tip]
> * **LVM** offre une gestion flexible du stockage, plus puissante que les partitions classiques.
> * Trois niveaux hiérarchiques :
>
>   * **PV** → disques physiques utilisés par LVM
>   * **VG** → groupe de volumes, regroupe un ou plusieurs PV
>   * **LV** → volumes logiques, montés comme des partitions normales
> * Commandes essentielles :
>
>   * `pvcreate`, `vgcreate`, `lvcreate` → création
>   * `pvs`, `vgs`, `lvs` → affichage
>   * `lvextend` + `resize2fs` → agrandissement
>   * `lvremove`, `vgremove`, `pvremove` → suppression
> * LVM est idéal sur **serveur ou machine virtuelle**, mais à manipuler uniquement sur un **disque de test** lors des premières expérimentations.
