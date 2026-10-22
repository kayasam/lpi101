# C04. Découvrir les conditions et les boucles

> [!note] Objectif
> Lire un test simple et répéter une action.

> [!info] Complément
> À découvrir après les bases, selon le rythme du groupe.

---

## Les tests conditionnels

```bash
if [ -f /etc/passwd ]; then
  echo "Le fichier existe."
else
  echo "Fichier introuvable."
fi
```

Autres opérateurs utiles :

* `-d` → test si c’est un dossier
* `-e` → test si le fichier existe
* `-z` → test si une variable est vide
* `=` ou `!=` → comparaison de chaînes
* `-lt`, `-gt`, `-eq` → comparaisons numériques

---

## Les boucles

**for** — répète une commande pour chaque élément :

```bash
for i in 1 2 3; do
  echo "Tour n°$i"
done
```

**while** — répète tant qu’une condition est vraie :

```bash
n=1
while [ $n -le 3 ]; do
  echo "Itération $n"
  n=$((n+1))
done
```

---

## Commandes interactives

Permettent de créer des scripts dynamiques :

```bash
read -p "Quel est ton nom ? " nom
echo "Bonjour $nom !"
```

`echo -e` permet d’interpréter les caractères spéciaux :

```bash
echo -e "Ligne 1\nLigne 2"
```

---

## À retenir
> [!tip]
> - Les tests conditionnels permettent d’exécuter du code selon une condition (`if`, `else`).
> - Les opérateurs `-f`, `-d`, `-e`, `-z`, `=`, `!=`, `-lt`, `-gt`, `-eq` servent à comparer fichiers, chaînes et valeurs.
> - Les boucles `for` et `while` permettent de répéter des instructions automatiquement.
> - `read` permet de demander une entrée à l’utilisateur dans un script.
> - `echo -e` active l’interprétation des caractères spéciaux comme `\n`.
