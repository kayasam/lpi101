# TP 09. Installer un outil et retrouver ses fichiers

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

**A2.** Installe hello, lance-le et vérifie l’endroit où le shell trouve sa commande.

**A3.** Affiche l’état du paquet, les fichiers qu’il fournit et le paquet propriétaire de `/usr/bin/hello`.

---

## Partie B — Comprendre les dépendances (15 min)

**B1.** Affiche la version installée et la version candidate, puis les dépendances du paquet.

**B2.** Affiche les bibliothèques de `/usr/bin/ls`, puis consulte le cache du chargeur. Pourquoi ne copie-t-on pas au hasard une bibliothèque trouvée sur Internet ?

---

## Partie C — Retirer et transposer (15 min)

**C1.** Retire le paquet hello, vérifie son absence puis demande sa purge. Distingue remove et purge.

**C2.** Sur une distribution RPM, quelles commandes serviraient à installer hello et à retrouver le paquet d’un fichier ? Ne les lance pas sur Debian.
