---
title: "08. Se déplacer et comprendre les chemins"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/08-chemins-et-navigation"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/08-chemins-et-navigation/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/08-chemins-et-navigation/08-chemins-et-navigation.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Utiliser les chemins absolus et relatifs sans confondre racine et dossier personnel.

**Repères LPI 101 :** 103.1, 104.7.

**Commandes à connaître :** `pwd`, `cd`, `ls`.

---

## Navigation dans l’arborescence

Sous Linux, tout est organisé dans une **arborescence unique** partant de la racine `/`.

![Chemin absolu et chemin relatif vers le même répertoire.](https://kayasam.github.io/lpi101/assets/course-media/b02d089e0fd34249.svg)

Les principales commandes de navigation sont :

## `pwd` — afficher le répertoire courant

Affiche le chemin complet du répertoire dans lequel on se trouve.

```bash
pwd
```

Exemple de sortie :

```text
/home/kaya/Documents
```

## `cd` — changer de répertoire

Permet de se déplacer dans l’arborescence.

Exemples :

```bash
cd /home           # aller dans /home
cd ..              # remonter d’un dossier
cd                 # revenir dans le dossier personnel
cd ~/Documents     # aller directement dans Documents
```

## `ls` — lister le contenu d’un répertoire

Affiche la liste des fichiers et dossiers du répertoire courant ou d’un autre répertoire.

Exemples :

```bash
ls                 # liste simple
ls -l              # liste détaillée
ls -a              # affiche les fichiers cachés
ls -lh /etc        # affiche les fichiers de /etc avec tailles lisibles
```

Quelques options utiles :

- `-l` : format long (permissions, propriétaire, taille…)

- `-a` : affiche aussi les fichiers cachés

- `-h` : affiche les tailles dans un format lisible (Ko, Mo)

---

## Chemin absolu ou relatif

Un **chemin absolu** commence par `/` et part de la racine. Un **chemin relatif** part du répertoire courant.

```text
/
├── etc/
└── home/
    └── sam/
        └── Documents/
```

Depuis `/home/sam`, `Documents` et `/home/sam/Documents` désignent le même dossier. `.` désigne le dossier courant, `..` son parent et `~` le dossier personnel du compte courant. `/root` est le dossier personnel de root ; `/` est la racine du système.

```bash
cd /home/sam
cd Documents
pwd
cd ..
cd -
```

`cd -` retourne au répertoire précédent. Adapter le nom du compte à la VM.

## Casse, espaces et fichiers cachés

`rapport.txt` et `Rapport.txt` sont généralement deux noms différents sous Linux. Un nom commençant par `.` est caché dans l’affichage habituel de `ls`.

```bash
mkdir -p "$HOME/mes documents"
cd "$HOME/mes documents"
ls -a
```

Les guillemets gardent le chemin contenant un espace dans **un seul argument**. Dans les guillemets doubles, `$HOME` est développé ; dans les guillemets simples, il reste du texte littéral.

## À retenir

> [!tip]
> Avant d’agir sur un fichier, vérifier le répertoire courant avec `pwd`, puis lire le chemin utilisé par la commande.
