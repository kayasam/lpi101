---
title: "TP 12. Donner un accès ciblé avec les ACL"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="complements/01-acl"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/complements/01-acl/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/complements/01-acl/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/complements/complements/c01-acl/tp/tp-12-acl.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


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
