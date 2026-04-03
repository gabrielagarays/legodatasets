import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Archive from dataset
file_path = "colors.csv"

# Load dataset
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "rtatman/lego-database",
    file_path
)

print("First 5 records:")
print(df.head())

lego_df = df

#Colors commons in LEGO 
print("\nINFO:")
print(df.info())

print("\nDESCRIBE:")
print(df.describe())

print("\nCOLUMNAS:")
print(df.columns)

#values in columms
print("\nValores únicos en is_trans:")
print(df['is_trans'].unique())

#rename values
df['is_trans'] = df['is_trans'].map({'f': 'No', 't': 'Sí'})

print("\nConteo de valores en is_trans:")
print(df['is_trans'].value_counts())
