''' Travaux pratiques P03 - mouvement parabolique - modèle trajectoire'''
import sys
import numpy as np # bibliothèque des fonctions mathématiques
import scipy as sp  # bibliothèque des fonctions scientifiques
from scipy.optimize.minpack import curve_fit
from fonctions_cinematique import *
##
# Le programme principal
nom_fichier=input("Quel est le nom du fichier de pointage (sans l'extension .csv)? : ")+".csv"
t0,x,y=LectureCSV(nom_fichier)
#---------------
initial_a,initial_b,initial_c=1,1,1 # valeurs initiales des paramètres de la modélisation
initial=[initial_a,initial_b,initial_c] # organisation en tableau de valeurs
parabole=lambda x,a,b,c:a*x**2+b*x+c # fonction lambda des paramètres x,a,b,c retournant la valeur de l'expression définie après les deux points :
params, cov=curve_fit(parabole,x,y,p0=initial) # ajustement du modèle au tableau des valeurs en partant des valeurs initiales des paramètres
print("valeurs des paramètres de la trajectoire parabolique ax2+bx+c")
print(params)
#--------------
graphXY(t0,x,y)
vx,vy,v=calcul_vitesses_aval(t0,x,y)
t1=t0[:-1]
graphVxVy(t1,vx,vy)
representation_graphique(x,y,vx,vy)
show()
if sys.platform.startswith('darwin'):
    sys.exit()