---
title: "13. Archiver et compresser"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/13-archives-compression"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/13-archives-compression/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/13-archives-compression/13-archives-compression.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Distinguer regroupement de fichiers et réduction de leur taille.

**Repères LPI 101 :** 103.3.

**Commandes à connaître :** `tar`, `gzip`, `gunzip`, `bzip2`, `bunzip2`, `xz`, `unxz`.

---

## Introduction

Une archive rassemble des fichiers ; la compression réduit leur taille. Ce chapitre présente `tar`, `gzip`, `bzip2` et `xz`. Les transferts SSH, la recherche de texte et les redirections sont expliqués dans leurs chapitres respectifs.

---

## Création et extraction d’archives

## `tar` — créer et extraire des archives

`tar` (Tape ARchive) regroupe plusieurs fichiers dans une seule archive.
Elle ne compresse pas par défaut, mais on peut l’associer à `gzip` ou `bzip2`.

Créer une archive :

```bash
tar -cvf archive.tar dossier1
```

* `-c` : créer une archive
* `-v` : afficher les fichiers ajoutés (mode verbeux)
* `-f` : nom du fichier archive

Extraire une archive :

```bash
tar -xvf archive.tar
```

Lister le contenu sans extraire :

```bash
tar -tvf archive.tar
```

---

## Compression avec `gzip`

`gzip` compresse un fichier unique (extension `.gz`).

```bash
gzip fichier.txt
```

Le fichier devient `fichier.txt.gz`.
Pour le décompresser :

```bash
gunzip fichier.txt.gz
```

`tar` peut l’utiliser directement :

```bash
tar -czvf archive.tar.gz dossier1
tar -xzvf archive.tar.gz
```

---

## Compression avec `bzip2`

`bzip2` offre souvent une compression plus forte que `gzip`, avec un temps de traitement plus long ; le résultat dépend des données (extension `.bz2`).

```bash
bzip2 fichier.txt
bunzip2 fichier.txt.bz2
```

Avec `tar` :

```bash
tar -cjvf archive.tar.bz2 dossier1
tar -xjvf archive.tar.bz2
```

---

## Compression avec xz

```bash
xz -k rapport.txt
mkdir -p decompression
xz -dc rapport.txt.xz > decompression/rapport.txt
tar -cJf documents.tar.xz Documents/
tar -tJf documents.tar.xz
```

`-k` conserve le fichier d’entrée ; `tar -t` liste le contenu d’une archive. `unxz fichier.xz` décompresse normalement à côté du fichier compressé ; ici `xz -dc` écrit vers un autre dossier et garde le fichier `.xz`.

## Vérifier avant d’extraire

```bash
tar -tf sauvegarde.tar
mkdir -p restauration
tar -xf sauvegarde.tar -C restauration
```

Adapter le nom à une archive créée précédemment. Lister le contenu permet de voir les chemins avant l’extraction. Les transferts réseau avec `scp` se trouvent dans le chapitre SSH.

## À retenir

> [!tip]
> `tar` regroupe plusieurs fichiers ; `gzip`, `bzip2` et `xz` compressent. Une archive `.tar.gz` combine les deux opérations.
