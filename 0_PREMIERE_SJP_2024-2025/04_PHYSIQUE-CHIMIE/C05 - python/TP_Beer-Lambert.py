''' C05 - dosage par étalonnage - Loi de Kohlraush
Leroy-Bury 2023'''
##
# importation des bibliothèques et modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import sys
from Lecture_csv import LectureCSV
##
# Les fonctions
# modèle d'ajustement linéaire
def modele(x,p):
	return p * x
##
# ajustement des données au modèle d'ajustement linéaire et renvoi de la valeur de la pente
def ajust_donnees(modele,Xmes,Ymes) :
    coeff,pcov =curve_fit(modele,Xmes,Ymes)
    incert = np.sqrt(np.diag(pcov))
    pente = coeff
    return pente,incert
##
# affichage des graphiques
def representation_graphique(fC,fG,fpente,fincert,Ames):
    plt.figure(num="courbe d'étalonnage – beer-Lambert",figsize=(16,8))
    plt.subplots_adjust(left=0.06, bottom=0.16, right=0.99, top=0.92,
                wspace=0.2, hspace=None)
    #------------------------------
    plt.subplot(1,3,1)
    plt.title('Absorbance A en fonction de la concentration en soluté C',fontsize=10)
    plt.xlabel('C (en moL/L)')
    plt.ylabel('A (640 nm)')
    plt.axis(xmin=0,xmax=1.2*max(fC),ymin=0,ymax=1.2*max(fG))
    plt.grid(linestyle="-.")
    plt.scatter(fC,fG,marker='+') # affichage des points de mesure
    #------------------------------
    plt.subplot(1,3,2)
    plt.title("modèle de l'absorbance A=f(C)")
    plt.xlabel('C (en moL/L)')
    plt.ylabel('A (640 nm)')
    plt.axis(xmin=0,xmax=1.2*max(fC),ymin=0,ymax=1.2*max(fG))
    plt.grid(linestyle="-.")
    plt.scatter(fC,fG,marker='+') # affichage des points calculés
    Cp = np.linspace(0,1.2*max(fC),100) # création d'une abscisse "continue"
    plt.plot(Cp,fpente*Cp,"r--") # affichage de la droite de regression
    Cmes=Ames/fpente # calcul de la concentration correspondant à la mesure de A
    UCmes=Cmes*fincert/fpente # incertitude combinée
    plt.annotate('A mesurée', xy=(0, Ames), xytext=(1.2*Cmes,Ames),arrowprops=dict(facecolor='blue', arrowstyle='->'))
    plt.annotate('C', xy=(Cmes, 0), xytext=(Cmes,1.2*Ames),arrowprops=dict(facecolor='blue', arrowstyle='->'))
    #-------------------------------
    plt.subplot(1,3,3,frameon=False) # Affichage des résultats de la régression
    plt.xticks([])
    plt.yticks([])
    plt.text(0.08,0.5,'concentration de la solution de bonbon (mol/L) : ' r'$C=$%1.3E'%Cmes)
    plt.text(0.08,0.4,'incertitude sur la concentration (mol/L) : ' r'$U(C)=$%1.1E'%UCmes)
    V=50e-3 # volume de dissolution (50 mL)
    M=566.7 # masse molaire du bleu patenté V en g/mol (donnée INRS)
    masse=V*M*Cmes
    Umasse=masse*UCmes/Cmes
    plt.text(0.08,0.3,'masse de bleu patenté (g) : ' r'$m=$%1.3E'%masse)
    plt.text(0.08,0.2,'incertitude sur la masse (g) : ' r'$U(m)=$%1.1E'%Umasse)
    #-------------------------------
    plt.tight_layout()
    plt.savefig('dosage_etalonnage.png')
    plt.show()
##
# Le programme principal
# Nom du fichier à traiter et extraction des mesures
nom_fichier=input("Quel est le nom du fichier de données (sans l'extension .csv)? : ")+".csv"
C=[]
A=[]
C,A=LectureCSV(nom_fichier)
# paramètres expérimentaux
Ames=float(input("Quelle est l'absorbance de la solution ? "))
pente,incert=ajust_donnees(modele,C,A)
representation_graphique(C,A,pente,incert,Ames)
if sys.platform.startswith('darwin'):
    sys.exit()