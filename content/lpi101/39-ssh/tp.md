---
title: "TP 11. Se connecter et transférer avec SSH"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="lpi101/39-ssh"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/lpi101/39-ssh/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a><a class="resource-button" data-resource-kind="tp" href="https://kayasam.github.io/lpi101/lpi101/39-ssh/tp"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</span><span class="resource-label">TP</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/lpi101/cours/39-ssh/tp/tp-11-ssh.md">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


> Durée estimée : 45 min

> Chapitres associés : [39. Se connecter à distance avec SSH](https://kayasam.github.io/lpi101/lpi101/39-ssh/)

---

## Objectifs

- Distinguer client, serveur et clé d’hôte.
- Installer une clé publique puis tester l’authentification.
- Transférer un fichier et vérifier le résultat.

## Avant de commencer

Pour être autonome avec une seule VM, cet atelier utilise d’abord la VM comme client et comme serveur via 127.0.0.1. Le compte doit avoir un mot de passe connu pour ssh-copy-id. Le dernier exercice transpose au poste physique. La clé sans phrase de passe créée ici est dédiée à ce laboratoire ; en usage habituel, protéger la clé privée. Ne désactive pas l’authentification par mot de passe du serveur pendant cet atelier.

**Préparation fournie :**

```bash
sudo apt update
sudo apt install openssh-client openssh-server
sudo systemctl start ssh
mkdir -p ~/lpi101-tp/tp11
cd ~/lpi101-tp/tp11
```

---

## Partie A — Identifier les interlocuteurs (10 min)

**A1.** Affiche l’état du serveur et l’empreinte de sa clé d’hôte Ed25519. Quel secret ne doit pas être partagé ?

**A2.** Établis une première connexion locale et compare l’empreinte affichée avant de l’accepter. Quitte ensuite la session distante.

---

## Partie B — Installer une clé utilisateur (20 min)

**B1.** Génère une clé Ed25519 dédiée `cle_labo` dans le dossier du TP. Identifie la clé privée et la clé publique.

**B2.** Installe uniquement la clé publique sur le compte serveur avec ssh-copy-id, puis vérifie une commande distante sans mot de passe du compte.

**B3.** Teste explicitement l’authentification par clé en interdisant le dialogue de mot de passe du client.

---

## Partie C — Transférer et transposer (15 min)

**C1.** Crée un fichier local `message.txt`, transfère-le vers `/tmp/lpi101-message.txt` du serveur et compare les deux contenus.

**C2.** Depuis le poste physique, comment adapter la première connexion ? Quelles informations changent ?

**C3.** Retire seulement la clé publique de laboratoire d’authorized_keys et le fichier temporaire transféré.
