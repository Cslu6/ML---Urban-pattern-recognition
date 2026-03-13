# Urban Pattern Recognition

**But du projet**

- Explorer et reconnaître des motifs urbains à partir de données géospatiales (GeoJSON).
- Fournir un notebook reproductible avec un pipeline d'entraînement/validation et un rendu de soumission.

**Points forts**

- Données GeoJSON prêtes à l'emploi (`data/train.geojson`, `data/test.geojson`).
- Notebook interactif pour l'exploration et la reproduction : `Notebook.ipynb`.
- Exemple de sortie : `outputs/submission_hybrid.csv`.

**Aperçu rapide**

1. Créez un environnement à partir de `environment.yml`.
2. Lancez Jupyter et ouvrez `Notebook.ipynb`.
3. Explorez les cellules : préparation des données → features → entraînement → export de soumission.

**Structure du dépôt**

- `environment.yml` - configuration Conda pour reproduire l'environnement.
- `Notebook.ipynb` - notebook principal (exploration & pipeline).
- `data/` - jeux de données GeoJSON (`train.geojson`, `test.geojson`).
- `outputs/` - résultats et soumissions exemple.

**Installation rapide**

```bash
conda env create -f environment.yml
conda activate urban-patterns
jupyter lab
```

Ouvrez ensuite `Notebook.ipynb` dans Jupyter Lab/Notebook.

**Données**

- Les fichiers GeoJSON sont fournis dans le dossier `data/` pour un démarrage immédiat.
- Le notebook montre comment charger, visualiser et convertir ces données en features exploitables.

**Résultats**

- Un exemple de soumission est présent dans `outputs/submission_hybrid.csv`.

