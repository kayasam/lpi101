# C05. Lire des scripts utilitaires

> [!note] Objectif
> Comprendre une petite automatisation et vérifier son résultat.

> [!info] Complément
> À découvrir après les bases, selon le rythme du groupe.

---

Quelques exemples simples :

**Afficher des infos système :**

```bash
#!/bin/bash
echo "Utilisateur : $USER"
echo "Répertoire : $PWD"
echo "Système actif depuis :"
uptime
```

**Sauvegarde basique :**

```bash
#!/bin/bash
SRC="/etc"
DEST="/mnt/backup"
DATE=$(date +%Y-%m-%d)
if tar czf "$DEST/sauvegarde-$DATE.tar.gz" "$SRC"; then
  echo "Sauvegarde terminée."
else
  echo "Échec de la sauvegarde." >&2
  exit 1
fi
```

---

## À retenir
> [!tip]
> * Un **script shell** est une suite de commandes exécutées automatiquement.
> * Il commence par un **shebang** (`#!/bin/bash`).
> * On doit lui donner le **droit d’exécution** avec `chmod +x`.
> * Les **variables** stockent et réutilisent des valeurs.
> * Les **tests** (`if`, `else`) et **boucles** (`for`, `while`) contrôlent le déroulement du script.
> * `read` et `echo` rendent les scripts interactifs.
> * Même avec des bases simples, on peut automatiser beaucoup de tâches répétitives.

> [!note] Préparer la destination
> L’exemple de sauvegarde suppose que `/mnt/backup` existe, est monté si nécessaire et est accessible en écriture. Vérifier la destination et les droits de lecture de la source avant l’exécution.
