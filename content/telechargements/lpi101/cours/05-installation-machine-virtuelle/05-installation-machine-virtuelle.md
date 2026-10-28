# 05. Installer Debian dans une machine virtuelle

> [!note] Objectif
> Créer une VM de formation, installer Debian et comprendre son environnement.

**Repères LPI 101 :** 102.6.

---

## Créer une machine virtuelle sous VirtualBox

VirtualBox permet d’exécuter une machine virtuelle (VM) Linux dans un environnement isolé sur ton ordinateur.
Cela évite de modifier le système principal.

## Étapes de création :

1. **Nom et type :** choisis un nom (ex. _Debian-LPI_) et sélectionne

    - Type : **Linux**

    - Version : **Debian (64-bit)**

2. **Mémoire vive (RAM) :**
    Alloue **2 à 4 Go** selon ta configuration.

3. **Processeur (CPU) :**
    Minimum **2 cœurs**, idéalement **4** pour de meilleures performances.

4. **Disque dur virtuel :**

    - Type : VDI (VirtualBox Disk Image)

    - Taille dynamique

    - Taille : **20 à 40 Go**

5. **Réseau :**

    - **NAT** : pour accéder à Internet depuis la VM

    - **Host-Only** : pour communiquer avec la machine hôte sans accès Internet

    - Les deux peuvent être combinés pour des scénarios plus avancés (NAT + Host-Only).

---

## Étapes de l’installation Debian

Une fois la VM créée, démarre-la en sélectionnant ton **image ISO Debian** (NetInstall, DVD, etc.).

Installation en images : [Debian 13 trixie : Install : Server World](https://www.server-world.info/en/note?os=Debian_13&p=install)
## Déroulement de l’installation (mode graphique ou texte) :

1. **Langue et disposition du clavier**

2. **Nom de la machine** (hostname)

3. **Configuration du réseau**

    - DHCP automatique (recommandé en NAT)

    - Ou configuration manuelle (IP fixe, DNS, passerelle)

4. **Création des utilisateurs :**

    - **root** (administrateur)

    - **utilisateur standard**

5. **Partitionnement du disque :**

    - Automatique recommandé pour débuter

    - Possibilité de séparer `/home`, `/var`,  si besoin

6. **Sélection des paquets :**

    - **Environnement graphique** (GNOME, XFCE, etc.)

    - **Utilitaires standard du système**

    - Serveur SSH (optionnel mais utile pour l’administration à distance)

7. **Installation du chargeur GRUB** sur le disque principal.

Une fois l’installation terminée, la machine redémarre sur Debian.

---

## Configuration réseau de la VM

|Type d’adaptateur|Description|Utilisation|
|---|---|---|
|**NAT**|La VM accède à Internet via la machine hôte.|Téléchargements, mises à jour.|
|**Host-Only**|Réseau interne entre l’hôte et la VM.|Tests et échanges de fichiers locaux.|
|**Bridged (pont)**|La VM est visible sur le réseau local.|Cas avancés ou tests réseau.|

---

## Hôte, invité et hyperviseur

L’**hôte** est l’ordinateur physique et son système ; l’**invité** est le système installé dans la VM. L’hyperviseur partage les ressources du matériel entre les invités.

Un hyperviseur de **type 1** s’exécute directement sur le matériel ; un **type 2**, comme VirtualBox dans ce cours, fonctionne au-dessus d’un système hôte. Hyper-V utilise une architecture de type 1 même sur un poste Windows.

![DR02.Hyperviseur-Type](https://kayasam.github.io/lpi101/assets/course-media/dr02-hyperviseur-type.svg)

## Instantané et clone

Un **instantané** aide à revenir à un état précédent avant une manipulation. Un **clone** crée une autre VM. Un instantané stocké avec le disque virtuel ne remplace pas une sauvegarde indépendante.

Après un clone destiné à devenir une nouvelle machine, vérifier le nom d’hôte, l’adresse MAC, l’adressage IP, l’identité système et les clés d’hôte SSH. Les outils de clonage et de préparation d’images peuvent prendre en charge une partie de cette régénération.

## VM, conteneur et cloud

| Élément | Idée à retenir |
|---|---|
| VM | Possède son propre noyau et ses disques virtuels. |
| Conteneur Linux | Partage le noyau de l’hôte Linux ; isole des processus et leur environnement. |
| Instance IaaS | Machine fournie à la demande avec réseau et volumes de stockage. |
| Image cloud | Modèle de système prêt à être instancié, souvent initialisé par Cloud-init. |

Pour la formation, conserver une VM Debian comme environnement commun. Le complément Cloud-init montre ensuite un exemple d’initialisation automatisée.

## À retenir
> [!info]
> - Créer une **VM VirtualBox** permet d’installer Linux sans modifier son PC.
> - Allouer environ **2–4 Go de RAM** et **20–40 Go de disque**.
> - Utiliser un réseau **NAT** pour Internet et **Host-Only** pour le lien local.
> - Suivre les étapes de l’installateur Debian : langue, réseau, utilisateurs, partitions, paquets.
> - Installer **GRUB** pour permettre le démarrage du système.
>
