# 34. Observer les événements matériels

> [!note] Objectif
> Lire les événements du noyau et observer la détection d’un périphérique.

**Repères LPI 101 :** 101.1, 101.2.

**Commandes à connaître :** `dmesg`, `journalctl -k`, `udevadm`, `lshw`, `hwinfo`.

---

## Introduction

Linux détecte automatiquement le matériel lors du démarrage, mais aussi **dynamiquement** lorsqu’un périphérique est branché (USB, disque externe, carte réseau…).
Ces événements sont gérés par le **sous-système udev** et enregistrés dans les **journaux du noyau**.

Ce chapitre aborde :

- l’affichage des **messages système du noyau** (`dmesg`) ;

- la gestion des périphériques par **udev** ;

- l’inspection matérielle avec des outils plus complets (`hwinfo`, `lshw`).

---

## `dmesg` — messages du noyau

Le noyau Linux journalise tous les événements matériels : détection des disques, périphériques USB, pilotes chargés, erreurs, etc.

Afficher les derniers messages :

```bash
sudo dmesg | less
```

Chercher une ligne spécifique :

```bash
sudo dmesg | grep -i usb
sudo dmesg | grep -i ethernet
```

Afficher uniquement les nouveaux messages en temps réel (utile lors d’un branchement USB) :

```bash
sudo dmesg --follow
```

---

## `journalctl -k` — journal des événements du noyau (systemd)

Sous systemd, les messages de `dmesg` sont aussi consultables via `journalctl` :

```bash
sudo journalctl -k
```

Afficher uniquement les 20 dernières lignes :

```bash
sudo journalctl -k -n 20
```

Surveiller en temps réel :

```bash
sudo journalctl -kf
```

---

## `udevadm` — gestion des périphériques à chaud

`udev` est le composant chargé de **créer dynamiquement les fichiers dans `/dev/`** lors du branchement d’un périphérique.

Lister les périphériques connus par udev :

```bash
udevadm info --export-db | less
```

Afficher les informations d’un périphérique particulier :

```bash
udevadm info --query=all --name=/dev/sdb
```

Surveiller en direct les événements matériels (branchements / retraits) :

```bash
udevadm monitor
```

---

## `hwinfo` — inventaire complet du matériel

`hwinfo` fournit un **résumé exhaustif** de la configuration matérielle (CPU, mémoire, réseau, bus, USB…).

Installer si nécessaire :

```bash
sudo apt install hwinfo
```

Lister tout le matériel détecté :

```bash
sudo hwinfo --short
```

Afficher les détails d’un composant précis :

```bash
sudo hwinfo --cpu
sudo hwinfo --network
```

---

## `lshw` — description hiérarchique du matériel

`lshw` affiche la **hiérarchie complète du matériel**, depuis la carte mère jusqu’aux périphériques.

```bash
sudo lshw | less
```

Pour une vue synthétique :

```bash
sudo lshw -short
```

Exporter un rapport matériel (utile pour un inventaire) :

```bash
sudo lshw -html > rapport_hardware.html
```

---

## À retenir

> [!tip]
> - Linux enregistre tous les événements matériels dans les **journaux du noyau**.
> - `dmesg` permet de suivre en direct ce que détecte le système (USB, disques, pilotes…).
> - Avec systemd, les messages du noyau sont aussi accessibles via **`journalctl -k`**.
> - **udev** gère la création dynamique des périphériques dans `/dev/` lors des branchements.
> - `udevadm monitor` permet d’observer en temps réel les événements matériels.
> - `hwinfo` fournit un inventaire matériel très complet.
> - `lshw` affiche une **vue hiérarchique** de l’ensemble du matériel du système.
