# Moteur de Recherche et d'Analyse (Netflix & TMDB) - Projet M1

Projet réalisé dans le cadre du Master 1 Économétrie & Statistiques (Paris 1 Panthéon-Sorbonne).

Ce projet utilise les bases de données Netflix et TMDB pour analyser les tendances du cinéma et proposer une application de recherche de films basée sur des filtres.

## 1. Structure du Projet

Ce dépôt est organisé en trois fichiers principaux :

### a. L'analyse exploratoire (`Analyse_Exploratoire.ipynb`)
Le [Notebook Jupyter](./Analyse_Exploratoire.ipynb) contient toute la démarche d'analyse exploratoire (EDA) :
* Chargement et nettoyage des données.
* Analyse de la note moyenne par genre.
* Analyse de la répartition des films par année.
* Étude des facteurs de popularité (budget, durée, etc.).

### b. Le module de données (`Mod1netflix.py`)
Le script [<code>Mod1netflix.py</code>](./Mod1netflix.py) contient les fonctions de base pour charger et nettoyer les données (`load_data()`, `summary()`). Il est importé par le Notebook et l'interface.

### c. L'Interface Graphique (`Interface_Recherche.py`)
Le script [<code>Interface_Recherche.py</code>](./Interface_Recherche.py) lance l'application de bureau (créée avec **Tkinter**). Il contient la logique de recherche qui **filtre le DataFrame** (par genre, année, pays) pour retourner les résultats pertinents.

## 2. Technologies et Librairies

* **Langage :** Python
* **Analyse & Données :** Pandas, NumPy, Jupyter
* **Visualisation :** Matplotlib
* **Application :** Tkinter

(Pour installer les dépendances : `pip install -r requirements.txt`)
