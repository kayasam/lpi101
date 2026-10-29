---
title: "TP 08a. Ajouter un disque NVMe et le monter — Correction"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/27-montage-fstab"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/27-montage-fstab/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/27-montage-fstab/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/27-montage-fstab/tp/tp-08a-disque-nvme-correction.md">↓ Télécharger le corrigé (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://kayasam.github.io/lpi101/lpi101/27-montage-fstab/tp">Énoncé</a><a class="exercise-correction" href="https://kayasam.github.io/lpi101/lpi101/27-montage-fstab/tp-corrigev2" aria-current="page">Corrigé</a></nav>

> Essaie chaque question avant d’ouvrir **Afficher la correction**. Chaque réponse se replie indépendamment.

> Durée estimée : 40 min

> Chapitres associés : [26. Créer des partitions et des systèmes de fichiers](https://kayasam.github.io/lpi101/lpi101/26-partitions-formatage/), [27. Monter un système de fichiers et utiliser fstab](https://kayasam.github.io/lpi101/lpi101/27-montage-fstab/)

---

## Objectifs

- Ajouter un disque NVMe à la VM dans VMware.
- Partitionner, formater et monter ce nouveau disque.
- Rendre le montage permanent avec `/etc/fstab`.

---

## Partie A — Ajouter le disque dans VMware (5 min)

**A1.** Éteins la VM, puis ajoute-lui un **nouveau disque dur NVMe de 5 Go**. Redémarre la VM.

> [!success]- Afficher la correction — A1
> 1. Éteindre la VM : `sudo poweroff`.
> 2. Dans VMware : **VM → Settings… → Add… → Hard Disk → Next**.
> 3. Type de disque : **NVMe** → **Create a new virtual disk**.
> 4. Taille : **5 GB** → **Next** → **Finish** → **OK**.
> 5. Démarrer la VM.

---

## Partie B — Identifier le disque (5 min)

**B1.** Affiche les disques de la machine. Quel est le nom du nouveau disque ? Comment le reconnais-tu ?

> [!success]- Afficher la correction — B1
> ```bash
> lsblk
> ```
>
> Le nouveau disque fait **5G**, n’a **aucune partition** et **aucun point de montage**. Selon la VM, il s’appelle `nvme0n1` (disque système en SATA/SCSI) ou `nvme0n2` (disque système déjà en NVMe).
>
> La suite utilise `/dev/nvme0n2`. Sur NVMe, les partitions prennent un `p` : `nvme0n2p1`.

---

## Partie C — Partitionner (10 min)

**C1.** Avec `fdisk`, crée sur le nouveau disque une table **GPT** et **une seule partition** qui occupe tout le disque.

> [!success]- Afficher la correction — C1
> ```bash
> sudo fdisk /dev/nvme0n2
> ```
>
> Dans fdisk :
>
> | Touche | Action |
> |---|---|
> | `g` | créer une table GPT vide |
> | `n` | nouvelle partition |
> | `Entrée` ×3 | numéro 1, premier et dernier secteur par défaut (tout le disque) |
> | `p` | afficher le résultat |
> | `w` | écrire et quitter |

**C2.** Vérifie que la partition apparaît.

> [!success]- Afficher la correction — C2
> ```bash
> lsblk /dev/nvme0n2
> ```
>
> `nvme0n2p1` apparaît sous le disque. Elle n’a pas encore de système de fichiers : impossible d’y ranger des fichiers.

---

## Partie D — Formater (5 min)

**D1.** Formate la partition en **ext4** avec l’étiquette `donnees`, puis affiche son type et son UUID.

> [!success]- Afficher la correction — D1
> ```bash
> sudo mkfs.ext4 -L donnees /dev/nvme0n2p1
> sudo blkid /dev/nvme0n2p1
> ```
>
> `blkid` affiche `LABEL="donnees"`, `TYPE="ext4"` et l’`UUID` à noter pour fstab.

---

## Partie E — Monter (10 min)

**E1.** Crée le point de montage `/mnt/donnees` et monte la partition dessus.

> [!success]- Afficher la correction — E1
> ```bash
> sudo mkdir -p /mnt/donnees
> sudo mount /dev/nvme0n2p1 /mnt/donnees
> ```

**E2.** Vérifie le montage, puis crée un fichier `preuve.txt` sur le disque.

> [!success]- Afficher la correction — E2
> ```bash
> findmnt /mnt/donnees
> df -h /mnt/donnees
> echo "Montage réussi" | sudo tee /mnt/donnees/preuve.txt
> ls /mnt/donnees
> ```
>
> On voit `preuve.txt` et `lost+found` (créé par mkfs.ext4).

**E3.** Démonte la partition. Le fichier est-il encore visible dans `/mnt/donnees` ? Pourquoi ?

> [!success]- Afficher la correction — E3
> ```bash
> cd ~
> sudo umount /mnt/donnees
> ls /mnt/donnees
> ```
>
> Le dossier est vide : le fichier est **sur le disque**, pas dans le dossier. Démonté, `/mnt/donnees` redevient un simple répertoire vide. Si `umount` répond « target is busy », sortir du dossier (`cd ~`).

---

## Partie F — Montage permanent (5 min)

**F1.** Ajoute une ligne dans `/etc/fstab` (par UUID) pour monter la partition automatiquement sur `/mnt/donnees`. Teste-la sans redémarrer, puis redémarre et vérifie.

> [!success]- Afficher la correction — F1
> ```bash
> sudo blkid -s UUID -o value /dev/nvme0n2p1
> sudo cp /etc/fstab /etc/fstab.bak
> sudo nano /etc/fstab
> ```
>
> Ajouter en fin de fichier (avec l’UUID affiché) :
>
> ```text
> UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  /mnt/donnees  ext4  defaults  0  2
> ```
>
> Tester **avant** de redémarrer :
>
> ```bash
> sudo systemctl daemon-reload
> sudo mount -a
> findmnt /mnt/donnees
> cat /mnt/donnees/preuve.txt
> ```
>
> Aucun message d’erreur et `preuve.txt` réapparaît : la ligne est correcte. Redémarrer (`sudo reboot`) puis refaire `findmnt /mnt/donnees`.
>
> En cas d’erreur dans fstab, restaurer la sauvegarde : `sudo cp /etc/fstab.bak /etc/fstab`.
