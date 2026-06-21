import pandas as pd

url = "https://data.ameli.fr/api/explore/v2.1/catalog/datasets/effectifs/exports/csv"

print("Téléchargement des données...")

df = pd.read_csv(url)

print("\nPremières lignes :")
print(df.head())

print("\nColonnes disponibles :")
print(df.columns)

