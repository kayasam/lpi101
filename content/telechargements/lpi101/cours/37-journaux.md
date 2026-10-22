# 37 — Consulter les journaux et diagnostiquer

> [!note] Objectif
> Choisir le journal utile et filtrer ses messages.

**Repères LPI 101 :** 101.2.

**Commandes à connaître :** `journalctl`, `less`, `tail`, `grep`.

---

## Introduction

Sous Linux, l’analyse des **journaux (logs)** est essentielle pour comprendre le fonctionnement du système, diagnostiquer des pannes et surveiller les services.
Depuis l’arrivée de **systemd**, la majorité des logs sont centralisés par **systemd-journald** et consultables avec `journalctl`.
Les applications traditionnelles continuent néanmoins d’écrire leurs fichiers de logs dans **`/var/log/`**.

Ce chapitre couvre :

- l’utilisation efficace de **journalctl** ;
- la recherche avancée via les champs du journal systemd ;
- l’utilisation des **facilities** et **priorités**  ;
- les fichiers de logs classiques dans `/var/log/`.

---

## Logs centralisés avec journalctl

`journalctl` permet d’explorer les journaux collectés par **systemd-journald**.

## Affichage général

```bash
sudo journalctl           # Tous les logs accessibles
sudo journalctl -r        # Affichage inversé (du plus récent au plus ancien)
sudo journalctl -b        # Logs du dernier démarrage
sudo journalctl -f        # Suivi en temps réel
```

## Filtrer par gravité (priorité)

```bash
sudo journalctl -p 3 -xb   # Erreurs et niveaux critiques
sudo journalctl -p warning # Avertissements et niveaux plus graves
sudo journalctl -p alert..err
```

## Filtrer par service (unit systemd)

```bash
sudo journalctl -u ssh
sudo journalctl -u apache2
```

## Filtrer par date

```bash
sudo journalctl --since "2025-01-01"
sudo journalctl --since "1 hour ago"
sudo journalctl --until "10 minutes ago"
```

## Filtrer par application ou champ structuré

`journalctl` peut filtrer sur n’importe quel **champ structuré** du journal :
(exemples issus du manuel `systemd.journal-fields`)

```bash
journalctl _PID=1234
journalctl _EXE=/usr/bin/ssh
journalctl _COMM=nginx
journalctl _SYSTEMD_UNIT=cron.service
```

---

## Facilities et priorités syslog

Avant systemd, le système de logs reposait principalement sur **syslog**.
Systemd conserve ces informations pour la compatibilité.

## Liste des facilities

|Code|Facility|Description|
|---|---|---|
|0|kern|Messages du noyau|
|1|user|Programmes utilisateur|
|2|mail|Serveurs de mail|
|3|daemon|Services système|
|4|auth|Authentification|
|5|syslog|Messages du démon syslog|
|6|lpr|Impression|
|7|news|Usenet (ancien)|
|8|uucp|Protocole UUCP|
|9|cron|Planification de tâches|
|10|authpriv|Authentification privée|
|11|ftp|Serveur FTP|
|12|ntp|Synchronisation NTP|
|13|security|Sécurité|
|14|console|Console locale|
|15|cron|Tâches planifiées|
|16–23|local0–local7|Facilités réservées|

## Filtrer par facility dans journalctl

Afficher l’aide :

```bash
journalctl --facility=help
```

Filtrer :

```bash
journalctl --facility daemon
```

## Priorités (gravité)

|Code|Nom|Signification|
|---|---|---|
|0|emerg|Système inutilisable|
|1|alert|Action immédiate|
|2|crit|Erreur critique|
|3|err|Erreur|
|4|warning|Avertissement|
|5|notice|Info importante|
|6|info|Information|
|7|debug|Débogage|

Exemple :

```bash
journalctl -p alert..err
```

---

## Fichiers de logs classiques dans /var/log

Certains programmes n’utilisent pas systemd-journald et continuent d’écrire dans `/var/log/`.

|Fichier|Description|
|---|---|
|`/var/log/syslog` ou `/var/log/messages`|Messages généraux|
|`/var/log/auth.log`|Authentification (sudo, ssh)|
|`/var/log/kern.log`|Messages du noyau|
|`/var/log/dpkg.log`|Actions sur les paquets Debian|
|`/var/log/apt/history.log`|Historique APT|
|`/var/log/apache2/*`|Logs d’Apache|
|`/var/log/cron.log`|Tâches cron|
|`/var/log/Xorg.0.log`|Serveur graphique|

## Commandes utiles

```bash
sudo tail -n 30 /var/log/syslog
sudo less /var/log/auth.log
sudo grep "error" /var/log/syslog
```

---

## Pourquoi la migration vers journalctl / systemd-journald ?

- Le journal de systemd collecte des **logs structurés et indexés**, avec champs précis (PID, unité systemd, exécutable, etc.), ce qui facilite les filtrages et recherches.

- Il centralise dans un même format les logs du noyau, des services, et des applications, évitant de fouiller dans de nombreux fichiers dispersés.

- Le format binaire (ou semi-binaire) permet d’optimiser la recherche et de produire différents formats de sortie (JSON, export, etc.).

- Il permet une gestion intégrée de la rotation, de la persistance ou non des logs (en mémoire ou sur disque), et des quotas de taille.

- Pour la sécurité et la conformité, systemd-journald offre des métadonnées supplémentaires et des fonctions de scellage (log sealing) pour garantir l’intégrité des logs.

---

## Disponibilité des fichiers de journaux

Les fichiers `/var/log/syslog`, `/var/log/auth.log` et `/var/log/cron.log` dépendent des services et règles de journalisation installés. Sur une VM sans rsyslog, certains peuvent être absents : utiliser `journalctl` et vérifier la configuration plutôt que supposer une panne. Les fichiers de journaux doivent être lus avec les droits nécessaires.

## À retenir
> [!tip]
> - `journalctl` centralise la majorité des logs du système et des services.
> - Les **facilities** et **priorités**  permettent de classer les messages par rôle et gravité.
> - Les fichiers sous **`/var/log/`** restent incontournables pour certains programmes traditionnels.
> - La commande `journalctl -u <service>` est essentielle pour diagnostiquer un service.
> - `--since`, `--until`, `-p`, `-u`, `-f` sont les options les plus utilisées pour l’analyse quotidienne.
