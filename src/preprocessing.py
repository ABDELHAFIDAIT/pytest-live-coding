import pandas as pd


# Supprimer les Doublons
def remove_doublons(df:pd.DataFrame) -> pd.DataFrame :
    return df.drop_duplicates()


# Remplir les Valeurs Manquantes d'un Colonne
def fill_missing_values(df:pd.DataFrame, col:str, value) :
    df[col] = df[col].fillna(value)
    return df


# Normaliser un Colonne
def normalize_col(df:pd.DataFrame, col:str) :
    min_v = df[col].min()
    max_v = df[col].max()
    df[col] = (df[col] - min_v) / (max_v - min_v)
    return df
