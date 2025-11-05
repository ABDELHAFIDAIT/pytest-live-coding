# <center style="color:green;">**Live Coding - PyTest**</center>

L’objectif de ce Live Coding est de montrer comment valider automatiquement les étapes de prétraitement des données à l’aide de tests **Pytest**, afin d'évalue à quel point un dataset est fiable, complet, cohérent et utile pour un usage donné(analyse, IA, reporting, etc.).


## <span style="color:orange;">**Consigne :**</span>

### **Etape 1 - Introduction et installation :**

- ``Pytest`` comme un outil léger et puissant pour automatiser les tests Python.

- La différence entre les tests manuels (visuels, dans Jupyter) et les tests automatisés.


### **Etape 2 - Création des Fonctions à Tester :**

Construire un petit module ``preprocessing.py`` contenant des fonctions simples.

Chaque fonction représente une étape du pipeline de préparation :

- Suppression des doublons,
- Remplissage des valeurs manquantes,
- Normalisation de colonnes numériques.


### **Étape 3 – Création des Premiers Tests Unitaires :**

- Tester la suppression des doublons.

- Tester le remplissage des valeurs manquantes.

### **Étape 4 – Introduction des Fixtures :**

- Créer une fixture pour le DataFrame de test.

- Écrire un fixture pour lire un fichier CSV, le stocker dans un DataFrame et le retourner.

- Vérifier si le DataFrame contient des valeurs manquantes.

- Vérifier les doublons.


### **Étape 5 – Paramétrisation des Tests :**

- Vérifier l’absence d’outliers avec ``@pytest.mark.parametrize`` après nettoyage.