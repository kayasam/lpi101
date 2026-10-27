# TP 13. Agrandir un volume logique de laboratoire

> Durée estimée : 45 min

> Chapitres associés : [C02. Comprendre et manipuler LVM](https://cours.kaya.ovh/lpi101/complements/02-lvm/)

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
