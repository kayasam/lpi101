---
title: "10. Créer, copier, déplacer et supprimer"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/10-manipuler-fichiers"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/10-manipuler-fichiers/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/10-manipuler-fichiers/10-manipuler-fichiers.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Manipuler les fichiers et répertoires en comprenant les effets des commandes.

**Repères LPI 101 :** 103.3.

**Commandes à connaître :** `touch`, `mkdir`, `rmdir`, `cp`, `mv`, `rm`.

---

## Introduction

Sous Linux, la manipulation de fichiers et de répertoires se fait principalement à l’aide de la ligne de commande.
Les commandes que nous allons voir permettent de **créer, supprimer, déplacer, copier et rechercher** des fichiers ou des dossiers.
Elles constituent la base du travail quotidien sur un système Linux.

---

## Création et suppression de fichiers et de répertoires

## `touch` — créer un fichier vide

La commande `touch` permet de créer un fichier vide ou de mettre à jour la date de dernière modification d’un fichier existant.

```bash
touch fichier.txt
```

Si le fichier `fichier.txt` n’existe pas, il sera créé.
S’il existe déjà, sa date de modification sera actualisée.

---

## `mkdir` — créer un répertoire

```bash
mkdir dossier1
```

Crée un répertoire nommé `dossier1`.
Pour créer plusieurs niveaux de répertoires d’un coup, utilisez l’option `-p` :

```bash
mkdir -p dossier1/sousdossier1/sousdossier2
```

---

## `rmdir` — supprimer un répertoire vide

```bash
rmdir dossier1
```

Supprime un répertoire **vide uniquement**.
Si le répertoire contient des fichiers, la commande échouera.

---

## `rm` — supprimer un ou plusieurs fichiers ou répertoires

```bash
rm fichier.txt
```

Supprime le fichier spécifié.
Pour supprimer un répertoire et tout son contenu, utilisez :

```bash
rm -r dossier1
```

L’option `-r` signifie “récursif”.
On peut ajouter `-f` pour forcer la suppression sans demande de confirmation :

```bash
rm -rf dossier1
```
> [!danger]
>
> ⚠️ Cette commande est **destructive** : les fichiers supprimés de cette façon ne sont pas récupérables via une corbeille.

---

## Déplacement et copie

## `mv` — déplacer ou renommer un fichier

```bash
mv fichier.txt /home/kaya/Documents/
```

Déplace le fichier `fichier.txt` dans le répertoire `/home/kaya/Documents`.
La même commande sert à renommer un fichier :

```bash
mv fichier.txt nouveau_nom.txt
```

Si la destination est un répertoire, le fichier est déplacé.
Si la destination est un nom de fichier, il est renommé.

---

## `cp` — copier un fichier ou un répertoire

```bash
cp fichier.txt /home/kaya/Documents/
```

Copie le fichier vers un autre répertoire.
Pour copier un répertoire complet avec tout son contenu, ajoutez `-r` :

```bash
cp -r dossier1 sauvegarde_dossier1
```

L’option `-i` permet d’éviter d’écraser un fichier existant sans confirmation.

```bash
cp -i fichier.txt /tmp/
```

---

## Distinguer les opérations

| Commande | Résultat |
|---|---|
| `cp source copie` | Crée un autre fichier avec son propre contenu. |
| `mv ancien nouveau` | Déplace ou renomme l’entrée. |
| `rm fichier` | Supprime le nom du fichier ; aucune corbeille n’est utilisée par défaut. |

```bash
mkdir -p ~/labo-lpi/documents
touch ~/labo-lpi/documents/notes.txt
cp -i ~/labo-lpi/documents/notes.txt ~/labo-lpi/documents/copie.txt
mv -i ~/labo-lpi/documents/copie.txt ~/labo-lpi/documents/rapport.txt
```

L’option `-i` demande confirmation avant certains écrasements. Pour copier un dossier avec son contenu : `cp -r dossier copie`. `cp -a` préserve davantage de métadonnées et les liens ; le résultat dépend aussi des droits de l’utilisateur et du système de fichiers.

## À retenir

> [!tip]
> Vérifier le chemin avant une suppression, surtout avec `-r`. Pour apprendre, utiliser un dossier de travail dans son répertoire personnel.
