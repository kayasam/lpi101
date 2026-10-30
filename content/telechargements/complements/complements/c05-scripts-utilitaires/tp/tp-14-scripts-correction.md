# TP 14. Écrire un petit script de contrôle — Correction

> Essaie chaque question avant d’ouvrir **Afficher la correction**. Chaque réponse se replie indépendamment.

> Durée estimée : 45 min

> Chapitres associés : [C03. Écrire un premier script Bash](https://kayasam.github.io/lpi101/complements/03-premiers-scripts/), [C04. Découvrir les conditions et les boucles](https://kayasam.github.io/lpi101/complements/04-conditions-boucles/), [C05. Lire des scripts utilitaires](https://kayasam.github.io/lpi101/complements/05-scripts-utilitaires/)

---

## Objectifs

- Créer un script exécutable avec un paramètre.
- Utiliser une condition et un code retour.
- Vérifier un résultat avant d’annoncer un succès.

## Avant de commencer

Cet atelier est un prolongement après l’initiation au shell. L’énoncé donne le comportement attendu ; plusieurs solutions sont possibles.

> [!info] Atelier optionnel
> À proposer après les bases, selon le rythme du groupe.

**Préparation fournie :**

```bash
mkdir -p ~/lpi101-tp/tp14
cd ~/lpi101-tp/tp14
```

---

## Partie A — Écrire et exécuter (15 min)

**A1.** Crée `bonjour.sh` : il affiche `Bonjour PRENOM`, en prenant le premier argument comme prénom et `stagiaire` si aucun argument n’est fourni.

> [!success]- Afficher la correction — A1
> ```bash
> cat > bonjour.sh <<'EOF'
> #!/bin/bash
> prenom="${1:-stagiaire}"
> printf 'Bonjour %s\n' "$prenom"
> EOF
> chmod +x bonjour.sh
> ./bonjour.sh Alice
> ./bonjour.sh
> ```
>
> Le shebang indique l’interpréteur pour l’exécution directe. Les guillemets conservent un argument contenant des espaces.

**A2.** Vérifie sa syntaxe puis lance-le avec le prénom composé `Jean Paul`. Quelle différence entre `bash bonjour.sh` et `./bonjour.sh` ?

> [!success]- Afficher la correction — A2
> ```bash
> bash -n bonjour.sh
> ./bonjour.sh "Jean Paul"
> bash bonjour.sh Alice
> ```
>
> bash -n ne lance pas le script. L’exécution directe nécessite notamment le droit x et un interpréteur adapté ; `bash fichier` lit le fichier via Bash.

---

## Partie B — Contrôler une condition (20 min)

**B1.** Crée `controle.sh` : il reçoit un chemin, affiche `OK : chemin` si c’est un fichier ordinaire, sinon écrit `Absent : chemin` sur stderr et termine avec le code 1.

> [!success]- Afficher la correction — B1
> ```bash
> cat > controle.sh <<'EOF'
> #!/bin/bash
> chemin="${1:-}"
> if [ -f "$chemin" ]; then
>   printf 'OK : %s\n' "$chemin"
> else
>   printf 'Absent : %s\n' "$chemin" >&2
>   exit 1
> fi
> EOF
> chmod +x controle.sh
> ./controle.sh bonjour.sh
> ./controle.sh fichier-absent.txt
> code_retour=$?
> echo "$code_retour"
> ```
>
> Le deuxième test doit afficher une erreur et renvoyer 1. Une commande lancée après le script remplacerait $? ; on le mémorise immédiatement.

**B2.** Avec une boucle, lance le contrôle sur `bonjour.sh`, `controle.sh` et `fichier-absent.txt`, en signalant clairement les échecs.

> [!success]- Afficher la correction — B2
> ```bash
> for fichier in bonjour.sh controle.sh fichier-absent.txt; do
>   if ./controle.sh "$fichier"; then
>     echo 'Contrôle réussi'
>   else
>     echo 'Contrôle en échec'
>   fi
> done
> ```
>
> Tester le code retour évite d’afficher un succès après une erreur. Le chemin inexistant sert de cas négatif volontaire.

---

## Partie C — Conserver une preuve (10 min)

**C1.** Archive les deux scripts dans `scripts.tar.gz`. N’affiche `Archive créée` que si tar a réussi, puis liste le contenu.

> [!success]- Afficher la correction — C1
> ```bash
> if tar -czf scripts.tar.gz bonjour.sh controle.sh; then
>   echo 'Archive créée'
> else
>   echo 'Échec de l’archive' >&2
> fi
> tar -tzf scripts.tar.gz
> ```
>
> Une archive de ce type conserve le travail ; elle ne constitue pas à elle seule une stratégie de sauvegarde.
