# 14. Variables, environnement et historique

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
