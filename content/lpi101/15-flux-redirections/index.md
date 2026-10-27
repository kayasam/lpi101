---
title: "15. Flux, redirections et tubes"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/15-flux-redirections"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/15-flux-redirections/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/15-flux-redirections/15-flux-redirections.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Relier des commandes et distinguer résultat normal et message d’erreur.

**Repères LPI 101 :** 103.4.

**Commandes à connaître :** `echo`, `tee`, `xargs`.

---

## Introduction

Sous Linux, **tout est flux** : chaque programme communique via des canaux standards d’entrée et de sortie.
Comprendre et manipuler ces flux est essentiel pour combiner les commandes, automatiser des traitements et chaîner des opérations complexes.

---

## Les trois flux standards

| Nom        | Numéro | Description                                             | Exemple                        |
| ---------- | ------ | ------------------------------------------------------- | ------------------------------ |
| **stdin**  | 0      | Entrée standard — données lues par le programme         | `cat < fichier.txt`            |
| **stdout** | 1      | Sortie standard — résultat “normal” d’un programme      | `echo "OK" > fichier.txt`      |
| **stderr** | 2      | Sortie d’erreur — messages d’erreur séparés du résultat | `ls /inexistant 2> erreur.log` |

![Les trois flux standards et un tube : stdin 0 entre dans une commande ; stdout 1 et stderr 2 en sortent séparément. Le tube relie stdout à stdin.](https://cours.kaya.ovh/lpi101/assets/course-media/6203e91e1bfc5301.svg)

Le haut du schéma distingue les trois flux ; le bas montre comment le tube relie deux commandes.

---

## Redirections de base

* **Envoyer la sortie vers un fichier (création/écrasement)**

  ```bash
  commande > fichier.txt
  ```

  Remplace le contenu du fichier par la sortie.

* **Ajouter à la fin d’un fichier (sans écraser)**

  ```bash
  commande >> fichier.txt
  ```

  Concatène le résultat au fichier existant.

* **Lire à partir d’un fichier**

  ```bash
  commande < fichier.txt
  ```

  Fournit le contenu du fichier comme entrée.

---

## Redirection des erreurs

* **Rediriger les erreurs vers un fichier dédié**

  ```bash
  commande 2> erreurs.log
  ```

* **Rediriger la sortie et les erreurs ensemble**

  ```bash
  commande &> tout.log
  ```

  ou équivalent POSIX :

  ```bash
  commande > tout.log 2>&1
  ```

* **Ignorer les erreurs (envoyer vers le “trou noir”)**

  ```bash
  commande 2>/dev/null
  ```

---

## Chaînage de commandes

* **Enchaîner seulement si la commande précédente réussit**

  ```bash
  commande1 && commande2
  ```

  (`commande2` ne s’exécute que si la première renvoie un code 0)

* **Enchaîner seulement si la commande précédente échoue**

  ```bash
  commande1 || commande2
  ```

  (`commande2` ne s’exécute que si la première échoue)

* **Exécuter plusieurs commandes à la suite, peu importe le résultat**

  ```bash
  commande1 ; commande2
  ```

---

## Les pipes (`|`)

Le **pipe** relie la sortie standard d’une commande à l’entrée standard d’une autre :

```bash
commande1 | commande2
```

Exemples :

```bash
ls -l /etc | less
cat /etc/passwd | grep root
```

> Le tube permet de chaîner les commandes sans passer par des fichiers temporaires : on crée ainsi des **chaînes de traitement efficaces**.

---

## Codes de retour

Chaque commande se termine par un **code de sortie** :

* `0` → succès
* autre → erreur

Afficher le dernier code de retour :

```bash
echo $?
```

Utile dans les scripts ou pour tester le comportement des commandes combinées avec `&&` et `||`.

---

## Afficher et enregistrer avec tee

```bash
printf 'Bonjour\n' | tee resultat.txt
printf 'Suite\n' | tee -a resultat.txt
```

`tee` envoie les mêmes données vers l’écran et le fichier ; `-a` ajoute au lieu d’écraser. Il n’est donc plus nécessaire de relancer la commande pour voir son résultat.

## Transmettre des arguments avec xargs

```bash
printf '%s\0' /etc/hostname /etc/hosts | xargs -0 wc -l
```

Le tube transmet du texte sur l’entrée standard ; `xargs` transforme cette entrée en **arguments** de la commande `wc`. Le séparateur nul et `-0` permettent de conserver les noms contenant des espaces.

## Lire l’ordre des redirections

```bash
ls /etc /inexistant > resultat.log 2>&1
```

La sortie standard va d’abord dans le fichier ; la sortie d’erreur est ensuite reliée à cette destination. Inverser `2>&1` et `> resultat.log` change le résultat.

---

## À retenir
> [!tip]
> * Linux gère trois flux : **entrée (0)**, **sortie (1)** et **erreur (2)**.
> * Les redirections `>`, `>>`, `<` permettent d’écrire ou de lire depuis un fichier.
> * `2>` redirige les erreurs ; `&>` combine sortie + erreur.
> * Le symbole `|` (pipe) envoie la sortie d’une commande vers une autre.
> * Les opérateurs `&&`, `||`, `;` permettent de contrôler l’exécution selon le résultat.
> * `$?` affiche le code de retour de la dernière commande.
