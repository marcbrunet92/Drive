''' Modélisation mathématique d'un ensemble de données expérimentales

Application à la relation de conjugaison de Descartes
Leroy-Bury (2023)'''
##import numpy as np # bibliothèque des fonctions mathématiques
import scipy as sp  # bibliothèque des fonctions scientifiques
import numpy as np
import pylab as pl
from scipy.optimize.minpack import curve_fit
from Lecture_csv import LectureCSV
import sys
##
# chargement des données du fichier
fichier=input("Quel est le nom du fichier de données (sans l'extension .csv) ?")
a,b=LectureCSV(fichier+".csv")
a=np.array(a)
b=np.array(b)
objet=1/a
image=1/b
# création d'un ensemble de points lissés de la variable objet pour le modèle
liss_obj=np.linspace(objet[0],objet[-1],20)
##
# valeurs initiales des trois paramètres de la modélisation
initial_a,initial_c=1.0,0.0
 # organisation en tableau de valeurs
initial=[initial_a,initial_c]
##
# fonction lambda des paramètres A,C et de la variable objet retournant
# la valeur de l'expression définie après les deux points :
exp_image=lambda objet,A,C:A*objet+C
##
# ajustement du modèle au tableau des valeurs en partant des valeurs initiales des paramètres
params, cov=curve_fit(exp_image,objet,image,p0=initial)
stdevs = np.sqrt(np.diag(cov))
# imprime les valeurs des paramètres calculés dans la console
A,C=params # affectation des valeurs des paramètres
print("-----------------------------------------")
print("\n modèle y = A x + B")
print("A = ",np.round(A,3), " ± ", np.round(stdevs[0],3))
print("C = ",np.round(C,3), " ± ", np.round(stdevs[1],3))
print("distance focale (cm) f'=",np.round(100/C,2)," ± ",np.round(100*stdevs[1]/C**2,2))
##
# définition de la fonction avec les valeurs calculées du modèle (même expression que le modèle)
best_fit=lambda objet:A*objet+C
##
# Affichage des courbes
fig=pl.figure(num="modélisation relation de conjugaison de Descartes",figsize=(16,8))
ax = fig.add_subplot(111)
pl.grid(visible=True, which='major', color='b', linestyle='-')
pl.grid(visible=True,which='minor', color='g', linestyle=':')
pl.minorticks_on()
pl.title("modélisation des données expérimentales")
# affichage des valeurs expérimentales en bleu avec des points séparés
pl.plot(objet,image,'b.')
# affichage des valeurs modélisées en rouge avec des points liés
pl.plot(liss_obj,best_fit(liss_obj),'r-')
# légende axe des abscisses
pl.xlabel(r"$x=\dfrac{1}{\overline{\mathrm{OA}}}\,(\mathrm{m^{-1}})$")
# légende axe des ordonnées
pl.ylabel(r"$y=\dfrac{1}{\overline{\mathrm{OA'}}}\, (\mathrm{m^{-1}})$")
# affichage des résultats dans la fenetre graphique
results = ('modèle y = A x + C \n'
            f'\n$A$ = {A:.2f}'r'$\pm$'f'{stdevs[0]:.2f}\n'
            f'$C$ = {C:.2f}'r'$\pm$'f'{stdevs[1]:.2f}')
boite = dict(boxstyle='round', fc='blanchedalmond', ec='orange', alpha=0.7)
pl.text(0.2, 0.85, results, fontsize=10, bbox=boite, horizontalalignment='left',transform = ax.transAxes)
# ouverture de la fenêtre graphique (et sauvegarde de la figure)
pl.savefig(fichier+".png")
pl.show()
if sys.platform.startswith('darwin'):
    sys.exit()
