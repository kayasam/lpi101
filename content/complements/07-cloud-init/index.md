---
title: "C07. Découvrir Cloud-init"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="complements/07-cloud-init"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/complements/07-cloud-init/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/complements/complements/c07-cloud-init/c07-cloud-init.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Comprendre l’initialisation d’une image cloud et lire un exemple YAML.

**Repères LPI 101 :** 102.6.

> [!info] Complément
> À découvrir après les bases, selon le rythme du groupe.

---

## Introduction

**Cloud-init** est un outil utilisé dans les environnements **cloud** (AWS, Azure, OpenStack, Proxmox, VirtualBox, etc.) pour **personnaliser automatiquement une machine virtuelle lors de son premier démarrage**.
Il permet d’automatiser la configuration d’une instance sans intervention manuelle : création d’utilisateurs, configuration réseau, installation de paquets, déploiement de clés SSH, etc.

Cloud-init récupère les métadonnées et la configuration auprès d’une **source de données** (datasource), en général au format **YAML**, et exécute les actions correspondantes dès le premier boot de la machine.
C’est un **outil largement utilisé** pour la configuration initiale des systèmes Linux déployés à partir d’images “cloud”.

---

## Fonctionnement général

Lors du premier démarrage :

1. **Le système détecte un support cloud-init** (image ISO, metadatas d’un cloud, etc.).

2. Cloud-init **lit les fichiers de configuration** fournis (souvent `user-data` et `network-config`).

3. Il exécute les directives pour :

    - configurer le clavier, la langue et le fuseau horaire ;

    - créer ou modifier des utilisateurs ;

    - activer SSH et déployer des clés ;

    - installer des paquets ;

    - exécuter des commandes personnalisées ;

    - écrire des fichiers ou des scripts sur le disque.

Une fois les actions terminées, la machine est prête à l’emploi, déjà configurée selon les besoins.

---

## Créer le fichier `user-data.yaml`

Ce fichier définit les **paramètres de base** appliqués au premier démarrage.

Exemple de laboratoire avec un compte par défaut fourni par l’image :

```yaml
#cloud-config

# Langue et fuseau horaire
keyboard:
  layout: fr
locale: fr_FR.UTF-8
timezone: Europe/Paris

# Gestion des utilisateurs
manage_etc_hosts: true
password: dawan
chpasswd: { expire: False }
ssh_pwauth: True

# Paquets à installer
packages:
  - micro
  - htop
```

Ce fichier peut aussi contenir des directives plus avancées :

- `users` pour créer des comptes spécifiques,

- `runcmd` pour exécuter des commandes au premier démarrage,

- `write_files` pour écrire des fichiers de configuration.

Avant d’utiliser le fichier, on peut vérifier sa validité :

```bash
sudo cloud-init schema -c user-data.yaml
```

---

## Créer le fichier `network-config.yaml`

Ce fichier utilise ici la configuration réseau Cloud-init **version 2**. Le moteur qui l’applique dépend de l’image ; il ne faut pas supposer que toute installation Debian utilise Netplan. Dans un fichier NoCloud `network-config` séparé, les champs commencent directement à `version`.

Exemple : activer le DHCP sur les interfaces dont le nom commence par `en` :

```yaml
version: 2
ethernets:
  all_interfaces:
    match:
      name: "en*"
    dhcp4: true
```

Exemple : IP fixe sur une interface secondaire :

```yaml
version: 2
ethernets:
  enp0s3:
    dhcp4: true
  enp0s8:
    dhcp4: false
    addresses:
      - 192.168.56.200/24
```

---

## Générer l’image ISO de configuration

Créer aussi `meta-data.yaml`, qui identifie l’instance :

```yaml
instance-id: debcloud-001
local-hostname: debcloud
```

Une fois les fichiers prêts, on utilise l’outil `cloud-localds` (fourni par le paquet `cloud-image-utils` sur Debian) pour créer une petite image ISO que la VM lira au démarrage :

