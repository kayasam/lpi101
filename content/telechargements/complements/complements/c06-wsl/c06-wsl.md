# C06. Découvrir Linux sous Windows avec WSL

> [!note] Objectif
> Reconnaître les possibilités de WSL et ses différences avec la VM de formation.

> [!info] Complément
> À découvrir après les bases, selon le rythme du groupe.

---

## Introduction

**WSL (Windows Subsystem for Linux)** permet d’exécuter une distribution Linux directement sous Windows, avec une intégration forte à Windows ; WSL 2 utilise une machine virtuelle légère gérée par Windows.
C’est une solution légère et intégrée qui offre un véritable environnement Linux pour le développement, l’administration ou la formation.

> **Sources officielles :**
>
> - [Documentation officielle Microsoft WSL](https://learn.microsoft.com/fr-fr/windows/wsl/)
>
> - [Tutoriels WSL sur IT-Connect](https://www.it-connect.fr/cours-tutoriels/administration-systemes/windows-client/tutos-wsl/)
>

---

## Présentation générale

WSL offre une compatibilité entre le noyau Windows et Linux.
Deux versions existent :

|Version|Description|
|---|---|
|**WSL 1**|Traduit les appels système Linux vers le noyau Windows. Plus rapide pour les opérations sur fichiers Windows.|
|**WSL 2**|Utilise un vrai noyau Linux dans une machine virtuelle optimisée. Large compatibilité des appels système ; réseau selon la configuration Windows/WSL.|

Sur une version compatible de Windows, `wsl --install` permet d’installer les composants nécessaires. WSL n’est pas nécessairement déjà installé sur le poste.

---

## Installation de WSL

Ouvre **PowerShell en administrateur** et lance :

```powershell
wsl --install
```

Cette commande :

- active les composants nécessaires ;

- installe WSL 2 ;

- télécharge la dernière distribution Ubuntu.

Vérifie ensuite l’état :

```powershell
wsl --status
```

> [!danger]
> **Attention à la compatibilité avec VirtualBox**
>
> Depuis **WSL 2**, Windows active la technologie de virtualisation **Hyper-V**.
> Or, **VirtualBox** et **Hyper-V** utilisent toutes deux la même couche de virtualisation matérielle (VT-x/AMD-V).
> Cela peut provoquer des lenteurs importantes, voire empêcher le démarrage des machines VirtualBox.

---

## Gestion des distributions

Lister les distributions disponibles :

```powershell
wsl --list --online
```

Installer une distribution spécifique :

```powershell
wsl --install -d Debian
```

Lister les distributions installées :

```powershell
wsl --list --verbose
```

Exemple :

```text
  NAME      STATE           VERSION
* Ubuntu    Running         2
  Debian    Stopped         2
```

---
> [!info]
> On peut aussi passer par le Microsoft store pour installer une distribution linux
> ![10.2 WSL — Linux sous Windows-1](https://cours.kaya.ovh/lpi101/assets/course-media/5e208c7e7b969f0e.png)

## Commandes de gestion

|Action|Commande|
|---|---|
|Démarrer une distribution|`wsl -d Debian`|
|Changer la version|`wsl --set-version Debian 2`|
|Définir WSL 2 par défaut|`wsl --set-default-version 2`|
|Arrêter toutes les distributions|`wsl --shutdown`|
|Exporter une distribution|`wsl --export Debian D:\Sauvegarde\debian.tar`|
|Importer une sauvegarde|`wsl --import Debian D:\WSL\Debian D:\Sauvegarde\debian.tar --version 2`|

---

## Accès aux fichiers

Sous WSL, les disques Windows sont montés automatiquement dans `/mnt/` :

|Disque Windows|Emplacement sous Linux|
|---|---|
|`C:\`|`/mnt/c/`|
|`D:\`|`/mnt/d/`|

Exemple :

```bash
cd /mnt/c/Users
ls
```

Pour accéder aux fichiers Linux depuis Windows, utiliser `explorer.exe .` depuis WSL ou le partage `\\wsl$` / `\\wsl.localhost`. Ne pas modifier directement les fichiers internes du disque virtuel de la distribution dans les dossiers système de Windows.

---

## Intégration Windows ↔ Linux

|Fonction|Exemple|
|---|---|
|Exécuter une commande Linux depuis PowerShell|`wsl ls -l /home`|
|Exécuter une commande Windows depuis Linux|`explorer.exe .`|
|Ouvrir VS Code dans le dossier courant|`code .`|
|Partage du presse-papier et du réseau|Automatique sous WSL 2|

---

## Gestion des ressources

Les ressources utilisées par WSL 2 peuvent être ajustées avec le fichier de configuration suivant :

Chemin :
`C:\Users\<nom>\.wslconfig`

Exemple :

```ini
[wsl2]
memory=4GB
processors=2
swap=0
```

Appliquer les changements :

```powershell
wsl --shutdown
```

> [!info]
> Il y a une interface graphique `WSL Settings`
> ![10.2 WSL — Linux sous Windows](https://cours.kaya.ovh/lpi101/assets/course-media/02e412ac13c1f863.png)

---

## Bonnes pratiques

- Préférer **WSL 2** pour une large compatibilité avec les outils Linux.

- Accéder aux fichiers Linux par les mécanismes prévus : `explorer.exe .` ou le partage WSL.

- Utiliser WSL pour les tests et scripts ; garder la VM Debian commune pour les exercices de démarrage et de stockage.

- Choisir WSL, une VM ou un serveur selon la tâche ; ils ne présentent pas tous le même matériel ni le même démarrage.

---

## À retenir
> [!tip]
> - WSL offre un environnement Linux complet directement dans Windows.
>
> - WSL 2 repose sur un vrai noyau Linux et peut utiliser systemd et des outils de conteneurs, selon les versions et la configuration.
>
> - Les fichiers Windows sont accessibles sous `/mnt/`.
>
> - Idéal pour pratiquer Linux sans installation complète.
