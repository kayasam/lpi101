---
title: "TP 10. Observer la machine et dépanner un service"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/38-grub-recuperation"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/38-grub-recuperation/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/38-grub-recuperation/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/38-grub-recuperation/tp/tp-10-machine-services-journaux.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://kayasam.github.io/lpi101/lpi101/38-grub-recuperation/tp" aria-current="page">Énoncé</a><a class="exercise-correction" href="https://kayasam.github.io/lpi101/lpi101/38-grub-recuperation/tp-corrigev2">Afficher les corrections</a></nav>

> Durée estimée : 85 min

> Chapitres associés : [33. Identifier le matériel et les modules du noyau](https://kayasam.github.io/lpi101/lpi101/33-materiel-modules/), [34. Observer les événements matériels](https://kayasam.github.io/lpi101/lpi101/34-evenements-materiels/), [35. Démarrage, arrêt et cibles systemd](https://kayasam.github.io/lpi101/lpi101/35-demarrage-arret/), [36. Gérer les services avec systemd](https://kayasam.github.io/lpi101/lpi101/36-services/), [37. Consulter les journaux et diagnostiquer](https://kayasam.github.io/lpi101/lpi101/37-journaux/), [38. Comprendre GRUB et la récupération](https://kayasam.github.io/lpi101/lpi101/38-grub-recuperation/)

---

## Objectifs

- Observer ressources et messages du démarrage.
- Distinguer service actif et service activé.
- Utiliser les journaux pour expliquer une panne simple.
- Automatiser une sauvegarde avec un timer systemd.

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

## Partie D — Automatiser une sauvegarde avec un timer (20 min)

**D1.** Crée le script `/usr/local/bin/lpi101-sauvegarde.sh` avec le modèle ci-dessous, rends-le exécutable puis lance-le une fois à la main. Que fait-il, et où se trouve le résultat ?

```bash
#!/bin/sh
# Sauvegarde compressée de /etc, conserve les 5 archives les plus récentes
set -e
dest=/var/backups/lpi101
mkdir -p "$dest"
archive="$dest/etc-$(date +%Y%m%d-%H%M%S).tar.gz"
tar -czf "$archive" -C / etc
ls -1t "$dest"/etc-*.tar.gz | tail -n +6 | xargs -r rm --
echo "Sauvegarde creee : $archive ($(du -h "$archive" | cut -f1))"
```

**D2.** Crée le service `/etc/systemd/system/lpi101-sauvegarde.service` et le timer `/etc/systemd/system/lpi101-sauvegarde.timer` avec les modèles ci-dessous, puis recharge la configuration de systemd. Comment le timer sait-il quel service lancer ? Pourquoi le service n’a-t-il pas de section `[Install]` ? Que signifie `*:0/2` ?

```ini
[Unit]
Description=Sauvegarde de /etc du TP LPI101

[Service]
Type=oneshot
ExecStart=/usr/local/bin/lpi101-sauvegarde.sh
```

```ini
[Unit]
Description=Sauvegarde de /etc toutes les 2 minutes

[Timer]
OnCalendar=*:0/2
AccuracySec=1s
Persistent=true

[Install]
WantedBy=timers.target
```

**D3.** Active et démarre le timer en une seule commande, puis affiche sa prochaine échéance. Compare l’état d’activation du timer et celui du service.

**D4.** Attends au moins une échéance, puis vérifie que de nouvelles archives apparaissent et retrouve les messages de la sauvegarde dans les journaux. Restaure ensuite le seul fichier `etc/hostname` de la dernière archive dans `/tmp/restau`, sans toucher au vrai `/etc`.

---

## Partie E — Nettoyer (10 min)

**E1.** Désactive et arrête le service de démonstration ainsi que le timer. Efface l’état d’échec de l’unité volontairement défaillante et l’état mémorisé du timer. Retire seulement les quatre fichiers d’unité, le script, les archives et le dossier de restauration créés pour ce TP, puis recharge la configuration de systemd.
