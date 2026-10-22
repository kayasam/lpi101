# TP 01 — Prendre en main sa VM et le terminal

> Durée estimée : 55 min

> Chapitres associés : [01 — Comprendre GNU/Linux et le logiciel libre](https://kayasam.github.io/lpi101/lpi101/01-comprendre-gnu-linux/), [02 — Choisir et reconnaître une distribution Linux](https://kayasam.github.io/lpi101/lpi101/02-distributions/), [03 — Comprendre les composants du système](https://kayasam.github.io/lpi101/lpi101/03-architecture-linux/), [04 — Préparer une installation Linux](https://kayasam.github.io/lpi101/lpi101/04-preparer-installation/), [05 — Installer Debian dans une machine virtuelle](https://kayasam.github.io/lpi101/lpi101/05-installation-machine-virtuelle/), [06 — Accéder à la VM et préparer sa session](https://kayasam.github.io/lpi101/lpi101/06-acceder-et-configurer/), [07 — Comprendre et utiliser une commande](https://kayasam.github.io/lpi101/lpi101/07-premieres-commandes/), [08 — Se déplacer et comprendre les chemins](https://kayasam.github.io/lpi101/lpi101/08-chemins-et-navigation/), [09 — Lire et identifier des fichiers](https://kayasam.github.io/lpi101/lpi101/09-lire-fichiers/)

---

## Objectifs

- Identifier la machine, le compte et la distribution.
- Naviguer avec des chemins absolus et relatifs.
- Lire un fichier et consulter l’aide sans rester bloqué dans un programme.

## Avant de commencer

La VM Debian vient d’être installée. Utilise le compte standard créé à l’installation. Aucun nom de compte particulier n’est imposé. Les opérations d’installation dans VirtualBox sont réalisées avec le formateur ; ce TP commence après le premier démarrage.

---

## Partie A — Identifier son environnement (15 min)

**A1.** Affiche ton nom d’utilisateur, le nom de la machine et le répertoire courant. Que décrit chaque résultat ?

**A2.** Affiche le fichier qui identifie la distribution. Relève son nom et sa version.

**A3.** Distingue le terminal, Bash et le noyau. Affiche la version du noyau.

---

## Partie B — Se déplacer sans se perdre (20 min)

**B1.** Crée `~/lpi101-tp/tp01`, place-toi dedans et affiche son chemin.

**B2.** Va dans `/etc/apt` par un chemin absolu, puis dans son parent par un chemin relatif. Affiche les deux chemins.

**B3.** Reviens dans ton dossier personnel de deux façons. Va dans `/tmp`, puis reviens au dossier précédent sans retaper son nom.

**B4.** Depuis `/tmp`, affiche le contenu de ton dossier TP sans te déplacer. Crée ensuite dans le TP un fichier caché, puis fais-le apparaître.

---

## Partie C — Lire et demander de l’aide (20 min)

**C1.** Affiche `/etc/hostname`, puis seulement les trois premières lignes de `/etc/passwd` et les deux dernières.

**C2.** Ouvre `/etc/passwd` avec `less`, cherche `root`, puis quitte. Comment quittes-tu ce lecteur ?

**C3.** Trouve l’option de `ls` qui affiche les fichiers cachés. Consulte aussi le manuel et quitte-le.

**C4.** Explique la différence entre `/`, `/root` et ton dossier personnel. Vérifie les métadonnées de `/etc` lui-même.
