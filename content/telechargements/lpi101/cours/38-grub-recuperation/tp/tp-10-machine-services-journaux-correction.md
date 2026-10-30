# TP 10. Observer la machine et dépanner un service — Correction

> Essaie chaque question avant d’ouvrir **Afficher la correction**. Chaque réponse se replie indépendamment.

> Durée estimée : 80 min

> Chapitres associés : [33. Identifier le matériel et les modules du noyau](https://kayasam.github.io/lpi101/lpi101/33-materiel-modules/), [34. Observer les événements matériels](https://kayasam.github.io/lpi101/lpi101/34-evenements-materiels/), [35. Démarrage, arrêt et cibles systemd](https://kayasam.github.io/lpi101/lpi101/35-demarrage-arret/), [36. Gérer les services avec systemd](https://kayasam.github.io/lpi101/lpi101/36-services/), [37. Consulter les journaux et diagnostiquer](https://kayasam.github.io/lpi101/lpi101/37-journaux/), [38. Comprendre GRUB et la récupération](https://kayasam.github.io/lpi101/lpi101/38-grub-recuperation/)

---

## Objectifs

- Observer ressources et messages du démarrage.
- Distinguer service actif et service activé.
- Utiliser les journaux pour expliquer une panne simple.
- Planifier une tâche avec un timer systemd.

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

## Partie D — Planifier une tâche avec un timer (15 min)

**D1.** Crée le service `/etc/systemd/system/lpi101-horodatage.service` puis le timer `/etc/systemd/system/lpi101-horodatage.timer` avec les modèles ci-dessous, et recharge la configuration de systemd. Pourquoi le service n’a-t-il pas de section `[Install]` ? Que signifie `%%` ?

```ini
[Unit]
Description=Horodatage periodique du TP LPI101

[Service]
Type=oneshot
ExecStart=/usr/bin/date "+TP-LPI101-timer %%H:%%M:%%S"
```

```ini
[Unit]
Description=Declenche lpi101-horodatage toutes les minutes

[Timer]
OnCalendar=*-*-* *:*:00
AccuracySec=1s
Persistent=true

[Install]
WantedBy=timers.target
```

> [!success]- Afficher la correction — D1
> ```bash
> sudo tee /etc/systemd/system/lpi101-horodatage.service > /dev/null <<'EOF'
> [Unit]
> Description=Horodatage periodique du TP LPI101
>
> [Service]
> Type=oneshot
> ExecStart=/usr/bin/date "+TP-LPI101-timer %%H:%%M:%%S"
> EOF
> sudo tee /etc/systemd/system/lpi101-horodatage.timer > /dev/null <<'EOF'
> [Unit]
> Description=Declenche lpi101-horodatage toutes les minutes
>
> [Timer]
> OnCalendar=*-*-* *:*:00
> AccuracySec=1s
> Persistent=true
>
> [Install]
> WantedBy=timers.target
> EOF
> sudo systemd-analyze verify /etc/systemd/system/lpi101-horodatage.timer
> systemd-analyze calendar '*-*-* *:*:00' --iterations=3
> sudo systemctl daemon-reload
> ```
>
> Le timer porte le même nom que le service : il active `lpi101-horodatage.service` par défaut (sinon, directive `Unit=`). Le service n’a pas de `[Install]` car ce n’est pas lui qu’on active au démarrage, mais le timer, rattaché à `timers.target`. Dans une unité, `%` introduit un spécificateur systemd ; `%%` produit un `%` littéral pour `date`. `OnCalendar` fixe l’échéance (ici chaque minute à la seconde 00), `AccuracySec=1s` évite le regroupement par défaut d’une minute et `Persistent=true` rattrape une échéance manquée pendant que la machine était éteinte.

**D2.** Active et démarre le timer en une seule commande, puis affiche sa prochaine échéance. Compare l’état d’activation du timer et celui du service.

> [!success]- Afficher la correction — D2
> ```bash
> sudo systemctl enable --now lpi101-horodatage.timer
> systemctl list-timers lpi101-horodatage.timer --no-pager
> systemctl is-active lpi101-horodatage.timer
> systemctl is-enabled lpi101-horodatage.timer lpi101-horodatage.service
> ```
>
> `list-timers` affiche les colonnes NEXT, LEFT, LAST et PASSED, ainsi que l’unité activée. Le timer est `enabled` ; le service est `static` : sans section `[Install]`, il ne peut pas être activé directement, il est déclenché par une autre unité.

**D3.** Attends au moins une minute, puis retrouve les déclenchements dans les journaux du service. Lance aussi le service une fois à la main : le timer est-il indispensable pour l’exécuter ?

> [!success]- Afficher la correction — D3
> ```bash
> sudo systemctl start lpi101-horodatage.service
> sudo journalctl --sync
> sudo journalctl -u lpi101-horodatage.service --no-pager -n 10
> systemctl list-timers lpi101-horodatage.timer --no-pager
> ```
>
> Chaque exécution laisse une ligne `TP-LPI101-timer HH:MM:SS` entre « Starting » et « Finished » ; les déclenchements du timer tombent à la seconde 00, l’exécution manuelle à l’heure du lancement. Les colonnes LAST et PASSED sont maintenant renseignées. Le service reste une unité ordinaire : le timer ne fait que décider quand le démarrer. Par rapport à cron, la sortie est journalisée et l’état se consulte avec `systemctl`.

---

## Partie E — Nettoyer (10 min)

**E1.** Désactive et arrête le service de démonstration ainsi que le timer. Efface l’état d’échec de l’unité volontairement défaillante et l’état mémorisé du timer, retire seulement les quatre fichiers d’unité créés pour ce TP, puis recharge la configuration de systemd.

> [!success]- Afficher la correction — E1
> ```bash
> sudo systemctl disable --now lpi101-demo.service lpi101-horodatage.timer
> sudo systemctl reset-failed lpi101-echec.service
> sudo systemctl clean --what=state lpi101-horodatage.timer
> sudo rm /etc/systemd/system/lpi101-demo.service /etc/systemd/system/lpi101-echec.service
> sudo rm /etc/systemd/system/lpi101-horodatage.timer /etc/systemd/system/lpi101-horodatage.service
> sudo systemctl daemon-reload
> systemctl list-timers --all --no-pager | grep lpi101
> ```
>
> On arrête le timer, pas seulement le service : sinon il relancerait le service à la minute suivante. `systemctl clean --what=state` efface la date du dernier déclenchement mémorisée par `Persistent=true` dans `/var/lib/systemd/timers/`, qui survivrait sinon au retrait de l’unité. Le dernier `grep` ne doit rien afficher. Les journaux historiques peuvent rester après retrait de l’unité. On ne supprime ni les journaux système ni d’autres services.