```bash
sudo apt install cloud-image-utils
cloud-localds cloud-init.iso user-data.yaml meta-data.yaml
```

Si un fichier réseau est utilisé :

```bash
cloud-localds --network-config=network-config.yaml cloud-init.iso user-data.yaml meta-data.yaml
```

Cette ISO sera montée comme **lecteur CD** dans la machine virtuelle au moment du premier boot.

---

## Utilisation dans VirtualBox ou un hyperviseur

1. Télécharger une image cloud officielle (ex. Ubuntu ou Debian Cloud).

2. Créer une nouvelle VM et **utiliser ce disque comme disque système**.

3. Ajouter un **lecteur CD-ROM** dans lequel on montera `cloud-init.iso`.

4. Démarrer la VM : cloud-init applique automatiquement la configuration.

Le nom du compte par défaut dépend de l’image (souvent `ubuntu` ou `debian`). De nombreuses images n’ont pas de mot de passe de connexion utilisable tant qu’il n’a pas été configuré. Les exemples `dawan` et `admin` sont des valeurs de démonstration pour un laboratoire isolé, à remplacer ; pour un déploiement, préférer une clé publique SSH et un compte verrouillé pour le mot de passe.

---

## Réinitialiser Cloud-init

Si la configuration doit être rejouée sans recréer la VM, on peut nettoyer les traces précédentes :

```bash
sudo cloud-init clean --logs
sudo reboot
```

Sur une VM de laboratoire préparée pour cela, ce nettoyage permet de rejouer des étapes d’initialisation. Leur résultat dépend de la source de données et de la configuration ; un changement d’instance-id identifie une nouvelle instance. Préférer un clone neuf pour répéter proprement la démonstration.

---

## Fonctions avancées

Cloud-init offre de nombreuses possibilités :

## Exécution de commandes (`runcmd`)

```yaml
runcmd:
  - apt update
  - apt install -y apache2
  - systemctl enable --now apache2
```

## Création d’utilisateurs

```yaml
users:
  - name: admin
    plain_text_passwd: admin
    sudo: ALL=(ALL) NOPASSWD:ALL
    shell: /bin/bash
```

## Écriture de fichiers (`write_files`)

```yaml
write_files:
  - path: /etc/motd
    permissions: '0644'
    content: |
      Bienvenue sur cette VM configurée automatiquement avec Cloud-init !
```

---

## Cloud-init sous Debian et Ubuntu

Les images **Ubuntu Cloud** sont prêtes à l’emploi : il suffit d’ajouter l’ISO cloud-init.
Sous **Debian**, quelques ajustements peuvent être nécessaires :

- installation du paquet `console-setup` pour le clavier,

- correction du fichier `/etc/locale.gen` pour la francisation,

- choix des paquets et composants nécessaires selon l’image et l’hyperviseur, en suivant la documentation de la distribution.

---

## À retenir

- Cloud-init automatise la **configuration initiale** d’une VM ou d’un serveur cloud.

- Il lit un fichier YAML (`user-data`, `network-config`) et applique les directives au premier démarrage.

- L’image ISO générée par `cloud-localds` remplace les installations manuelles répétitives.

- Compatible avec la plupart des hyperviseurs et clouds modernes.

- Idéal pour **déployer rapidement** plusieurs machines préconfigurées (mot de passe, SSH, paquets, réseau…).

Les fichiers YAML et l’ISO du cours d’origine sont conservés dans `ressources/fichiers`, sans modification : ce sont des exemples historiques de laboratoire, à distinguer des commandes corrigées de cette note.

Documentation : [NoCloud — Cloud-init](https://docs.cloud-init.io/en/latest/reference/datasources/nocloud.html) et [cloud-localds — Debian](https://manpages.debian.org/trixie/cloud-image-utils/cloud-localds.1.en.html).
