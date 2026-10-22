# 27 — Monter un système de fichiers et utiliser fstab

> [!note] Objectif
> Rendre un système de fichiers accessible puis comprendre son montage au démarrage.

**Repères LPI 101 :** 104.3.

**Commandes à connaître :** `mount`, `umount`, `findmnt`, `blkid`.

**Fichiers et emplacements :** `/etc/fstab`.

---

## Montage et démontage

Un **système de fichiers** doit être monté dans un répertoire pour être accessible.

## `mount` — monter un système de fichiers

```bash
sudo mount /dev/sdb1 /mnt
```

→ `/mnt` devient le point d’accès à la partition.

Afficher les systèmes montés :

```bash
mount | grep "^/dev"
```

---

## `umount` — démonter un système de fichiers

```bash
sudo umount /mnt
```
> [!warning]
> ⚠️ Ne pas oublier de fermer les fichiers ouverts avant de démonter.
> Si un message indique que le périphérique est occupé :
>
> ```bash
> sudo lsof +f -- /mnt
> ```

---

## Montage automatique avec `/etc/fstab`

Le fichier `/etc/fstab` définit les systèmes de fichiers montés automatiquement au démarrage.

Exemple d’entrée :

```text
UUID=a7b5d-1234   /data   ext4   defaults   0   2
```

Colonnes :

1. périphérique ou UUID
2. point de montage
3. type de FS
4. options (`defaults`, `ro`, `noexec`, `user`, etc.)
5. dump (0 = non)
6. ordre de vérification (0 = désactivé, 1 = racine, 2 = autres)

Tester une ligne avant redémarrage :

```bash
sudo mount -a
```

---

## Choisir les options et identifier le volume

`ro` demande un montage en lecture seule ; `rw`, en lecture-écriture. `noexec`, `nosuid` et `nodev` limitent respectivement l’exécution directe, les bits SUID/SGID et l’interprétation des fichiers de périphériques sur le montage.

```bash
lsblk -f
findmnt /
```

Un UUID identifie un système de fichiers de manière plus stable qu’un nom tel que `/dev/sdb1`. Une étiquette peut être utilisée sous la forme `LABEL=donnees`. Les six champs de `fstab` décrivent la source, le point de montage, le type, les options, le champ dump et l’ordre de vérification.

## Vérifier avant de redémarrer

Après modification de `/etc/fstab`, garder une console ouverte, vérifier les chemins et tester le montage voulu. `mount -a` tente les montages automatiques de `fstab` mais ne simule pas complètement un redémarrage et ne remonte pas forcément ce qui est déjà monté.

```bash
sudo systemctl daemon-reload
sudo mount -a
findmnt
```

Sous systemd, les entrées de `fstab` sont converties en unités `.mount`. Des unités `.automount` peuvent déclencher un montage à l’accès ; leur écriture manuelle reste un approfondissement.

## À retenir

> [!tip]
> Formater prépare le contenu ; monter le rend accessible à un point de l’arborescence. Démonter avant de retirer un support ; en cas de volume occupé, quitter les dossiers et applications qui l’utilisent.
