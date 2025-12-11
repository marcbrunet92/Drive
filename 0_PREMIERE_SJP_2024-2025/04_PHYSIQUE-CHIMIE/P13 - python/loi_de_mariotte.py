'''LOI DE MARIOTTE
lecture sur une broche analogique d'un microcontrôleur type Arduino
capteur branché sur la broche analogique A0'''
# bibliothèques nécessaires pour les acquisitions et le tracé du graphique
from microcontroleurs import arduino , port_Arduino
import time, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
#----------------- paramétrage de la communication ----------------------------
try:
    port=port_Arduino()
    carte=arduino(port)
except:
    port=input("Erreur de connexion  - sur quel port série est branché le microcontrôleur ? ")
    carte=arduino(port)
time.sleep(0.1)
#------------------------------- mesures --------------------------------------
vol_tube=3.0 # À modifier pour tenir compte du volume du tube de jonction
#              entre la seringue et le capteur (en mL)
pression=[]                   # liste des pressions
volume=[]                     # liste des volumes
time.sleep(1)
print("--------- début des mesures --------------")
poursuite=True
while poursuite:
    vol_lu=float(input('volume en mL :'))
    v=vol_lu+vol_tube
    volume.append(v)
    a=input('taper ENTER pour effectuer la mesure')
    mes_num=carte.entree_analogique(0) # lecture de la valeur numérique (1024 niveaux)
    tension=np.round(5.00/1023*mes_num,4)
    print('mesure : ',tension)
    pression.append(498.6*tension + 116)  # équation à modifier selon étalonnage du capteur
    poursuite=input('nouvelle mesure o/n : ')
    if poursuite!='o' and poursuite!='O':
        poursuite=False
carte.fermer()                      # fermeture de la communication sur le port
#-------------- sauvegarde des données ----------------------------------------
nomFichier="Mariotte"
valeurs = {'volume (en mL)': volume,'pression (en V)': pression}
data = pd.DataFrame(valeurs)
print("________________________________")
print("Récapitulatif des données saisies ")
print(data)
print("________________________________")
print("sauvegarde des données dans le fichier %s.csv"%nomFichier)
data.to_csv(nomFichier+'.csv',sep=';',index=False)
#--------------- exploitation des données et modélisation ----------------------
fig = plt.figure(num="loi de mariotte", figsize =(10,10))
p=np.array(pression)
V=np.array(volume)
# affichage du premier graphique : proposition p = k V
ax1 = plt.subplot2grid((18,18),(0,0),rowspan =7,colspan=8)
ax1.set_title('p = f(V)',color='blue',fontsize=16)
ax1.set_xlabel('Volume (mL)', color='grey')
ax1.set_ylabel('Pression (en hPa)', color='grey')
plt.plot(V,p,'or:')
# affichage du deuxième graphique : proposition V = k p
ax2 = plt.subplot2grid((18,18),(0,10),rowspan =7,colspan=8)
ax2.set_title('V = f(p)',color='blue',fontsize=16)
ax2.set_xlabel('Pression (en hPa)', color='grey')
ax2.set_ylabel('Volume (mL)', color='grey')
plt.plot(p,V,'or:')
# affichage du troisième graphique : proposition p V = k
ax3 = plt.subplot2grid((18,18),(10,5),rowspan =7,colspan=8)
ax3.set_title('p V = f(V)',color='blue',fontsize=16)
ax3.set_ylabel('p V (mL.hPa)', color='grey')
ax3.set_xlabel('Volume (en mL)', color='grey')
ax3.set_ylim(0,250000)
plt.plot(V,p*V,'or:')
# sauvegarde des courbes
print("________________________________")
print("sauvegarde de la courbe dans le fichier %s.png"%nomFichier)
plt.savefig(nomFichier+'.png')
plt.show()
sys.exit()
