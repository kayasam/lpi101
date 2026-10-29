---
title: "TP 08a. Ajouter un disque NVMe et le monter"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/27-montage-fstab"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/27-montage-fstab/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/27-montage-fstab/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/27-montage-fstab/tp/tp-08a-disque-nvme.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://kayasam.github.io/lpi101/lpi101/27-montage-fstab/tp" aria-current="page">Énoncé</a><a class="exercise-correction" href="https://kayasam.github.io/lpi101/lpi101/27-montage-fstab/tp-corrigev2">Afficher les corrections</a></nav>

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
