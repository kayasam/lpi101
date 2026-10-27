---
title: "C05. Lire des scripts utilitaires"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="complements/05-scripts-utilitaires"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/complements/05-scripts-utilitaires/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://cours.kaya.ovh/lpi101/complements/05-scripts-utilitaires/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/complements/complements/c05-scripts-utilitaires/c05-scripts-utilitaires.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

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
