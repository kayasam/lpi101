---
title: "04. Préparer une installation Linux"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/04-preparer-installation"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/04-preparer-installation/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/04-preparer-installation/04-preparer-installation.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Choisir une image d’installation et reconnaître les étapes du démarrage.

**Repères LPI 101 :** 101.2, 102.1, 102.2.

---

## Télécharger une ISO officielle

Une **ISO** est une image disque contenant tout le nécessaire pour installer un système d’exploitation.
Elle peut être gravée sur un DVD ou copiée sur une clé USB pour démarrer l’installation.

## Les principaux types d’ISO

|Type d’image|Description|Utilisation|
|---|---|---|
|**NetInstall**|Image généralement plus petite qu’un DVD complet ; taille variable selon la version. Télécharge les paquets depuis Internet pendant l’installation.|Idéale pour une installation personnalisée ou sur machine virtuelle.|
|**CD/DVD complet**|Contient une sélection importante de paquets ; d’autres peuvent demander un téléchargement.|À utiliser sans connexion Internet.|
|**Live**|Permet de tester Linux sans l’installer (exécution depuis la RAM).|Utile pour découvrir l’environnement avant installation.|
|**Minimal / Cloud / ARM**|Versions destinées à des environnements spécifiques (serveurs, cloud, architectures ARM).|Pour les usages avancés.|

## Liens officiels :

- Debian : [https://www.debian.org/distrib/netinst](https://www.debian.org/distrib/netinst)

- Ubuntu : [https://ubuntu.com/download](https://ubuntu.com/download)

---

## BIOS vs UEFI

Le **BIOS** (Basic Input/Output System) et **UEFI** (Unified Extensible Firmware Interface) sont des programmes de bas niveau qui démarrent le matériel et chargent le système d’exploitation.

|Caractéristique|BIOS|UEFI|
|---|---|---|
|Période|Ancien (années 1980)|Moderne (depuis 2010)|
|Interface|Souvent textuelle|Textuelle ou graphique selon le firmware|
|Partitionnement courant|MBR ou GPT selon le système|GPT habituellement ; partition système EFI|
|Chargeur d’amorçage|Stocké dans le MBR|Stocké dans la partition EFI|
|Sécurité|Aucune|Secure Boot (signature numérique)|

Les PC récents utilisent UEFI, mais le BIOS reste courant sur les machines virtuelles ou les anciens ordinateurs.

---

## Le chargeur d’amorçage (GRUB)

Le **chargeur d’amorçage** (ou **bootloader**) est le programme lancé juste après le BIOS/UEFI.
Son rôle est de **charger le noyau Linux** et de **démarrer le système**.

Le plus utilisé sous Linux est **GRUB 2**.

## Étapes de démarrage :

1. Le BIOS ou l’UEFI charge GRUB depuis le disque.

2. GRUB affiche un menu si plusieurs OS sont présents.

3. GRUB charge le noyau Linux (`vmlinuz`) et l’image initrd.

4. Le noyau initialise le matériel et lance le processus d’initialisation, qui démarre notamment les services.

## Commandes utiles :

```bash
sudo grub-install /dev/sda    # Exemple BIOS sur disque de laboratoire ; ne pas lancer sans identifier la cible
sudo update-grub              # Met à jour la configuration
sudo nano /etc/default/grub   # Modifie les options du menu
```

Pour restaurer GRUB, on peut démarrer sur un **Live CD** et réinstaller le chargeur manuellement.

## Pour aller plus loin :

[102.2 Leçon 1](https://learning.lpi.org/fr/learning-materials/101-500/102/102.2/102.2_01/#:~:text=GRUB%20est%20le%20chargeur%20d,d'entr%C3%A9es%20de%20menu%20s%C3%A9par%C3%A9es.)

---

## À retenir
> [!info]
> - Une **ISO** contient l’image du système à installer (NetInstall, Live, complète, etc.).
> - Le **partitionnement** organise l’espace disque (/, /home, swap…).
> - **UEFI** remplace le **BIOS** sur les systèmes récents.
> - Le **chargeur d’amorçage GRUB** lance le noyau Linux au démarrage.
> - En cas de problème, GRUB peut être réparé depuis un **Live CD**.

> [!info] Démarrage UEFI
> L’installation de GRUB en UEFI utilise la partition système EFI montée et des options adaptées. La commande BIOS sur `/dev/sda` ne constitue pas une procédure universelle de réparation.
