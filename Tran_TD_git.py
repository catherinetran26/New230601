# Importation des librairies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import seaborn as sns
# Importation des données
f = open(r"D:\MesDocs\DUDataAnalyst\Projets\TD_Git\iris.data") 
df = pd.read_csv(f, sep = ',')
f.close()
# Définir les nouveaux titres de colonnes
nvx_titres_col = ["sepal_length","sepal_width","petal_length","petal_width","class"]

# Assigner les nouveaux titres de colonnes au DataFrame
df.columns = nvx_titres_col
# Statistiques de base
print(df.head(5))

# Utilisation du groupby
df_grp = df.groupby(["class"]).agg(nb_sepal_length = ("sepal_length", "count"), nb_sepal_width = ("sepal_width", "count"), nb_petal_length = ("petal_length", "count"),nb_petal_with = ("petal_width", "count")).reset_index()
print(df_grp)


#FEATURE 1
# Filtrer sur la variable "class" pour les valeurs "Iris-setosa"
df_filtre = df.loc[df["class"] == "Iris-setosa"]

# Afficher le DataFrame filtré
print(df_filtre)