''' Script de lecture d'un fichier de données sauvegardées en format CSV
    séparateur ; et décimal ,'''
''' Leroy-Bury (2022)'''
# À placer dans le répertoire de travail comme module
# Utilisation "from Lecture_csv import LectureCSV"

import pandas as pd
import numpy as np
#-------------------------------------------------------------------------------
def LectureCSV(fichier):
    # Récupération et lecture des données en évitant deux lignes d'entête à partir
    # des données du fichier CSV sur deux colonnes
    try :
        data = pd.read_csv(fichier, decimal=",",sep = ';',skiprows=[0],names = ['x','y','z'])
    except :
        print("fichier de données absent ou non reconnu")
        # initialisation avec des zéros sur deux lignes et trois colonnes
        data = pd.DataFrame(0, index = [0, 1], columns = ['x', 'y','z'])

# Conversion en flottant avec le point en séparateur décimal
    L="xyz"
    for var in L :
        try :
             data[var] = [x.replace(',', '.') for x in data[var]]
        except :
            pass
        data[var] = data[var].astype(np.float64)
# Création des listes des variables
    abscisse=data['x'].values.tolist()
    ordonnee1=data['y'].values.tolist()
    ordonnee2=data['z'].values.tolist()
# affichage du résultat sous forme d'un tableau
    print(data)
    return abscisse,ordonnee1,ordonnee2

# Le programme principal--------------------------------------------
if __name__ == "__main__":
    print("à utiliser comme un module")
    fichier=input("Quel est le nom du fichier de données (sans l'extension .csv) ?")+".csv"
    x,y,z=LectureCSV(fichier)



