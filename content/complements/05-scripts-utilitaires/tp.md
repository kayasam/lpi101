---
title: "TP 14. Écrire un petit script de contrôle"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="complements/05-scripts-utilitaires"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/complements/05-scripts-utilitaires/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/complements/05-scripts-utilitaires/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/complements/complements/c05-scripts-utilitaires/tp/tp-14-scripts.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


> Durée estimée : 45 min

> Chapitres associés : [C03. Écrire un premier script Bash](https://kayasam.github.io/lpi101/complements/03-premiers-scripts/), [C04. Découvrir les conditions et les boucles](https://kayasam.github.io/lpi101/complements/04-conditions-boucles/), [C05. Lire des scripts utilitaires](https://kayasam.github.io/lpi101/complements/05-scripts-utilitaires/)

---

## Objectifs

- Créer un script exécutable avec un paramètre.
- Utiliser une condition et un code retour.
- Vérifier un résultat avant d’annoncer un succès.

## Avant de commencer

Cet atelier est un prolongement après l’initiation au shell. L’énoncé donne le comportement attendu ; plusieurs solutions sont possibles.

> [!info] Atelier optionnel
> À proposer après les bases, selon le rythme du groupe.

**Préparation fournie :**

```bash
mkdir -p ~/lpi101-tp/tp14
cd ~/lpi101-tp/tp14
```

---

## Partie A — Écrire et exécuter (15 min)

**A1.** Crée `bonjour.sh` : il affiche `Bonjour PRENOM`, en prenant le premier argument comme prénom et `stagiaire` si aucun argument n’est fourni.

**A2.** Vérifie sa syntaxe puis lance-le avec le prénom composé `Jean Paul`. Quelle différence entre `bash bonjour.sh` et `./bonjour.sh` ?

---

## Partie B — Contrôler une condition (20 min)

**B1.** Crée `controle.sh` : il reçoit un chemin, affiche `OK : chemin` si c’est un fichier ordinaire, sinon écrit `Absent : chemin` sur stderr et termine avec le code 1.

**B2.** Avec une boucle, lance le contrôle sur `bonjour.sh`, `controle.sh` et `fichier-absent.txt`, en signalant clairement les échecs.

---

## Partie C — Conserver une preuve (10 min)

**C1.** Archive les deux scripts dans `scripts.tar.gz`. N’affiche `Archive créée` que si tar a réussi, puis liste le contenu.
