# TP 08 — Préparer et monter un espace de données

> Durée estimée : 90 min

> Chapitres associés : [24 — Se repérer dans l’arborescence Linux](https://kayasam.github.io/lpi101/lpi101/24-arborescence-fhs/), [25 — Concevoir un partitionnement simple](https://kayasam.github.io/lpi101/lpi101/25-concevoir-partitionnement/), [26 — Créer des partitions et des systèmes de fichiers](https://kayasam.github.io/lpi101/lpi101/26-partitions-formatage/), [27 — Monter un système de fichiers et utiliser fstab](https://kayasam.github.io/lpi101/lpi101/27-montage-fstab/), [28 — Mesurer l’espace, la mémoire et les inodes](https://kayasam.github.io/lpi101/lpi101/28-espace-disque-inodes/), [29 — Vérifier et entretenir les systèmes de fichiers](https://kayasam.github.io/lpi101/lpi101/29-integrite-maintenance/)

---

## Objectifs

- Distinguer disque, partitions, système de fichiers et point de montage.
- Formater et monter une partition ext4 de laboratoire.
- Tester une entrée fstab et vérifier un volume démonté.

## Avant de commencer

Pour travailler sur une VM neuve sans ajouter de matériel dans l’hyperviseur, la préparation fournie transforme un fichier de 2 Gio en disque de laboratoire `/dev/loopN`. Le formateur explique cette préparation ; les objectifs portent sur les partitions et montages. Conserve le même terminal et les variables de ce TP. Ne remplace pas DISQUE_TP par le disque système. Ne rejoue pas truncate si une image de ce nom est encore attachée ou montée. Le TP se termine par le nettoyage de fstab et le détachement de ce disque.

**Préparation fournie :**

```bash
sudo apt update
sudo apt install fdisk e2fsprogs util-linux
mkdir -p ~/lpi101-tp/tp08
cd ~/lpi101-tp/tp08
truncate -s 2G disque-labo.img
DISQUE_TP=$(sudo losetup --find --show --nooverlap --partscan disque-labo.img)
printf '%s\n' "$DISQUE_TP" > disque-actuel.txt
sudo losetup "$DISQUE_TP"
```

---

## Partie A — Identifier et partitionner (25 min)

**A1.** Affiche les disques et le système de fichiers de `/`. Quel élément indique que le disque de laboratoire n’est pas le disque système ?

**A2.** Sur le disque de laboratoire, crée une table GPT, une première partition de 512 Mio et une deuxième avec le reste. La correction utilise sfdisk, version pilotable par texte des outils de partitionnement.

**A3.** Avant tout formatage, affiche la table de partitions et explique ce qui manque encore pour stocker des fichiers.

---

## Partie B — Formater et monter (25 min)

**B1.** Formate la première partition en ext4 avec l’étiquette `lpi101-data`, puis affiche son type et son UUID.

**B2.** Crée `/mnt/lpi101-data`, monte la partition et écris un petit fichier `preuve.txt` contenant `Montage réussi`. Vérifie le montage.

**B3.** Prépare puis active la deuxième partition comme swap. Affiche les espaces d’échange actifs.

---

## Partie C — Tester fstab (20 min)

**C1.** Démonte la partition, sauvegarde fstab puis ajoute une entrée par UUID avec l’option noauto et le commentaire `lpi101-tp08`.

**C2.** Monte le volume en ne donnant que son point de montage. Vérifie que la preuve réapparaît. Quelle information mount a-t-il lue ?

**C3.** Compare la place du volume, celle de ses fichiers et l’utilisation des inodes.

---

## Partie D — Vérifier et nettoyer (20 min)

**D1.** Démonte la partition puis lance une vérification ext4 en lecture seule, sans réparation.

**D2.** Retire l’entrée de laboratoire de fstab, désactive son swap et détache seulement son disque loop. Vérifie que l’entrée a disparu.
