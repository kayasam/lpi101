---
title: "C01. Donner des droits précis avec les ACL"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="complements/01-acl"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/complements/01-acl/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://cours.kaya.ovh/lpi101/complements/01-acl/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/complements/complements/c01-acl/c01-acl.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

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
