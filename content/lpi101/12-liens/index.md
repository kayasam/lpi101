---
title: "12 — Comprendre les liens physiques et symboliques"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/12-liens"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/12-liens/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/12-liens/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/12-liens.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Créer un lien et prévoir ce qui se passe lorsque sa cible est déplacée ou supprimée.

**Repères LPI 101 :** 104.6.

**Commandes à connaître :** `ln`, `ls -li`, `readlink`, `stat`.

---

## Un fichier, un nom et un inode

Un fichier possède des métadonnées stockées dans un **inode**. Un répertoire associe un nom à un numéro d’inode. Les données sont stockées séparément des noms.

Un **lien physique** ajoute un autre nom pour le même inode sur le même système de fichiers. Il n’y a pas de fichier « original » privilégié : les noms donnent accès au même contenu.

```bash
mkdir -p ~/labo-liens
cd ~/labo-liens
printf 'Version 1\n' > original.txt
ln original.txt physique.txt
ls -li original.txt physique.txt
printf 'Version 2\n' >> physique.txt
cat original.txt
```

Les deux noms ont le même numéro d’inode. Modifier le contenu en place par l’un des noms le modifie pour l’autre. Certains éditeurs remplacent cependant le fichier à l’enregistrement, créant alors un nouvel inode.

## Le lien symbolique

Un **lien symbolique** est un fichier distinct contenant un chemin vers sa cible. Il peut viser un dossier ou traverser les systèmes de fichiers.

```bash
ln -s original.txt raccourci.txt
ls -l raccourci.txt
readlink raccourci.txt
```

```text
original.txt ──┐
              ├── inode commun → contenu
physique.txt ─┘
raccourci.txt → chemin « original.txt »
```

Une cible relative est interprétée depuis le dossier contenant le lien symbolique, pas depuis le dossier courant de l’utilisateur.

## Supprimer un nom

Dans ce dossier de démonstration :

```bash
rm original.txt
cat physique.txt
ls -l raccourci.txt
```

Le contenu reste accessible par `physique.txt`. Le lien symbolique devient **cassé**, car le chemin `original.txt` n’existe plus. Les données peuvent être libérées lorsque le dernier lien physique disparaît et qu’aucun processus ne conserve le fichier ouvert.

## Copie ou lien ?

| Opération | Inode distinct | Contenu indépendant | Traverse les systèmes de fichiers |
|---|---|---|---|
| Copie | Oui | Oui | Oui |
| Lien physique | Non | Non | Non |
| Lien symbolique | Oui, pour le lien | Renvoie vers une cible | Oui |

Les liens physiques vers des répertoires ne sont pas autorisés dans l’usage courant. `cp -a` conserve les liens symboliques ; `cp -L` suit leurs cibles.

## À retenir

> [!tip]
> `ln` ajoute un nom au même fichier ; `ln -s` crée un chemin vers une cible ; `cp` crée une copie indépendante.
