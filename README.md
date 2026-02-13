# ML Kaggle Project - Change Type Classification

Projet de classification multi-classe pour identifier le type de changement urbain à partir de données géospatiales.

## Setup Instructions

### 1. Cloner le projet
```bash
git clone https://github.com/Cslu6/ML---Projet-Kaggle.git
cd ML---Projet-Kaggle
```

### 2. Créer l'environnement conda
```bash
conda env create -f environment.yml
conda activate kaggle_project
```

### 3. Ajouter les données
Créer un dossier `data/` à la racine du projet et y placer les fichiers Kaggle :
```
ML---Projet-Kaggle/
├── data/
│   ├── train.geojson
│   └── test.geojson
├── Notebook.ipynb
├── environment.yml
└── README.md
```

**Les données ne sont pas sur Git** (trop volumineuses). Téléchargez-les depuis Kaggle ou demandez-les au propriétaire du projet.

### 4. Ouvrir le notebook
```bash
code .
```
Dans VS Code :
- Ouvrir `Notebook.ipynb`
- Sélectionner l'interpréteur Python : `kaggle_project`
- Exécuter les cellules

## Structure du projet
```
├── data/                  # Données (non versionnées)
├── outputs/               # Sorties du modèle (créé automatiquement)
├── Notebook.ipynb         # Pipeline ML principal
├── environment.yml        # Dépendances conda
└── README.md             # Ce fichier
```

## Pipeline
1. Data Loading & Preprocessing
2. Feature Engineering & Dimensionality Reduction
3. Learning Algorithms
4. Evaluation
5. Submission

## Collaboration
Dépôt GitHub privé. Pour ajouter un collaborateur : Settings → Collaborators sur GitHub.
