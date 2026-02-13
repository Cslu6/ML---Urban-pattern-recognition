"""
This script can be used as skelton code to read the challenge train and test
geojsons, to train a trivial model, and write data to the submission file.
"""
import geopandas as gpd
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Chargement des données (Chemins relatifs)
# Assurez-vous que train.geojson et test.geojson sont dans le même dossier que ce script
print("Chargement des données...")
train_df = gpd.read_file('train.geojson', index_col=0)
test_df = gpd.read_file('test.geojson', index_col=0)

def preprocess_data(df):
    """
    Fonction de pré-traitement pour nettoyer et préparer les données
    """
    # Convertir les coordonnées GPS (degrés) en Mètres (Projection Mercator)
    if df.crs.to_string() != 'EPSG:3857':
        df = df.to_crs(epsg=3857)

    # CONVERSION DES DATES
    date_cols = ['date0', 'date1', 'date2', 'date3', 'date4']
    # Vérification que les colonnes existent avant de les convertir
    existing_date_cols = [col for col in date_cols if col in df.columns]
    
    for col in existing_date_cols:
        df[col] = pd.to_datetime(df[col], format='%d-%m-%Y')

    # Encodage One-Hot pour le type urbain
    if 'urban_type' in df.columns:
        df = pd.get_dummies(df, columns=['urban_type'], prefix='urban', dtype=int)

    # Encodage pour le type géographique (séparé par des virgules)
    if 'geography_type' in df.columns:
        geo_dummies = df['geography_type'].str.get_dummies(sep=',')
        geo_dummies = geo_dummies.add_prefix('geo_') # Ajoute un préfixe pour la clarté
        
        df = pd.concat([df, geo_dummies], axis=1)
        df = df.drop('geography_type', axis=1)

    return df

print("Pré-traitement des données...")
train_df_clean = preprocess_data(train_df)
test_df_clean = preprocess_data(test_df)

# Encodage de la variable cible (Target Mapping)
change_type_map = {
    'Demolition': 0, 
    'Road': 1, 
    'Residential': 2, 
    'Commercial': 3, 
    'Industrial': 4, 
    'Mega Projects': 5
}

# On applique le mapping seulement sur le train (le test n'a pas la colonne change_type)
if 'change_type' in train_df_clean.columns:
    train_df_clean['change_type'] = train_df_clean['change_type'].map(change_type_map)

# Sauvegarde du fichier pré-traité
output_file = 'train_preprocessed.csv'
train_df_clean.to_csv(output_file, index=True)
print(f"Fichier sauvegardé avec succès : {output_file}")