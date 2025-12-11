''' Modélisation affine d'un ensemble de données expérimentales'''
''' Leroy-Bury (2022)'''
##
# importation des bibliothèques
import sys
import numpy as np
import pylab as pl
from scipy.optimize.minpack import curve_fit
from Lecture_csv import LectureCSV
##
# chargement des données du fichier
fichier=input("Quel est le nom du fichier de données (sans l'extension .csv) ?")
x,t=LectureCSV(fichier+".csv")
d=2*np.array(x) # la distance parcourue est le double de celle à l'écran
# création d'un ensemble de points lissés de la variable t pour le modèle
liss_t=np.linspace(t[0],t[-1],20)
##
# valeurs initiales des trois paramètres de la modélisation
initial_a,initial_b=0.0,1.0
 # organisation en tableau de valeurs
initial=[initial_a,initial_b]
##
# fonction lambda des paramètres A,B et de la variable t retournant
# la valeur de l'expression définie après les deux points :
fonction=lambda t,A,B:A*t+B # modèle affine
##
# ajustement du modèle au tableau des valeurs en partant des valeurs initiales des paramètres
params, pcov=curve_fit(fonction,t,d,p0=initial)
perr = np.sqrt(np.diag(pcov))
# imprime les valeurs des paramètres calculés dans la console
A,B=params # affectation des valeurs des paramètres
print("\n _____________________________________")
print("A = ",f"{A:.3E}"," m/s","\nB = ",f"{B:.3E}"," m")
print("u(A) = ",f"{perr[0]:.1E}"," m/s","\nu(B) = ",f"{perr[1]:.1E}"," m")
##
# définition de la fonction avec les valeurs calculées du modèle (même expression que le modèle)
ajust_fonction=lambda t:A*t+B
##
# Affichage des courbes
fig=pl.figure(num="ajustement des données",figsize=(16,8))
ax = fig.add_subplot(111)
pl.grid(b=True, which='major', color='c', linestyle='-')
pl.grid(b=True, which='minor', color='g', linestyle=':')
pl.minorticks_on()
pl.title("modélisation affine - télémétrie US")
# affichage des valeurs expérimentales en bleu avec des points séparés
pl.plot(t,d,'b+')
# affichage des valeurs modélisées en rouge avec des points liés
pl.plot(liss_t,ajust_fonction(liss_t),'r-')
# légende axe des abscisses
pl.xlabel(r"retard $\tau\,(\mathrm{s})$")
pl.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
# légende axe des ordonnées
pl.ylabel(r"distance aller-retour $d (\mathrm{m})$")
# affichage des résultats dans la fenetre graphique
results = ('modèle affine : 'r'$d = A \tau + B$'' \n'
            f'\n$A$ = {A:.1f}'r'$\,\pm\,$'f'{perr[0]:.1f}\n'
            f'$B$ = {B:.1e}'r'$\,\pm \,$'f'{perr[1]:.1e}')
boite = dict(boxstyle='round', fc='blanchedalmond', ec='orange', alpha=0.7)
pl.text(0.2, 0.85, results, fontsize=10, bbox=boite, horizontalalignment='left',transform = ax.transAxes)
# ouverture de la fenêtre graphique (et sauvegarde de la figure)
pl.savefig(fichier+".png")
pl.show()
##
if sys.platform.startswith('darwin'):
    sys.exit()