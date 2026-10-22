---
title: "18 — Modifier un fichier avec nano et vi"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/18-editeurs-texte"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/18-editeurs-texte/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/18-editeurs-texte/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/18-editeurs-texte.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

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
