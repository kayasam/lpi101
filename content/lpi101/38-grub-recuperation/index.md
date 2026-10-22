---
title: "38. Comprendre GRUB et la récupération"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/38-grub-recuperation"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/38-grub-recuperation/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/38-grub-recuperation/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/38-grub-recuperation/38-grub-recuperation.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Lire la configuration de GRUB et comprendre les options de récupération.

**Repères LPI 101 :** 101.2, 102.2.

---

## Introduction

**GRUB (GRand Unified Bootloader)** est le chargeur d’amorçage utilisé par la majorité des distributions Linux.
Il est responsable de :

- charger le noyau Linux ;
- transmettre les paramètres au noyau ;
- proposer un menu de démarrage ;
- permettre la récupération en cas de problème (mode rescue ou édition des options).

Comprendre GRUB est essentiel pour diagnostiquer un système qui ne démarre plus, modifier les paramètres du noyau, ou restaurer un accès administrateur local dans un laboratoire autorisé.

---

## Fonctionnement général de GRUB

GRUB s’affiche juste après le BIOS/UEFI. Il accède à sa configuration dans :

```text
/boot/grub/grub.cfg
```

Ce fichier est **généré automatiquement** depuis les scripts dans `/etc/grub.d/` et les options de `/etc/default/grub`.

Pour régénérer la configuration (ex : après modification du noyau ou du fond d’écran) :

```bash
sudo update-grub
```

---

## Navigation dans le menu GRUB

Lors du démarrage, GRUB affiche un menu contenant :

- l’entrée principale (Debian / Ubuntu / autre) ;

- le sous-menu "Options avancées" ;

- les différents noyaux installés.

Touches utiles :

|Touche|Action|
|---|---|
|**Entrée**|Démarrer|
|**e**|Éditer les options de démarrage|
|**c**|Ouvrir un shell GRUB|
|**Esc**|Revenir au menu principal|

---

## Modifier les options du noyau (édition rapide)

Utile pour :

- activer des options de debug ;
- désactiver un pilote problématique ;
- démarrer en mode single-user ;
- réinitialiser un mot de passe root (procédure dans le TP d’origine).

Étapes :

1. Sélectionner l’entrée Debian/Ubuntu.
2. Appuyer sur **e** pour éditer.
3. Trouver la ligne commençant par :
    ```text
    linux /boot/vmlinuz-...
    ```
4. Ajouter une option à la fin, par exemple :

    ```text
    systemd.unit=rescue.target
    ```

5. Démarrer avec **Ctrl + X** ou **F10**.

---

## Configuration du fichier /etc/default/grub

Ce fichier contient les options principales :

```text
GRUB_DEFAULT=0
GRUB_TIMEOUT=5
GRUB_DISTRIBUTOR=`( . /etc/os-release && echo ${NAME} )`
GRUB_CMDLINE_LINUX_DEFAULT="quiet"
GRUB_CMDLINE_LINUX=""
```

- **GRUB_DEFAULT=0**
    Sélectionne automatiquement **la première entrée** du menu GRUB au démarrage (index 0).

- **GRUB_TIMEOUT=5**
    Délai (en secondes) durant lequel GRUB attend avant de démarrer l’entrée par défaut.

- **GRUB_DISTRIBUTOR=`( . /etc/os-release && echo ${NAME} )`**
    Automatiquement remplacé par le **nom de la distribution** (Debian, Ubuntu…), utilisé pour étiqueter les entrées dans le menu GRUB.

- **GRUB_CMDLINE_LINUX_DEFAULT="quiet"**
    Options passées au noyau en mode normal.
    `quiet` masque les messages de démarrage pour un boot plus propre (souvent ajouté : `quiet splash`).

- **GRUB_CMDLINE_LINUX=""**
    Options supplémentaires toujours passées au noyau (souvent laissé vide, utilisé pour des réglages avancés).

Une fois modifié :

```bash
sudo update-grub
```

---

## Reconnaître les variantes de GRUB

GRUB 2 utilise `grub.cfg`, généré à partir de la configuration. GRUB Legacy utilisait notamment `menu.lst` ou `grub.conf`. Sous Debian, `update-grub` facilite la génération ; `grub-mkconfig` est l’outil sous-jacent à reconnaître. `grub-install` installe des éléments du chargeur : ses arguments dépendent du mode BIOS/UEFI et de la cible.

En récupération, `rescue.target` et `emergency.target` offrent des environnements de secours distincts ; `init=/bin/bash` remplace le processus initial par un shell. Le chiffrement du disque et les protections de démarrage peuvent imposer d’autres étapes.

## À retenir — GRUB
> [!tip]
> - GRUB charge le noyau et permet de modifier les paramètres du démarrage.
> - L’édition rapide (touche **e**) est indispensable pour dépanner un système.
> - Les modes **rescue**, **emergency** et `init=/bin/bash` permettent différents niveaux de récupération.
> - `/etc/default/grub` contrôle la configuration principale, et `update-grub` la régénère.
> - La réinitialisation du mot de passe root via GRUB nécessite un accès local à la machine.
