---
title: "TP 03. Sauvegarder un dossier et préparer son shell — Correction"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/14-environnement-shell"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/14-environnement-shell/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://cours.kaya.ovh/lpi101/lpi101/14-environnement-shell/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/14-environnement-shell/tp/tp-03-archives-environnement-correction.md">↓ Télécharger le corrigé (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://cours.kaya.ovh/lpi101/lpi101/14-environnement-shell/tp">Énoncé</a><a class="exercise-correction" href="https://cours.kaya.ovh/lpi101/lpi101/14-environnement-shell/tp-corrigev2" aria-current="page">Corrigé</a></nav>

> Essaie chaque question avant d’ouvrir **Afficher la correction**. Chaque réponse se replie indépendamment.

> Durée estimée : 50 min

> Chapitres associés : [13. Archiver et compresser](https://cours.kaya.ovh/lpi101/lpi101/13-archives-compression/), [14. Variables, environnement et historique](https://cours.kaya.ovh/lpi101/lpi101/14-environnement-shell/)

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

> [!success]- Afficher la correction — A1
> ```bash
> tar -czf projet.tar.gz source
> tar -tzf projet.tar.gz
> ```
>
> Oui : on archive le dossier lui-même, pas seulement la sélection `source/*` qui omet habituellement les fichiers cachés.

**A2.** Restaure l’archive dans `restauration`, puis compare le fichier restauré avec celui de départ.

> [!success]- Afficher la correction — A2
> ```bash
> mkdir restauration
> tar -xzf projet.tar.gz -C restauration
> cmp source/rapport.txt restauration/source/rapport.txt
> ```
>
> `cmp` ne produit rien et renvoie 0 si les contenus sont identiques. Le chemin `source/` était enregistré dans l’archive.

**A3.** Compresse une copie de `rapport.txt` avec gzip, puis décompresse-la. Que devient le fichier d’entrée par défaut ?

> [!success]- Afficher la correction — A3
> ```bash
> cp source/rapport.txt rapport.txt
> gzip rapport.txt
> ls rapport.txt.gz
> gunzip rapport.txt.gz
> cat rapport.txt
> ```
>
> Par défaut, gzip remplace le fichier d’entrée par sa version compressée ; `-k` permet de le conserver. Archiver et compresser sont deux opérations distinctes.

---

## Partie B — Variables et environnement (15 min)

**B1.** Crée la variable `message` contenant `Bonjour Linux`. Affiche-la avec des guillemets doubles puis simples et explique la différence.

> [!success]- Afficher la correction — B1
> ```bash
> message="Bonjour Linux"
> echo "$message"
> echo '$message'
> ```
>
> Les doubles permettent l’expansion ; les simples affichent littéralement `$message`. L’affectation n’a pas d’espaces autour de `=`.

**B2.** Exporte la variable, lis-la depuis un nouveau Bash, puis supprime-la de la session.

> [!success]- Afficher la correction — B2
> ```bash
> export message
> bash -c 'echo "$message"'
> unset message
> ```
>
> Le processus enfant reçoit les variables exportées. L’export n’est pas une écriture dans un fichier de configuration.

**B3.** Affiche HOME et PATH. Comment lancerais-tu un script `outil.sh` présent dans ton dossier actuel et absent de PATH ?

> [!success]- Afficher la correction — B3
> ```bash
> echo "$HOME"
> printf '%s\n' "$PATH"
> command -v bash
> ```
>
> On peut utiliser `./outil.sh` s’il est exécutable, ou `bash outil.sh` s’il est lisible. Ne pas retirer les répertoires existants de PATH.

---

## Partie C — Réutiliser une commande (10 min)

**C1.** Dans ton terminal interactif, retrouve une commande précédente avec les flèches puis avec Ctrl+R. Affiche les dix dernières commandes.

> [!success]- Afficher la correction — C1
> ```bash
> history 10
> ```
>
> Les commandes du script de test ne constituent pas l’historique interactif de l’élève. Cette partie s’effectue dans le terminal ouvert.

**C2.** Pourquoi une archive conservée uniquement sur le même disque n’est-elle pas une sauvegarde suffisante ?

> [!success]- Afficher la correction — C2
> Une panne ou la perte de ce disque peut supprimer les données et leur archive. Une sauvegarde doit être conservée séparément et sa restauration vérifiée.
