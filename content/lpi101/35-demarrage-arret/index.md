---
title: "35. Démarrage, arrêt et cibles systemd"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/35-demarrage-arret"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/35-demarrage-arret/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/35-demarrage-arret/35-demarrage-arret.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Suivre le démarrage et reconnaître les principaux modes du système.

**Repères LPI 101 :** 101.2, 101.3.

**Commandes à connaître :** `systemctl`, `shutdown`, `wall`, `who`.

---

## Introduction

Sous Linux, la gestion du démarrage, de l’arrêt et des modes de fonctionnement du système repose sur **systemd**, le gestionnaire d’initialisation utilisé par la plupart des distributions modernes.
Il remplace les anciens systèmes comme **SysVinit** et permet de contrôler finement le démarrage des services, les transitions entre modes (console, graphique, secours) et l’arrêt propre du système.

---

![Les étapes d’un démarrage Debian courant : UEFI, GRUB, noyau et systemd.](https://cours.kaya.ovh/lpi101/assets/course-media/4867440117dde9d6.svg)

## Commandes de base

## Arrêt et redémarrage avec systemctl

```bash
sudo systemctl poweroff
sudo systemctl reboot
```

Ces commandes demandent à **systemd** d’arrêter ou de redémarrer le système proprement.
Tous les services sont stoppés dans le bon ordre avant la coupure ou le redémarrage.

---

## Commande shutdown

La commande historique `shutdown` reste disponible et fonctionne toujours sous systemd.
Elle permet en plus de **planifier un arrêt** ou un **redémarrage différé**.

```bash
sudo shutdown now         # arrêt immédiat
sudo shutdown -r now      # redémarrage immédiat
sudo shutdown +10         # arrêt dans 10 minutes
sudo shutdown -c          # annule un arrêt planifié
```

---

## Différence entre poweroff et shutdown

| Commande   | Fonction principale       | Particularité                                                    |
| ---------- | ------------------------- | ---------------------------------------------------------------- |
| `poweroff` | Arrêt immédiat du système | exécute la coupure directement via systemd                       |
| `shutdown` | Arrêt planifié ou différé | permet de choisir un délai, un redémarrage ou d’annuler l’action |

En pratique, `shutdown` est plus flexible, tandis que `poweroff` agit plus directement.

---

## Les cibles systemd (targets)

Systemd utilise des **targets** pour définir l’état du système (équivalent moderne des *runlevels*).
Chaque target correspond à un ensemble de services actifs.

| Target              | Ancien runlevel | Description                      |
| ------------------- | --------------- | -------------------------------- |
| `poweroff.target`   | 0               | arrêt complet du système         |
| `rescue.target`     | 1               | mode de secours mono-utilisateur |
| `multi-user.target` | 3               | mode console multi-utilisateur   |
| `graphical.target`  | 5               | mode graphique                   |
| `reboot.target`     | 6               | redémarrage du système           |

---

## Commandes de gestion des modes

Afficher le mode par défaut :

```bash
systemctl get-default
```

Changer temporairement de mode :

```bash
sudo systemctl isolate multi-user.target
```

Définir le mode par défaut au démarrage :

```bash
sudo systemctl set-default graphical.target
```
---
## Différence entre graphical.target et multi-user.target

## `graphical.target`

Mode graphique complet — utilisé par défaut sur les distributions de bureau (Debian GNOME, Ubuntu, Fedora Workstation, etc.).
Il lance :

- Tous les services nécessaires au multi-utilisateur (`multi-user.target`)

- Le **système d’affichage** (serveur Xorg ou compositeur Wayland)

- Le **gestionnaire de session** (GDM, LightDM, SDDM, etc.)

- La possibilité d’ouvrir une session graphique ; l’environnement de bureau est lancé lors de la connexion de l’utilisateur

**Conséquences :**

- Charge CPU et mémoire plus élevée

- Démarrage plus long

- Accès à une interface graphique complète

---

## `multi-user.target`

Mode console / texte — sans interface graphique.
Il charge uniquement les services essentiels : réseau, journaux, SSH, etc.
L’utilisateur accède à une console texte (TTY) pour administrer le système.

**Conséquences :**

- Consommation mémoire et CPU faible

- Idéal pour les serveurs ou environnements légers

- Moins de risques de plantage liés à l’interface graphique

---

## Mode de secours

Le **mode rescue** permet de démarrer un environnement minimal avec un seul utilisateur (root).
Il est souvent utilisé pour la maintenance ou le dépannage.

Entrer dans le mode de secours :

```bash
sudo systemctl rescue
```

Revenir au mode normal :

```bash
sudo systemctl default
```

---

## Relier les étapes du démarrage

```text
BIOS/UEFI → chargeur GRUB → noyau et initramfs → init/systemd (PID 1)
          → services et cibles → connexion utilisateur
```

L’initramfs fournit un environnement initial, notamment pour accéder au système de fichiers racine. Les journaux du démarrage s’observent avec `journalctl -b` ; les messages du noyau avec `journalctl -k`.

## Prévenir les utilisateurs

```bash
who
wall 'Redémarrage prévu dans 10 minutes pour maintenance.'
sudo shutdown -r +10
sudo shutdown -c
```

`wall` diffuse un message aux terminaux qui l’acceptent. `shutdown` annonce aussi l’arrêt planifié. Une transition de cible peut fermer des sessions : effectuer les démonstrations de secours depuis la console de la VM.

## Repères historiques

SysVinit utilise des niveaux d’exécution, `/etc/inittab` et des scripts sous `/etc/init.d/`. `init` et `telinit` peuvent changer de niveau sur les systèmes concernés. Upstart est un autre système d’initialisation, à reconnaître sans le déployer ici. `acpid` traite des événements ACPI sur les installations qui l’utilisent ; systemd-logind prend aussi en charge des événements d’alimentation selon la configuration.

---

## À retenir
> [!tip]
> * **systemd** gère le démarrage, l’arrêt et les différents modes du système.
> * Les **targets** remplacent les anciens *runlevels* (ex. `multi-user`, `graphical`, `rescue`).
> * **`shutdown`** permet de planifier ou d’annuler un arrêt, tandis que **`poweroff`** agit immédiatement.
> * **`systemctl isolate`** permet de basculer entre modes sans redémarrer.
> * Le **mode rescue** offre un environnement minimal pour effectuer des réparations système.
