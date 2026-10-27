---
title: "07. Comprendre et utiliser une commande"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/07-premieres-commandes"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/07-premieres-commandes/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/07-premieres-commandes/07-premieres-commandes.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

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
