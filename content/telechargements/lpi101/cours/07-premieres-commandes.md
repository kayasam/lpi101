# 07 — Comprendre et utiliser une commande

> [!note] Objectif
> Lire une commande, identifier ses options et consulter son aide.

**Repères LPI 101 :** 103.1.

**Commandes à connaître :** `man`, `help`, `echo`, `whoami`.

---

## Introduction

Sous Linux, la majorité des opérations peuvent être effectuées en ligne de commande à l’aide du terminal.
Le terminal est une interface textuelle qui permet d’interagir directement avec le système d’exploitation en tapant des commandes.

Ce chapitre explique la structure d’une commande et l’utilisation de son aide. Les deux suivants présentent la navigation et la lecture de fichiers.

---

## Structure d’une commande

Une commande Linux suit en général la structure suivante :

```bash
commande [options] [arguments]
```

- **commande** : nom du programme ou de l’outil à exécuter (ex. `ls`, `cd`, `cat`).

- **options** : modifient le comportement de la commande (ex. `-l`, `-a`).

- **arguments** : précisent sur quoi la commande agit (fichiers, dossiers, texte, etc.).

Exemple :

```bash
ls -l /home
```

- `ls` : liste les fichiers.

- `-l` : affiche les détails (taille, droits, propriétaire…).

- `/home` : indique le répertoire sur lequel agir.

De nombreuses commandes disposent d’une page d’aide appelée **page de manuel** :

```bash
man ls
```

ou plus rapidement :

```bash
ls --help
```

---

## Trouver de l’aide et quitter un programme

Dans `man ls`, utiliser `/mot` pour rechercher, `n` pour l’occurrence suivante et `q` pour quitter. Le numéro de section distingue les manuels : `man 1 passwd` décrit la commande ; `man 5 passwd` décrit le fichier.

```bash
man ls
man -k archive
ls --help
```

| Geste | Utilité |
|---|---|
| Tab | Compléter un nom de commande ou un chemin ; deux pressions peuvent afficher les possibilités. |
| Flèches haut/bas | Reprendre les commandes précédentes. |
| Ctrl+C | Demander l’interruption du programme au premier plan. |
| Ctrl+L | Nettoyer l’affichage du terminal. |
| `q` | Quitter `less`, `man` ou `top`. |

Les symboles `$` et `#` qui précèdent parfois les commandes dans une documentation représentent l’invite : ne pas les recopier. En général, `$` indique un compte standard et `#` une session root.

## À retenir

> [!tip]
> Lire `commande options arguments`, consulter l’aide et savoir quitter le programme évitent beaucoup de blocages.
