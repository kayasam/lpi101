# 17 — Rechercher avec les expressions régulières

> [!note] Objectif
> Construire des motifs simples et distinguer expressions régulières et jokers du shell.

**Repères LPI 101 :** 103.7.

**Commandes à connaître :** `grep`, `grep -E`, `sed`.

---

## Avant tout : ne pas confondre **wildcards** et **expressions régulières**

Les **wildcards** (ou _motifs génériques du shell_) et les **expressions régulières** (ou _regex_) se ressemblent, mais ce ne sont **pas du tout la même chose**.

|Type|Utilisation|Exemple|Signification|
|---|---|---|---|
|**Wildcards**|Utilisés par le **shell** (ex : `ls`, `rm`, `cp`)|`ls *.txt`|Tous les fichiers qui se terminent par `.txt`|
|**Regex**|Utilisées par des outils comme **`grep`**, **`sed`**, **`awk`**, **`find`**, etc.|`grep '.*txt$' fichier`|Toutes les lignes qui se terminent par "txt"|

**Différences clés :**

- Les **wildcards** servent à filtrer des **noms de fichiers**, pas du texte.

- Les **regex** servent à chercher des **motifs dans du contenu texte** (lignes de fichiers, logs, etc.).

- Les **symboles n’ont pas la même signification** :

    - En shell : `*` = une suite de zéro ou plusieurs caractères

    - En regex : `*` = “répète le caractère précédent 0 ou plusieurs fois”

---

## Introduction

Les **expressions régulières** (ou **regex**) sont des motifs de recherche puissants permettant d’analyser, filtrer et manipuler du texte de manière avancée.
Elles sont utilisées dans de nombreux outils Linux (`grep`, `sed`, `awk`, `find`, `vim`, etc.) et dans la plupart des langages de programmation.

---

## Notions de base

Une expression régulière décrit **un motif de caractères** à rechercher dans un texte.
Elle permet d’aller bien au-delà d’une simple recherche de mot exact.

Exemples simples :

| Motif      | Signification                         | Exemple de correspondance       |
| ---------- | ------------------------------------- | ------------------------------- |
| `root`     | Mot exact                             | "root"                          |
| `r..t`     | `.` remplace n’importe quel caractère | "root", "rebt"                  |
| `^user`    | Commence par "user"                   | "username"                      |
| `bash$`    | Finit par "bash"                      | "/bin/bash"                     |
| `[0-9]`    | Un chiffre entre 0 et 9               | "3", "8"                        |
| `[A-Za-z]` | Une lettre majuscule ou minuscule     | "a", "Z"                        |
| `[^0-9]`   | Tout sauf un chiffre                  | "a", "-"                        |
| `*`        | Répétition (0 ou plusieurs fois)      | `go*` → "g", "go", "goo"        |
| `+`        | Répétition (1 ou plusieurs fois)      | `go+` → "go", "goo"             |
| `?`        | Optionnel (0 ou 1 fois)               | `colou?r` → "color" ou "colour" |

---

## Types d’expressions régulières

Sous Linux, il existe deux types principaux de syntaxe pour les expressions régulières POSIX :

---

## **BRE (Basic Regular Expressions)**

→ utilisées par défaut avec la commande `grep`.

Certains symboles spéciaux doivent être **échappés avec un antislash (`\`)** pour être reconnus.
C’est une syntaxe plus ancienne et un peu moins lisible.

**Exemple :**

```bash
grep '^\(root\|daemon\):' /etc/passwd
```

Explications :

- `\(` et `\)` → délimitent un **groupe** (il faut les échapper)

- `\|` → signifie **OU** avec GNU grep ; c’est une extension de sa syntaxe BRE

- `^` → début de ligne

- `:` → séparateur après le nom du compte (dans cet exemple)

Cette commande affiche toutes les **lignes dont le premier champ est “root” ou “daemon”** dans `/etc/passwd`.

---

## **ERE (Extended Regular Expressions)**

→ activées avec `grep -E` (ancien nom : `egrep`).

Dans cette version, les symboles `()`, `|`, `+`, `?` et `{}` sont **interprétés directement**, sans besoin d’antislashs.

**Exemple équivalent :**

```bash
grep -E '^(root|daemon):' /etc/passwd
```

Explications :

- Les parenthèses `()` et le `|` sont compris **sans les `\`**, donc la syntaxe est **plus simple et plus lisible**.

- Le motif est identique en logique : il recherche les lignes dont le premier champ est **“root” ou “daemon”**.

---

## Comparatif clair

|Objectif|Syntaxe **BRE** (grep)|Syntaxe **ERE** (grep -E)|
|---|---|---|
|Grouper|`\( ... \)`|`( ... )`|
|OU logique|`\\|`|`\|`|
|Un ou plusieurs (`+`)|`\+`|`+`|
|Zéro ou un (`?`)|`\?`|`?`|
|Répétition `{m,n}`|`\{m,n\}`|`{m,n}`|

---
> [!info]
> - `grep` (BRE) = plus ancien, **antislash obligatoire** pour certains symboles.
>
> - `grep -E` (ERE) = **plus moderne et plus lisible**, plus courant aujourd’hui.
>
> - Les deux font la même chose, mais **ERE est recommandé** pour plus de clarté.

---

## Exemples pratiques

```bash
# Lignes commençant par root
grep '^root' /etc/passwd

# Lignes finissant par /bin/bash
grep '/bin/bash$' /etc/passwd

# Lignes contenant un chiffre
grep '[0-9]' /etc/passwd

# Lignes ne contenant PAS de chiffre
grep -v '[0-9]' /etc/passwd

# Utilisation d’une expression étendue (option -E)
grep -E '^(root|daemon)' /etc/passwd
```

---

## Combinaisons avec sed et awk

* Avec `sed` :

  ```bash
  sed -n '/bash$/p' /etc/passwd
  sed 's/[0-9]/#/g' fichier.txt     # remplace les chiffres par #
  ```

* Avec `awk` :

  ```bash
  awk -F: '/bash$/ {print $1}' /etc/passwd
  awk -F: '/^root:/ {print $1,$6}' /etc/passwd
  ```

---

## Outils interactifs pour s’entraîner

* [Regex101](https://regex101.com/) — permet de tester ses expressions avec explications en direct (supporte plusieurs syntaxes).
* [RegexOne](https://regexone.com/) — propose des **leçons progressives** et des exercices interactifs pour apprendre étape par étape.
* [Regexlearn](https://regexlearn.com/fr/learn/regex101) — offre un **apprentissage interactif et progressif en français**, idéal pour s’initier pas à pas aux expressions régulières.

---

## À retenir
> [!tip]
> * Les **expressions régulières** servent à rechercher, filtrer et manipuler du texte de manière très fine.
> * Les symboles principaux :
>
>   * `.` : un caractère quelconque
>   * `^` : début de ligne
>   * `$` : fin de ligne
>   * `[]` : ensemble de caractères autorisés
>   * `[^]` : ensemble interdit
>   * `*`, `+`, `?` : répétitions
>   * `|` : OU logique
>   * `()` : regroupement
> * **BRE** (basic) pour `grep`, **ERE** (extended) pour `grep -E` (ancien nom : `egrep`).
> * Outils principaux : `grep`, `sed`, `awk`.
> * Pour s’exercer :
>
>   * [Regex101.com](https://regex101.com/)
>   * [RegexOne.com](https://regexone.com/)
>   * [Regexlearn](https://regexlearn.com/fr/learn/regex101)
