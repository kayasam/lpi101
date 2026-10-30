---
title: "TP 10. Observer la machine et dépanner un service — Correction"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/38-grub-recuperation"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/38-grub-recuperation/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/38-grub-recuperation/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/38-grub-recuperation/tp/tp-10-machine-services-journaux-correction.md">↓ Télécharger le corrigé (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://kayasam.github.io/lpi101/lpi101/38-grub-recuperation/tp">Énoncé</a><a class="exercise-correction" href="https://kayasam.github.io/lpi101/lpi101/38-grub-recuperation/tp-corrigev2" aria-current="page">Corrigé</a></nav>

> Essaie chaque question avant d’ouvrir **Afficher la correction**. Chaque réponse se replie indépendamment.

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

> [!success]- Afficher la correction — A1
> ```bash
> lscpu
> free -h
> lsblk -o NAME,SIZE,TYPE,MOUNTPOINTS
> ```
>
> L’hyperviseur présente du matériel virtuel et une allocation de ressources. La VM ne voit pas nécessairement tous les composants physiques.

**A2.** Consulte les derniers messages du noyau et les paramètres de son lancement.

> [!success]- Afficher la correction — A2
> ```bash
> sudo journalctl -k -b --no-pager -n 15
> cat /proc/cmdline
> ```
>
> Le journal est limité au noyau et au démarrage courant. `/proc/cmdline` expose les paramètres transmis au noyau.

**A3.** Affiche la cible de démarrage par défaut et quelques services en cours. Quelle différence entre cible et service ?

> [!success]- Afficher la correction — A3
> ```bash
> systemctl get-default
> systemctl list-units --type=service --state=running --no-pager | head -n 15
> ```
>
> Une cible regroupe des unités pour représenter un état du système ; un service décrit l’exécution d’une tâche. Aucun changement de cible n’est demandé.

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

> [!success]- Afficher la correction — B1
> ```bash
> sudo tee /etc/systemd/system/lpi101-demo.service > /dev/null <<'EOF'
> [Unit]
> Description=Service de demonstration LPI 101
>
> [Service]
> Type=oneshot
> ExecStart=/usr/bin/echo TP-LPI101-demarrage-reussi
> RemainAfterExit=yes
>
> [Install]
> WantedBy=multi-user.target
> EOF
> sudo systemctl daemon-reload
> ```
>
> Unit décrit l’unité ; Service la commande et le comportement ; Install les liens d’activation. RemainAfterExit maintient ici un état actif après la fin de la commande, sans processus permanent.

**B2.** Démarre ce service, vérifie qu’il est actif puis vérifie s’il est déjà activé au démarrage.

> [!success]- Afficher la correction — B2
> ```bash
> sudo systemctl start lpi101-demo.service
> systemctl is-active lpi101-demo.service
> systemctl is-enabled lpi101-demo.service
> ```
>
> Le service est actif mais initialement disabled. is-enabled retourne alors un code non nul : c’est l’état observé, pas un problème de connexion.

**B3.** Active-le pour le démarrage puis arrête-le. Est-il toujours activé ? Redémarre-le pour la suite.

> [!success]- Afficher la correction — B3
> ```bash
> sudo systemctl enable lpi101-demo.service
> sudo systemctl stop lpi101-demo.service
> systemctl is-enabled lpi101-demo.service
> sudo systemctl start lpi101-demo.service
> ```
>
> Oui : stop modifie l’état immédiat, pas les liens d’activation. enable ne signifie pas forcément start ; `enable --now` combine les deux.

---

## Partie C — Lire une panne (20 min)

**C1.** Retrouve le message du service dans ses journaux, puis limite la recherche au démarrage courant.

> [!success]- Afficher la correction — C1
> ```bash
> sudo journalctl --sync
> sudo journalctl -u lpi101-demo.service --no-pager -n 15
> sudo journalctl -u lpi101-demo.service -b --no-pager
> ```
>
> Le message TP-LPI101-demarrage-reussi doit apparaître. La sortie réelle contient des dates et identifiants propres à la VM.

**C2.** Crée le fichier `/etc/systemd/system/lpi101-echec.service` avec le modèle ci-dessous. Recharge la configuration de systemd, tente de démarrer cette unité, puis cherche la cause de l’échec dans les journaux.

```ini
[Unit]
Description=Panne volontaire du TP LPI101
[Service]
Type=oneshot
ExecStart=/usr/bin/false
```

> [!success]- Afficher la correction — C2
> ```bash
> sudo tee /etc/systemd/system/lpi101-echec.service > /dev/null <<'EOF'
> [Unit]
> Description=Panne volontaire du TP LPI101
> [Service]
> Type=oneshot
> ExecStart=/usr/bin/false
> EOF
> sudo systemctl daemon-reload
> sudo systemctl start lpi101-echec.service
> systemctl --failed --no-pager
> sudo journalctl -u lpi101-echec.service --no-pager -n 12
> ```
>
> Le démarrage échoue volontairement : false renvoie 1. Une unité failed n’implique pas nécessairement une panne générale du système.

**C3.** Comment distinguer un problème du démarrage Linux et celui de cette seule unité ? Où GRUB intervient-il ?

> [!success]- Afficher la correction — C3
> La VM fonctionne et les journaux isolent l’échec de lpi101-echec. GRUB intervient avant le lancement du noyau et de systemd. Une panne du chargeur n’est pas diagnostiquée de la même façon qu’un service qui renvoie un code non nul.

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

> [!success]- Afficher la correction — D1
> ```bash
> sudo tee /usr/local/bin/lpi101-sauvegarde.sh > /dev/null <<'EOF'
> #!/bin/sh
> # Sauvegarde compressée de /etc, conserve les 5 archives les plus récentes
> set -e
> dest=/var/backups/lpi101
> mkdir -p "$dest"
> archive="$dest/etc-$(date +%Y%m%d-%H%M%S).tar.gz"
> tar -czf "$archive" -C / etc
> ls -1t "$dest"/etc-*.tar.gz | tail -n +6 | xargs -r rm --
> echo "Sauvegarde creee : $archive ($(du -h "$archive" | cut -f1))"
> EOF
> sudo chmod 755 /usr/local/bin/lpi101-sauvegarde.sh
> sudo /usr/local/bin/lpi101-sauvegarde.sh
> sudo ls -lh /var/backups/lpi101/
> ```
>
> Le script archive et compresse `/etc` dans `/var/backups/lpi101/`, avec la date et l’heure dans le nom du fichier (environ 1 Mo sur une Debian 13). Il ne garde que les 5 archives les plus récentes : `ls -1t` trie de la plus récente à la plus ancienne et `tail -n +6` sélectionne les suivantes, que l’on supprime. `set -e` arrête le script à la première erreur. On le teste à la main avant de l’automatiser.

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

> [!success]- Afficher la correction — D2
> ```bash
> sudo tee /etc/systemd/system/lpi101-sauvegarde.service > /dev/null <<'EOF'
> [Unit]
> Description=Sauvegarde de /etc du TP LPI101
>
> [Service]
> Type=oneshot
> ExecStart=/usr/local/bin/lpi101-sauvegarde.sh
> EOF
> sudo tee /etc/systemd/system/lpi101-sauvegarde.timer > /dev/null <<'EOF'
> [Unit]
> Description=Sauvegarde de /etc toutes les 2 minutes
>
> [Timer]
> OnCalendar=*:0/2
> AccuracySec=1s
> Persistent=true
>
> [Install]
> WantedBy=timers.target
> EOF
> sudo systemd-analyze verify /etc/systemd/system/lpi101-sauvegarde.timer
> systemd-analyze calendar '*:0/2' --iterations=3
> sudo systemctl daemon-reload
> ```
>
> Le timer porte le même nom que le service : il active `lpi101-sauvegarde.service` par défaut (sinon, directive `Unit=`). Le service n’a pas de `[Install]` car ce n’est pas lui qu’on active au démarrage, mais le timer, rattaché à `timers.target`. `*:0/2` signifie « chaque heure, à partir de la minute 0 puis toutes les 2 minutes » ; `systemd-analyze calendar` affiche la forme complète `*-*-* *:00/2:00` et les prochaines échéances. En production, on écrirait plutôt `OnCalendar=daily` ou `OnCalendar=*-*-* 02:00:00`. `AccuracySec=1s` évite le décalage d’une minute que systemd s’autorise par défaut, et `Persistent=true` rattrape une échéance manquée pendant que la machine était éteinte.

**D3.** Active et démarre le timer en une seule commande, puis affiche sa prochaine échéance. Compare l’état d’activation du timer et celui du service.

> [!success]- Afficher la correction — D3
> ```bash
> sudo systemctl enable --now lpi101-sauvegarde.timer
> systemctl list-timers lpi101-sauvegarde.timer --no-pager
> systemctl is-active lpi101-sauvegarde.timer
> systemctl is-enabled lpi101-sauvegarde.timer lpi101-sauvegarde.service
> ```
>
> `list-timers` affiche la prochaine échéance (NEXT, LEFT), la dernière (LAST, PASSED) et le service déclenché (ACTIVATES). Le timer est `enabled` ; le service est `static` : sans section `[Install]`, il ne peut pas être activé directement, il est déclenché par une autre unité.

**D4.** Attends au moins une échéance, puis vérifie que de nouvelles archives apparaissent et retrouve les messages de la sauvegarde dans les journaux. Restaure ensuite le seul fichier `etc/hostname` de la dernière archive dans `/tmp/restau`, sans toucher au vrai `/etc`.

> [!success]- Afficher la correction — D4
> ```bash
> sudo ls -lh /var/backups/lpi101/
> sudo journalctl --sync
> sudo journalctl -u lpi101-sauvegarde.service --no-pager -n 12
> systemctl list-timers lpi101-sauvegarde.timer --no-pager
> derniere=$(sudo ls -1t /var/backups/lpi101/etc-*.tar.gz | head -n 1)
> sudo tar -tzf "$derniere" | head -n 5
> mkdir -p /tmp/restau
> sudo tar -xzf "$derniere" -C /tmp/restau etc/hostname
> cat /tmp/restau/etc/hostname
> ```
>
> Une nouvelle archive apparaît à chaque échéance paire (12:02, 12:04…). Le journal contient, pour chaque exécution, la ligne `Sauvegarde creee : …` écrite par le script, encadrée par « Starting » et « Finished ». L’exécution manuelle de D1 n’y figure pas : le script a été lancé directement, hors de systemd. La sortie standard d’un service est envoyée au journal, ce que cron ne fait pas par défaut. Les noms dans l’archive commencent par `etc/` (sans `/`) grâce à `-C /` : la restauration dans `/tmp/restau` n’écrase donc rien dans le vrai `/etc`.

---

## Partie E — Nettoyer (10 min)

**E1.** Désactive et arrête le service de démonstration ainsi que le timer. Efface l’état d’échec de l’unité volontairement défaillante et l’état mémorisé du timer. Retire seulement les quatre fichiers d’unité, le script, les archives et le dossier de restauration créés pour ce TP, puis recharge la configuration de systemd.

> [!success]- Afficher la correction — E1
> ```bash
> sudo systemctl disable --now lpi101-demo.service lpi101-sauvegarde.timer
> sudo systemctl reset-failed lpi101-echec.service
> sudo systemctl clean --what=state lpi101-sauvegarde.timer
> sudo rm /etc/systemd/system/lpi101-demo.service /etc/systemd/system/lpi101-echec.service
> sudo rm /etc/systemd/system/lpi101-sauvegarde.timer /etc/systemd/system/lpi101-sauvegarde.service
> sudo rm /usr/local/bin/lpi101-sauvegarde.sh
> sudo rm -r /var/backups/lpi101 /tmp/restau
> sudo systemctl daemon-reload
> systemctl list-timers --all --no-pager | grep lpi101
> ```
>
> On arrête le timer, pas seulement le service : sinon il relancerait la sauvegarde à l’échéance suivante. `systemctl clean --what=state` efface la date du dernier déclenchement mémorisée par `Persistent=true` dans `/var/lib/systemd/timers/`, qui survivrait sinon au retrait de l’unité. Le dernier `grep` ne doit rien afficher. Les journaux historiques peuvent rester après retrait de l’unité. On ne supprime ni les journaux système ni d’autres services.
