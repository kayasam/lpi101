---
title: "TP 03 — Sauvegarder un dossier et préparer son shell"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/14-environnement-shell"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/14-environnement-shell/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/14-environnement-shell/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/tp/14-environnement-shell.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


> Durée estimée : 50 min

> Chapitres associés : [13 — Archiver et compresser](https://kayasam.github.io/lpi101/lpi101/13-archives-compression/), [14 — Variables, environnement et historique](https://kayasam.github.io/lpi101/lpi101/14-environnement-shell/)

---

## Objectifs

- Créer une archive, vérifier son contenu et la restaurer.
- Utiliser des variables et distinguer expansion et texte littéral.
- Comprendre PATH et retrouver une commande.

## Avant de commencer

Utilise un compte standard dans la VM Debian. Les parties se suivent dans le même terminal.

**Préparation fournie :**

```bash
mkdir -p ~/lpi101-tp/tp03/source
cd ~/lpi101-tp/tp03
printf 'Compte rendu\n' > source/rapport.txt
printf 'Paramètre de test\n' > source/.reglage
```

---

## Partie A — Archiver et restaurer (25 min)

**A1.** Crée une archive compressée `projet.tar.gz` de `source`, puis liste son contenu sans l’extraire. Le fichier caché est-il présent ?

**A2.** Restaure l’archive dans `restauration`, puis compare le fichier restauré avec celui de départ.

**A3.** Compresse une copie de `rapport.txt` avec gzip, puis décompresse-la. Que devient le fichier d’entrée par défaut ?

---

## Partie B — Variables et environnement (15 min)

**B1.** Crée la variable `message` contenant `Bonjour Linux`. Affiche-la avec des guillemets doubles puis simples et explique la différence.

**B2.** Exporte la variable, lis-la depuis un nouveau Bash, puis supprime-la de la session.

**B3.** Affiche HOME et PATH. Comment lancerais-tu un script `outil.sh` présent dans ton dossier actuel et absent de PATH ?

---

## Partie C — Réutiliser une commande (10 min)

**C1.** Dans ton terminal interactif, retrouve une commande précédente avec les flèches puis avec Ctrl+R. Affiche les dix dernières commandes.

**C2.** Pourquoi une archive conservée uniquement sur le même disque n’est-elle pas une sauvegarde suffisante ?
