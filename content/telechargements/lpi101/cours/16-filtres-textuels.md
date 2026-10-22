# 16 — Filtrer et transformer du texte

> [!note] Objectif
> Rechercher, extraire, trier, compter et transformer des lignes.

**Repères LPI 101 :** 103.2.

**Commandes à connaître :** `grep`, `cut`, `sort`, `uniq`, `wc`, `tr`, `sed`, `awk`.

---

## Introduction

Les **filtres** sont des commandes qui lisent un flux de texte (souvent depuis l’entrée standard) et produisent un nouveau flux en sortie.
Ils sont souvent utilisés avec les **pipes (`|`)** pour transformer, trier ou extraire des informations à partir de fichiers ou de commandes.

---

## Commandes de base

## `cat` — afficher le contenu d’un fichier

`cat`, `head` et `tail` ont été présentés dans le chapitre 09. On les utilise ici comme étapes d’une chaîne de traitement ; `cat` peut aussi concaténer plusieurs fichiers.

---

## `grep` — rechercher un motif dans un texte

```bash
grep motif fichier.txt
```

Exemples :

```bash
grep root /etc/passwd
grep -i "sam" fichier.txt      # ignore la casse
grep -v "daemon" fichier.txt   # inverse la recherche (exclut)
```

Options utiles :

* `-n` : affiche les numéros de ligne
* `-r` : recherche récursive dans un répertoire
* `-E` : active les expressions régulières étendues

---

## `cut` — extraire des colonnes ou des champs

```bash
cut -d ':' -f 1 /etc/passwd
```

Options principales :

* `-d` : définit le délimiteur (ici `:`)
* `-f` : sélectionne les champs à afficher

Exemple : extraire les noms d’utilisateur du fichier `/etc/passwd`.

---

## `sort` — trier les lignes d’un texte

```bash
sort fichier.txt
```

Options :

* `-r` : ordre inverse
* `-n` : tri numérique
* `-u` : supprime les doublons

Exemples :

```bash
sort -u noms.txt              # tri alphabétique unique
sort -nr nombres.txt          # tri numérique inverse
```

---

## `uniq` — supprimer les doublons consécutifs

```bash
uniq fichier.txt
```

Souvent utilisé après `sort`, car `uniq` ne détecte que les doublons **successifs**.
Exemple :

```bash
sort noms.txt | uniq
```

Options :

* `-c` : affiche le nombre d’occurrences de chaque ligne

---

## `wc` — compter lignes, mots, caractères

```bash
wc fichier.txt
```

Affiche trois valeurs :

1. nombre de lignes
2. nombre de mots
3. nombre d’octets

Exemples :

```bash
wc -l fichier.txt    # lignes seulement
wc -w fichier.txt    # mots seulement
wc -c fichier.txt    # octets
wc -m fichier.txt    # caractères
```

---

## `tr` — transformer ou supprimer des caractères

```bash
tr a-z A-Z < fichier.txt
```

→ convertit le texte en majuscules.

Autres exemples :

```bash
tr -d ' ' < fichier.txt        # supprime les espaces
tr ':' ',' < fichier.txt       # remplace les deux-points par des virgules
```

---

## `head` et `tail` — afficher le début ou la fin d’un fichier

Dans un tube, `head -n 10` conserve les dix premières lignes ; `tail -n 20`, les vingt dernières. Voir le chapitre 09 pour la lecture et le suivi d’un fichier.

---

## Chaînage des filtres

Les filtres deviennent puissants lorsqu’on les combine :

```bash
cat /etc/passwd | cut -d ':' -f 1 | sort | uniq | wc -l
```

→ compte les noms de comptes distincts du fichier local `/etc/passwd`.

Autres exemples :

```bash
dmesg | grep error | tail -n 5
ls /bin | grep ssh | sort
```

---
## `sed` — modifier le texte à la volée

`sed` (Stream EDitor) est un éditeur de flux : il lit ligne par ligne et applique des transformations sans ouvrir le fichier.

Exemples :

```bash
sed 's/root/admin/' /etc/passwd         # remplace le premier "root" par "admin" dans chaque ligne
sed 's/root/admin/g' /etc/passwd        # remplace toutes les occurrences sur chaque ligne
sed -n '1,5p' fichier.txt               # affiche uniquement les lignes 1 à 5
sed '/^#/d' fichier.txt                 # supprime les lignes commençant par #
```

> `sed` est idéal pour automatiser de petites modifications dans des scripts ou pipelines.

---

## `awk` — traiter et filtrer des colonnes

`awk` lit les fichiers ligne par ligne et découpe chaque ligne en **champs** séparés (par défaut par des espaces).
C’est un outil très puissant pour l’analyse de texte et de rapports.

Exemples :

```bash
awk -F: '{print $1}' /etc/passwd        # affiche le 1er champ (nom d’utilisateur)
awk '{print $1, $3}' fichier.txt        # affiche les colonnes 1 et 3
awk '{s+=$1} END {print s}' data.txt    # additionne tous les nombres de la première colonne
awk '/root/ {print $1,$6}' /etc/passwd  # affiche certaines colonnes pour les lignes contenant "root"
```

`awk` est souvent utilisé pour extraire ou reformater des données tabulaires.

---

## À retenir
> [!tip]
> * Les **filtres** transforment un flux de texte en entrée pour produire un résultat en sortie.
> * Les plus courants sont : `grep`, `cut`, `sort`, `uniq`, `wc`, `tr`, `head`, `tail`.
> * Les **pipes** (`|`) permettent de combiner plusieurs filtres pour créer une chaîne de traitement.
> * `grep` recherche, `cut` extrait, `sort` trie, `uniq` élimine les doublons, `wc` compte, `tr` remplace, `head/tail` affichent une partie.
> * Les exemples affichent leur résultat sans modifier le fichier d’entrée ; certaines options, comme `sed -i`, peuvent modifier un fichier.
> * **`sed`** permet d’éditer ou de remplacer du texte à la volée.
> * **`awk`** permet de traiter des colonnes et d’appliquer des conditions sur les lignes.
