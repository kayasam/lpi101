# TP 07. Piloter des tâches dans son terminal

> Durée estimée : 50 min

> Chapitres associés : [22. Observer et contrôler les processus](https://cours.kaya.ovh/lpi101/lpi101/22-processus/), [23. Comprendre les priorités des processus](https://cours.kaya.ovh/lpi101/lpi101/23-priorites/)

---

## Objectifs

- Distinguer PID, tâche du shell et processus parent.
- Suspendre, reprendre et arrêter une tâche.
- Lire et modifier une priorité sans lancer de charge lourde.

## Avant de commencer

Utilise un compte standard dans la VM Debian. Les parties se suivent dans le même terminal.

**Préparation fournie :**

```bash
mkdir -p ~/lpi101-tp/tp07
cd ~/lpi101-tp/tp07
```

---

## Partie A — Observer une tâche (15 min)

**A1.** Lance `sleep 600` en arrière-plan, mémorise son PID dans `pid_tp`, puis affiche ses informations et la liste des tâches.

**A2.** Retrouve les processus sleep par leur nom. Pourquoi ne faut-il pas arrêter tous ces résultats sans les vérifier ?

---

## Partie B — Suspendre et arrêter (20 min)

**B1.** Suspends la tâche par un signal STOP, observe son état, puis reprends-la par CONT.

**B2.** Dans un terminal interactif, lance un second sleep au premier plan ; suspends-le avec Ctrl+Z, reprends-le avec bg, ramène-le avec fg puis termine-le avec Ctrl+C.

**B3.** Demande l’arrêt normal de la première tâche, puis vérifie sa disparition.

---

## Partie C — Priorité et déconnexion (15 min)

**C1.** Lance un sleep avec une niceness augmentée de 10, lis sa valeur NI puis rends-le encore moins prioritaire avec NI 15.

**C2.** Lance une tâche de cinq minutes avec nohup en redirigeant son résultat, mémorise son PID puis arrête-la après vérification.
