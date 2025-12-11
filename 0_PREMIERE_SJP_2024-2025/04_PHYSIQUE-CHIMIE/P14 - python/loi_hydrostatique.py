'''LOI DE L HYDROSTATIQUE
lecture sur une broche analogique d'un microcontrôleur type Arduino
capteur branché sur la broche analogique A1'''
##
#  importation des bibliothèques et modules
from microcontroleurs import arduino,port_Arduino
import time, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
##
# paramétrage de la communication avec l'arduino
try:
    port=port_Arduino()
    carte=arduino(port)
except:
    port=input("Erreur de connexion  - sur quel port série USB est branché le microcontrôleur ? ")
    carte=arduino(port)
time.sleep(0.1)
##
# initialisation
pression=[]                   # liste des pressions
profondeur=[]                 # liste des profondeurs
broche=1 # broche analogique A1 pour le capteur
time.sleep(1)
print("\n --------- début des mesures --------------\n")
poursuite=True
carte.sortie_numerique(13,1) # allume la led pour le début des mesures
##
# mesures avec saisie au clavier de la profondeur
while poursuite:
    prof=1e-2*float(input('saisir la profondeur en centimètre ––> '))   # saisie de la profondeur
    profondeur.append(prof)             # enregistrement de la profondeur dans la liste
    a=input('valider en appuyant entrée pour effectuer la mesure')
    mes_num=carte.entree_analogique(broche) # lecture de la valeur numérique (1024 niveaux)
    pression.append(mes_num/1023*5000)  # calcul pression en fonction du modèle du capteur
    poursuite=input('nouvelle mesure o/n : ')
    if poursuite!='o' and poursuite!='O':
        poursuite=False
carte.sortie_numerique(13,0) # éteind la led pour la fin des mesures
carte.fermer()                      # fermeture de la communication sur le port
##
# sauvegarde des données
nomFichier="hydrostatique"
valeurs = {'profondeur (en m)': profondeur,'pression (en V)': pression}
data = pd.DataFrame(valeurs)
print("________________________________")
print("Récapitulatif des données saisies \n")
print(data)
print("________________________________")
print("\n sauvegarde des données dans le fichier %s.csv"%nomFichier)
data.to_csv(nomFichier+'.csv',sep=';',index=False)
##
# exploitation des données et modélisation affine
fig= plt.figure(figsize =(14,10),num="loi de l'hydrostatique")
regression = np.polyfit(profondeur, pression, 1)    # régression linéaire
f_reg=np.poly1d(regression)                         # initialisation de la fonction modèle affine
plt.plot(profondeur,pression,'+',label='mesures')   # tracé des valeurs expérimentales
x=np.linspace(0,1.2*max(profondeur),50)             # création des abcisses pour le tracé du modèle
plt.plot(x,f_reg(x),'-',color='r',label='régression linéaire')      # tracé du modèle
plt.title('$\Delta p=f(\Delta z)$')  # titre de la figure
plt.xlim(0, 1.2*max(profondeur))    # paramétrage axe des abscisses entre 0 et 1,2*profondeur max
plt.ylim(0, 1.2*max(pression))      # paramétrage axe des ordonnées entre 0 et 1,2*pression max
plt.xlabel('profondeur $\Delta \, z(m)$')        # légendes des axes
plt.ylabel('$\Delta p\,(Pa)$')
plt.legend(loc='lower right',fontsize=12) # paramétrages de la légende
# Affichage en consolde des valeurs de la pente et de l'ordonnée à l'origine
pente=round(regression[0],1)
ordonneeOrigine=round(regression[1],1)
print(r"$\Delta p$ = "+str(pente) + " $\times \Delta z$ + "+ str(ordonneeOrigine))
# sauvegarde des courbes
print("\n________________________________")
print("\n sauvegarde de la courbe dans le fichier %s.png"%nomFichier)
plt.savefig(nomFichier+'.png',dpi=150)
plt.show()                                # tracé de la figure
##
if sys.platform.startswith('darwin'):
    sys.exit()