---
title: "C03. Écrire un premier script Bash"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="complements/03-premiers-scripts"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/complements/03-premiers-scripts/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/complements/complements/c03-premiers-scripts/c03-premiers-scripts.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Regrouper quelques commandes et utiliser des paramètres.

> [!info] Complément
> À découvrir après les bases, selon le rythme du groupe.

---

## Qu’est-ce qu’un script shell ?

Un **script shell** est un fichier texte contenant une suite de commandes exécutées automatiquement par l’interpréteur **bash** (ou un autre shell).
Il permet d’automatiser des tâches répétitives : sauvegardes, vérifications, installations, etc.

---

## Exécution et droits

Pour une exécution directe, un script utilise généralement une **ligne d’en-tête** appelée *shebang*, qui indique quel interpréteur doit l’exécuter :

```bash
#!/bin/bash
```

Pour qu’un script soit exécutable :

```bash
chmod +x monscript.sh
./monscript.sh
```

---

## Variables et expansions

Les variables stockent des valeurs temporaires utilisées dans le script.

```bash
NOM="Sam"
echo "Bonjour $NOM"
```

Quelques variables prédéfinies utiles :

* `$HOME` → répertoire personnel
* `$USER` → nom de l’utilisateur courant
* `$PWD` → répertoire courant
* `$0`, `$1`, `$2` → nom du script et paramètres passés en ligne de commande

---

## 📌 À retenir
> [!tip]
> - Un **script shell** est un simple fichier texte exécuté automatiquement par le shell.
> - Le _shebang_ (`#!/bin/bash`) indique quel interpréteur utiliser.
> - Pour `./script.sh`, le droit d’exécution est nécessaire ; `bash script.sh` permet aussi de lancer un script lisible sans ce droit.
> - Les **variables** permettent de stocker des valeurs et de les réutiliser dans le script.
> - Les variables prédéfinies comme `$HOME`, `$USER`, `$PWD` ou `$1` sont très utiles dans les scripts.
> - L’exécution d’un script peut se faire avec `./script.sh` depuis son répertoire.

---

## Passer un paramètre

```bash
#!/bin/bash
nom="${1:-Sam}"
printf 'Bonjour %s\n' "$nom"
```

Enregistrer dans `bonjour.sh`, puis lancer `bash bonjour.sh Alex`. `$1` représente le premier argument et `${1:-Sam}` fournit une valeur par défaut.
