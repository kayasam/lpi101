---
title: "TP 07 — Utilisateurs et permissions — Correction"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/20-permissions"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/20-permissions/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/20-permissions/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/20-permissions/tp/tp-07-permissions-correction.md">↓ Télécharger le corrigé (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://kayasam.github.io/lpi101/lpi101/20-permissions/tp">Énoncé</a><a class="exercise-correction" href="https://kayasam.github.io/lpi101/lpi101/20-permissions/tp-corrigev2" aria-current="page">Corrigé</a></nav>

> Essaie chaque question avant de cliquer sur **Afficher la correction**. Chaque réponse s’ouvre et se referme indépendamment.

> Durée estimée : 40 min

---

## Objectifs
Comprendre et manipuler les utilisateurs, groupes et permissions.

---

## Partie A — Utilisateurs (15 min)

**A1.** Affiche ton nom d'utilisateur, ton UID et tes groupes.

> [!success]- Afficher la correction — A1
> ```bash
> whoami
> id
> ```

**A2.** Liste les utilisateurs connectés en ce moment.

> [!success]- Afficher la correction — A2
> ```bash
> who
> ```

**A3.** Affiche les 3 premières lignes de `/etc/passwd`. Identifie les champs (nom, UID, home, shell).

> [!success]- Afficher la correction — A3
> ```bash
> head -3 /etc/passwd
> # Format : nom:x:UID:GID:commentaire:home:shell
> # Exemple : stagiaire:x:1000:1000:Stagiaire:/home/stagiaire:/bin/bash
> ```

**A4.** Crée un nouvel utilisateur appelé `testuser`. Définis-lui un mot de passe.

> [!success]- Afficher la correction — A4
> ```bash
> sudo adduser testuser
> # (suit les instructions interactives)
> sudo passwd testuser
> ```

**A5.** Connecte-toi en tant que `testuser` avec la commande `su - testuser`. Vérifie dans quel dossier tu es. Quitte avec `exit`.

> [!success]- Afficher la correction — A5
> ```bash
> su - testuser
> pwd     # /home/testuser
> exit
> ```

**A6.** Supprime l'utilisateur `testuser` et son dossier personnel.

---

> [!success]- Afficher la correction — A6
> ```bash
> sudo deluser --remove-home testuser
> ```

## Partie B — Permissions (25 min)

**B1.** Dans ton dossier `formation`, crée un fichier `secret.txt` et écris du texte dedans.

> [!success]- Afficher la correction — B1
> ```bash
> echo "Ceci est un fichier secret" > ~/formation/secret.txt
> ```

**B2.** Affiche ses permissions avec `ls -l`. Lis les droits (propriétaire, groupe, autres).

> [!success]- Afficher la correction — B2
> ```bash
> ls -l ~/formation/secret.txt
> # -rw-r--r-- 1 stagiaire stagiaire ...
> # Propriétaire : rw- (lecture + écriture)
> # Groupe       : r-- (lecture seule)
> # Autres       : r-- (lecture seule)
> ```

**B3.** Rends le fichier `secret.txt` accessible en lecture seule pour tout le monde.
> Indice : `chmod 444`

> [!success]- Afficher la correction — B3
> ```bash
> chmod 444 ~/formation/secret.txt
> ls -l ~/formation/secret.txt
> # -r--r--r--
> ```

**B4.** Essaie d'écrire dedans avec `echo`. Que se passe-t-il ?

> [!success]- Afficher la correction — B4
> ```bash
> echo "test" >> ~/formation/secret.txt
> # bash: secret.txt: Permission denied
> # → Le propriétaire n'a plus le droit d'écriture non plus
> ```

**B5.** Redonne-toi le droit d'écriture en mode symbolique.

> [!success]- Afficher la correction — B5
> ```bash
> chmod u+w ~/formation/secret.txt
> ```
>
> `u+w` redonne le droit d’écriture au propriétaire, sans remplacer les autres droits.

**B6.** Crée un fichier `script.sh` contenant `echo "Bonjour !"`. Rends-le exécutable et exécute-le.

> [!success]- Afficher la correction — B6
> ```bash
> echo 'echo "Bonjour !"' > ~/formation/script.sh
> chmod +x ~/formation/script.sh
> ~/formation/script.sh
> # Bonjour !
> ```

**B7.** Crée un dossier `prive` avec les permissions `700`. Vérifie qu'un autre utilisateur n'y a pas accès.

> [!success]- Afficher la correction — B7
> ```bash
> mkdir ~/formation/prive
> chmod 700 ~/formation/prive
> ls -ld ~/formation/prive
> ```
>
> Attendu : `drwx------`. Seul le propriétaire dispose des droits lecture, écriture et traversée. Un autre compte non privilégié ne peut pas entrer dans ce dossier. À vérifier depuis la session de cet autre compte ; `root` ne constitue pas un bon test de ces restrictions.

**Bonus.** Change le propriétaire de `notes.txt` vers `root` (avec `sudo`). Qu'est-ce que ça change pour toi ?

> [!success]- Afficher la correction — Bonus
> ```bash
> sudo chown root ~/formation/notes.txt
> ls -l ~/formation/notes.txt
> ```
>
> `chown root` change le propriétaire, mais conserve le groupe. Avec les droits `644`, seul root peut écrire. Si le groupe reste celui de ton compte, tu relèves de la catégorie **groupe**, pas de la catégorie autres ; tu gardes la lecture.
>
> Pour rendre ensuite la propriété à ton compte :
>
> ```bash
> sudo chown "$USER" ~/formation/notes.txt
> ```
