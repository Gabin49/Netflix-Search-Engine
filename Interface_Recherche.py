from tkinter import *
from tkinter import ttk
import pandas as pd

#On se place dans la partie 3 du dossier
from Mod1netflix import *
from Mod2netflix import *

df_netflix,df_tmdb = load_data()


def interface(df):
    
    """
    Crée une interface graphique pour rechercher des films dans un DataFrame.

    Cette fonction utilise Tkinter pour afficher une fenêtre où l'utilisateur peut 
    saisir des critères de recherche (genre, année, pays). Les résultats correspondant 
    aux critères sont affichés dans un tableau interactif (Treeview).

    Paramètres
    ----------
    df :Le DataFrame contenant les informations sur les films, avec des colonnes telles 
        que 'genres', 'release_year', et 'production_countries'.

    Retourne
    -------
    None
    """
    
    fenetre = Tk()
    fenetre.geometry("1000x800+100+100")
    fenetre.title("Moteur de Recherche de Film")

    intro = Label(fenetre, text='Bonjour !', fg='black')

    question_Genres = Label(fenetre, text="Quel genre voulez vous ?", fg="black")
    question_year = Label(fenetre, text="Année de sortie du film ?", fg="black")
    question_pays = Label(fenetre, text="Quel pays de production ?", fg="black")
    reponse_Genres = Entry(fenetre)
    reponse_year = Entry(fenetre)
    reponse_pays = Entry(fenetre)

    def affichage(df_resultats):

        tree.delete(*tree.get_children())

        for row in df_resultats.itertuples(index=False):
            tree.insert("", "end", values=row)

    def rechercher():
        
        """"Un mélange des fonctions search_gy et suggest"""
        # Récupérer les entrées utilisateur
        genre = reponse_Genres.get().title()
        year_str = reponse_year.get()
        pays = reponse_pays.get().title()
        
       
        filtre_genre = df["genres"].str.contains(genre, na=False) if genre else True
        filtre_pays = df["production_countries"].str.contains(pays, na=False) if pays else True

        if not year_str:
            filtre_year = True
        else:
            try:
                year_int = int(year_str)  # On convertit en entier
                filtre_year = (df["release_year"] == year_int)
            except ValueError:
                print(f"'{year_str}' n'est pas une année valide. Filtre ignoré.")
                filtre_year = True  # On ignore le filtre si l'année est invalide

        df_filtre = df.loc[filtre_genre & filtre_year & filtre_pays]
        df_trie = df_filtre.sort_values(by=["vote_average", "popularity", "vote_count"], ascending=False)
        df_final = df_trie[["title", "vote_average", "release_date"]]

        affichage(df_final)


    rechercher_button = Button(fenetre, text="Rechercher", command=rechercher)
    
    # Créer ou mettre à jour le Treeview
    tree = ttk.Treeview(fenetre, columns=["title", "vote_average","release_date"], show="headings") 
    #Widget pour améliorer l'interface

    # Ajouter des en-têtes de colonnes cliquables
    tree.heading("title", text="Titre")
    tree.heading("vote_average", text="Note Moyenne")
    tree.heading("release_date", text="Date de Sortie")

    # Définir la largeur des colonnes
    tree.column("title", width=400)
    tree.column("vote_average", width=100)
    tree.column("release_date", width=150)

    # Ajouter les autres widgets
    intro.pack(pady=5)
    question_Genres.pack()
    reponse_Genres.pack(pady=2)
    question_year.pack()
    reponse_year.pack(pady=2)
    question_pays.pack()
    reponse_pays.pack(pady=2)
    rechercher_button.pack(pady=10)
    tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

    fenetre.mainloop()

interface(df_tmdb)


