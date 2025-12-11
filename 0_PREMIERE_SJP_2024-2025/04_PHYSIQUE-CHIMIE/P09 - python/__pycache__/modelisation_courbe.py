''' Modélisation mathématique d'un ensemble de données expérimentales'''
''' Leroy-Bury (2022)'''
import sys
import numpy as np # bibliothèque des fonctions mathématiques
import scipy as sp  # bibliothèque des fonctions scientifiques
import pylab as pl
from scipy.optimize.minpack import curve_fit
from Lecture_csv import LectureCSV
#-------------------------------------------------------------------------------
# chargement des données du fichier
fichier=input("Quel est le nom du fichier de données (sans l'extension .csv) ?")+".csv"
date,tension=LectureCSV(fichier)
# création d'un ensemble de points lissés de la variable t pour le modèle
liss_t=np.linspace(date[0],date[-1],20)
#-------------------------------------------------------------------------------
# valeurs initiales des trois paramètres de la modélisation
initial_a,initial_b,initial_c=1.0,-1.0,0.0
 # organisation en tableau de valeurs
initial=[initial_a,initial_b,initial_c]
#-------------------------------------------------------------------------------
# fonction lambda des paramètres A,B,C et de la variable date retournant
# la valeur de l'expression définie après les deux points :
exp_decay=lambda date,A,B,C:A*np.exp(date*B)+C
#-------------------------------------------------------------------------------
# ajustement du modèle au tableau des valeurs en partant des valeurs initiales des paramètres
params, cov=curve_fit(exp_decay,date,tension,p0=initial)
# imprime les valeurs des paramètres calculés dans la console
A,B,C=params # affectation des valeurs des paramètres
print("A = ",np.round(A,3)," B = ",np.round(B,3)," C = ", np.round(C,3))
#-------------------------------------------------------------------------------
# définition de la fonction avec les valeurs calculées du modèle (même expression que le modèle)
best_fit=lambda date:A*np.exp(date*B)+C
#-------------------------------------------------------------------------------
# efface la figure courante
pl.clf()
pl.grid()
pl.title("modélisation des données expérimentales")
# affichage des valeurs expérimentales en bleu avec des points séparés
pl.plot(date,tension,'b.')
# affichage des valeurs modélisées en rouge avec des points liés
pl.plot(liss_t,best_fit(liss_t),'r-')
# légende axe des abscisses
pl.xlabel('temps (s)')
# légende axe des ordonnées
pl.ylabel('tension (V)')
# ouverture de la fenêtre graphique (et sauvegarde de la figure)
pl.savefig(fichier+".png")
pl.show()
sys.exit()
