# TP 12. Donner un accès ciblé avec les ACL

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

**A2.** Vérifie que lpi_audit ne peut pas modifier le rapport.

---

## Partie B — Comprendre le masque et l’héritage (15 min)

**B1.** Limite le masque du rapport à aucun droit, observe getfacl puis reteste la lecture. Rétablis ensuite un masque de lecture.

**B2.** Ajoute une ACL par défaut donnant la lecture et la traversée à lpi_audit. Crée un nouveau fichier comme root et vérifie les droits obtenus.

---

## Partie C — Retirer les ressources (5 min)

**C1.** Supprime uniquement le dossier et le compte créés pour cet atelier.


[Afficher les corrections](https://kayasam.github.io/lpi101/complements/01-acl/tp-corrigev2)
