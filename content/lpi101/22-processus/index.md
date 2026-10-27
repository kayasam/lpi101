---
title: "22. Observer et contrôler les processus"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/22-processus"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/22-processus/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/22-processus/22-processus.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Identifier un processus, le suspendre, le reprendre et lui demander de s’arrêter.

**Repères LPI 101 :** 103.5.

**Commandes à connaître :** `ps`, `top`, `jobs`, `bg`, `fg`, `kill`, `pgrep`, `pkill`, `nohup`.

---

## Introduction

Sous Linux, **un processus** correspond à un programme en cours d’exécution.
Les commandes externes sont exécutées dans des processus ; certaines commandes internes, comme `cd`, agissent directement dans le shell courant.
Le système permet d’en **afficher la liste**, de **contrôler leur exécution** et de **modifier leur priorité**.

Dans cette section, nous verrons :

* comment **consulter** les processus actifs ;
* comment **contrôler** leur exécution (arrêter, suspendre, relancer) ;
* comment **ajuster la priorité** d’un processus.

---

![Un shell parent et des processus enfants au premier plan ou en arrière-plan.](https://cours.kaya.ovh/lpi101/assets/course-media/ff5c6977d2387ca5.svg)

## Consulter les processus

## `ps` — afficher les processus en cours

La commande `ps` affiche les processus associés à la session courante.

Exemples :

```bash
ps
```

Affiche les processus lancés depuis le même terminal.

```bash
ps -ef
```

Affiche **tous les processus** du système avec plus d’informations :

* UID : utilisateur propriétaire du processus
* PID : identifiant du processus
* PPID : identifiant du processus parent
* CMD : commande lancée

Rechercher un processus particulier :

```bash
ps -ef | grep ssh
```

---

## `top` — surveiller les processus en temps réel

`top` affiche la liste des processus triés par utilisation CPU ou mémoire.

```bash
top
```

Touches utiles :

* `q` → quitter
* `P` → trier par utilisation CPU
* `M` → trier par utilisation mémoire
* `k` → tuer un processus (demande le PID)

---

## `htop` — vue améliorée

`htop` est une version plus lisible et interactive de `top`.
Il affiche les processus sous forme de tableau coloré et permet la navigation au clavier.

Installer (si nécessaire) :

```bash
sudo apt install htop
```

Lancer :

```bash
htop
```

---

## Contrôle des processus

Chaque processus a un **PID (Process ID)** unique.
On peut suspendre, mettre en arrière-plan ou arrêter un processus.

## Lancer un processus en arrière-plan

Ajouter `&` à la fin d’une commande :

```bash
gedit &
```

Le programme se lance en arrière-plan et rend la main au terminal.

Lister les tâches du terminal :

```bash
jobs
```

Ramener une tâche en avant-plan :

```bash
fg %1
```

Renvoyer une tâche en arrière-plan :

```bash
bg %1
```

---

## `kill` — terminer un processus

La commande `kill` envoie un signal à un processus.

Exemples :

```bash
kill 1234
```

(envoie par défaut le signal `SIGTERM` pour demander l’arrêt proprement)

Forcer l’arrêt d’un processus bloqué :

```bash
kill -9 1234
```

(`-9` correspond au signal `SIGKILL` — arrêt immédiat sans nettoyage)

Envoyer un signal aux processus correspondant à un nom :

```bash
pkill firefox
```

---

## Suspendre et reprendre une tâche

```bash
sleep 300
```

Pendant l’attente, **Ctrl+Z** suspend la tâche. Puis saisir :

```bash
jobs
bg %1
fg %1
```

Adapter `%1` au numéro affiché par `jobs`. `bg` reprend une tâche suspendue en arrière-plan ; `fg` la place au premier plan. Terminer le `sleep` au premier plan avec **Ctrl+C**. Un numéro de tâche du shell n’est pas un PID.

## Laisser une commande continuer après la déconnexion

```bash
nohup sleep 300 > attente.log 2>&1 &
echo $!
```

`nohup` fait ignorer le signal de déconnexion SIGHUP et `&` rend la main au terminal. `$!` affiche le PID du dernier processus lancé en arrière-plan. Cela ne protège pas d’un arrêt de la machine ni d’une politique de session qui termine les processus.

## Retrouver un processus

```bash
pgrep -a sleep
ps -eo pid,ppid,user,stat,ni,comm --sort=comm
```

`pgrep` recherche par nom ; `pkill` envoie un signal aux processus correspondant au nom. Vérifier la sélection avant d’agir. Les multiplexeurs `screen` et `tmux` permettent de détacher puis retrouver une session de terminal ; leur utilisation détaillée reste un prolongement.

## À retenir

> [!tip]
> Ctrl+C demande une interruption ; Ctrl+Z suspend ; `bg` reprend en arrière-plan ; `fg` ramène au premier plan. Préférer une demande d’arrêt normale à `kill -9`.
