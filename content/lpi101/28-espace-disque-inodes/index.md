---
title: "28 — Mesurer l’espace, la mémoire et les inodes"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/28-espace-disque-inodes"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/28-espace-disque-inodes/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/28-espace-disque-inodes.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Distinguer capacité du système de fichiers, taille d’un dossier et mémoire disponible.

**Repères LPI 101 :** 104.2.

**Commandes à connaître :** `df`, `du`, `free`, `swapon`.

---

## Gestion de l’espace disque

## `df` — affichage de l’espace disque par système de fichiers

```bash
df -h
```

Affiche la taille totale, utilisée et libre sur chaque système de fichiers.

Exemple :

```text
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        96G   12G   79G  14% /
tmpfs           1.9G  2.0M  1.9G   1% /run
```

---

## `du` — taille d’un répertoire ou d’un fichier

```bash
du -sh /var/log
```

* `-s` : total uniquement
* `-h` : taille lisible (Ko, Mo, Go)

Lister les plus gros dossiers :

```bash
du -h --max-depth=1 /home | sort -hr | head
```

---

## `free` — état de la mémoire et du swap

```bash
free -h
```

Affiche la mémoire utilisée, libre et partagée, ainsi que la taille du swap.

Exemple :

```text
               total        used        free      shared  buff/cache   available
Mem:           3.8Gi       1.2Gi       1.5Gi       110Mi       1.1Gi       2.3Gi
Swap:          4.0Gi          0B       4.0Gi
```

---

## Suivi de l’espace et des inodes

Chaque fichier du système possède un **inode** — une entrée contenant ses métadonnées.
Même avec de l’espace disque libre, un système peut être bloqué si tous les inodes sont utilisés.

Vérifier leur usage :

```bash
df -i
```

Exemple :

```text
Filesystem     Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1      655360  49217  606143    8% /
```
> [!warning]
> Si **IUse%** atteint 100%, cela signifie que trop de petits fichiers ont été créés (souvent dans `/var/log` ou `/tmp`).

---

## Choisir le bon indicateur

| Question | Commande |
|---|---|
| Le système de fichiers est-il plein ? | `df -h` |
| Quel dossier occupe de la place ? | `du -sh dossier` |
| Reste-t-il des inodes ? | `df -i` |
| Quelle mémoire est disponible ? | `free -h` |
| Quel swap est actif ? | `swapon --show` |

`df` et `du` mesurent des choses différentes. Un fichier supprimé mais encore ouvert peut continuer à occuper de l’espace ; les métadonnées et blocs réservés expliquent aussi certaines différences.

## À retenir

> [!tip]
> Un système peut manquer d’inodes alors qu’il reste des octets libres. Ne pas confondre espace disque et mémoire vive.
