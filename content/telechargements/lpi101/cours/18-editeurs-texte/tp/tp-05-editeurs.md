# TP 05. Modifier une petite configuration

> Durée estimée : 35 min

> Chapitres associés : [18. Modifier un fichier avec nano et vi](https://kayasam.github.io/lpi101/lpi101/18-editeurs-texte/)

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

**A2.** Remplace le port par `9090`, ajoute `responsable=stagiaire`, enregistre et quitte.

**A3.** Vérifie depuis Bash les lignes enregistrées. La sauvegarde a-t-elle changé ?

---

## Partie B — Éditer avec vi (15 min)

**B1.** Copie le fichier obtenu dans `application-vi.conf`, puis ouvre la copie avec vi.

**B2.** Cherche `mode`, remplace `test` par `production`, puis enregistre et quitte.

**B3.** Rouvre le fichier, supprime la ligne `responsable`, puis annule cette suppression avant de quitter sans enregistrer.

---

## Partie C — Vérifier et choisir (5 min)

**C1.** Affiche le fichier final et choisis nano comme éditeur pour cette session. Ces variables modifient-elles le fichier de configuration ?
