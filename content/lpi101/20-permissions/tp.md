---
title: "TP 07 — Utilisateurs et permissions"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/20-permissions"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/20-permissions/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/20-permissions/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/20-permissions/tp/tp-07-permissions.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://kayasam.github.io/lpi101/lpi101/20-permissions/tp" aria-current="page">Énoncé</a><a class="exercise-correction" href="https://kayasam.github.io/lpi101/lpi101/20-permissions/tp-corrigev2">Afficher les corrections</a></nav>

> Durée estimée : 40 min

---

## Objectifs
Comprendre et manipuler les utilisateurs, groupes et permissions.

---

## Partie A — Utilisateurs (15 min)

**A1.** Affiche ton nom d'utilisateur, ton UID et tes groupes.

**A2.** Liste les utilisateurs connectés en ce moment.

**A3.** Affiche les 3 premières lignes de `/etc/passwd`. Identifie les champs (nom, UID, home, shell).

**A4.** Crée un nouvel utilisateur appelé `testuser`. Définis-lui un mot de passe.

**A5.** Connecte-toi en tant que `testuser` avec la commande `su - testuser`. Vérifie dans quel dossier tu es. Quitte avec `exit`.

**A6.** Supprime l'utilisateur `testuser` et son dossier personnel.

---

## Partie B — Permissions (25 min)

**B1.** Dans ton dossier `formation`, crée un fichier `secret.txt` et écris du texte dedans.

**B2.** Affiche ses permissions avec `ls -l`. Lis les droits (propriétaire, groupe, autres).

**B3.** Rends le fichier `secret.txt` accessible en lecture seule pour tout le monde.
> Indice : `chmod 444`

**B4.** Essaie d'écrire dedans avec `echo`. Que se passe-t-il ?

**B5.** Redonne-toi le droit d'écriture en mode symbolique.

**B6.** Crée un fichier `script.sh` contenant `echo "Bonjour !"`. Rends-le exécutable et exécute-le.

**B7.** Crée un dossier `prive` avec les permissions `700`. Vérifie qu'un autre utilisateur n'y a pas accès.

**Bonus.** Change le propriétaire de `notes.txt` vers `root` (avec `sudo`). Qu'est-ce que ça change pour toi ?
