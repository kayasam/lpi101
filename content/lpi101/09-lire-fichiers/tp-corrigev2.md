---
title: "TP 01. Prendre en main sa VM et le terminal — Correction"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/09-lire-fichiers"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/09-lire-fichiers/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/09-lire-fichiers/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/09-lire-fichiers/tp/tp-01-premiers-pas-correction.md">↓ Télécharger le corrigé (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://kayasam.github.io/lpi101/lpi101/09-lire-fichiers/tp">Énoncé</a><a class="exercise-correction" href="https://kayasam.github.io/lpi101/lpi101/09-lire-fichiers/tp-corrigev2" aria-current="page">Corrigé</a></nav>

> Essaie chaque question avant d’ouvrir **Afficher la correction**. Chaque réponse se replie indépendamment.

> Durée estimée : 55 min

> Chapitres associés : [01. Comprendre GNU/Linux et le logiciel libre](https://kayasam.github.io/lpi101/lpi101/01-comprendre-gnu-linux/), [02. Choisir et reconnaître une distribution Linux](https://kayasam.github.io/lpi101/lpi101/02-distributions/), [03. Comprendre les composants du système](https://kayasam.github.io/lpi101/lpi101/03-architecture-linux/), [04. Préparer une installation Linux](https://kayasam.github.io/lpi101/lpi101/04-preparer-installation/), [05. Installer Debian dans une machine virtuelle](https://kayasam.github.io/lpi101/lpi101/05-installation-machine-virtuelle/), [06. Accéder à la VM et préparer sa session](https://kayasam.github.io/lpi101/lpi101/06-acceder-et-configurer/), [07. Comprendre et utiliser une commande](https://kayasam.github.io/lpi101/lpi101/07-premieres-commandes/), [08. Se déplacer et comprendre les chemins](https://kayasam.github.io/lpi101/lpi101/08-chemins-et-navigation/), [09. Lire et identifier des fichiers](https://kayasam.github.io/lpi101/lpi101/09-lire-fichiers/)

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

> [!success]- Afficher la correction — A1
> ```bash
> whoami
> hostname
> pwd
> ```
>
> `whoami` indique le compte effectif, `hostname` la machine et `pwd` le répertoire courant. Les résultats dépendent de ta VM.

**A2.** Affiche le fichier qui identifie la distribution. Relève son nom et sa version.

> [!success]- Afficher la correction — A2
> ```bash
> cat /etc/os-release
> ```
>
> Lire notamment `PRETTY_NAME`, `ID` et `VERSION_ID`. La version du noyau n’est pas la version de la distribution.

**A3.** Distingue le terminal, Bash et le noyau. Affiche la version du noyau.

> [!success]- Afficher la correction — A3
> ```bash
> uname -r
> ```
>
> Le terminal affiche la session ; Bash interprète les commandes ; le noyau gère les ressources et le matériel.

---

## Partie B — Se déplacer sans se perdre (20 min)

**B1.** Crée `~/lpi101-tp/tp01`, place-toi dedans et affiche son chemin.

> [!success]- Afficher la correction — B1
> ```bash
> mkdir -p ~/lpi101-tp/tp01
> cd ~/lpi101-tp/tp01
> pwd
> ```
>
> `~` est développé vers ton répertoire personnel. `-p` crée les parents manquants.

**B2.** Va dans `/etc/apt` par un chemin absolu, puis dans son parent par un chemin relatif. Affiche les deux chemins.

> [!success]- Afficher la correction — B2
> ```bash
> cd /etc/apt
> pwd
> cd ..
> pwd
> ```
>
> Le premier chemin commence à la racine ; `..` dépend de la position actuelle.

**B3.** Reviens dans ton dossier personnel de deux façons. Va dans `/tmp`, puis reviens au dossier précédent sans retaper son nom.

> [!success]- Afficher la correction — B3
> ```bash
> cd
> cd "$HOME"
> cd /tmp
> cd -
> ```
>
> `cd` sans argument et `cd "$HOME"` ramènent au dossier personnel ; `cd -` retourne au dossier précédent.

**B4.** Depuis `/tmp`, affiche le contenu de ton dossier TP sans te déplacer. Crée ensuite dans le TP un fichier caché, puis fais-le apparaître.

> [!success]- Afficher la correction — B4
> ```bash
> cd /tmp
> ls "$HOME/lpi101-tp/tp01"
> touch "$HOME/lpi101-tp/tp01/.repere"
> ls -a "$HOME/lpi101-tp/tp01"
> ```
>
> Une commande accepte un chemin. Le point initial masque le nom dans l’affichage habituel ; ce n’est pas une protection.

---

## Partie C — Lire et demander de l’aide (20 min)

**C1.** Affiche `/etc/hostname`, puis seulement les trois premières lignes de `/etc/passwd` et les deux dernières.

> [!success]- Afficher la correction — C1
> ```bash
> cat /etc/hostname
> head -n 3 /etc/passwd
> tail -n 2 /etc/passwd
> ```
>
> `cat` affiche tout ; `head` et `tail` limitent la lecture. Les comptes présents varient selon l’installation.

**C2.** Ouvre `/etc/passwd` avec `less`, cherche `root`, puis quitte. Comment quittes-tu ce lecteur ?

> [!success]- Afficher la correction — C2
> ```bash
> less /etc/passwd
> ```
>
> Taper `/root`, Entrée, puis `q`. Avec `tail -f`, on utiliserait Ctrl+C plutôt que `q`.

**C3.** Trouve l’option de `ls` qui affiche les fichiers cachés. Consulte aussi le manuel et quitte-le.

> [!success]- Afficher la correction — C3
> ```bash
> ls --help
> man ls
> ```
>
> L’option est `-a`. Dans `man`, utiliser `/mot` pour chercher et `q` pour quitter. Les pages d’aide peuvent être traduites ou en anglais.

**C4.** Explique la différence entre `/`, `/root` et ton dossier personnel. Vérifie les métadonnées de `/etc` lui-même.

> [!success]- Afficher la correction — C4
> ```bash
> ls -ld /etc
> ```
>
> `/` est la racine de l’arborescence ; `/root` est le dossier personnel de root ; ton dossier est donné par `$HOME`. `-d` évite de lister le contenu du dossier.
