---
title: "TP 07 — Piloter des tâches dans son terminal"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/23-priorites"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/23-priorites/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/23-priorites/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/tp/23-priorites.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


> Durée estimée : 50 min

> Chapitres associés : [22 — Observer et contrôler les processus](https://kayasam.github.io/lpi101/lpi101/22-processus/), [23 — Comprendre les priorités des processus](https://kayasam.github.io/lpi101/lpi101/23-priorites/)

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
