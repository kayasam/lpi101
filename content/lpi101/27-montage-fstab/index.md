---
title: "27. Monter un système de fichiers et utiliser fstab"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/27-montage-fstab"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/27-montage-fstab/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/27-montage-fstab/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/27-montage-fstab/27-montage-fstab.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Rendre un système de fichiers accessible puis comprendre son montage au démarrage.

**Repères LPI 101 :** 104.3.

**Commandes à connaître :** `mount`, `umount`, `findmnt`, `blkid`.

**Fichiers et emplacements :** `/etc/fstab`.

---

## Montage et démontage

Un **système de fichiers** doit être monté dans un répertoire pour être accessible.

![Un volume ext4 sur /dev/sdb1 devient accessible sous /mnt après son montage. Les fichiers restent sur le volume.](https://kayasam.github.io/lpi101/assets/course-media/3f58013fb2e518fa.svg)

Le répertoire `/mnt` sert ici de porte d’entrée vers les fichiers du volume : monter ne déplace pas les données.

## `mount` — monter un système de fichiers

```bash
sudo mount /dev/sdb1 /mnt/disque1
```

→ `/mnt` devient le point d’accès à la partition.

Afficher les systèmes montés :

```bash
mount | grep "^/dev"
```

---

## `umount` — démonter un système de fichiers

```bash
sudo umount /mnt/disque1
```
> [!warning]
> ⚠️ Ne pas oublier de fermer les fichiers ouverts avant de démonter.
> Si un message indique que le périphérique est occupé :
>
> ```bash
> sudo lsof +f -- /mnt/disque1
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
