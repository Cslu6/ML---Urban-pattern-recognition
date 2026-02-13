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

change_type_map = {'Demolition': 0, 'Road': 1, 'Residential': 2, 'Commercial': 3, 'Industrial': 4,
       'Mega Projects': 5}

#read 

train_df = gpd.read_file('/Users/pauledouardbacot/Desktop/2-el-1730-machine-learning-project-2026/train.geojson', index_col=0)
test_df = gpd.read_file('/Users/pauledouardbacot/Desktop/2-el-1730-machine-learning-project-2026/test.geojson', index_col=0)

def preprocess_data(df):
    # Convertir les coordonnées GPS (degrés) en Mètres 
    if df.crs.to_string() != 'EPSG:3857':
        df = df.to_crs(epsg=3857)

    # CONVERSION DES DATESconda --version
    date_cols = ['date0', 'date1', 'date2', 'date3', 'date4']
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], format='%d-%m-%Y')

    
    df = pd.get_dummies(df, columns=['urban_type'], prefix='urban', dtype=int)

    geo_dummies = df['geography_type'].str.get_dummies(sep=',')
    geo_dummies = geo_dummies.add_prefix('geo_') # Ajoute un préfixe pour la clarté
    
    df = pd.concat([df, geo_dummies], axis=1)
    df = df.drop('geography_type', axis=1)

    return df

train_df_clean = preprocess_data(train_df)

test_df_clean = preprocess_data(test_df)

change_type_map = {'Demolition': 0, 'Road': 1, 'Residential': 2, 'Commercial': 3, 'Industrial': 4, 'Mega Projects': 5}
train_df_clean['change_type'] = train_df_clean['change_type'].map(change_type_map)

train_df_clean.to_csv('/Users/pauledouardbacot/Desktop/2-el-1730-machine-learning-project-2026/train_preprocessed.csv', index=True)

