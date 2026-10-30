---
title: "TP 13. Agrandir un volume logique de laboratoire — Correction"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="complements/02-lvm"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/complements/02-lvm/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/complements/02-lvm/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/complements/complements/c02-lvm/tp/tp-13-lvm-correction.md">↓ Télécharger le corrigé (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://kayasam.github.io/lpi101/complements/02-lvm/tp">Énoncé</a><a class="exercise-correction" href="https://kayasam.github.io/lpi101/complements/02-lvm/tp-corrigev2" aria-current="page">Corrigé</a></nav>

> Essaie chaque question avant d’ouvrir **Afficher la correction**. Chaque réponse se replie indépendamment.

> Durée estimée : 55 min

> Chapitres associés : [C02. Comprendre et manipuler LVM](https://kayasam.github.io/lpi101/complements/02-lvm/)

---

## Objectifs

- Ajouter un disque à la VM et l’identifier sans risque.
- Relier PV, VG et LV.
- Agrandir séparément volume logique et système de fichiers.
- Démonter et retirer les ressources dans le bon ordre.

## Avant de commencer

Complément facultatif après le stockage (TP 08a). Le TP utilise un **nouveau disque NVMe de 2 Go**, entièrement consacré à LVM. Le groupe `lpi101_vg_tp13` doit être absent avant l’atelier.

> [!warning] Le système utilise déjà LVM
> L’installation Debian a créé son propre groupe de volumes (par exemple `debian13-vg`) qui porte `/` et le swap. Ne touche jamais à ses PV, VG ou LV : toutes les commandes de ce TP visent uniquement le nouveau disque et le groupe `lpi101_vg_tp13`.

> [!info] Atelier optionnel
> À proposer après les bases, selon le rythme du groupe.

---

## Partie A — Ajouter et identifier le disque (10 min)

**A1.** Éteins la VM, ajoute-lui un **nouveau disque dur NVMe de 2 Go**, puis redémarre-la. Installe ensuite le paquet `lvm2` s’il est absent.

> [!success]- Afficher la correction — A1
> 1. Éteindre la VM : `sudo poweroff`.
> 2. Dans VMware : **VM → Settings… → Add… → Hard Disk → Next**.
> 3. Type de disque : **NVMe** → **Create a new virtual disk**.
> 4. Taille : **2 GB** → **Next** → **Finish** → **OK**.
> 5. Démarrer la VM, puis :
>
> ```bash
> sudo apt update
> sudo apt install lvm2 e2fsprogs
> ```
>
> Sur une Debian installée avec LVM, `lvm2` est déjà présent : apt l’indique simplement.

**A2.** Identifie le nouveau disque et enregistre son chemin dans une variable `DISQUE`. Vérifie qu’il n’a ni partition, ni point de montage, ni signature. Quels PV et VG existent déjà sur la machine ?

> [!success]- Afficher la correction — A2
> ```bash
> lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
> DISQUE=/dev/nvme0n2
> lsblk "$DISQUE"
> sudo wipefs "$DISQUE"
> sudo pvs
> sudo vgs
> ```
>
> Le nouveau disque fait **2G**, sans partition ni point de montage. Si le disque NVMe du TP 08a est encore présent (`nvme0n1`), le nouveau s’appelle `nvme0n2` ; adapter la variable au nom réellement observé.
>
> `wipefs` sans option se contente de **lister** les signatures : aucune ligne affichée signifie un disque vierge. `pvs` et `vgs` montrent le LVM du système (par exemple `/dev/sda3` dans `debian13-vg`), qui ne doit pas être modifié.
>
> On utilise ici le disque entier comme PV, sans partition. Créer d’abord une partition de type « Linux LVM » est aussi possible ; c’est une convention, pas une obligation.

---

## Partie B — Construire les trois niveaux (15 min)

**B1.** Initialise le nouveau disque comme volume physique, puis crée le groupe `lpi101_vg_tp13`. Affiche la taille et l’espace libre.

> [!success]- Afficher la correction — B1
> ```bash
> sudo pvcreate "$DISQUE"
> sudo vgcreate lpi101_vg_tp13 "$DISQUE"
> sudo pvs "$DISQUE"
> sudo vgs lpi101_vg_tp13
> ```
>
> Le PV est le support ; le VG regroupe son espace (environ 2 Go, un peu moins à cause des métadonnées LVM). Un VG peut contenir plusieurs PV, mais un seul suffit pour ce premier atelier.

**B2.** Crée un LV nommé `donnees` de 256 Mio, formate-le en ext4 puis monte-le sous `/mnt/lpi101-lvm`. Écris un fichier `preuve.txt` dedans.

> [!success]- Afficher la correction — B2
> ```bash
> sudo lvcreate -L 256M -n donnees lpi101_vg_tp13
> sudo mkfs.ext4 /dev/lpi101_vg_tp13/donnees
> sudo mkdir -p /mnt/lpi101-lvm
> sudo mount /dev/lpi101_vg_tp13/donnees /mnt/lpi101-lvm
> printf 'Donnee a conserver\n' | sudo tee /mnt/lpi101-lvm/preuve.txt
> lsblk "$DISQUE"
> ```
>
> Le LV joue le rôle de volume à formater ; le système de fichiers et le point de montage restent des objets distincts. `lsblk` montre le LV `lpi101_vg_tp13-donnees` sous le disque.

---

## Partie C — Agrandir sans perdre le fichier (20 min)

**C1.** Relève la taille du LV et celle du système de fichiers, puis agrandis seulement le LV de 128 Mio.

> [!success]- Afficher la correction — C1
> ```bash
> sudo lvs lpi101_vg_tp13
> df -h /mnt/lpi101-lvm
> sudo lvextend -L +128M /dev/lpi101_vg_tp13/donnees
> sudo lvs lpi101_vg_tp13
> df -h /mnt/lpi101-lvm
> ```
>
> Le LV passe de 256 à 384 Mio ; sans option de redimensionnement du FS, celui-ci garde encore sa taille initiale. Lire les valeurs plutôt qu’attendre exactement les mêmes arrondis de df.

**C2.** Agrandis maintenant le système de fichiers ext4 et vérifie le contenu de `preuve.txt`.

> [!success]- Afficher la correction — C2
> ```bash
> sudo resize2fs /dev/lpi101_vg_tp13/donnees
> df -h /mnt/lpi101-lvm
> cat /mnt/lpi101-lvm/preuve.txt
> ```
>
> L’agrandissement ext4 est possible à chaud dans ce cas. On n’en déduit pas qu’une réduction ou un autre système de fichiers suit la même procédure.

**C3.** Donne au LV tout l’espace encore libre du groupe, en agrandissant le système de fichiers dans la même commande.

> [!success]- Afficher la correction — C3
> ```bash
> sudo lvextend -r -l +100%FREE /dev/lpi101_vg_tp13/donnees
> sudo vgs lpi101_vg_tp13
> df -h /mnt/lpi101-lvm
> cat /mnt/lpi101-lvm/preuve.txt
> ```
>
> `-l` compte en extents (ou en pourcentage) au lieu d’une taille : `+100%FREE` prend tout l’espace libre du VG, dont la colonne VFree tombe à 0. `-r` (`--resizefs`) enchaîne l’agrandissement du système de fichiers : c’est la forme habituelle en production, qui évite d’oublier l’étape de C2. Le fichier est toujours là.

---

## Partie D — Nettoyer (10 min)

**D1.** Démonte puis retire le LV, le VG et le PV dans cet ordre. Vérifie que seul le LVM du système reste visible.

> [!success]- Afficher la correction — D1
> ```bash
> sudo umount /mnt/lpi101-lvm
> sudo lvremove /dev/lpi101_vg_tp13/donnees
> sudo vgremove lpi101_vg_tp13
> sudo pvremove "$DISQUE"
> sudo rmdir /mnt/lpi101-lvm
> sudo pvs
> sudo vgs
> lsblk "$DISQUE"
> ```
>
> `lvremove` demande une confirmation : lire le nom avant de répondre `y`. Ensuite, `pvs` et `vgs` ne montrent plus que le LVM du système, et le disque de 2 Go est redevenu vierge.

**D2.** *(Facultatif)* Éteins la VM et retire le disque de 2 Go dans VMware.

> [!success]- Afficher la correction — D2
> 1. `sudo poweroff`.
> 2. Dans VMware : **VM → Settings…**, sélectionner le disque NVMe de 2 Go → **Remove** → **OK**.
>
> Retirer le disque seulement après D1. Si on retire un disque qui porte encore un PV, LVM signale au démarrage suivant un PV manquant dans `lpi101_vg_tp13`.
