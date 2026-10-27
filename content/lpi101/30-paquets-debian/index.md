---
title: "30. Installer et gérer les paquets Debian"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/30-paquets-debian"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/30-paquets-debian/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/30-paquets-debian/30-paquets-debian.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Utiliser APT et distinguer dépôts, index, dépendances et paquets locaux.

**Repères LPI 101 :** 102.4.

**Commandes à connaître :** `apt`, `apt-get`, `apt-cache`, `dpkg`, `apt-mark`.

---

## Introduction

Sous Debian/Ubuntu, l’écosystème **APT** gère les dépôts, la résolution des dépendances et les mises à jour.
La couche basse, **dpkg**, manipule les paquets `.deb` localement (installation, liste des fichiers, état…).

---

## Vocabulaire rapide

* **Paquet** : archive `.deb` contenant fichiers + scripts d’installation.
* **Dépôt** : source de paquets décrite dans `/etc/apt/sources.list` ou dans des fichiers `.list` / `.sources` sous `/etc/apt/sources.list.d/`.
* **Index** : catalogue local des paquets récupéré par `apt update`.

---

## Fichiers et emplacements clés

* **Sources** :

  * `/etc/apt/sources.list` (format traditionnel, parfois absent)
  * `/etc/apt/sources.list.d/*.list` et `*.sources` (dont les sources principales selon l’installation)
* **Clés de dépôt** : `/usr/share/keyrings/` pour les clés gérées par paquets, `/etc/apt/keyrings/` pour celles ajoutées par l’administrateur ; associer la clé au dépôt avec `Signed-By`
* **Cache APT** : `/var/lib/apt/lists/` (index), `/var/cache/apt/archives/` (paquets téléchargés)
* **État dpkg** : `/var/lib/dpkg/` (`status`, listes des fichiers installés)

---

## Cycle de base (APT)

1. **Mettre à jour l’index**

```bash
sudo apt update
```

2. **Mettre à niveau les paquets**

```bash
sudo apt upgrade              # met à niveau ; lire les changements proposés
sudo apt full-upgrade         # peut changer/désinstaller pour résoudre les deps
```

3. **Installer / supprimer**

```bash
sudo apt install htop curl
sudo apt remove htop          # supprime le paquet, garde les configs
sudo apt purge htop           # supprime aussi les fichiers de config
```

4. **Nettoyer**

```bash
sudo apt autoremove           # enlève les dépendances devenues inutiles
sudo apt clean                # vide les .deb téléchargés
```

---

## Recherche et informations

```bash
apt search nginx              # chercher par nom/description
apt show nginx                # fiche détaillée (version, dépendances, mainteneur…)
apt list --installed          # lister les paquets installés
apt-cache policy nginx              # versions dispo, priorité (pin)
```

Astuce : pour lister rapidement les binaires installés par un paquet :

```bash
dpkg -L nginx | less          # liste les fichiers fournis par le paquet
```

---

## Geler / tenir une version

Empêcher les mises à jour d’un paquet :

```bash
sudo apt-mark hold nginx
sudo apt-mark unhold nginx
```

Voir la liste des paquets geléss :
```bash
apt-mark showhold
```

---

## Ajouter un dépôt tiers (méthode moderne)

Un dépôt tiers doit correspondre à la distribution et à sa version. Suivre les instructions de son éditeur ; conserver sa clé dans un fichier dédié et l’associer avec `Signed-By`. Éviter de rendre cette clé globalement fiable pour tous les dépôts.

Pour le parcours débutant, utiliser d’abord les dépôts fournis par Debian. Les PPA concernent Ubuntu et ne doivent pas être ajoutés tels quels à Debian.

---

## Lire un fichier de dépôt .sources

Les nouveaux formats `.sources` remplacent progressivement les anciens fichiers `.list`.
Ils regroupent les paramètres du dépôt en champs lisibles : URI, suites, composants et référence de clé ; ils peuvent aussi contenir une clé intégrée.

Exemple :

```bash
Types: deb
URIs: https://repo.example.com/debian
Suites: stable
Components: main
Signed-By: /usr/share/keyrings/repo.gpg
```

Sur les versions d’APT qui la proposent, la commande suivante convertit les sources existantes ; lire les modifications avant de l’utiliser :

```bash
sudo apt modernize-sources
```

---
## Gestion directe de `.deb` (dpkg)

* **Installer un .deb local** :

```bash
sudo apt install ./package.deb   # recommandé (résout les dépendances)
# ou, couche basse :
sudo dpkg -i package.deb         # peut laisser des dépendances non satisfaites
sudo apt -f install              # corrige les manques après dpkg -i
```

* **Interroger dpkg** :

```bash
dpkg -l | less                   # liste des paquets (état)
dpkg -s nginx                    # état + méta du paquet installé
dpkg -L nginx                    # fichiers installés par nginx
dpkg -S /usr/sbin/nginx          # quel paquet possède ce fichier ?
```

---
> [!info]
> **Bonnes pratiques (prod & postes)**
>
> * Actualiser l’index avec `apt update` avant une session d’installation ou de mise à niveau.
> * Préférer `apt install ./fichier.deb` plutôt que `dpkg -i`.
> * Lire les installations et suppressions proposées par `apt full-upgrade`. Une montée de version de Debian suit les notes de publication de la version cible.
> * Nettoyer régulièrement : `apt autoremove` et `apt clean`.
> * Limiter le nombre de dépôts tiers, documenter leur ajout.

---

## Retrouver le paquet fournissant un fichier

`dpkg -S /chemin/fichier` interroge les paquets installés. Pour chercher aussi dans les dépôts :

```bash
sudo apt install apt-file
sudo apt-file update
apt-file search /usr/bin/htop
```

`apt-get` et `apt-cache` sont également à reconnaître pour l’examen. `apt` convient aux usages interactifs du cours ; les scripts privilégient généralement les interfaces prévues pour eux, comme `apt-get`.

Documentation : [sources.list — Debian](https://manpages.debian.org/trixie/apt/sources.list.5.en.html).

## À retenir
> [!tip]
> * **APT** gère les dépôts, les dépendances et les mises à jour, tandis que **dpkg** manipule directement les paquets `.deb`.
> * Cycle courant : `apt update` → `apt upgrade` / `apt full-upgrade` → `apt install / remove / purge` → `apt autoremove` / `apt clean`.
> * `apt show`, `apt search`, `apt policy` permettent d’obtenir des informations détaillées sur les paquets.
> * `apt-mark hold` permet de **geler** un paquet pour éviter sa mise à jour.
> * Les dépôts sont configurés dans `/etc/apt/sources.list` et `/etc/apt/sources.list.d/`.
> * Installer un `.deb` local avec `apt install ./fichier.deb` permet de résoudre automatiquement les dépendances.
>
