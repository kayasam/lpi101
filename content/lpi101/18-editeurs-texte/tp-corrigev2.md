---
title: "TP 05. Modifier une petite configuration — Correction"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/18-editeurs-texte"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/18-editeurs-texte/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://cours.kaya.ovh/lpi101/lpi101/18-editeurs-texte/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/18-editeurs-texte/tp/tp-05-editeurs-correction.md">↓ Télécharger le corrigé (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://cours.kaya.ovh/lpi101/lpi101/18-editeurs-texte/tp">Énoncé</a><a class="exercise-correction" href="https://cours.kaya.ovh/lpi101/lpi101/18-editeurs-texte/tp-corrigev2" aria-current="page">Corrigé</a></nav>

> Essaie chaque question avant d’ouvrir **Afficher la correction**. Chaque réponse se replie indépendamment.

> Durée estimée : 35 min

> Chapitres associés : [18. Modifier un fichier avec nano et vi](https://cours.kaya.ovh/lpi101/lpi101/18-editeurs-texte/)

---

## Objectifs

- Enregistrer et quitter nano.
- Passer du mode normal au mode insertion dans vi.
- Rechercher, corriger et annuler dans un fichier de laboratoire.

## Avant de commencer

Les touches se pratiquent dans le terminal de la VM. Les lignes marquées comme commandes se tapent dans Bash ; les touches indiquées pour l’éditeur se tapent dans cet éditeur. Installe les outils si nécessaire : `sudo apt update`, puis `sudo apt install nano vim`.

**Préparation fournie :**

```bash
mkdir -p ~/lpi101-tp/tp05
cd ~/lpi101-tp/tp05
printf 'service=demo\nport=8080\nmode=test\n' > application.conf
```

---

## Partie A — Éditer avec nano (15 min)

**A1.** Fais une copie de sauvegarde du fichier, puis ouvre `application.conf` avec nano.

> [!success]- Afficher la correction — A1
> ```bash
> cp application.conf application.conf.bak
> nano application.conf
> ```
>
> La copie permet de comparer ou restaurer. Le contrôle automatisé vérifie les fichiers, mais pas les frappes dans l’interface.

**A2.** Remplace le port par `9090`, ajoute `responsable=stagiaire`, enregistre et quitte.

> [!success]- Afficher la correction — A2
> Dans nano : modifier le texte, Ctrl+O, Entrée pour confirmer le nom, puis Ctrl+X. Le fichier doit conserver `service=demo` et `mode=test`.

**A3.** Vérifie depuis Bash les lignes enregistrées. La sauvegarde a-t-elle changé ?

> [!success]- Afficher la correction — A3
> ```bash
> cat application.conf
> cat application.conf.bak
> ```
>
> La sauvegarde contient toujours le port 8080 et n’a pas la nouvelle ligne. Le fichier de travail doit avoir le port 9090.

---

## Partie B — Éditer avec vi (15 min)

**B1.** Copie le fichier obtenu dans `application-vi.conf`, puis ouvre la copie avec vi.

> [!success]- Afficher la correction — B1
> ```bash
> cp application.conf application-vi.conf
> vi application-vi.conf
> ```
>
> Dans le mode normal, les touches sont des commandes. `i` passe en insertion ; Échap revient au mode normal.

**B2.** Cherche `mode`, remplace `test` par `production`, puis enregistre et quitte.

> [!success]- Afficher la correction — B2
> Taper `/mode`, Entrée ; se placer sur le mot, utiliser `cw`, saisir `production`, Échap, puis `:wq`, Entrée. La recherche et les déplacements se font en mode normal.

**B3.** Rouvre le fichier, supprime la ligne `responsable`, puis annule cette suppression avant de quitter sans enregistrer.

> [!success]- Afficher la correction — B3
> En mode normal : `/responsable`, Entrée, `dd`, puis `u`. Quitter avec `:q!`. La version enregistrée doit toujours contenir la ligne responsable.

---

## Partie C — Vérifier et choisir (5 min)

**C1.** Affiche le fichier final et choisis nano comme éditeur pour cette session. Ces variables modifient-elles le fichier de configuration ?

> [!success]- Afficher la correction — C1
> ```bash
> cat application-vi.conf
> export EDITOR=nano
> export VISUAL=nano
> ```
>
> Non, les variables influencent les programmes qui les consultent. Elles n’éditent pas les fichiers déjà existants.
