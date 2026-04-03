import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Archivo dentro del dataset
file_path = "colors.csv"

# Cargar dataset
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "rtatman/lego-database",
    file_path
)

print("First 5 records:")
print(df.head())

lego_df = df

#Analizar los colores más utilizados en LEGO y su distribución.
print("\nINFO:")
print(df.info())

print("\nDESCRIBE:")
print(df.describe())

print("\nCOLUMNAS:")
print(df.columns)


