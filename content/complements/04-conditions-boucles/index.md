---
title: "C04. Découvrir les conditions et les boucles"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="complements/04-conditions-boucles"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/complements/04-conditions-boucles/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/complements/complements/c04-conditions-boucles/c04-conditions-boucles.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

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
