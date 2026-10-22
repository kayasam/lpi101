---
title: "21 — Droits par défaut et bits spéciaux"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/21-umask-bits-speciaux"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/21-umask-bits-speciaux/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/21-umask-bits-speciaux/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/21-umask-bits-speciaux.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Expliquer umask, SUID, SGID et sticky bit avec des cas concrets.

**Repères LPI 101 :** 104.5.

**Commandes à connaître :** `umask`, `chmod`.

---

## Masque `umask`

`umask` retire des droits aux permissions demandées lors de la création d’un fichier ou d’un répertoire. Ce masque se combine par opérations sur les bits, pas par une soustraction arithmétique générale.

Afficher la valeur actuelle :

```bash
umask
```

Exemple :

```text
0022
```

Interprétation :

* Fichier créé → permissions par défaut `644` avec un masque `022` (rw-r--r--)
* Répertoire créé → permissions par défaut `755` avec un masque `022` (rwxr-xr-x)

Modifier temporairement la valeur :

```bash
umask 002
```

Cela donnera par défaut :

* fichiers : `664`
* répertoires : `775`

---

## Bits spéciaux : `suid`, `sgid`, `sticky bit`

Ces bits modifient le comportement d’exécution ou d’accès à certains fichiers.

## `suid` (Set User ID)

* Sur un fichier exécutable : le programme s’exécute avec les droits du propriétaire.
* Exemple : `/usr/bin/passwd` possède le bit `s` pour root :

  ```text
  -rwsr-xr-x 1 root root /usr/bin/passwd
  ```

  Cela permet à un utilisateur de modifier son mot de passe sans être root.

## `sgid` (Set Group ID)

* Sur un dossier : les nouveaux fichiers héritent du groupe du dossier.
* Exemple :

  ```bash
  chmod g+s /srv/projets
  ```

  Tous les fichiers créés dans `/srv/projets` appartiendront au même groupe.

## `sticky bit`

* Dans un dossier partagé, réserve la suppression ou le renommage d’une entrée au propriétaire du fichier, au propriétaire du dossier ou à un processus suffisamment privilégié.
* Utilisé dans `/tmp` :

  ```text
  drwxrwxrwt 10 root root /tmp
  ```

  Le `t` final indique le sticky bit.

---

## Calculer les droits à la création

Le masque retire des droits aux permissions demandées par le programme. Pour les créations courantes : base `666` pour un fichier ordinaire et `777` pour un dossier.

| Masque | Fichier courant | Dossier courant |
|---|---|---|
| `022` | `644` | `755` |
| `027` | `640` | `750` |
| `077` | `600` | `700` |

`umask` ne modifie pas les fichiers déjà existants et n’ajoute pas de droit d’exécution aux nouveaux fichiers ordinaires. Les ACL par défaut peuvent aussi intervenir.

## À retenir

> [!tip]
> `umask` concerne les droits à la création ; SGID sur un dossier facilite le partage de groupe ; le sticky bit protège la suppression des entrées d’un dossier partagé. SUID sur un exécutable change l’identité effective du processus.
