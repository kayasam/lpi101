---
title: "03. Comprendre les composants du système"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/03-architecture-linux"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/03-architecture-linux/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/03-architecture-linux/03-architecture-linux.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

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
   * Elle repose sur les bibliothèques et services fournis par le noyau.

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

```text
Utilisateur → terminal / applications → bibliothèques → noyau → matériel
                         services ↗
```

Le terminal affiche une session ; le **shell** interprète les commandes. Bash est un shell courant. Un pilote peut être intégré au noyau ou fourni comme module chargeable.

Schéma du cours : ![DR01.BIOS-GRUB-ARCHI](https://kayasam.github.io/lpi101/assets/course-media/dr01-bios-grub-archi.svg)

## À retenir
> [!info]
> * Le **noyau** est le cœur du système et communique avec le matériel.
> * Les **pilotes** permettent la reconnaissance et le contrôle des périphériques.
> * Les **processus** exécutent les programmes et certains tournent en arrière-plan (services/démons).
> * Les **utilisateurs et groupes** définissent les droits d’accès.
> * **systemd** gère le démarrage, les services et l’arrêt du système moderne.
