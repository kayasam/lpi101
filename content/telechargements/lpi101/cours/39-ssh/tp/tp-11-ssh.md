# TP 11. Se connecter et transférer avec SSH

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
