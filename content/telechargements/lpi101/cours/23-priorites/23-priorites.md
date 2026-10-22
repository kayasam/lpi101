# 23. Comprendre les priorités des processus

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
