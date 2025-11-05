import pandas as pd
from src.preprocessing import remove_doublons, fill_missing_values, normalize_col
import pytest


# Etape 3 =====================================================

data = {
    "A" : [1, 2, 2, 6, None],
    "B" : [3, 6, 6, 8, 9]
}

sample_df = pd.DataFrame(data)



# Tester la Suppression des Doublons
def test_remove_doublons() :
    df_clean = remove_doublons(sample_df)
    assert df_clean.duplicated().sum() == 0, "Error lors du test"



# Tester le Remplissage des Valeurs Manquantes
def test_fill_missing_values() :
    df_clean = fill_missing_values(sample_df, "A", 0)
    assert df_clean["A"].isna().sum() == 0 and df_clean["A"].iloc[4] == 0



# Tester la Normalisation d'un Colonne
def test_normalize_col() :
    df_clean = normalize_col(sample_df, "B")
    assert df_clean["B"].min() == 0
    assert df_clean["B"].max() == 1



# Etape 4 - fixture =============================================

@pytest.fixture
def csv_df() :
    df = pd.read_csv("./data/camera.csv")
    return df

# Tester La Présence des Valeurs Manquantes
def test_missing_values(csv_df) :
    nb_missing = csv_df.isna().sum().sum()
    assert nb_missing > 0


# Tester La Présence des Doublons
def test_doublons(csv_df):
    nb_doublons = csv_df.duplicated().sum()
    assert nb_doublons > 0
    df_clean = remove_doublons(csv_df)
    assert df_clean.duplicated().sum() == 0




# Etape 5 - parametrize ==========================================

@pytest.mark.parametrize("col, upper, lower", [
    ("Release date", 2007, 1994),
    ("Price", 7999.0, 14.0)
])


# Tester l'Abscence des Outliers
def test_no_outliers(csv_df, col, upper, lower) :
    assert csv_df[col].between(lower, upper).all()