# C01. Donner des droits précis avec les ACL

> [!note] Objectif
> Ajouter une autorisation ciblée après avoir compris les permissions classiques.

> [!info] Complément
> À découvrir après les bases, selon le rythme du groupe.

---

## Introduction

Les **ACL** (_Access Control Lists_) permettent d’aller **au-delà des permissions classiques** (`rwx` pour propriétaire, groupe et autres).
Elles offrent une **gestion plus fine des droits** d’accès, en autorisant des permissions spécifiques pour **plusieurs utilisateurs ou groupes** sur un même fichier ou répertoire.

Cette section explique :

- comment **installer** et **afficher** les ACL ;

- comment **attribuer** des droits avancés à des utilisateurs et groupes ;

- comment **comprendre le fonctionnement du masque** (_mask_).

---

## Installation du support ACL

Les systèmes modernes supportent les ACL nativement.
Si les commandes `getfacl` et `setfacl` ne sont pas disponibles, installez le paquet suivant :

```bash
sudo apt install acl
```

---

## Commandes principales

## `getfacl` — afficher les ACL

Cette commande affiche les permissions étendues d’un fichier ou répertoire.

```bash
getfacl fichier.txt
```

Exemple de sortie :

```text
# file: fichier.txt
# owner: sam
# group: compta
user::rw-
group::r--
group:rh:r-x
mask::rwx
other::r--
```

Explications :

- `user::` → droits du propriétaire

- `group::` → droits du groupe principal

- `group:rh:` → droits spécifiques au groupe `rh`

- `mask::` → limite maximale des permissions effectives

- `other::` → droits des autres utilisateurs

---

## `setfacl` — définir une ACL

Attribuer un droit spécifique à un utilisateur :

```bash
setfacl -m u:alice:rw fichier.txt
```

Attribuer un droit spécifique à un groupe :

```bash
setfacl -m g:rh:r-x fichier.txt
```

Supprimer une ACL :

```bash
setfacl -x u:alice fichier.txt
```

---

## Héritage et ACL par défaut

Les répertoires peuvent définir des **ACL par défaut** : elles seront automatiquement appliquées aux nouveaux fichiers ou dossiers créés à l’intérieur.

Définir une ACL par défaut :

```bash
setfacl -m d:u:alice:rwx /srv/partage
```

Afficher les ACL par défaut :

```bash
getfacl /srv/partage
```

Les lignes commençant par `default:` indiquent ces ACL héritées.

---

## Le rôle du masque (`mask`)

Le **mask** limite les droits effectifs des entrées ACL pour les utilisateurs et groupes **autres que le propriétaire**.
Même si une ACL accorde `rwx`, le **mask** peut restreindre l’accès réel.

Vérifier l’effet du masque :

```bash
getfacl fichier.txt
```

Modifier le masque :

```bash
setfacl -m m:r-x fichier.txt
```

---

## Supprimer toutes les ACL

Pour réinitialiser un fichier à ses permissions classiques :

```bash
setfacl -b fichier.txt
```

(`-b` supprime toutes les ACL associées)

---

## À retenir
> [!tip]
> - Les **ACL** permettent une **gestion plus granulaire** que les permissions classiques `rwx`.
>
> - `getfacl` affiche les ACL, `setfacl` les modifie.
>
> - Le **mask** limite les droits effectifs des ACL.
>
> - Les **ACL par défaut** permettent l’héritage dans un répertoire.
>
> - `setfacl -b` réinitialise un fichier en supprimant toutes les ACL.
>
