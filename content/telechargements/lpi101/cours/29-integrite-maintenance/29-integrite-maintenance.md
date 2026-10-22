# 29. Vérifier et entretenir les systèmes de fichiers

> [!note] Objectif
> Comprendre les outils d’inspection et les conditions d’une vérification.

**Repères LPI 101 :** 104.2.

**Commandes à connaître :** `tune2fs`, `fsck`, `e2fsck`, `rsync`.

---

## Introduction

Même si les systèmes de fichiers Linux comme **ext4** ou **xfs** sont très fiables, il peut arriver qu’un volume soit endommagé après une coupure brutale ou un problème matériel.
Cette partie explique comment **observer** l’état d’un système de fichiers et, de manière encadrée, comment **lancer une vérification** en cas de besoin.

---
> [!danger]
>  ⚠️ Avertissement important
>
> Les outils de vérification (`fsck`, `e2fsck`) peuvent **modifier la structure interne du système de fichiers**.
> 👉 **Ne les utilisez jamais sur une partition montée** ou sur le disque système actif.
> Ils doivent être réservés :
>
> * aux partitions de test, ou
> * à une utilisation en **mode maintenance (live CD)**.
>
> Dans le cadre de cette formation, **on se limite à la consultation et à la compréhension** de leur usage.

---

## Vérification et inspection d’un système de fichiers

## `tune2fs` — afficher les informations d’un volume ext4

Avec l’option `-l`, `tune2fs` lit les **métadonnées de maintenance** d’un système de fichiers ext2/3/4 sans modifier ses paramètres.

```bash
sudo tune2fs -l /dev/sdb1
```

Exemples de champs utiles :

* **Filesystem state** : indique si le système est propre (`clean`) ou s’il a besoin d’une vérification.
* **Last checked** : date de la dernière vérification.
* **Mount count / Maximum mount count** : nombre de montages avant vérification automatique.
> [!info]
> `tune2fs -l` affiche des informations. D’autres options de `tune2fs` modifient les paramètres du système de fichiers.

---

## `fsck` — vérifier la cohérence d’un système de fichiers

`fsck` est un frontal qui appelle l’outil de vérification adapté au type de système de fichiers. Les options et possibilités dépendent de cet outil ; les exemples suivants concernent ext4, démonté, dans le laboratoire.

```bash
sudo fsck -n /dev/sdb1
```

Options courantes :

* `-n` : demande une vérification sans réparation, selon l’outil appelé ; conserver le volume démonté
* `-y` : répond “oui” automatiquement aux corrections
* Vérifier les options du vérificateur concerné dans son manuel ; ne pas automatiser les réparations pendant cette initiation.

> [!danger]
> ⚠️ N’utilisez **jamais `fsck` sur une partition montée**.
> Pour une vérification en sécurité : démontez d’abord le volume :
> ```bash
> sudo umount /dev/sdb1
> ```

---

## `e2fsck` — version spécifique pour ext2/ext3/ext4

`e2fsck` est la version dédiée des systèmes de fichiers ext*.
`fsck` appelle normalement `e2fsck` pour un système ext2/3/4. L’utiliser directement permet de choisir ses options propres.

Exemple :

```bash
sudo e2fsck -fn /dev/sdb1
```

Options :

* `-f` : force la vérification même si le système est marqué “clean”.
* `-n` : lecture seule, sans réparation.

---

## Sauvegarde et prévention

Avant toute manipulation ou vérification, il est essentiel de **sauvegarder les données importantes**.
Deux commandes simples permettent de le faire :

## Copie complète d’un répertoire

```bash
cp -rpv /home/sam/Documents /mnt/backup/
```

* `-r` : récursif
* `-p` : conserve les droits et dates
* `-v` : affiche les fichiers copiés

## Synchronisation rapide avec `rsync`

```bash
rsync -av /home/sam/Documents /mnt/backup/
```

* `-a` : mode archive
* `-v` : mode verbeux
* `--delete` (optionnel) : synchronise en supprimant les fichiers disparus côté source

---

## À retenir
> [!tip]
> * **`tune2fs -l`** : affiche l’état d’un système de fichiers ext4 sans le modifier.
> * **`fsck` / `e2fsck`** : vérifient et réparent la cohérence d’un volume (uniquement quand il est démonté).
> * **`df -i`** : indique l’utilisation des inodes (utile pour diagnostiquer un disque “plein” de petits fichiers).
> * Toujours **sauvegarder avant de corriger** : `cp -r` ou `rsync` permettent de copier les données ; contrôler la destination et vérifier la restauration.
> * En cas de doute, **ne jamais exécuter une vérification sur le disque système actif** — passer par un live CD ou un mode de secours.
