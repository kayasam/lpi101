# 09 — Lire et identifier des fichiers

> [!note] Objectif
> Choisir un outil de lecture et reconnaître le type d’un fichier.

**Repères LPI 101 :** 103.2, 103.3.

**Commandes à connaître :** `cat`, `less`, `head`, `tail`, `file`, `stat`.

---

## Consultation de fichiers

## `cat` — afficher le contenu complet d’un fichier

```bash
cat /etc/hostname
```

Cette commande affiche tout le contenu du fichier à l’écran.
Utile pour de petits fichiers, mais peu pratique pour les gros volumes de texte.

## `less` — lecture page par page

```bash
less /var/log/syslog
```

Permet de naviguer dans le contenu avec les flèches du clavier.
Touches utiles :

- `espace` → page suivante

- `b` → page précédente

- `/mot` → recherche d’un mot

- `q` → quitter

## `head` — afficher les premières lignes d’un fichier

```bash
head -n 10 /etc/passwd
```

Affiche les 10 premières lignes du fichier (par défaut, 10 si `-n` non précisé).

## `tail` — afficher les dernières lignes d’un fichier

```bash
tail -n 20 /var/log/syslog
```

Affiche les 20 dernières lignes du fichier.
Option utile :

```bash
tail -f /var/log/syslog
```

`-f` permet de suivre en temps réel les ajouts au fichier (utile pour surveiller des logs).

---

## Reconnaître le type d’un fichier

L’extension aide à se repérer, mais ne suffit pas à connaître le contenu réel.

```bash
file /etc/hostname
stat /etc/hostname
```

`file` tente d’identifier la nature du contenu. `stat` affiche notamment la taille, les permissions, les dates et le numéro d’inode. Les liens et les inodes sont expliqués dans leur chapitre.

## À retenir

> [!tip]
> `cat` convient à un petit fichier ; `less` à une lecture longue ; `head` et `tail` à un extrait. `tail -f` attend les nouvelles lignes jusqu’à Ctrl+C.
