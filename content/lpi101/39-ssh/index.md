---
title: "39. Se connecter à distance avec SSH"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/39-ssh"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/39-ssh/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://cours.kaya.ovh/lpi101/lpi101/39-ssh/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/39-ssh/39-ssh.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Utiliser SSH, transférer un fichier et comprendre l’authentification par clé.

**Commandes à connaître :** `ssh`, `ssh-keygen`, `ssh-copy-id`, `scp`.

---

## Introduction

**SSH (Secure Shell)** est un protocole permettant d’administrer un système Linux à distance, de manière chiffrée.
Il permet :

- d’exécuter des commandes à distance,

- de transférer des fichiers,

- ou de se connecter à une session shell distante.

Sous Linux, le client SSH est intégré.
Sous Windows, il est inclus depuis Windows 10 et peut être utilisé via **PowerShell** ou **Windows Terminal**.

> **Liens externes :**
>
> - [Tutoriel SSH — Microsoft Learn](https://learn.microsoft.com/fr-fr/windows/terminal/tutorials/ssh)
>
> - [Apprenez à utiliser le client SSH de Windows 11](https://www.it-connect.fr/comment-utiliser-le-client-ssh-natif-de-windows-10/)
>

---

## Utilisation du client SSH

Syntaxe générale :

```bash
ssh [-p port] [utilisateur@]hôte
```

Exemples :

```bash
ssh debian@192.168.56.101
ssh root@serveur.exemple.local -p 2222
```

Si aucun utilisateur n’est précisé, celui de la session actuelle est utilisé.
Lors de la première connexion, vérifier l’empreinte de la clé d’hôte auprès d’une source connue avant de l’accepter.

---

## Génération de clés SSH

Une paire de clés est composée :

- d’une **clé privée** (gardée sur le poste local),

- et d’une **clé publique** (copiée sur le serveur).

Créer une paire de clés sur le poste client :

```bash
ssh-keygen -t ed25519
```

Le programme crée :

```text
~/.ssh/id_ed25519      (clé privée)
~/.ssh/id_ed25519.pub  (clé publique)
```

**Ed25519** est un choix courant pour ce laboratoire ; les algorithmes autorisés dépendent aussi des politiques et des systèmes utilisés.

---

## Copier la clé sur le serveur

## Depuis Linux

```bash
ssh-copy-id utilisateur@serveur
```

## Depuis Windows (PowerShell)

```powershell
type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh utilisateur@serveur "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

Vérifie ensuite que le contenu de la clé publique est bien ajouté dans `~/.ssh/authorized_keys` sur le serveur.

---

## Connexion sans mot de passe

Une fois la clé installée :

```bash
ssh utilisateur@serveur
```

Le mot de passe du compte distant n’est normalement plus demandé. Une **phrase de passe de la clé privée** peut encore être demandée si la clé est protégée et n’est pas chargée dans un agent.

Après avoir vérifié l’authentification par clé dans **une seconde connexion** et conservé un accès console, on peut désactiver le mot de passe dans une configuration du serveur :

```bash
sudo tee /etc/ssh/sshd_config.d/00-disable-password.conf <<< "PasswordAuthentication no"
sudo sshd -t
sudo systemctl reload ssh
```

---

## Commandes utiles

|Action|Commande|
|---|---|
|Tester une connexion|`ssh utilisateur@serveur`|
|Copier un fichier distant|`scp utilisateur@serveur:/chemin/fichier .`|
|Copier un répertoire entier|`scp -r dossier utilisateur@serveur:/chemin/`|
|Vérifier le service SSH|`sudo systemctl status ssh`|
|Voir les logs SSH|`sudo journalctl -u ssh`|

---

## Exemple de fichier de configuration client (`~/.ssh/config`)

```bash
Host debian
    HostName 192.168.56.101
    User sam
    Port 22
    IdentityFile ~/.ssh/id_ed25519
```

Connexion simplifiée :

```bash
ssh debian
```

---

## Structure du dossier `.ssh` sous Windows

Sous Windows, les fichiers SSH sont stockés dans :
`%USERPROFILE%\.ssh\` (ou `$env:USERPROFILE\.ssh` dans PowerShell)

|Fichier|Rôle|
|---|---|
|`id_ed25519` ou `id_rsa`|Clé privée (à ne jamais partager).|
|`id_ed25519.pub` ou `id_rsa.pub`|Clé publique à copier sur le serveur.|
|`known_hosts`|Liste des serveurs déjà connus et validés.|
|`config`|Fichier de configuration du client SSH (alias, ports, chemins de clés, etc.).|
|`known_hosts.old`|Sauvegarde automatique de la liste des serveurs connus.|

> Ces fichiers sont automatiquement utilisés par **OpenSSH**, intégré à PowerShell et Windows Terminal.

---

## Bonnes pratiques sur la gestion des clés

Il est **possible d’utiliser la même clé SSH sur plusieurs serveurs**, mais ce n’est pas toujours conseillé.

|Cas d’usage|Recommandation|
|---|---|
|Environnement personnel / lab|Une seule clé pour tout est acceptable.|
|Environnement professionnel|Créer une clé par utilisateur ou par serveur.|
|Serveurs sensibles (production)|Clé spécifique par utilisateur, protégée par passphrase.|
|Automatisation (Ansible, scripts, CI/CD)|Clé dédiée à la tâche, droits restreints et stockage protégé ; utiliser un agent ou un gestionnaire de secrets selon le contexte.|

Exemple de génération de deux clés :

```bash
# Clé pour le lab
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_lab

# Clé pour la production
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_prod
```

Puis configuration dans `~/.ssh/config` :

```bash
Host lab-*
    IdentityFile ~/.ssh/id_ed25519_lab

Host prod-*
    IdentityFile ~/.ssh/id_ed25519_prod
```

---

## À retenir
> [!tip]
> - SSH chiffre les communications entre client et serveur.
>
> - Une clé privée protégée et une vérification de l’identité du serveur renforcent l’authentification.
>
> - Les fichiers de configuration et de clés se trouvent dans `~/.ssh/` (ou `%userprofile%\.ssh\` sous Windows).
>
> - SCP permet de transférer des fichiers de manière sécurisée.
>
> - Une clé peut être utilisée sur plusieurs serveurs, mais il est préférable d’en générer une par usage critique.
