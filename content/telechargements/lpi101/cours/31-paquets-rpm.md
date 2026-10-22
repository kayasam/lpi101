# 31 — Reconnaître RPM, DNF, YUM et Zypper

> [!note] Objectif
> Retrouver les actions de gestion des paquets sur les autres grandes familles Linux.

**Repères LPI 101 :** 102.5.

**Commandes à connaître :** `rpm`, `dnf`, `yum`, `zypper`.

---

## Introduction

Les distributions **de la famille Red Hat** (RHEL, AlmaLinux, Rocky Linux, Fedora) ainsi que **SUSE/openSUSE** n’utilisent pas les paquets `.deb`, mais des paquets **.rpm** (*Red Hat Package Manager*).
Le principe reste le même : chaque paquet contient les fichiers d’un logiciel et les métadonnées nécessaires à son installation, sa mise à jour et sa suppression.

---

## Gestionnaires de paquets

| Niveau      | Outil principal        | Rôle                                                                                         |
| ----------- | ---------------------- | -------------------------------------------------------------------------------------------- |
| Bas niveau  | `rpm`                  | installe, supprime, interroge directement les fichiers `.rpm` (contrôle les dépendances, sans les télécharger ni les résoudre automatiquement) |
| Haut niveau | `yum`, `dnf`, `zypper` | gèrent les dépôts, les dépendances, les mises à jour et la recherche                         |

---

## Le gestionnaire RPM (bas niveau)

* **Installer un paquet local**

  ```bash
  sudo rpm -ivh paquet.rpm
  ```

  (`-i` : installer, `-v` : verbeux, `-h` : barre de progression)

* **Mettre à jour / supprimer**

  ```bash
  sudo rpm -Uvh paquet.rpm
  sudo rpm -e nom_du_paquet
  ```

* **Lister / interroger**

  ```bash
  rpm -qa              # tous les paquets installés
  rpm -qi nginx        # infos détaillées
  rpm -ql nginx        # fichiers installés
  rpm -qf /usr/sbin/nginx   # quel paquet possède ce fichier ?
  ```
> [!warning]
> ⚠️ `rpm` ne résout **pas** les dépendances ; il faut donc préférer `dnf` ou `yum`.

---

## Le gestionnaire DNF (ou YUM)

`dnf` (*Dandified YUM*) est l’évolution de `yum`. Il gère automatiquement les dépendances et succède à `yum` sur de nombreux systèmes.

* **Mettre à jour les dépôts et le système**

  ```bash
  sudo dnf check-update
  sudo dnf upgrade
  ```

* **Installer / supprimer un paquet**

  ```bash
  sudo dnf install htop
  sudo dnf remove htop
  ```

* **Rechercher un paquet**

  ```bash
  dnf search nginx
  dnf info nginx
  ```

* **Nettoyer le cache**

  ```bash
  sudo dnf clean all
  ```

* **Lister / verrouiller un paquet**

  ```bash
  dnf list installed nginx
  sudo dnf versionlock add nginx     # nécessite le module versionlock adapté à la version de DNF
  ```

> Sur **RHEL / AlmaLinux / Rocky**, `dnf` est standard.
> Sur **Fedora**, la version de DNF et les commandes de ses modules peuvent varier selon la version du système.

---

## Le gestionnaire Zypper (openSUSE)

`zypper` est l’équivalent de `dnf` pour les distributions **SUSE**.

Exemples :

```bash
sudo zypper refresh             # mise à jour de l’index
sudo zypper install htop        # installation
sudo zypper remove htop         # suppression
sudo zypper search nginx        # recherche
sudo zypper update              # mise à jour système
```

---

## Comparaison APT vs DNF/Zypper

| Fonction                 | Debian / Ubuntu (APT)   | Red Hat / SUSE (DNF / Zypper)                    |
| ------------------------ | ----------------------- | ------------------------------------------------ |
| Fichier de sources       | `/etc/apt/sources.list` | `/etc/yum.repos.d/*.repo` / `/etc/zypp/repos.d/` |
| Paquets                  | `.deb`                  | `.rpm`                                           |
| Gestionnaire bas niveau  | `dpkg`                  | `rpm`                                            |
| Gestionnaire haut niveau | `apt` / `apt-get`       | `dnf`, `yum`, `zypper`                           |
| Résolution dépendances   | automatique (`apt`)     | automatique (`dnf`/`zypper`)                     |
| Geler un paquet          | `apt-mark hold`         | `dnf versionlock add`                            |

---

## À retenir
> [!tip]
>
> * Les systèmes **Red Hat** utilisent des paquets **.rpm** au lieu de **.deb**.
> * `rpm` agit au **niveau bas**, sans résolution automatique des dépendances.
> * `dnf` (ou `yum`) est le **gestionnaire haut niveau** moderne ; `zypper` l’équivalent chez openSUSE.
> * Les fichiers de configuration des dépôts se trouvent dans `/etc/yum.repos.d/` ou `/etc/zypp/repos.d/`.
> * Les commandes sont globalement similaires à APT : `install`, `remove`, `search`, `update`, `clean`.
> * Toujours préférer **dnf/yum/zypper** à `rpm` pour éviter les erreurs de dépendances.
