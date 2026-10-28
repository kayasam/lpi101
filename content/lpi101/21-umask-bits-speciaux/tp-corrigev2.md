---
title: "TP 06. Partager des documents avec les bons droits — Correction"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/21-umask-bits-speciaux"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/21-umask-bits-speciaux/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/21-umask-bits-speciaux/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/21-umask-bits-speciaux/tp/tp-06-comptes-permissions-correction.md">↓ Télécharger le corrigé (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://kayasam.github.io/lpi101/lpi101/21-umask-bits-speciaux/tp">Énoncé</a><a class="exercise-correction" href="https://kayasam.github.io/lpi101/lpi101/21-umask-bits-speciaux/tp-corrigev2" aria-current="page">Corrigé</a></nav>

> Essaie chaque question avant d’ouvrir **Afficher la correction**. Chaque réponse se replie indépendamment.

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

> [!success]- Afficher la correction — A1
> ```bash
> sudo groupadd lpi_equipe
> sudo useradd -m -s /bin/bash lpi_alice
> sudo useradd -m -s /bin/bash lpi_bob
> sudo usermod -aG lpi_equipe lpi_alice
> sudo usermod -aG lpi_equipe lpi_bob
> ```
>
> `-aG` ajoute le groupe secondaire sans remplacer les autres. Ces comptes n’ont pas encore de mot de passe utilisable ; les tests passent par sudo.

**A2.** Vérifie le groupe de chaque compte et trouve ses informations dans la base des comptes.

> [!success]- Afficher la correction — A2
> ```bash
> id lpi_alice
> id lpi_bob
> getent passwd lpi_alice
> getent group lpi_equipe
> ```
>
> `getent` interroge la base configurée par le système ; sur cette VM, les comptes créés sont locaux.

**A3.** Exécute `whoami` en tant que lpi_alice. As-tu changé de session de manière permanente ?

> [!success]- Afficher la correction — A3
> ```bash
> sudo -u lpi_alice whoami
> ```
>
> La commande affiche lpi_alice ; à son retour, tu restes dans ton propre shell. Les futures commandes sudo -u prennent en compte le nouveau groupe sans reconnecter un ancien shell.

---

## Partie B — Mettre en place le partage (25 min)

**B1.** Crée `/srv/lpi101-equipe`, attribue-le à root et au groupe lpi_equipe, puis autorise uniquement root et ce groupe à y travailler.

> [!success]- Afficher la correction — B1
> ```bash
> sudo mkdir /srv/lpi101-equipe
> sudo chown root:lpi_equipe /srv/lpi101-equipe
> sudo chmod 2770 /srv/lpi101-equipe
> ls -ld /srv/lpi101-equipe
> ```
>
> `2770` signifie SGID + rwx pour le propriétaire et le groupe. Les autres n’ont aucun accès ; SGID fait hériter le groupe aux nouvelles entrées.

**B2.** En tant que lpi_alice, crée `rapport.txt` contenant `Version Alice` avec un umask 0002. Vérifie les droits et le groupe.

> [!success]- Afficher la correction — B2
> ```bash
> sudo -u lpi_alice sh -c 'umask 0002; printf "Version Alice\n" > /srv/lpi101-equipe/rapport.txt'
> sudo ls -l /srv/lpi101-equipe/rapport.txt
> ```
>
> Le groupe doit être lpi_equipe ; les permissions courantes du fichier sont 664. Le droit x d’un dossier permet de le traverser.

**B3.** En tant que lpi_bob, ajoute `Validation Bob` au rapport, puis vérifie le résultat.

> [!success]- Afficher la correction — B3
> ```bash
> sudo -u lpi_bob sh -c 'printf "Validation Bob\n" >> /srv/lpi101-equipe/rapport.txt'
> sudo cat /srv/lpi101-equipe/rapport.txt
> ```
>
> Bob peut écrire grâce au groupe. Le compte élève n’appartient pas forcément à ce groupe ; sudo permet ici de vérifier le contenu sans lui ajouter un accès permanent.

**B4.** Crée un fichier privé d’Alice avec un umask 0077. Vérifie que Bob ne peut pas le lire. Quelle permission faut-il modifier pour lui donner la lecture par groupe ?

> [!success]- Afficher la correction — B4
> ```bash
> sudo -u lpi_alice sh -c 'umask 0077; printf "Privé\n" > /srv/lpi101-equipe/prive.txt'
> sudo -u lpi_bob cat /srv/lpi101-equipe/prive.txt
> sudo chmod g+r /srv/lpi101-equipe/prive.txt
> sudo -u lpi_bob cat /srv/lpi101-equipe/prive.txt
> ```
>
> Le premier cat doit échouer ; le second réussit après ajout du droit r au groupe. La création sous umask 0077 donne normalement 600.

---

## Partie C — Protéger un répertoire partagé (20 min)

**C1.** Ajoute le sticky bit au dossier de partage. Essaie, en tant que Bob, de supprimer `rapport.txt` créé par Alice. Explique le résultat.

> [!success]- Afficher la correction — C1
> ```bash
> sudo chmod +t /srv/lpi101-equipe
> sudo -u lpi_bob rm /srv/lpi101-equipe/rapport.txt
> ls -ld /srv/lpi101-equipe
> ```
>
> Le refus est attendu malgré les droits d’écriture du groupe sur le dossier. Le sticky bit réserve cette suppression au propriétaire de l’entrée, au propriétaire du dossier ou à un processus privilégié.

**C2.** Affiche les métadonnées du rapport et vérifie que les deux lignes sont présentes. Quelle différence fais-tu entre changer les droits du fichier et ceux de son dossier ?

> [!success]- Afficher la correction — C2
> ```bash
> sudo stat /srv/lpi101-equipe/rapport.txt
> sudo cat /srv/lpi101-equipe/rapport.txt
> ```
>
> Les droits du fichier concernent son contenu ; ceux du dossier concernent notamment la traversée et les entrées. Le sticky bit ne rend pas le contenu du fichier privé.

---

## Partie D — Faire le bilan (15 min)

**D1.** Retrouve un exemple de programme SUID déjà présent et explique pourquoi on ne transforme pas arbitrairement un programme en SUID root.

> [!success]- Afficher la correction — D1
> ```bash
> ls -l /usr/bin/passwd
> ```
>
> Le bit s permet ici l’exécution avec une identité effective adaptée. Donner ce privilège à n’importe quel programme peut ouvrir un accès administrateur. Il n’est pas demandé d’en ajouter.

**D2.** Retire seulement les ressources de cet atelier : partage, comptes et groupe.

> [!success]- Afficher la correction — D2
> ```bash
> sudo rm -r /srv/lpi101-equipe
> sudo userdel -r lpi_alice
> sudo userdel -r lpi_bob
> sudo groupdel lpi_equipe
> ```
>
> La suppression porte sur les noms créés par cet atelier. userdel peut signaler l’absence d’un fichier de courrier ; ce n’est pas un échec si le compte et son dossier ont été supprimés.
