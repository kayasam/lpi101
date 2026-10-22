---
title: "36 — Gérer les services avec systemd"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/36-services"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/36-services/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/36-services.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Distinguer état immédiat d’un service et activation au démarrage.

**Repères LPI 101 :** 101.2, 101.3.

**Commandes à connaître :** `systemctl`, `journalctl -u`.

---

## Introduction

Sous Linux, les services (ou *daemons*) sont des processus qui s’exécutent en arrière-plan pour assurer des fonctions essentielles : réseau, SSH, serveur web, journalisation, etc.
Depuis l’adoption de **systemd**, la gestion de ces services est unifiée grâce à la commande **systemctl**, qui permet de les démarrer, arrêter, activer au démarrage ou vérifier leur état.

---

## Principes de base

Un **service** est généralement défini par une unité (*unit*) située dans `/etc/systemd/system/` ou `/lib/systemd/system/`.
Ces fichiers décrivent comment lancer, arrêter et surveiller le service.

Les services actifs en arrière-plan portent souvent un nom terminé par `.service`, par exemple :

* `ssh.service` : service SSH
* `apache2.service` : serveur web Apache
* `cron.service` : planificateur de tâches

---

## Commandes principales

| Action                     | Commande                              | Description                                           |
| -------------------------- | ------------------------------------- | ----------------------------------------------------- |
| Démarrer un service        | `sudo systemctl start ssh`            | Lance le service immédiatement                        |
| Arrêter un service         | `sudo systemctl stop ssh`             | Stoppe le service sans le désactiver                  |
| Redémarrer un service      | `sudo systemctl restart ssh`          | Redémarre le service (utile après modification)       |
| Recharger la configuration | `sudo systemctl reload ssh`           | Recharge la configuration sans interrompre le service |
| Vérifier l’état            | `systemctl status ssh`                | Affiche l’état du service et les journaux récents     |
| Lister les services actifs | `systemctl list-units --type=service --state=running` | Montre les services en cours d’exécution         |

---

## Activation et désactivation au démarrage

Les services peuvent être configurés pour se lancer automatiquement au démarrage du système.

```bash
sudo systemctl enable ssh
sudo systemctl disable ssh
```

* `enable` → crée les liens prévus par la section `[Install]`, par exemple dans `multi-user.target.wants/`
* `disable` → retire les liens d’activation concernés, sans arrêter le service à lui seul

Vérifier si un service est activé au démarrage :

```bash
systemctl is-enabled ssh
```

---

## Vérification et dépannage

Lister les services en échec :

```bash
systemctl --failed
```

Afficher uniquement les services inactifs :

```bash
systemctl list-units --state=inactive --type=service
```

Consulter les journaux récents d’un service :

```bash
journalctl -u ssh
```

Suivre les journaux en temps réel :

```bash
journalctl -u ssh -f
```

---

## Exemple d’utilisation pratique

```bash
# Démarrer et vérifier le service SSH
sudo systemctl start ssh
systemctl status ssh

# Lancer Apache et l’activer au démarrage
sudo systemctl start apache2
sudo systemctl enable apache2

# Recharger la configuration sans couper le service
sudo systemctl reload apache2
```

---

## Structure d’un fichier de service

Exemple simplifié d’un fichier administrateur `/etc/systemd/system/monservice.service` :

```text
[Unit]
Description=Mon service personnalisé
After=network.target

[Service]
ExecStart=/usr/local/bin/script.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Chaque section a un rôle :

* `[Unit]` → dépendances et description
* `[Service]` → commande à exécuter et comportement
* `[Install]` → cibles dans lesquelles le service est activé

---

## Actif et activé ne veulent pas dire la même chose

`start` agit maintenant ; `enable` prépare l’activation selon les dépendances au démarrage. `sudo systemctl enable --now ssh` combine activation et démarrage. Après création ou modification du fichier d’unité, utiliser `sudo systemctl daemon-reload`. `reload` concerne la configuration de l’application et n’est disponible que si le service le prévoit.

## À retenir

> [!tip]
>
> * **systemd** gère les services via la commande **systemctl**.
> * Un service est une *unit* décrite dans `/etc/systemd/system/` ou `/lib/systemd/system/`.
> * Les commandes principales :
>
>   * `start`, `stop`, `restart`, `reload`, `status`
>   * `enable`, `disable`, `is-enabled`
> * Les journaux des services sont accessibles avec **journalctl -u nom_du_service**.
> * La commande `systemctl --failed` permet d’identifier rapidement les services en erreur.
> * Comprendre et gérer les services est essentiel pour administrer un système Linux, qu’il soit serveur ou poste de travail.
