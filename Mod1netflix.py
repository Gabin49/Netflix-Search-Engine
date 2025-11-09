import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt



def summary(df):
    
    '''
    Sert à compter le nombre d'observations et de variables du dataframe
    ainsi que donner le nom et le type de ces dernières.
    '''
    
    
    nbobs  = df.shape[0]
    nbvar = df.shape[1]
    typvar = df.dtypes
    print(f"Le DataFrame comporte {nbobs} observations et {nbvar} variables.")
    print("Voici le nom et le type des données : ")
    return typvar



def load_data():
    """
    Charge les 2 bases de données nécessaires au projet, et les nettoie une première fois.
    
    """
    current_path = os.getcwd()
    path = os.path.abspath(os.path.join(current_path, ".."))
    path_data = os.path.join(path, "data_netflix")
    
    # Chargement des données
    df_netflix = pd.read_csv(os.path.join(path_data, "netflix_titles.csv"), encoding='latin1')
    df_tmdb = pd.read_csv(os.path.join(path_data, "TMDB_movie_dataset_v11.csv"), encoding='latin1')
    
    # Nettoyage des données Netflix
    df_netflix = df_netflix[[
        "show_id", "type", "title", "director", "cast", 
        "country", "date_added", "release_year", 
        "rating", "duration", "listed_in", "description"]] #car il y avait plusieurs colonnes vides
    
    
    #Nettoyage des données TMDB
    # 1. Conversion de la colonne release_date en datetime
    df_tmdb["release_date"] = pd.to_datetime(df_tmdb["release_date"], format="%Y-%m-%d")

    # 2. Création et nettoyage de la colonne release_year
    df_tmdb["release_year"] = df_tmdb["release_date"].dt.year  # Extrait l'année comme un nombre (float)
    df_tmdb["release_year"] = df_tmdb["release_year"].fillna(0)  # Remplace les NaN par 0
    df_tmdb["release_year"] = df_tmdb["release_year"].astype(int)  # Convertit toute la colonne en entier

    # 3. Remplacement des valeurs manquantes dans la colonne genres
    df_tmdb["genres"] = df_tmdb["genres"].fillna("Aucun genre") #Pour mieux comprendre le graph

    # 4. Application des filtres combinés
    df_tmdb = df_tmdb.loc[ (df_tmdb["vote_count"] > 0)]

    return df_netflix, df_tmdb



def analyse_genre(df_tmdb):
    """
    Fonction qui prend en entrée le dataframe de TMDB
    
    Cela affiche :
        - Le genre avec la meilleure moyenne de votes et la meilleure note.
        - Le genre avec la moins bonne moyenne de votes et la moins bonne note.
        

    Retourne :
        - le dataframe avec la moyenne des notes pour chaque genre
    """
    
    
    # Copier le DataFrame et préparer les données
    df_tmdb_copy = df_tmdb.copy()
    df_tmdb_copy["genres"] = df_tmdb["genres"].apply(lambda g: str(g).split(", "))
    df_tmdb_ex = df_tmdb_copy.explode("genres")
    
    # Calculer la moyenne des notes par genre
    df_tmdb_m = df_tmdb_ex.groupby("genres").agg({"vote_average": "mean"})
    
    # Trouver le genre avec la meilleure et la pire moyenne
    best_genre = df_tmdb_m["vote_average"].idxmax()
    best_score = df_tmdb_m["vote_average"].max()
    
    worst_genre = df_tmdb_m["vote_average"].idxmin()
    worst_score = df_tmdb_m["vote_average"].min()
    
    print(f"Le genre avec la meilleure note est '{best_genre}' avec une moyenne de {best_score:.2f}/10. ")
    print(f"Le genre le moins bien noté est '{worst_genre}' avec une moyenne de {worst_score:.2f}/10.")

    return df_tmdb_m