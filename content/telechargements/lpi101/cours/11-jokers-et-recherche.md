# 11 — Utiliser les jokers et rechercher

> [!note] Objectif
> Distinguer les motifs de noms, la recherche de fichiers et la recherche de commandes.

**Repères LPI 101 :** 103.3, 104.7.

**Commandes à connaître :** `find`, `locate`, `updatedb`, `type`, `command -v`, `which`, `whereis`.

---

## Utilisation des jokers (wildcards)

Les jokers permettent de sélectionner plusieurs fichiers à la fois selon un motif.

| Joker | Description                                   | Exemple                                                      |
| ----- | --------------------------------------------- | ------------------------------------------------------------ |
| `*`   | remplace n’importe quelle suite de caractères | `ls *.txt` → liste tous les fichiers se terminant par `.txt` |
| `?`   | remplace un seul caractère                    | `ls fichier?.txt` → `fichier1.txt`, `fichier2.txt`, etc.     |
| `[ ]` | remplace un caractère parmi ceux indiqués     | `ls fichier[12].txt` → `fichier1.txt` et `fichier2.txt`      |

Exemples pratiques :

```bash
rm *.log              # supprime tous les fichiers .log
cp *.txt /tmp/        # copie tous les fichiers .txt vers /tmp
ls fichier[0-9].txt   # affiche les fichiers dont le nom contient un chiffre de 0 à 9
```

---

## Commandes de recherche

## `find` — rechercher des fichiers dans l’arborescence

`find` parcourt l’arborescence à partir d’un répertoire donné et affiche les fichiers correspondant à certains critères.

```bash
find /home -name "fichier.txt"
```

Cherche un fichier nommé `fichier.txt` dans le répertoire `/home` et ses sous-dossiers.
Quelques options utiles :

* `-type f` : ne recherche que des fichiers.
* `-type d` : ne recherche que des répertoires.
* `-mtime -1` : fichiers modifiés dans les dernières 24h.
* `-size +10M` : fichiers de plus de 10 Mo.

Exemples :

```bash
find /etc -type f -name "*.conf"
find /home -type f -size +1M
```

---

## `locate` — rechercher rapidement un fichier

`locate` recherche un fichier dans une base de données pré-indexée (mise à jour avec `updatedb`).

```bash
locate passwd
```

Cette commande est beaucoup plus rapide que `find`, mais elle dépend de la dernière mise à jour de l’index :

```bash
sudo updatedb
```

## Chercher un fichier ou une commande

```bash
type cd
type ls
command -v bash
which bash
whereis bash
```

`type` indique comment le shell interprète un nom : commande interne, alias, fonction ou programme. `command -v` indique ce que le shell utiliserait ; `which` recherche habituellement un exécutable dans `PATH`. `whereis` recherche des binaires, sources et manuels dans des emplacements connus. La disponibilité de `which` et `locate` dépend des paquets installés.

## Filtrer une recherche par date et agir sur les résultats

```bash
find "$HOME" -type f -name '*.txt' -mtime -7
find "$HOME/labo-lpi" -type f -name '*.txt' -exec wc -l {} +
```

Le premier exemple cherche des fichiers texte modifiés depuis moins de sept jours. Le second compte leurs lignes en transmettant les chemins à `wc`. Les guillemets empêchent le shell de développer `*.txt` avant que `find` le reçoive.

`-mtime` concerne la modification du contenu ; `-atime`, l’accès ; `-ctime`, le changement des métadonnées de l’inode. `ctime` n’est pas la date de création.

## À retenir

> [!tip]
> `find` recherche dans l’arborescence ; `locate` consulte une base ; `type` renseigne sur une commande ; `grep` recherche dans du texte.
