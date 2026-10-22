# 18 — Modifier un fichier avec nano et vi

> [!note] Objectif
> Ouvrir, modifier et enregistrer un fichier texte depuis le terminal.

**Repères LPI 101 :** 103.8.

**Commandes à connaître :** `nano`, `vi`, `vim`, `vimtutor`.

---

## Rôle des éditeurs de texte

Sous Linux, la majorité des fichiers de configuration sont **des fichiers texte**.
Il est donc essentiel de savoir les **ouvrir, modifier et enregistrer** en ligne de commande.

Les éditeurs de texte permettent d’éditer ces fichiers directement depuis le terminal, sans interface graphique.

---

## Les principaux éditeurs de texte

|Éditeur|Type|Caractéristiques principales|Utilisation recommandée|
|---|---|---|---|
|**nano**|Simple|Interface claire, commandes affichées en bas de l’écran|Débutants|
|**vim / vi**|Avancé|Très puissant, modes multiples (commande / insertion)|Administrateurs expérimentés|
|**micro** _(optionnel)_|Moderne|Coloration syntaxique, gestion de la souris, intuitive|Alternative pratique|
|**gedit / mousepad**|Graphique|Interface graphique simple (si environnement GNOME/XFCE)|Utilisation bureautique|

---

## Nano — l’éditeur le plus simple

Nano est souvent installé par défaut.
Pour éditer un fichier :

```bash
nano /etc/hosts
```

## Commandes utiles :

|Action|Touche|
|---|---|
|Enregistrer|`Ctrl + O`|
|Quitter|`Ctrl + X`|
|Rechercher|`Ctrl + W`|
|Aller à une ligne|`Ctrl + _`|

En bas de l’écran, le symbole `^` signifie **Ctrl**.
Exemple : `^X` = `Ctrl + X`.

---

## Vim — l’éditeur puissant

Vim (ou son ancêtre vi) est plus complexe, mais indispensable à connaître pour l’examen LPI et les environnements serveur.

Pour l’ouvrir :

```bash
vim /etc/hosts
```

## Les deux modes principaux :

|Mode|Description|Entrée / sortie|
|---|---|---|
|**Mode commande**|Navigation, suppression, recherche, enregistrement|`Échap` pour y revenir|
|**Mode insertion**|Édition du texte librement|`i` pour insérer du texte|

## Commandes essentielles :

|Action|Commande|
|---|---|
|Passer en insertion|`i`|
|Sauvegarder|`:w`|
|Quitter|`:q`|
|Sauvegarder et quitter|`:wq`|
|Quitter sans enregistrer|`:q!`|
|Rechercher un mot|`/mot`|

Pour débuter, tape :

```bash
vimtutor
```

C’est un tutoriel interactif intégré.

---

## Micro — une alternative moderne

`micro` est un éditeur simple et coloré, inspiré de Sublime Text.
Il n’est pas inclus par défaut mais peut être installé facilement :

```bash
sudo apt install micro
```

Caractéristiques :

- Navigation au clavier ou à la souris

- Coloration syntaxique

- Copie/collage classiques (`Ctrl + C / V`)

- Barre de statut intuitive

C’est un excellent compromis pour les utilisateurs débutants souhaitant un peu plus de confort que nano.

---

## Éditeurs graphiques

Sur un environnement graphique, des éditeurs comme **gedit**, **mousepad** ou **kate** permettent de modifier les fichiers plus facilement, mais leur usage est limité aux systèmes avec interface graphique (non recommandé sur serveur).

---

## Les gestes essentiels dans vi

Dans le mode normal, les lettres sont des commandes. Appuyer sur Échap pour revenir dans ce mode avant les actions suivantes.

| Action | Touche ou commande |
|---|---|
| Déplacer le curseur | `h`, `j`, `k`, `l` ou les flèches |
| Début / fin de ligne | `0` / `$` |
| Début / fin de fichier | `gg` / `G` |
| Supprimer une ligne | `dd` |
| Copier une ligne | `yy` |
| Coller après le curseur | `p` |
| Annuler | `u` |
| Refaire | Ctrl+R |
| Occurrence suivante d’une recherche | `n` |

## Choisir son éditeur

```bash
export EDITOR=nano
export VISUAL=nano
```

Ces variables indiquent une préférence aux programmes qui les consultent. Sous Debian, `select-editor` configure aussi l’éditeur utilisé par certains outils de la distribution. Nano reste l’outil de départ ; les gestes vi constituent une petite compétence à acquérir progressivement.

---

## À retenir

> [!tip]
> - De nombreux fichiers de configuration Linux sont **du texte brut**.
> - **Nano** est l’éditeur le plus simple pour les débutants.
> - **Vim** est un outil courant en administration Linux.
> - On peut installer **micro** pour plus de confort.
> - Savoir **quitter et sauvegarder** sous Vim est une compétence indispensable.
>
