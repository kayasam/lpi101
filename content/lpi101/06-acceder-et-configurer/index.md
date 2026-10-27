---
title: "06. Accéder à la VM et préparer sa session"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/06-acceder-et-configurer"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/06-acceder-et-configurer/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/06-acceder-et-configurer/06-acceder-et-configurer.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Ouvrir une session locale ou distante et préparer les outils nécessaires.

---

## Accéder à la machine virtuelle

Une fois Debian installée, il existe plusieurs manières d’interagir avec la machine virtuelle.
Le choix dépend du **confort souhaité** et du **type d’utilisation** (formation, serveur, tests, etc.).

---

## Accès direct via VirtualBox

L’accès le plus simple consiste à **ouvrir la console intégrée** de VirtualBox.
C’est l’écran affiché par défaut au démarrage de la VM.

## Améliorer l’expérience : _les “Guest Additions”_

Les **additions invité** permettent :

- Le **redimensionnement automatique** de la fenêtre,

- Le **partage du presse-papiers**,

- Le **glisser-déposer** entre hôte et VM,

- Le **partage de dossiers**.

**Documentation officielle :**

- [Guest Additions VirtualBox (Oracle)](https://docs.oracle.com/en/virtualization/virtualbox/7.1/user/guestadditions.html#additions-windows)

- [Installer les Guest Additions sur Linux](https://linuxconfig.org/install-virtualbox-guest-additions-on-linux-guest)

---

## Première connexion SSH

SSH (Secure Shell) permet de se connecter à un système Linux depuis un autre ordinateur, **en ligne de commande**.
Il suffit que le paquet **openssh-server** soit installé sur la VM.

```bash
sudo apt install openssh-server
```

Connexion depuis une autre machine :

```bash
ssh utilisateur@adresse_ip
```

---

## Outils d’accès SSH

|Outil|Plateforme|Points forts|Limites|
|---|---|---|---|
|**Windows Terminal**|Windows 10/11|Intégré, rapide, moderne, compatible avec WSL|Interface uniquement en ligne de commande|
|**Visual Studio Code (Remote SSH)**|Multiplateforme|Accès SSH avec interface graphique et éditeur complet|Nécessite l’extension _Remote - SSH_|
|**MobaXterm**|Windows|Interface riche, gestion de sessions multiples, transfert de fichiers intégré|Logiciel tiers, non libre|

---

## Un environnement agréable

Disposer d’un **environnement de travail clair et personnalisé** est essentiel pour travailler efficacement :

- Affichage lisible, terminal coloré, invite de commande adaptée ;

- Outils essentiels installés (`vim`, `htop`, `curl`, `tree`, etc.) ;

- Accès fluide à la VM via la méthode de ton choix.

Un environnement bien configuré améliore la **productivité**, la **concentration** et le **plaisir d’utilisation**.

---
## Préparer les outils de formation

```bash
sudo apt update
sudo apt install sudo nano vim less man-db curl htop
```

Si `sudo` n’est pas encore installé ou si le compte n’est pas autorisé, utiliser la console de la VM et `su -` avec le mot de passe root défini à l’installation. Depuis cette session root :

```bash
apt update
apt install sudo
usermod -aG sudo sam
exit
```

Remplacer `sam` par le compte créé pendant l’installation. Fermer puis rouvrir sa session pour que l’ajout au groupe soit pris en compte. Le chapitre sur les utilisateurs explique les groupes ; celui sur APT détaille les paquets.

## Reconnaître sa session

```bash
whoami
hostname
pwd
```

Le premier résultat indique le compte, le deuxième la machine et le troisième le répertoire courant. C’est utile avant toute modification de configuration.

## À retenir
> [!info]
> - On peut accéder à une machine virtuelle **directement depuis VirtualBox** grâce à la console intégrée.
>
> - L’installation des **Guest Additions** améliore le confort (redimensionnement, presse-papiers, partage de fichiers).
>
> - L’accès **SSH** permet de se connecter à distance en ligne de commande.
>
> - Plusieurs outils existent pour le SSH :
>
>     - **Windows Terminal** : rapide et intégré, mais sans interface graphique.
>
>     - **VS Code (Remote SSH)** : offre un environnement complet et visuel.
>
>     - **MobaXterm** : pratique pour les transferts de fichiers, mais non libre.
>
> - Un **environnement de travail agréable** (couleurs, outils, confort d’accès) favorise la productivité et l’apprentissage.
