'''étalonnage du capteur de pression
lecture sur une broche analogique d'un microcontrôleur type Arduino
capteur branché sur la broche analogique A0'''
# --- bibliothèques nécessaires pour les acquisitions et le traitement --------
from microcontroleurs import arduino , port_Arduino
import time, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
# ---------------- paramétrage de la communication ----------------------------
try:
    port=port_Arduino()
    carte=arduino(port)
except:
    port=input("Erreur de connexion  - sur quel port série est branché le microcontrôleur ? ")
    carte=arduino(port)
time.sleep(0.1)
# ----------------- mesures ---------------------------------------------------
tension=[]                     # liste des mesures du capteur de pression 0 - 5V
pression=[]                    # liste des pressions
time.sleep(1)
print("--------- début des mesures --------------")
poursuite=True
while poursuite:
    p=float(input('pression en hPa :'))
    pression.append(p)
    a=input('taper ENTER pour effectuer la mesure')
    mes_num=carte.entree_analogique(0) # lecture de la valeur numérique (1024 niveaux)
    mes_ana=np.round(5.00/1023*mes_num,4)
    tension.append(mes_ana)
    print('mesure : ',mes_ana)
    poursuite=input('nouvelle mesure o/n : ')
    if poursuite!='o' and poursuite!='O':
        poursuite=False
carte.fermer()                       # fermeture de la communication sur le port
# ------------- sauvegarde des données ----------------------------------------
nomFichier="etalonnage"
valeurs = {'tension (en V)': tension, 'pression (en hPa)': pression}
data = pd.DataFrame(valeurs)
print("________________________________")
print("Récapitulatif des données saisies ")
print(data)
print("________________________________")
print("sauvegarde des données dans le fichier %s.csv"%nomFichier)
data.to_csv(nomFichier+'.csv',sep=';',index=False)
# ------------- exploitation des données --------------------------------------
f = plt.figure()
ax=f.add_subplot(111)
# paramétrage du graphique
plt.plot(tension,pression,'ob')
plt.xlabel("Tension U (V)")
plt.ylabel("Pression p (hPa)")
plt.title("Etalonnage : p = f(U)")
plt.xlim(xmin=0)
plt.ylim(ymin=0)

# calcul et affichage de la régression linéaire
regression=linregress(tension,pression)
pente=regression[0]
ordonneeOrigine=regression[1]
mn=np.min(tension)
mx=np.max(tension)
Um=np.linspace(mn,mx,500)
pm=pente*Um+ordonneeOrigine
plt.plot(Um,pm,'-r')

# Affichage des valeurs de la pente et de l'ordonnée à l'origine
pente=round(pente,1)
ordonneeOrigine=round(ordonneeOrigine,1)
plt.text(0.05,0.9,"p = "+str(pente) + " x U + "+ str(ordonneeOrigine),
        size=12, ha="left",va="center",transform=ax.transAxes,
        bbox=dict(boxstyle="round",ec=("#350a4e"),fc=("#dfcbeb")))
plt.show()