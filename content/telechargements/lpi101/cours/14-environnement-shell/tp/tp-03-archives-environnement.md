# TP 03. Sauvegarder un dossier et préparer son shell

> Durée estimée : 50 min

> Chapitres associés : [13. Archiver et compresser](https://kayasam.github.io/lpi101/lpi101/13-archives-compression/), [14. Variables, environnement et historique](https://kayasam.github.io/lpi101/lpi101/14-environnement-shell/)

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


[Afficher les corrections](https://kayasam.github.io/lpi101/lpi101/14-environnement-shell/tp-corrigev2)
