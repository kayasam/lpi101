# TP 06. Partager des documents avec les bons droits

> Durée estimée : 75 min

> Chapitres associés : [19. Utilisateurs, groupes et droits administrateur](https://kayasam.github.io/lpi101/lpi101/19-utilisateurs-groupes/), [20. Lire et modifier les permissions](https://kayasam.github.io/lpi101/lpi101/20-permissions/), [21. Droits par défaut et bits spéciaux](https://kayasam.github.io/lpi101/lpi101/21-umask-bits-speciaux/)

---

## Objectifs

- Créer des comptes et un groupe de laboratoire.
- Tester les accès sous l’identité de chaque compte.
- Appliquer umask, SGID et sticky bit.

## Avant de commencer

Utilise un compte autorisé à lancer sudo. Les comptes `lpi_alice`, `lpi_bob` et le groupe `lpi_equipe` servent uniquement à cet atelier. Aucun mot de passe partagé n’est nécessaire : les essais utilisent `sudo -u`. Si ces noms existent déjà après un premier passage, reprendre l’atelier avec le formateur.

---

## Partie A — Créer les identités (15 min)

**A1.** Crée le groupe `lpi_equipe` puis les comptes de laboratoire `lpi_alice` et `lpi_bob`, avec leur dossier personnel et Bash.

**A2.** Vérifie le groupe de chaque compte et trouve ses informations dans la base des comptes.

**A3.** Exécute `whoami` en tant que lpi_alice. As-tu changé de session de manière permanente ?

---

## Partie B — Mettre en place le partage (25 min)

**B1.** Crée `/srv/lpi101-equipe`, attribue-le à root et au groupe lpi_equipe, puis autorise uniquement root et ce groupe à y travailler.

**B2.** En tant que lpi_alice, crée `rapport.txt` contenant `Version Alice` avec un umask 0002. Vérifie les droits et le groupe.

**B3.** En tant que lpi_bob, ajoute `Validation Bob` au rapport, puis vérifie le résultat.

**B4.** Crée un fichier privé d’Alice avec un umask 0077. Vérifie que Bob ne peut pas le lire. Quelle permission faut-il modifier pour lui donner la lecture par groupe ?

---

## Partie C — Protéger un répertoire partagé (20 min)

**C1.** Ajoute le sticky bit au dossier de partage. Essaie, en tant que Bob, de supprimer `rapport.txt` créé par Alice. Explique le résultat.

**C2.** Affiche les métadonnées du rapport et vérifie que les deux lignes sont présentes. Quelle différence fais-tu entre changer les droits du fichier et ceux de son dossier ?

---

## Partie D — Faire le bilan (15 min)

**D1.** Retrouve un exemple de programme SUID déjà présent et explique pourquoi on ne transforme pas arbitrairement un programme en SUID root.

**D2.** Retire seulement les ressources de cet atelier : partage, comptes et groupe.


[Afficher les corrections](https://kayasam.github.io/lpi101/lpi101/21-umask-bits-speciaux/tp-corrigev2)
