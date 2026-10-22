# C09 — Repères pour poursuivre la préparation LPI 101

> [!note] Objectif
> Identifier les notions à revoir pour une préparation plus complète à l’examen.

**Repères LPI 101 :** 101 à 104.

> [!info] Complément
> À découvrir après les bases, selon le rythme du groupe.

---

## Utiliser cette fiche

Le parcours principal privilégie la compréhension et les gestes usuels. Cette fiche rassemble des repères supplémentaires ; elle ne remplace ni l’entraînement ni les leçons détaillées du référentiel LPI.

## Reconnaître cpio et dd

`cpio` construit ou extrait une archive à partir d’une liste de noms. Exemple dans un dossier de démonstration contenant `notes.txt` :

```bash
printf 'Exemple\n' > notes.txt
printf '%s\0' notes.txt | cpio --null -ov > notes.cpio
cpio -it < notes.cpio
```

`dd` copie des données avec des tailles de blocs choisies. Exemple limité à un fichier ordinaire, dans le dossier de travail :

```bash
dd if=/dev/zero of=exemple.bin bs=1M count=1 status=progress
ls -lh exemple.bin
```

`if` est l’entrée, `of` la sortie et `count` le nombre de blocs. Ne pas transposer cette commande sur un disque : une sortie vers un périphérique peut écraser son contenu.

## Reconnaître d’autres filtres

| Outil | Rôle | Exemple |
|---|---|---|
| `nl` | Numéroter des lignes | `nl /etc/hosts` |
| `od` | Afficher des données sous une forme numérique | `od -c /etc/hostname` |
| `paste` | Juxtaposer des lignes de fichiers | `paste noms.txt ages.txt` |
| `split` | Découper un fichier en morceaux | `split -l 100 grand.txt morceau-` |
| `sha256sum` | Calculer une empreinte pour contrôler une copie | `sha256sum exemple.bin` |

Les noms de fichiers illustratifs doivent être remplacés par des fichiers existants. `sha256sum -c liste.sha256` vérifie des empreintes enregistrées ; la confiance dans l’empreinte publiée dépend aussi de sa provenance.

## Compléter la gestion des paquets

```bash
apt-cache policy bash
apt-cache depends bash
dpkg --verify bash
rpm -V bash
rpm -K paquet.rpm
dnf provides '*/nom-de-fichier'
```

Ces commandes relèvent de distributions différentes : lancer les commandes APT sur Debian et les commandes RPM/DNF dans un environnement RPM. `rpm -V` compare les fichiers installés aux métadonnées enregistrées ; `rpm -K` vérifie les empreintes et signatures d’un paquet selon les clés disponibles.

## Étendre ses recherches

`find -perm` sélectionne selon les droits ; `find -user` selon le propriétaire. La base de `locate` est mise à jour avec `updatedb`, selon la configuration de l’implémentation installée.

## Préparer sa révision

Reprendre les objectifs officiels 101.1 à 104.7, noter les commandes non reconnues et les essayer dans une VM de laboratoire. Les variantes historiques de GRUB et d’init, les outils propres à XFS et Btrfs et les unités de montage systemd nécessitent des lectures complémentaires pour une préparation exhaustive.

Références : [objectifs LPI 101-500](https://www.lpi.org/fr/exam-101-102-objectives/) et [leçons LPI en français](https://learning.lpi.org/fr/learning-materials/101-500/).
