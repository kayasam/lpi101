---
title: "25 — Concevoir un partitionnement simple"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/25-concevoir-partitionnement"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/25-concevoir-partitionnement/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/25-concevoir-partitionnement.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Choisir les points de montage en fonction de l’usage de la machine.

**Repères LPI 101 :** 102.1.

**Commandes à connaître :** `lsblk -f`, `swapon --show`.

---

## Comprendre le partitionnement

Lors de l’installation, il faut définir **comment le disque sera découpé**.
Chaque partition aura un **point de montage**, c’est-à-dire un dossier où le système l’intégrera.

|Point de montage|Rôle principal|Taille conseillée|
|---|---|---|
|`/`|Racine du système (fichiers du noyau, binaires, etc.)|20 à 30 Go|
|`/home`|Données personnelles des utilisateurs|le reste du disque|
|`/boot`|Fichiers nécessaires au démarrage|selon les noyaux conservés et la distribution|
|`swap`|Espace d’échange (pas un point de montage)|selon RAM, charge et hibernation|
|`/var` _(optionnel)_|Journaux, caches et données variables|selon les services et leur croissance|
|`/srv` _(optionnel)_|Données des services (web, ftp, etc.)|selon besoin|

---

## Un exemple pour une VM de formation

Pour un disque virtuel de 40 Gio, un exemple possible en UEFI est une partition système EFI d’environ 512 Mio, une racine `/` d’environ 24 Gio, un espace swap adapté à la VM et le reste pour `/home`. Ces valeurs illustrent un choix ; elles ne constituent pas une règle universelle.

```text
Disque virtuel
├── partition EFI → /boot/efi (FAT, démarrage UEFI)
├── partition ext4 → / (système)
├── partition ext4 → /home (données personnelles)
└── espace swap (partition ou autre organisation adaptée)
```

La partition EFI et `/boot` ont des rôles différents : `/boot` contient les noyaux et images de démarrage ; l’ESP contient les exécutables EFI. Une installation BIOS n’utilise pas une ESP pour son démarrage BIOS. En BIOS avec GPT, GRUB peut demander une petite partition BIOS Boot.

## Pourquoi séparer des points de montage ?

| Point | Intérêt d’une séparation | Question à se poser |
|---|---|---|
| `/home` | Séparer les données des comptes du système | Quelle place pour les fichiers des utilisateurs ? |
| `/var` | Isoler les écritures des journaux, caches et services | Quels services et quelle croissance prévue ? |
| `/boot` | Répondre à certains besoins de démarrage | Combien de noyaux faut-il conserver ? |

Séparer apporte de l’isolation mais impose de répartir l’espace. Pour une première VM, le partitionnement guidé reste adapté ; on étudie ensuite le résultat avec `lsblk -f`.

## Dimensionner le swap

Le swap aide à gérer la pression mémoire ; il ne remplace pas la RAM. Sa taille dépend de la mémoire disponible, de la charge et d’un éventuel besoin d’hibernation. Le rapport « une à deux fois la RAM » n’est pas une règle générale.

## À retenir

> [!tip]
> Un point de montage est un endroit dans l’arborescence. Le choix des partitions dépend de l’usage et du mode de démarrage, pas seulement de la taille du disque.
