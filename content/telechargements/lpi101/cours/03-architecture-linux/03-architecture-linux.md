# 03. Comprendre les composants du système

> [!note] Objectif
> Situer le noyau, les pilotes, les programmes et les services.

**Repères LPI 101 :** 101.1, 101.2.

---

## Introduction

Un système Linux repose sur plusieurs **couches logicielles** qui coopèrent pour faire fonctionner l’ensemble de la machine.
Comprendre cette architecture permet de mieux saisir le rôle de chaque composant et de savoir où agir lorsqu’un problème survient.

---

## Les principales couches du système

1. **Le noyau (Kernel)**

   * C’est le cœur du système.
   * Il gère le matériel (processeur, mémoire, disques, périphériques) et assure la communication entre le matériel et les programmes.

2. **Les pilotes (Drivers)**

   * Ce sont les modules qui permettent au noyau de reconnaître et contrôler les composants matériels.
   * Ils sont souvent intégrés au noyau ou chargés dynamiquement au démarrage.

3. **Les processus et services**

   * Un **processus** est un programme en cours d’exécution.
   * Certains tournent en arrière-plan (appelés **services** ou **démons**).
   * Ils assurent des tâches continues : réseau, impression, gestion du temps, etc.

4. **Les utilisateurs et groupes**

   * Chaque action sous Linux est réalisée par un utilisateur.
   * Le compte **root** a tous les droits, les autres ont des permissions limitées.
   * Les **groupes** permettent de gérer les droits collectivement.

5. **L’espace utilisateur (User Space)**

   * C’est la partie visible pour l’utilisateur : commandes, applications, interfaces graphiques.
   * Elle utilise des bibliothèques et communique avec le noyau par des appels système.

---

## systemd et l’initialisation du système

Lors du démarrage, Linux charge le noyau puis lance un programme d’initialisation.
Aujourd’hui, c’est souvent **systemd** qui s’occupe :

* de démarrer les services,
* de gérer les sessions,
* et de contrôler l’arrêt ou le redémarrage du système.

Anciennement, ce rôle était assuré par **SysVinit**.

---

## Lire le système comme un ensemble

![Les couches de Linux : programmes et bibliothèques dans l’espace utilisateur, noyau et pilotes, puis matériel.](https://cours.kaya.ovh/lpi101/assets/course-media/b7d29b99d675ff4f.svg)

Le terminal affiche une session ; le **shell** interprète les commandes. Bash est un shell courant. Un pilote peut être intégré au noyau ou fourni comme module chargeable.

Le noyau est le passage entre les programmes et le matériel ; les services font partie de l’espace utilisateur.

## À retenir
> [!info]
> * Le **noyau** est le cœur du système et communique avec le matériel.
> * Les **pilotes** permettent la reconnaissance et le contrôle des périphériques.
> * Les **processus** exécutent les programmes et certains tournent en arrière-plan (services/démons).
> * Les **utilisateurs et groupes** définissent les droits d’accès.
> * **systemd** gère le démarrage, les services et l’arrêt du système moderne.
