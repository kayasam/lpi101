---
title: "C08. Personnaliser son terminal"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="complements/08-personnaliser-terminal"><div class="resource-buttons"><a class="resource-button" data-resource-kind="markdown" href="https://kayasam.github.io/lpi101/complements/08-personnaliser-terminal/"><span class="resource-icon"><svg class="resource-symbol" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg>
</span><span class="resource-label">Cours</span></a></div><div class="resource-actions"><a class="resource-download" download href="https://kayasam.github.io/lpi101/telechargements/complements/complements/c08-personnaliser-terminal/c08-personnaliser-terminal.md">↓ Télécharger le cours (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> [!note] Objectif
> Adapter l’affichage du shell après avoir acquis les commandes de base.

> [!info] Complément
> À découvrir après les bases, selon le rythme du groupe.

---

## Personnaliser le terminal (fichier `.bashrc`)

Le fichier **`~/.bashrc`** définit l’environnement du shell.
C’est ici qu’on peut activer les couleurs et personnaliser le prompt (l’invite de commande).

## Activer les couleurs de base :

Ouvre le fichier :

```bash
nano ~/.bashrc
```

Assure-toi que ces lignes sont présentes (ou décommentées) :

```bash
alias ls='ls --color=auto'
alias grep='grep --color=auto'
```

Recharge le fichier :

```bash
source ~/.bashrc
```

---

## Coloriser le prompt (variable PS1)

Le **prompt** est le texte affiché avant le curseur (par exemple `user@debian:~$`).
Il est défini par la variable **PS1**.

Exemple simple et coloré :

```bash
export PS1="\[\033[38;5;82m\]\u@\[\033[38;5;214m\]\h\[\033[0m\]:\[\033[38;5;14m\]\w\[\033[0m\]\$ "
```

Pour rendre cette personnalisation permanente :

```bash
echo 'export PS1="\[\033[38;5;82m\]\u@\h:\w\$ "' >> ~/.bashrc
```

Recharge :

```bash
source ~/.bashrc
```

Générateur de ps1 en ligne : [Bash Prompt Generator](https://bash-prompt-generator.org/)

---

## Coloriser les pages man (Debian 13)

L’affichage des pages `man` dépend du formateur, du pager et de la configuration du terminal. Les réglages ci-dessous sont des pistes de personnalisation à essayer, pas une étape nécessaire du cours.
Il faut réactiver cette fonction en configurant `groff` et `less`.

Ajoute à la fin du `~/.bashrc` :

```bash
# Couleurs dans les pages man
export PAGER=less
export LESS='-R'
export MANROFFOPT=-c

export LESS_TERMCAP_mb=$'\e[1;31m'
export LESS_TERMCAP_md=$'\e[1;36m'
export LESS_TERMCAP_me=$'\e[0m'
export LESS_TERMCAP_so=$'\e[1;44;33m'
export LESS_TERMCAP_se=$'\e[0m'
export LESS_TERMCAP_us=$'\e[1;32m'
export LESS_TERMCAP_ue=$'\e[0m'
```

Recharge ensuite :

```bash
source ~/.bashrc
```

> [!info]
> > Sur Debian 13, `groff` filtre désormais les séquences de couleurs par défaut pour compatibilité.
> > L’option `MANROFFOPT=-c` désactive ce filtrage et permet à `less` d’afficher les couleurs correctement.

---

## Conserver une personnalisation

`~/.bashrc` est généralement lu pour les shells Bash interactifs non lancés comme shells de connexion ; les fichiers de profil peuvent le charger lors d’une connexion. Avant de le modifier :

```bash
cp ~/.bashrc ~/.bashrc.sauvegarde
nano ~/.bashrc
bash -n ~/.bashrc
```

`bash -n` contrôle la syntaxe ; il ne garantit pas que les commandes auront l’effet voulu. Ouvrir un second terminal pour vérifier le résultat en conservant la session actuelle.

## À retenir

> [!tip]
> Une personnalisation facilite la lecture, mais les commandes doivent rester compréhensibles sans couleurs ni prompt particulier.
