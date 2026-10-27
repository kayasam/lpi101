---
title: "TP 06. Partager des documents avec les bons droits"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/21-umask-bits-speciaux"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/21-umask-bits-speciaux/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://cours.kaya.ovh/lpi101/lpi101/21-umask-bits-speciaux/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/21-umask-bits-speciaux/tp/tp-06-comptes-permissions.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


> Durée estimée : 75 min

> Chapitres associés : [19. Utilisateurs, groupes et droits administrateur](https://cours.kaya.ovh/lpi101/lpi101/19-utilisateurs-groupes/), [20. Lire et modifier les permissions](https://cours.kaya.ovh/lpi101/lpi101/20-permissions/), [21. Droits par défaut et bits spéciaux](https://cours.kaya.ovh/lpi101/lpi101/21-umask-bits-speciaux/)

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
