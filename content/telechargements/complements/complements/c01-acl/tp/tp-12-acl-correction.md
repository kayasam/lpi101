# TP 12. Donner un accès ciblé avec les ACL — Correction

> Essaie chaque question avant d’ouvrir **Afficher la correction**. Chaque réponse se replie indépendamment.

> Durée estimée : 35 min

> Chapitres associés : [C01. Donner des droits précis avec les ACL](https://kayasam.github.io/lpi101/complements/01-acl/)

---

## Objectifs

- Ajouter un droit pour un utilisateur nommé.
- Observer le masque et les droits effectifs.
- Tester une ACL par défaut sur un dossier.

## Avant de commencer

Complément après les permissions classiques. Le compte et le dossier sont créés par la préparation fournie ; ils ne dépendent pas du TP 06.

> [!info] Atelier optionnel
> À proposer après les bases, selon le rythme du groupe.

**Préparation fournie :**

```bash
sudo apt update
sudo apt install acl
sudo useradd -m -s /bin/bash lpi_audit
sudo mkdir /srv/lpi101-acl
sudo chmod 700 /srv/lpi101-acl
printf 'Compte rendu ACL\n' | sudo tee /srv/lpi101-acl/rapport.txt > /dev/null
sudo chmod 600 /srv/lpi101-acl/rapport.txt
```

---

## Partie A — Autoriser une lecture précise (15 min)

**A1.** Autorise lpi_audit à traverser le dossier et à lire son rapport, sans changer le propriétaire. Teste la lecture sous cette identité.

> [!success]- Afficher la correction — A1
> ```bash
> sudo setfacl -m u:lpi_audit:rx /srv/lpi101-acl
> sudo setfacl -m u:lpi_audit:r /srv/lpi101-acl/rapport.txt
> sudo -u lpi_audit cat /srv/lpi101-acl/rapport.txt
> sudo getfacl /srv/lpi101-acl/rapport.txt
> ```
>
> L’accès nécessite des droits sur le chemin et sur le fichier. Une ACL de fichier ne permet pas de traverser un dossier interdit.

**A2.** Vérifie que lpi_audit ne peut pas modifier le rapport.

> [!success]- Afficher la correction — A2
> ```bash
> sudo -u lpi_audit sh -c 'printf "Modification\n" >> /srv/lpi101-acl/rapport.txt'
> ```
>
> Le refus est attendu : l’entrée ACL n’accorde que la lecture.

---

## Partie B — Comprendre le masque et l’héritage (15 min)

**B1.** Limite le masque du rapport à aucun droit, observe getfacl puis reteste la lecture. Rétablis ensuite un masque de lecture.

> [!success]- Afficher la correction — B1
> ```bash
> sudo setfacl -m m::--- /srv/lpi101-acl/rapport.txt
> sudo getfacl /srv/lpi101-acl/rapport.txt
> sudo -u lpi_audit cat /srv/lpi101-acl/rapport.txt
> sudo setfacl -m m::r-- /srv/lpi101-acl/rapport.txt
> sudo -u lpi_audit cat /srv/lpi101-acl/rapport.txt
> ```
>
> L’entrée utilisateur reste enregistrée, mais le masque limite ses droits effectifs. La première lecture est refusée ; la dernière doit réussir.

**B2.** Ajoute une ACL par défaut donnant la lecture et la traversée à lpi_audit. Crée un nouveau fichier comme root et vérifie les droits obtenus.

> [!success]- Afficher la correction — B2
> ```bash
> sudo setfacl -d -m u:lpi_audit:rx /srv/lpi101-acl
> sudo sh -c 'printf "Nouveau fichier\n" > /srv/lpi101-acl/nouveau.txt'
> sudo getfacl /srv/lpi101-acl/nouveau.txt
> sudo -u lpi_audit cat /srv/lpi101-acl/nouveau.txt
> ```
>
> L’ACL par défaut agit sur les nouvelles créations ; les permissions demandées pour un fichier ordinaire n’ajoutent pas automatiquement x. Les anciens fichiers ne sont pas modifiés rétroactivement.

---

## Partie C — Retirer les ressources (5 min)

**C1.** Supprime uniquement le dossier et le compte créés pour cet atelier.

> [!success]- Afficher la correction — C1
> ```bash
> sudo rm -r /srv/lpi101-acl
> sudo userdel -r lpi_audit
> ```
>
> Cette étape retire aussi les ACL avec les fichiers ; `setfacl -b` aurait retiré les ACL étendues en conservant les fichiers.
