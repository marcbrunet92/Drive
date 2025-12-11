'''' programme d'utilisation du Télémètre Ultrason (Console)
     pour déterminer la vitesse de propagation des ondes
     ultrasonores, la distance à l'écran étant connue.

    S'utilise avec :
     - Sciencethic 651 049 - Télémètre Ultrason fixe
     - Grove - Ultrasonic Ranger 101020010

     Leroy-Bury (2023)'''
##
# importations des bibliothèques et modules
from drawnow import *
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from microcontroleurs import arduino
import time, sys
import pandas as pd
from port_Arduino import port_Arduino
##
# fonction d'affichage des valeurs
def plotValues():
 textstr = r"$\Delta t (\mu s) = $"+str(dureeAllerRetourMoy)+"   "+r"$d_{ecran} (m) = $"+str(distanceEcran)
 gridspec.GridSpec(2,2)
 plt.subplot2grid((2,2), (0,0), colspan=2, rowspan=1)
 plt.grid (which='both')
 plt.figure ("mesure de célérité par télémétrie US",figsize=(12,8))
 fig=plt.plot(duree ,distance , "b+")
 plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
 plt.title("Mesure de la distance à l'écran en fonction de la durée aller-retour des US")
 plt.xlabel('durée aller-retour en s')
 plt.ylabel('distance écran en m')
 plt.subplot2grid((2,1), (1,0)) # Affichage de la durée aller-retour
 plt.xticks([])
 plt.yticks([])
 plt.text(0.1,0.5, textstr, bbox=dict(boxstyle='round', facecolor='wheat', alpha=1))
 plt.tight_layout()
##
# programme principal
# paramétrage de la communication avec Plug'Uino
port=port_Arduino()
carte=arduino(port)
time.sleep(0.1) # durée d'établissement de la connexion sur le port série avec l'arduino
# définition des broches de connexion entre le microcontroleur et le module US
broche_echo=2
broche_trig=2
# initialisation des paramètres
nomFichier="mesure_celerite_US"
N=0
duree=[]
distance=[]
# début de la boucle de lecture à la demande (en console)
nombreMesures=int(input("combien de points de mesures souhaitez-vous réaliser ? : "))
while N<nombreMesures :
    if input(
            "\n"
            "Appuyer sur \"entrée\" pour effectuer une mesure."
            "\n"
            "Saisir \"stop\" pour mettre fin à l'execution du programme."
            "\n"
    ) == "stop" :
        # Termine l'execution de la boucle d'acquisition.
        break
    distanceEcran=float(input("quelle est la distance à l'écran (en cm) ? : "))*1e-2
    Nmoy=5 # nombre de mesures à moyenner pour le calcul
    dureeAllerRetour=0
    for i in range(Nmoy) :
        # lecture de l'intervalle de temps mesuré par le télémètre ultrason (en µs)
        dureeAllerRetour=dureeAllerRetour+carte.module_us(broche_echo,broche_trig)
    # calcul de la valeur moyenne de la mesure sur Nmoy valeurs
    dureeAllerRetourMoy=dureeAllerRetour/Nmoy
    print("durée  moyenne d'un aller-retour' : ",dureeAllerRetourMoy," µs")
    duree.append(dureeAllerRetourMoy*1e-6)
    distance.append(distanceEcran)
    drawnow(plotValues)
    N=N+1
# Fermeture de la connexion à Plug'Uino avant de quitter.
carte.fermer()
print("fin de l'acquisition des mesures")
# sauvegarde des données et de la courbe
valeurs = {'distance écran (en m)': distance,'duree aller-retour (en s)': duree}
data = pd.DataFrame(valeurs)
print("\n ________________________________")
print("Récapitulatif des données saisies ")
print(data)
print("\n ________________________________")
print("sauvegarde des données dans le fichier %s.csv"%nomFichier)
data.to_csv(nomFichier+'.csv',sep=';',index=False)
print("\n ________________________________")
print("sauvegarde de la courbe dans le fichier %s.png"%nomFichier)
plt.savefig(nomFichier+'.png')
plt.show()
##
if sys.platform.startswith('darwin'):
    sys.exit()
