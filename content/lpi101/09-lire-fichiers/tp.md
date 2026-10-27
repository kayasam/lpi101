---
title: "TP 01. Prendre en main sa VM et le terminal"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/09-lire-fichiers"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/09-lire-fichiers/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://cours.kaya.ovh/lpi101/lpi101/09-lire-fichiers/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/09-lire-fichiers/tp/tp-01-premiers-pas.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://cours.kaya.ovh/lpi101/lpi101/09-lire-fichiers/tp" aria-current="page">Énoncé</a><a class="exercise-correction" href="https://cours.kaya.ovh/lpi101/lpi101/09-lire-fichiers/tp-corrigev2">Afficher les corrections</a></nav>

> Durée estimée : 55 min

> Chapitres associés : [01. Comprendre GNU/Linux et le logiciel libre](https://cours.kaya.ovh/lpi101/lpi101/01-comprendre-gnu-linux/), [02. Choisir et reconnaître une distribution Linux](https://cours.kaya.ovh/lpi101/lpi101/02-distributions/), [03. Comprendre les composants du système](https://cours.kaya.ovh/lpi101/lpi101/03-architecture-linux/), [04. Préparer une installation Linux](https://cours.kaya.ovh/lpi101/lpi101/04-preparer-installation/), [05. Installer Debian dans une machine virtuelle](https://cours.kaya.ovh/lpi101/lpi101/05-installation-machine-virtuelle/), [06. Accéder à la VM et préparer sa session](https://cours.kaya.ovh/lpi101/lpi101/06-acceder-et-configurer/), [07. Comprendre et utiliser une commande](https://cours.kaya.ovh/lpi101/lpi101/07-premieres-commandes/), [08. Se déplacer et comprendre les chemins](https://cours.kaya.ovh/lpi101/lpi101/08-chemins-et-navigation/), [09. Lire et identifier des fichiers](https://cours.kaya.ovh/lpi101/lpi101/09-lire-fichiers/)

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
