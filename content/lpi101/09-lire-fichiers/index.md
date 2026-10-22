---
title: "09 — Lire et identifier des fichiers"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/09-lire-fichiers"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/09-lire-fichiers/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/09-lire-fichiers/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/09-lire-fichiers.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

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
