---
title: "TP 13. Agrandir un volume logique de laboratoire"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="complements/02-lvm"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/complements/02-lvm/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/complements/02-lvm/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/complements/complements/c02-lvm/tp/tp-13-lvm.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


> Durée estimée : 45 min

> Chapitres associés : [C02. Comprendre et manipuler LVM](https://kayasam.github.io/lpi101/complements/02-lvm/)

---

## Objectifs

- Relier PV, VG et LV.
- Agrandir séparément volume logique et système de fichiers.
- Démonter et retirer les ressources dans le bon ordre.

## Avant de commencer

Complément facultatif après le stockage. La préparation fournit un disque loop distinct de celui du TP 08. Le groupe `lpi101_vg_tp13` doit être absent avant l’atelier. Ne jamais utiliser les volumes du système, même si leurs noms ressemblent aux exemples du cours. Si LVM refuse les périphériques loop avec sa configuration locale, le formateur fournit un disque virtuel supplémentaire dédié.

> [!info] Atelier optionnel
> À proposer après les bases, selon le rythme du groupe.

**Préparation fournie :**

```bash
sudo apt update
sudo apt install lvm2 e2fsprogs
mkdir -p ~/lpi101-tp/tp13
cd ~/lpi101-tp/tp13
truncate -s 768M pv-labo.img
PV_TP=$(sudo losetup --find --show --nooverlap pv-labo.img)
printf '%s\n' "$PV_TP" > pv-actuel.txt
sudo losetup "$PV_TP"
```

---

## Partie A — Construire les trois niveaux (15 min)

**A1.** Initialise le périphérique de laboratoire comme volume physique puis crée le groupe lpi101_vg_tp13. Affiche la taille et l’espace libre.

**A2.** Crée un LV nommé donnees de 256 Mio, formate-le en ext4 puis monte-le sous `/mnt/lpi101-lvm`.

---

## Partie B — Agrandir sans perdre le fichier (20 min)

**B1.** Relève la taille du LV et celle du système de fichiers, puis agrandis seulement le LV de 128 Mio.

**B2.** Agrandis maintenant le système de fichiers ext4 et vérifie le contenu de preuve.txt.

---

## Partie C — Nettoyer (10 min)

**C1.** Démonte puis retire le LV, le VG et le PV dans cet ordre ; détache le périphérique loop de cet atelier.
