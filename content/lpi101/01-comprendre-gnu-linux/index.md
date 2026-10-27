---
title: "01. Comprendre GNU/Linux et le logiciel libre"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/01-comprendre-gnu-linux"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://cours.kaya.ovh/lpi101/lpi101/01-comprendre-gnu-linux/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://cours.kaya.ovh/lpi101/telechargements/lpi101/cours/01-comprendre-gnu-linux/01-comprendre-gnu-linux.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Distinguer noyau, système et logiciel libre ; comprendre les origines de Linux.

---

> [!tip]
> Hedgedoc complet sur l'histoire de Linux par  Bastien TRAVERSE
> - https://hedgedoc.dawan.fr/01dOettVSr63m4VojmMegA

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/Za6vGTLp-wg?si=ueYYRHLvkhvoIrtB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
## Introduction

Avant d’utiliser Linux, il est essentiel d’en comprendre l’origine, la philosophie et ce qui le distingue des autres systèmes d’exploitation.
Linux n’est pas seulement un logiciel : c’est un **écosystème** basé sur la **liberté**, la **collaboration** et la **transparence**.

---

## Historique de GNU/Linux

Dans les années 1980, **Richard Stallman** lance le projet **GNU** (GNU’s Not Unix) avec un objectif clair : créer un système d’exploitation libre, compatible avec Unix, où **tout le monde peut lire, modifier et redistribuer le code**.

Cependant, le projet GNU n’avait pas de noyau fonctionnel.
En 1991, **Linus Torvalds**, un étudiant finlandais, publie les premières versions du noyau **Linux**. Linux adopte la licence GNU GPL en 1992.

L’association du projet GNU et du noyau Linux donnera naissance à ce qu’on appelle souvent **GNU/Linux**.

---

## Pourquoi Linux ?

Linux s’est imposé grâce à plusieurs avantages :

* **Stabilité et fiabilité** : utilisé sur la majorité des serveurs web, routeurs, systèmes embarqués…
* **Sécurité** : structure des permissions stricte et mises à jour rapides.
* **Performance** : léger, optimisable et capable de tourner sur de vieilles machines.
* **Flexibilité** : adapté à tous les usages — serveur, poste de travail, embarqué, cloud, etc.
* **Gratuit et libre** : la plupart des distributions sont entièrement gratuites.

Aujourd’hui, Linux est partout :
dans les serveurs, les téléphones Android, les box internet, les voitures et même les supercalculateurs.

---

## Comparaison avec Windows et macOS

| Caractéristique      | Linux                  | Windows           | macOS            |
| -------------------- | ---------------------- | ----------------- | ---------------- |
| **Licence**          | Libre et gratuit       | Propriétaire      | Propriétaire     |
| **Code source**      | Ouvert                 | Fermé             | Fermé            |
| **Sécurité** | Dépend des mises à jour, de la configuration et des usages | Même principe | Même principe |
| **Performances** | Dépendent du matériel et de la charge | Même principe | Même principe |
| **Utilisation**      | Serveurs, dev, réseaux | Bureautique, jeux | Création, design |
| **Personnalisation** | Très élevée            | Limitée           | Faible           |
| **Écosystème** | Communautés et entreprises | Éditeur, partenaires et communautés | Éditeur, partenaires et communautés |

---

## Philosophie du Libre

Le **logiciel libre** ne signifie pas “gratuit” mais “libre d’utilisation”.
La **Free Software Foundation (FSF)**, fondée par Richard Stallman, définit **4 libertés fondamentales** :

1. La liberté d’**exécuter** le programme pour tout usage.
2. La liberté d’**étudier et modifier** son fonctionnement, avec accès au code source.
3. La liberté de **redistribuer des copies**.
4. La liberté de **distribuer des versions modifiées**, avec accès au code source.

Ces principes garantissent une **autonomie technologique** et favorisent l’innovation collective.

---

## L’Open Source Initiative (OSI)

Dans les années 1990, certains acteurs ont voulu rendre le concept plus “entrepreneurial”.
L’**Open Source Initiative (OSI)** reprend les mêmes principes, mais avec une approche **plus pragmatique** et orientée vers les entreprises.

Ainsi, “**logiciel libre**” (Free Software) et “**Open Source**” désignent souvent la même chose, mais avec **deux philosophies différentes** :

* **Libre** → liberté de l’utilisateur (philosophie éthique)
* **Open Source** → efficacité et transparence (philosophie pragmatique)

---

> [!tip]
>
>
> **Questions interactives**
>
> 1. **Vrai ou faux :**
>    Linux a été créé par Richard Stallman.
>
>    > 💡 *Indice : Stallman a fondé le projet GNU, mais pas le noyau.*
>
> 2. Quelle est la différence principale entre “logiciel libre” et “open source” ?
>
>    > 💡 *Une réponse en une phrase suffit.*
>
> 3. Donne un **exemple d’utilisation** de Linux dans la vie quotidienne (hors serveur).
>
> 4. Pourquoi penses-tu que les entreprises préfèrent souvent utiliser Linux sur leurs serveurs plutôt que Windows ?

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/pyXYRkB1v28?si=mbDfUuFt3RgxD7sy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## À retenir
> [!info]
>
>
> - Linux est né de la rencontre entre le projet **GNU** et le noyau créé par **Linus Torvalds**.
>
> - C’est un système **libre, ouvert et collaboratif**.
>
> - La **Free Software Foundation (FSF)** et l’**Open Source Initiative (OSI)** défendent deux visions complémentaires du logiciel libre.
>
> - Linux domine aujourd’hui les **serveurs**, le **cloud** et les **systèmes embarqués**.
>
