# Linux — Initiation et préparation LPI 101

Site public : https://kayasam.github.io/lpi101/

Un dossier par chapitre (`cours/01-comprendre-gnu-linux/01-comprendre-gnu-linux.md`), avec les TP dans le sous-dossier `tp/` du chapitre de déclenchement. La même organisation est conservée dans les ZIP Obsidian.

39 chapitres, 9 compléments et 14 TP, dans la présentation Quartz validée pour Linux initiation. Le logo et le favicon utilisent Tux.

## Actualiser le cours

La source est le dossier `Formations/lpi101/LPI-101-Obsidian` du coffre Obsidian, indiqué par `vaultRoot` dans `site.json`. `scripts/import-vault.py` lit uniquement les documents déclarés et les médias associés, sans modifier le coffre. Les copies intermédiaires de `sources/` restent privées et ignorées par Git.

```powershell
./installer.ps1
./construire.ps1
python scripts/serve-preview.py --port 8785
```

Le build importe le coffre, prépare les pages et les téléchargements puis contrôle les liens et l'exclusion des corrections privées. Pour un autre ordinateur, ajuster `vaultRoot` dans `site.json`.

Après vérification, versionner les changements et pousser sur `main` : GitHub Actions déploie le site sur GitHub Pages. Le workflow utilise les pages générées versionnées ; le coffre privé n'est pas nécessaire au déploiement.

Les corrections ne sont publiées que si leur frontmatter contient `publier: true`. Les notes formateur et les TP d'origine restent hors publication. Les ZIP regroupent les supports publics par parcours ; le PDF unique contient tous les cours.

## Référence du modèle

# Modèle de site de formation

Base Quartz figée à partir du site Linux initiation & Bash validé le 16 octobre 2026 (commit `92ef419`). Même typographie, mêmes palettes, navigation, boutons de ressources, sommaires, lecture sans menus, corrigés dépliables et présentation sobre des annexes.

## Créer une formation

Depuis ce dossier :

```powershell
python scripts/instantiate.py "D:/Projet-git/ma-nouvelle-formation" --title "Ma nouvelle formation" --base-url "https://mon-compte.github.io/ma-nouvelle-formation"
```

La destination doit être inexistante. La copie reçoit son propre dépôt Git, **sans remote**. Le script vérifie d’abord les empreintes des fichiers visuels du modèle. Il ne publie rien et n’installe rien.

Dans la copie :

```powershell
./installer.ps1
./construire.ps1
python scripts/serve-preview.py --port 8780
```

Ouvrir l’adresse indiquée par le serveur. Prérequis : Git, Node 24 (minimum 22), npm et Python 3.13. Les dépendances Node sont verrouillées dans `package-lock.json`. Les bibliothèques PDF s’installent dans `.pdf-tools`, sans modifier Python globalement.

## Contenu et configuration

Modifier **`site.json` et les fichiers de `sources/`**. `content/` est généré : ne pas y rédiger de cours. `examples/` contient seulement la démonstration publique du modèle ; `sources/` est ignoré par Git pour préserver les corrections privées. Le coffre Obsidian peut être indiqué par un `sourceRoot` absolu ; le modèle le lit sans le modifier.

`site.json` définit le titre, le titre court mobile, l’adresse publique, puis une liste de parcours. Chaque parcours possède un identifiant unique, un titre, une description, des chapitres et éventuellement une annexe. Les chapitres suivent l’ordre de cette liste, sans nombre fixé à 6, 10 ou 16.

Chaque chapitre déclare :

- `slug` : adresse de la forme `01-mon-chapitre` ;
- `course` : cours Markdown obligatoire ;
- `html` : compagnon interactif facultatif, rédigé manuellement ;
- `quiz` : JSON facultatif avec 20 questions ; chaque question possède `question`, `choices` (4 réponses), `answer` (indice 0 à 3), `explanation` ;
- `tp` et `correction` : fichiers Markdown facultatifs.

Pour plusieurs TP dans un chapitre, remplacer ces deux champs par `tps`, une liste d’objets `{ "file": "tp.md", "correction": "corrigev2.md", "slug": "pas-a-pas" }`. `slug` et `correction` sont facultatifs. Chaque TP conserve son propre état de publication ; une page les regroupe derrière le bouton TP du chapitre.

Les chemins des documents sont relatifs à `sourceRoot`. Le premier titre `#` devient le titre affiché, sans raccourcissement. Les liens Markdown entre documents déclarés sont résolus pour le site et le ZIP. Un lien vers une source non déclarée bloque la préparation. Pour un compagnon HTML, `{{BASE_URL}}` désigne l’adresse publique ; les dépendances locales doivent être incluses dans `assets/` et référencées depuis ce dossier. Les médias particuliers et les autres schémas de quiz nécessitent une adaptation explicite du préparateur.

## Publier une correction

Dans le fichier déclaré par `correction` :

```yaml
---
publier: true
---
```

Le TP reçoit alors son bouton **Afficher les corrections**. La correction entre dans le site et le ZIP. Avec `publier: false`, ou sans ce champ, elle reste absente. Le changement prend effet après une nouvelle construction/publication, jamais au seul enregistrement dans Obsidian.

Conserver l’énoncé complet et ajouter une réponse sous chaque question :

```markdown
> [!success]- Afficher la correction — A1
> Réponse et explication.
```

## Téléchargements et vérifications

Une archive Obsidian par parcours ; **un seul PDF réunissant tous les cours Markdown sur l’accueil**, sans PDF par chapitre. Les ZIP incluent les supports présents et les corrigés publiés. Les téléchargements sont versionnés par empreinte de contenu.

`construire.ps1` prépare, compile et vérifie les liens locaux, les téléchargements contextuels, les boutons conditionnels, l’absence des corrigés privés, les liens du ZIP, le PDF unique et ses signets. Vérifier ensuite dans un navigateur : clair/sombre, mobile, menus, boutons, réponses dépliables et quiz. Les compagnons HTML restent des activités complémentaires ; aucune conversion automatique du cours complet en HTML pédagogique.

## Publication GitHub Pages

Créer un dépôt **distinct** pour la nouvelle formation, y configurer GitHub Pages avec GitHub Actions, puis définir `origin` sur ce dépôt. Vérifier `baseUrl` avant le premier push. Le modèle n’ajoute jamais le remote du site Linux.

```powershell
./publier.ps1                  # prépare et vérifie seulement
./publier.ps1 -Push -Message "Publier ma formation"
```

Le workflow compile les contenus générés déjà validés et commités, sans dépendre du coffre local. Après publication, vérifier le déploiement et les téléchargements réellement servis. Publier uniquement à la demande de l’utilisateur.

## Référence et évolution

`template-manifest.json` conserve le commit d’origine, l’empreinte de l’archive exacte et celles des fichiers visuels. `reference/site-linux-bash-92ef419.zip` est la copie exacte du dépôt source, conservée localement avec ses anciens scripts spécialisés ; **ce n’est pas le préparateur du nouveau modèle**. Les styles de base restent ceux du site d’origine ; seules les adaptations de noms, d’adresses et de parcours rendent les composants génériques.

Une évolution du modèle se teste dans une copie, puis les empreintes sont renouvelées volontairement après validation visuelle. Ne pas régénérer le manifeste pour contourner une divergence inexpliquée. Le skill personnel `site-formation-quartz` accompagne ce modèle.
