# 300 fiches d'anglais

Application statique : 300 fiches d'anglais visuelles, classées par niveau (A1, A2, B1, B2, C1) et par catégorie (vocabulaire, grammaire, conversation, expressions, verbes, pièges).

- Recherche, filtres par niveau et par catégorie
- Prononciation au toucher (synthèse vocale du navigateur)
- Mode « cacher le français » pour se tester
- Progression enregistrée sur l'appareil

## Mise en ligne avec GitHub Pages

1. Créer un dépôt public et y déposer `index.html`.
2. Dans **Settings → Pages**, choisir **Deploy from a branch**, branche `main`, dossier `/ (root)`.
3. Le site est servi sur `https://<utilisateur>.github.io/<dépôt>/`.

## Modifier les fiches

Les fiches sont dans `data/*.txt`, une par ligne :

    emoji|catégorie|Title|Titre|item=traduction;item=traduction;…|Example=Exemple|Astuce

Catégories : `V` vocabulaire, `G` grammaire, `C` conversation, `E` expressions, `PV` verbes, `P` pièges.
Puis `python3 build.py` régénère `index.html`.
