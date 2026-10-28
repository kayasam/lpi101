# TP 07 — Utilisateurs et permissions

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


[Afficher les corrections](https://kayasam.github.io/lpi101/lpi101/20-permissions/tp-corrigev2)
