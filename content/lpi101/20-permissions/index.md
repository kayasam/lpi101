---
title: "20 — Lire et modifier les permissions"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/20-permissions"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/20-permissions/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/20-permissions.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Comprendre propriétaire, groupe et autres, puis attribuer des droits adaptés.

**Repères LPI 101 :** 104.5.

**Commandes à connaître :** `ls -l`, `chmod`, `chown`, `chgrp`.

---

## Introduction

Sous Linux, **chaque fichier et répertoire appartient à un utilisateur et à un groupe**, et possède un ensemble de **droits d’accès**.
Ces droits déterminent **qui peut lire, modifier ou exécuter** un fichier.
Le système de permissions est l’un des fondements de la sécurité sous Linux.

Cette section aborde :

* les droits **r**, **w**, **x** sur les fichiers et répertoires ;
* les commandes `chmod`, `chown` et `chgrp` ;
* le masque `umask` *(optionnel)* ;
* les bits spéciaux `suid`, `sgid` et `sticky bit` *(optionnel)*.

---

## Structure des permissions

Afficher les permissions d’un fichier ou dossier :

```bash
ls -l
```

Exemple de sortie :

```text
-rwxr-xr--
```

Décomposons cette chaîne :

| Position      | Signification                                           | Exemple |
| ------------- | ------------------------------------------------------- | ------- |
| 1er caractère | type d’objet : `-` (fichier), `d` (dossier), `l` (lien) | `-`     |
| 2-4           | droits du **propriétaire**                              | `rwx`   |
| 5-7           | droits du **groupe**                                    | `r-x`   |
| 8-10          | droits des **autres utilisateurs**                      | `r--`   |

---

## Signification des droits

| Droit | Valeur numérique | Signification sur un **fichier** | Signification sur un **répertoire**              |
| ----- | ---------------- | -------------------------------- | ------------------------------------------------ |
| `r`   | 4                | lecture du contenu               | lecture de la liste des fichiers                 |
| `w`   | 2                | modification du contenu          | création ou suppression de fichiers              |
| `x`   | 1                | exécution (programme ou script)  | accès (possibilité de “rentrer” dans le dossier) |

Exemples :

```text
rwx------  → le propriétaire a tous les droits
rw-r--r--  → lecture/écriture pour le propriétaire, lecture seule pour les autres
rwxr-xr-x  → fichier exécutable pour tout le monde
```
Schémas:
![](https://kayasam.github.io/lpi101/assets/course-media/90b22da2633afc1b.png)

![](https://kayasam.github.io/lpi101/assets/course-media/791114b9764a457e.png)

---

## Commande `chmod` — modifier les permissions

`chmod` permet de modifier les droits d’un fichier ou d’un dossier.

## Modes symbolique et numérique

**1. Mode symbolique**

```bash
chmod u+x script.sh
```

* `u` : utilisateur (owner)
* `g` : groupe
* `o` : autres
* `a` : tous
* `+` : ajouter un droit
* `-` : retirer un droit
* `=` : définir les droits exacts

Exemples :

```bash
chmod g+w fichier.txt     # ajoute l’écriture pour le groupe
chmod o-r fichier.txt     # retire la lecture aux autres
chmod a+x script.sh       # rend le fichier exécutable pour tous
```

**2. Mode numérique**

Chaque droit correspond à un chiffre :

* `r` = 4
* `w` = 2
* `x` = 1

Additionne les valeurs pour chaque catégorie :

| Droits | Valeur |
| ------ | ------ |
| `rwx`  | 7      |
| `rw-`  | 6      |
| `r--`  | 4      |

Exemples :

```bash
chmod 600 fichier.txt   # lecture/écriture pour le propriétaire
chmod 755 script.sh     # rwx pour propriétaire, rx pour groupe et autres
chmod 644 document.txt  # rw- pour propriétaire, r-- pour les autres
```

---

## Commande `chown` — changer le propriétaire

Changer le propriétaire d’un fichier :

```bash
sudo chown alice fichier.txt
```

Changer le propriétaire et le groupe :

```bash
sudo chown alice:developpeurs fichier.txt
```

Appliquer récursivement à un dossier et son contenu :

```bash
sudo chown -R alice:alice /home/alice
```

---

## Commande `chgrp` — changer uniquement le groupe

```bash
sudo chgrp admin fichier.txt
```

Permet de modifier uniquement le groupe sans toucher au propriétaire.

---

## Lire les droits d’un répertoire

Sur un **fichier**, `r` permet de lire le contenu, `w` de le modifier et `x` de tenter son exécution. Sur un **répertoire**, `r` permet de lister les noms, `w` de modifier ses entrées et `x` de le traverser et d’accéder aux éléments par leur nom.

La création et la suppression d’une entrée demandent généralement `w` et `x` sur le répertoire parent. Pouvoir supprimer un fichier ne dépend donc pas simplement du droit d’écriture sur le fichier lui-même. Le sticky bit ajoute une restriction, expliquée dans le chapitre suivant.

## À retenir

> [!tip]
> `chmod` change les droits, `chown` le propriétaire et `chgrp` le groupe. Comprendre l’accès attendu avant de choisir une valeur numérique ; `777` est rarement une réponse adaptée.
