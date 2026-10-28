# TP 10. Observer la machine et dépanner un service

> Durée estimée : 70 min

> Chapitres associés : [33. Identifier le matériel et les modules du noyau](https://kayasam.github.io/lpi101/lpi101/33-materiel-modules/), [34. Observer les événements matériels](https://kayasam.github.io/lpi101/lpi101/34-evenements-materiels/), [35. Démarrage, arrêt et cibles systemd](https://kayasam.github.io/lpi101/lpi101/35-demarrage-arret/), [36. Gérer les services avec systemd](https://kayasam.github.io/lpi101/lpi101/36-services/), [37. Consulter les journaux et diagnostiquer](https://kayasam.github.io/lpi101/lpi101/37-journaux/), [38. Comprendre GRUB et la récupération](https://kayasam.github.io/lpi101/lpi101/38-grub-recuperation/)

---

## Objectifs

- Observer ressources et messages du démarrage.
- Distinguer service actif et service activé.
- Utiliser les journaux pour expliquer une panne simple.

## Avant de commencer

Le TP crée ses propres unités systemd et ne coupe pas SSH. Les changements de cible, redémarrages et manipulations de GRUB se font uniquement à la console avec le formateur ; ils ne sont pas nécessaires pour l’atelier distant.

---

## Partie A — Observer le système (15 min)

**A1.** Affiche les informations CPU, la mémoire et les disques ; explique pourquoi la vue matérielle d’une VM diffère de celle du PC hôte.

**A2.** Consulte les derniers messages du noyau et les paramètres de son lancement.

**A3.** Affiche la cible de démarrage par défaut et quelques services en cours. Quelle différence entre cible et service ?

---

## Partie B — Créer un service de démonstration (20 min)

**B1.** Crée le fichier `/etc/systemd/system/lpi101-demo.service` avec le modèle ci-dessous, puis recharge la configuration de systemd. À quoi servent les trois sections ?

```ini
[Unit]
Description=Service de demonstration LPI 101

[Service]
Type=oneshot
ExecStart=/usr/bin/echo TP-LPI101-demarrage-reussi
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

Utilise un éditeur avec les droits nécessaires. Les commandes pour créer le fichier et recharger systemd restent à trouver.

**B2.** Démarre ce service, vérifie qu’il est actif puis vérifie s’il est déjà activé au démarrage.

**B3.** Active-le pour le démarrage puis arrête-le. Est-il toujours activé ? Redémarre-le pour la suite.

---

## Partie C — Lire une panne (20 min)

**C1.** Retrouve le message du service dans ses journaux, puis limite la recherche au démarrage courant.

**C2.** Crée le fichier `/etc/systemd/system/lpi101-echec.service` avec le modèle ci-dessous. Recharge la configuration de systemd, tente de démarrer cette unité, puis cherche la cause de l’échec dans les journaux.

```ini
[Unit]
Description=Panne volontaire du TP LPI101
[Service]
Type=oneshot
ExecStart=/usr/bin/false
```

**C3.** Comment distinguer un problème du démarrage Linux et celui de cette seule unité ? Où GRUB intervient-il ?

---

## Partie D — Nettoyer (15 min)

**D1.** Désactive et arrête le service de démonstration. Efface l’état d’échec de l’unité volontairement défaillante, retire seulement les deux fichiers d’unité créés pour ce TP, puis recharge la configuration de systemd.
