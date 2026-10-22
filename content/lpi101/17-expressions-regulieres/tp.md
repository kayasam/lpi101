---
title: "TP 04 — Analyser un petit journal de support"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/17-expressions-regulieres"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/17-expressions-regulieres/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/17-expressions-regulieres/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/tp/17-expressions-regulieres.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


> Durée estimée : 75 min

> Chapitres associés : [15 — Flux, redirections et tubes](https://kayasam.github.io/lpi101/lpi101/15-flux-redirections/), [16 — Filtrer et transformer du texte](https://kayasam.github.io/lpi101/lpi101/16-filtres-textuels/), [17 — Rechercher avec les expressions régulières](https://kayasam.github.io/lpi101/lpi101/17-expressions-regulieres/)

---

## Objectifs

- Séparer sortie standard et erreur.
- Combiner les filtres pour produire un rapport.
- Distinguer recherche simple, regex et joker.

## Avant de commencer

Le jeu de données est volontairement petit pour pouvoir vérifier les résultats à la main. La ligne d’en-tête ne compte pas comme un ticket.

**Préparation fournie :**

```bash
mkdir -p ~/lpi101-tp/tp04
cd ~/lpi101-tp/tp04
cat > tickets.csv <<'EOF'
id;service;niveau;etat
101;web;INFO;clos
102;ssh;ERROR;ouvert
103;web;WARNING;ouvert
104;dns;ERROR;ouvert
105;ssh;INFO;clos
106;web;ERROR;ouvert
EOF
```

---

## Partie A — Comprendre les flux (20 min)

**A1.** Enregistre les noms de `/etc` dans `liste.txt`, puis ajoute les noms de `/var/log` à la fin. Vérifie quelques lignes.

**A2.** Provoque une erreur avec `ls` sur `absent-lpi101`, sépare les résultats et erreurs dans deux fichiers, puis vérifie le code retour immédiatement.

**A3.** Envoie cette fois la sortie et l’erreur dans `ensemble.txt`. Pourquoi l’ordre des redirections compte-t-il ?

---

## Partie B — Construire le rapport (30 min)

**B1.** Affiche seulement les tickets de niveau ERROR et compte-les, sans compter l’en-tête.

**B2.** Affiche les services sans l’en-tête, trie-les et compte les occurrences de chacun.

**B3.** Enregistre les tickets ouverts dans `ouverts.csv` tout en les affichant à l’écran.

**B4.** Avec awk, affiche seulement le numéro et le service des tickets ERROR.

---

## Partie C — Motifs et transformations (25 min)

**C1.** Avec une expression étendue, affiche les tickets web ou ssh. Pourquoi `web*` n’exprime-t-il pas « tout le texte qui commence par web » dans une regex ?

**C2.** Remplace `ouvert` par `a_traiter` à l’affichage, sans modifier le fichier source. Vérifie ensuite que le fichier contient toujours `ouvert`.

**C3.** Transmets les deux noms `sortie.txt` et `erreurs.txt` à `wc -l` avec xargs. Quel est son rôle par rapport au tube ?
