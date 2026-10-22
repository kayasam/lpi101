---
title: "14 — Variables, environnement et historique"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/14-environnement-shell"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/14-environnement-shell/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/14-environnement-shell/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/14-environnement-shell.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Comprendre où Bash cherche les commandes et réutiliser son historique.

**Repères LPI 101 :** 103.1.

**Commandes à connaître :** `echo`, `env`, `export`, `set`, `unset`, `history`, `type`, `command -v`.

**Fichiers et emplacements :** `~/.bash_history`, `~/.bashrc`.

---

## Afficher une valeur

```bash
echo "$HOME"
echo "$USER"
echo "$PWD"
echo "$PATH"
```

`HOME` désigne le dossier personnel, `USER` un nom d’utilisateur fourni par l’environnement et `PWD` le répertoire courant du shell. `whoami` indique l’identité effective de la commande.

`PATH` est une liste de dossiers séparés par `:`. Bash y cherche les programmes dont on saisit le nom sans chemin. Pour un script présent dans le dossier courant, on utilise généralement `./script.sh`.

## Variable du shell et variable exportée

```bash
message="Bonjour Sam"
echo "$message"
export message
bash -c 'echo "$message"'
unset message
```

L’affectation ne contient aucun espace autour de `=`. `export` transmet la variable aux futurs processus enfants. Une modification dans un enfant ne change pas la variable de son parent. `env` affiche l’environnement exporté ; `set` affiche aussi des variables et fonctions du shell et produit souvent une longue sortie.

## Comprendre les guillemets et les substitutions

```bash
nom="Sam"
echo "Bonjour $nom"
echo 'Bonjour $nom'
aujourdhui=$(date +%F)
echo "$aujourdhui"
```

Les guillemets doubles permettent l’expansion de `$nom` tout en gardant un argument. Les simples conservent le texte littéral. `$(commande)` remplace l’expression par la sortie de la commande.

## Retrouver une commande

```bash
history
history 10
```

Utiliser les flèches haut/bas pour parcourir les dernières commandes et **Ctrl+R** pour rechercher un fragment. Modifier la commande retrouvée avant de l’exécuter. L’historique est généralement enregistré dans `~/.bash_history`, avec un comportement qui dépend de la configuration et des sessions ouvertes.

## Ajouter un dossier de commandes

```bash
mkdir -p "$HOME/bin"
export PATH="$HOME/bin:$PATH"
command -v bash
```

Cette modification concerne la session et ses futurs enfants. Le complément sur `.bashrc` explique comment conserver une personnalisation. Ne pas supprimer les anciennes valeurs de `PATH`.

## À retenir

> [!tip]
> `$nom` lit une variable, `export` la transmet et `PATH` sert à retrouver les programmes. L’historique évite de tout retaper.
