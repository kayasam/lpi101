# TP 09. Installer un outil et retrouver ses fichiers — Correction

> Essaie chaque question avant d’ouvrir **Afficher la correction**. Chaque réponse se replie indépendamment.

> Durée estimée : 50 min

> Chapitres associés : [30. Installer et gérer les paquets Debian](https://kayasam.github.io/lpi101/lpi101/30-paquets-debian/), [31. Reconnaître RPM, DNF, YUM et Zypper](https://kayasam.github.io/lpi101/lpi101/31-paquets-rpm/), [32. Comprendre les bibliothèques partagées](https://kayasam.github.io/lpi101/lpi101/32-bibliotheques/)

---

## Objectifs

- Distinguer index des dépôts et paquets installés.
- Installer, interroger et retirer un petit paquet.
- Observer une bibliothèque partagée et reconnaître les équivalents RPM.

## Avant de commencer

Une connexion Internet et les dépôts Debian configurés sont nécessaires. Le paquet hello sert de support jetable à cet atelier. Les commandes RPM/DNF sont uniquement à reconnaître sur cette VM Debian.

---

## Partie A — Chercher et installer (20 min)

**A1.** Actualise le catalogue des paquets, puis cherche le paquet hello et affiche ses informations.

> [!success]- Afficher la correction — A1
> ```bash
> sudo apt update
> apt search '^hello$'
> apt show hello
> ```
>
> apt update met à jour les index ; il n’installe pas les nouvelles versions des logiciels. La version proposée varie selon les dépôts.

**A2.** Installe hello, lance-le et vérifie l’endroit où le shell trouve sa commande.

> [!success]- Afficher la correction — A2
> ```bash
> sudo apt install hello
> hello
> command -v hello
> ```
>
> Le programme affiche une salutation. Il faut lire les paquets proposés avant de confirmer l’installation.

**A3.** Affiche l’état du paquet, les fichiers qu’il fournit et le paquet propriétaire de `/usr/bin/hello`.

> [!success]- Afficher la correction — A3
> ```bash
> dpkg -s hello
> dpkg -L hello
> dpkg -S /usr/bin/hello
> ```
>
> dpkg interroge ici la base locale des paquets installés. Une recherche dans les dépôts non installés utiliserait par exemple apt-file.

---

## Partie B — Comprendre les dépendances (15 min)

**B1.** Affiche la version installée et la version candidate, puis les dépendances du paquet.

> [!success]- Afficher la correction — B1
> ```bash
> apt-cache policy hello
> apt-cache depends hello
> ```
>
> La candidate est la version choisie pour une installation ou mise à niveau selon les dépôts et priorités. Une dépendance est un autre paquet nécessaire ou recommandé selon son type.

**B2.** Affiche les bibliothèques de `/usr/bin/ls`, puis consulte le cache du chargeur. Pourquoi ne copie-t-on pas au hasard une bibliothèque trouvée sur Internet ?

> [!success]- Afficher la correction — B2
> ```bash
> ldd /usr/bin/ls
> sudo ldconfig -p | head -n 12
> ```
>
> Le paquet de la distribution apporte une version adaptée et des métadonnées vérifiables. ldd est utilisé sur un exécutable connu de la VM ; ldconfig -p consulte le cache.

---

## Partie C — Retirer et transposer (15 min)

**C1.** Retire le paquet hello, vérifie son absence puis demande sa purge. Distingue remove et purge.

> [!success]- Afficher la correction — C1
> ```bash
> sudo apt remove hello
> dpkg-query -W -f='${db:Status-Status}\n' hello
> sudo apt purge hello
> ```
>
> La requête peut échouer si le paquet n’a plus d’entrée locale. remove retire le paquet ; purge retire aussi les fichiers de configuration gérés par dpkg. Avec hello, la différence visible est limitée car ce n’est pas un service configuré.

**C2.** Sur une distribution RPM, quelles commandes serviraient à installer hello et à retrouver le paquet d’un fichier ? Ne les lance pas sur Debian.

> [!success]- Afficher la correction — C2
> Exemples : `sudo dnf install hello`, `rpm -ql hello` et `rpm -qf /chemin/du/fichier`. YUM est à reconnaître dans cette famille ; SUSE utilise notamment Zypper.
