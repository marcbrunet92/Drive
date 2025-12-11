import numpy as np # bibliothèque des fonctions mathématiques
import scipy as sp  # bibliothèque des fonctions scientifiques
import pylab as pl
from scipy.optimize.minpack import curve_fit
##
# modifier les valeurs des listes ci-dessous
Duree=np.array([3.13,3.03,2.97,2.90,2.83,2.76,2.69]) # valeurs à modifier
Hauteur=np.array([0.50,0.47,0.45,0.43,0.41,0.39,0.37]) # valeurs à modifier
##
SqrDuree=(Duree)**2
LissageDuree=np.linspace(SqrDuree[0],SqrDuree[-1],20) # création d'un ensemble de points de la variable Duree pour le modèle

initial_p,initial_m=1,1 # valeurs initiales des paramètres de la modélisation
initial=[initial_p,initial_m] # organisation en tableau de valeurs
Affine=lambda SqrDuree,p,m,:p*SqrDuree+m # fonction lambda des paramètres Duree , p et m retournant la valeur de l'expression définie après les deux points :
params, cov=curve_fit(Affine,SqrDuree,Hauteur) # ajustement du modèle au tableau des valeurs en partant des valeurs initiales des paramètres
p,m=params # affectation des valeurs des paramètres
print("pente de l'affine ",p) # imprime les valeurs des paramètres calculés dans la console
print("ordonnée à l'origine ",m)
pl.clf() # efface la figure courante
AjustFonc=lambda t:p*t+m # définition de la fonction pour le calcul des valeurs du modèle
pl.plot(SqrDuree,Hauteur,'b.') # affichage des valeurs expérimentales en bleu avec des points séparés
pl.plot(LissageDuree,AjustFonc(LissageDuree),'r-')# affichage des valeurs modélisées en rouge avec des points liés
pl.xlabel('∆t² (s²)') # légende axe des abscisses
pl.ylabel('h (m)') # légende axe des ordonnées
pl.show() # ouverture de la fenêtre graphique (affichage de la figure)
