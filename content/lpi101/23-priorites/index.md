---
title: "23. Comprendre les priorités des processus"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/23-priorites"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/23-priorites/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/23-priorites/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/23-priorites/23-priorites.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Lire la valeur de niceness et diminuer la priorité d’une tâche coûteuse.

**Repères LPI 101 :** 103.6.

**Commandes à connaître :** `nice`, `renice`, `ps`.

---

## Priorité des processus

Tous les processus ont une **priorité d’exécution**.
Plus la priorité est élevée, plus le processus obtient du temps CPU.
Sous Linux, cette priorité est définie par une valeur appelée **“niceness”**.

## `nice` — lancer un processus avec une priorité donnée

Les valeurs possibles vont de **-20 (plus prioritaire)** à **19 (moins prioritaire)**.
La valeur par défaut est **0**.

Lancer un processus avec une priorité basse :

```bash
nice -n 10 commande
```

Exemple :

```bash
nice -n 10 tar -czf sauvegarde.tar.gz /home
```

---

## `renice` — modifier la priorité d’un processus existant

Changer la priorité d’un processus en cours :

```bash
sudo renice -n 5 -p 1234
```

Affiche la priorité actuelle et la modifie si autorisé.
Augmenter la priorité demande des autorisations adaptées ; le cas courant est une commande lancée avec les privilèges administrateur.

---

## Lire la valeur NI

```bash
nice -n 10 sleep 300 &
pid_tache=$!
ps -o pid,ni,comm -p "$pid_tache"
renice -n 15 -p "$pid_tache"
kill "$pid_tache"
```

Pour les tâches ordinaires, une valeur NI plus élevée correspond à une moindre priorité relative. L’effet apparaît surtout lorsque des tâches se disputent le CPU ; ce réglage ne fixe pas un pourcentage de processeur. Les enfants héritent normalement de la niceness du parent. `nice -n 10` ajoute 10 à la valeur héritée ; `renice -n 15` fixe ici la valeur à 15.

## À retenir

> [!tip]
> Sans autorisation particulière, un utilisateur peut généralement rendre ses tâches moins prioritaires. Abaisser la valeur NI pour augmenter leur priorité demande des privilèges ou des limites adaptées.
