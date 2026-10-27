# TP 05. Modifier une petite configuration — Correction

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
