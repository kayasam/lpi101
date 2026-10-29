# TP 08a. Ajouter un disque NVMe et le monter

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

---

## Partie B — Identifier le disque (5 min)

**B1.** Affiche les disques de la machine. Quel est le nom du nouveau disque ? Comment le reconnais-tu ?

> [!warning]
> Dans la suite, remplace `/dev/nvme0n2` par le nom trouvé ici. Ne touche jamais au disque qui porte `/`.

---

## Partie C — Partitionner (10 min)

**C1.** Avec `fdisk`, crée sur le nouveau disque une table **GPT** et **une seule partition** qui occupe tout le disque.

**C2.** Vérifie que la partition apparaît.

---

## Partie D — Formater (5 min)

**D1.** Formate la partition en **ext4** avec l’étiquette `donnees`, puis affiche son type et son UUID.

---

## Partie E — Monter (10 min)

**E1.** Crée le point de montage `/mnt/donnees` et monte la partition dessus.

**E2.** Vérifie le montage, puis crée un fichier `preuve.txt` sur le disque.

**E3.** Démonte la partition. Le fichier est-il encore visible dans `/mnt/donnees` ? Pourquoi ?

---

## Partie F — Montage permanent (5 min)

**F1.** Ajoute une ligne dans `/etc/fstab` (par UUID) pour monter la partition automatiquement sur `/mnt/donnees`. Teste-la sans redémarrer, puis redémarre et vérifie.
