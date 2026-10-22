---
title: "19 — Utilisateurs, groupes et droits administrateur"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/19-utilisateurs-groupes"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/19-utilisateurs-groupes/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/19-utilisateurs-groupes.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Reconnaître un compte et donner les droits nécessaires sans travailler constamment en root.

**Commandes à connaître :** `id`, `groups`, `useradd`, `usermod`, `passwd`, `groupadd`, `sudo`, `su`.

---

## Introduction

Sous Linux, la gestion des utilisateurs et des groupes permet de **contrôler l’accès au système** et de **séparer les droits** entre les différents comptes.
Chaque utilisateur dispose d’un identifiant unique, d’un répertoire personnel et d’un ensemble de permissions.
Cette séparation est essentielle pour la sécurité et la stabilité du système.

Dans cette section, nous verrons :

* la différence entre **root** et les **utilisateurs standards** ;
* le rôle des fichiers **/etc/passwd** et **/etc/group** ;
* les principales **commandes de gestion des comptes**.

---

## Comptes root et utilisateurs standards

## Le compte **root**

* C’est le **super-utilisateur** du système.
* Il a **tous les droits**, sans restriction : il peut installer, modifier, ou supprimer n’importe quel fichier.
* Son répertoire personnel est généralement `/root`.
* On l’utilise uniquement pour des tâches d’administration.

Pour exécuter une commande en tant que root :

```bash
sudo commande
```

Exemple :

```bash
sudo apt update
```

Pour ouvrir une session root :

```bash
sudo -i
```

ou, sur certains systèmes :

```bash
su -
```
> [!warning]
> ⚠️ **Attention :** une erreur avec le compte root peut rendre le système inutilisable.
> Toujours préférer `sudo` à une connexion directe en root.

---

## Les utilisateurs standards

* Ce sont les comptes créés pour les personnes ou les services.
* Chaque utilisateur possède :

  * un identifiant unique (**UID**) ;
  * un groupe principal (**GID**) ;
  * un répertoire personnel (souvent `/home/nom_utilisateur`) ;
  * un shell par défaut (souvent `/bin/bash`).

L’utilisateur ne peut pas modifier les fichiers système sans droits administratifs.

Pour connaître le nom de l’utilisateur actuel :

```bash
whoami
```

Pour afficher des informations sur son compte :

```bash
id
```

---

## Les fichiers de configuration

## `/etc/passwd`

Ce fichier contient les informations de base sur tous les comptes utilisateurs.

Afficher son contenu :

```bash
cat /etc/passwd
```

Chaque ligne correspond à un utilisateur et contient plusieurs champs séparés par des `:` :

```text
nom_utilisateur:x:UID:GID:commentaire:/home/nom:/bin/bash
```

Exemple :

```text
kaya:x:1000:1000:Samuel Guillard:/home/kaya:/bin/bash
```

* **nom_utilisateur** : nom du compte
* **x** : mot de passe chiffré (stocké dans `/etc/shadow`)
* **UID** : identifiant de l’utilisateur
* **GID** : identifiant du groupe principal
* **commentaire** : informations facultatives
* **/home/nom** : répertoire personnel
* **/bin/bash** : shell par défaut

---

## `/etc/group`

Ce fichier définit les groupes du système.
Chaque ligne contient la liste des membres d’un groupe :

```text
nom_du_groupe:x:GID:liste_utilisateurs
```

Exemple :

```text
sudo:x:27:kaya
```

Cela signifie que l’utilisateur **kaya** appartient au groupe **sudo**.

Pour afficher les groupes d’un utilisateur :

```bash
groups kaya
```

---

## Commandes de gestion des utilisateurs

## `useradd` — créer un nouvel utilisateur

Crée un utilisateur avec un répertoire personnel et un shell par défaut.

```bash
sudo useradd -m -s /bin/bash alice
```

* `-m` : crée automatiquement le dossier `/home/alice`
* `-s` : spécifie le shell de connexion

---

## `passwd` — définir ou changer un mot de passe

```bash
sudo passwd alice
```

Le système demande alors d’entrer et de confirmer le mot de passe.

Pour modifier son propre mot de passe :

```bash
passwd
```

---

## `usermod` — modifier un utilisateur existant

Modifier le nom, le shell ou ajouter un utilisateur à un groupe :

```bash
sudo usermod -l nouveau_nom alice
sudo usermod -s /bin/zsh alice
sudo usermod -aG sudo alice
```

* `-l` : change le nom d’utilisateur
* `-s` : change le shell
* `-aG` : ajoute l’utilisateur à un groupe (sans retirer les autres)

---
## `groupadd` — créer un nouveau groupe

Crée un groupe système ou un groupe d’utilisateurs personnalisé.

```bash
sudo groupadd compta
```

- `groupadd` : commande utilisée pour créer un groupe.

- `compta` : nom du groupe créé, qui sera ajouté au fichier `/etc/group`.

Pour vérifier la création du groupe :

```bash
getent group compta
```

Et pour supprimer un groupe :

```bash
sudo groupdel compta
```
## `deluser` — supprimer un utilisateur

Supprime un compte utilisateur :

```bash
sudo userdel alice
```

Supprimer aussi son répertoire personnel :

```bash
sudo userdel -r alice
```

---

## Consultation et vérification

Lister les utilisateurs actuellement connectés :

```bash
who
```

Afficher des informations détaillées sur les sessions actives :

```bash
loginctl list-sessions
```

---

## Utiliser su et sudo

```bash
id
groups
sudo whoami
su -
```

`sudo` exécute une commande selon les autorisations du compte, en demandant habituellement son mot de passe. `su -` ouvre une session de connexion pour root et demande normalement le mot de passe de root. Quitter cette session avec `exit`.

Sur Debian, les membres du groupe `sudo` sont généralement autorisés par la configuration fournie. La politique se consulte dans `/etc/sudoers` et `/etc/sudoers.d/` ; utiliser `visudo` pour toute modification. `/etc/shadow` contient les empreintes de mots de passe et des informations d’expiration, et doit rester protégé.

---

## À retenir
> [!tip]
> * Le compte **root** dispose de tous les droits : à utiliser avec précaution.
> * Les utilisateurs standards ont des droits limités et un répertoire personnel dans `/home`.
> * Les informations sur les utilisateurs et groupes sont stockées dans `/etc/passwd` et `/etc/group`.
> * Commandes principales :
>
>   * `useradd` : créer un utilisateur
>   * `passwd` : définir ou changer un mot de passe
>   * `usermod` : modifier un utilisateur existant
>   * `userdel` : supprimer un utilisateur
> * Les groupes permettent de gérer les permissions collectivement.
