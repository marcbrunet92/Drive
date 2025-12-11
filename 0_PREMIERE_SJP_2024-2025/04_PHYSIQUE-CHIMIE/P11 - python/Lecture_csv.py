''' Script de lecture d'un fichier de données sauvegardées en format CSV
    sur deux colonnes avec une seule ligne d'entête
    Leroy-Bury (2022)

    # À placer dans le répertoire de travail comme module
    # intégration par "from Lecture_csv_2col import LectureCSV"
'''
import pandas as pd
import numpy as np
#-------------------------------------------------------------------------------
def LectureCSV(fichier):
    # Récupération et lecture des données en évitant la ligne d'entête à partir
    # des données du fichier CSV sur deux colonnes
    try :
        data = pd.read_csv(fichier, sep = ';',skiprows=[0],names = ['x','y'])
    except :
        print("fichier de données absent ou non reconnu")
        # initialisation avec des zéros sur deux lignes et deux colonnes
        data = pd.DataFrame(0, index = [0, 1], columns = ['x', 'y'])

# Conversion en flottant avec le point en séparateur décimal
    L="xy"
    for var in L :
        try :
             data[var] = [x.replace(',', '.') for x in data[var]]
        except :
            pass
        data[var] = data[var].astype(np.float64)
# Création des listes des variables
    donnee1=data['x'].values.tolist()
    donnee2=data['y'].values.tolist()
# affichage du résultat sous forme d'un tableau
    print("\n Lecture du fichier de données %s sur 2 colonnes et 1 ligne d'entête"%fichier)
    print("\n ____________________ \n")
    print(data,"\n")
    return donnee1,donnee2

# Le programme principal--------------------------------------------
if __name__ == "__main__":
    print("Lecture d'un fichier de données sur 2 colonnes et 1 ligne d'entête")
    fichier=input("Quel est le nom du fichier de données (sans l'extension .csv) ?")+".csv"
    x,y=LectureCSV(fichier)


