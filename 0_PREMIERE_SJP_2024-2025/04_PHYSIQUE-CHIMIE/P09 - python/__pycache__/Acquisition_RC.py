""" étude de la charge d'un condensateur et mesure de la constante tau=RC
avec CONSTRUCTION PROGRESSIVE de la courbe de charge
Leroy-Bury (2022)"""

# Lecture de la tension aux borne du condensateur sur la broche A0
# Envoi de la tension de charge sur la broche D2
# Impédance de sortie de la carte R = 1 kohm - il faut ajouter +1k pour le calcul de C

# téléversement de "microcontroleurs.ino" dans l'arduino via l'IDE
# placer "microcontroleurs.py" dans le répertoire de travail de python
#-------------------------------------------------------------------------------
# bibliothèques nécessaires pour les acquisitions et le tracé du graphique
from drawnow import *
import matplotlib.pyplot as plt
from microcontroleurs import arduino
import time, sys
import numpy as np
import pandas as pd
#----------------- paramétrage de la communication -----------------------------
carte=arduino("/dev/cu.usbmodem14701") # à modifier en  fonction de la liaison USB vers l'arduino
#----------------- fonction d'affichage des valeurs ---------------------------
def plotValues():
    plt.grid ()
    plt.title("Charge d'un condensateur - circuit RC")
    plt.xlabel('Temps en secondes')
    plt.ylabel('tension')
    plt.plot(valeurs_t,valeurs_U)
#-------------------------------------------------------------------------------
#------------- programme principal ---------------------------------------------
valeurs_t = [] # dates en abcisse
valeurs_U = [] # tensions en ordonnée
plt.ion()
plt.figure(figsize=(5,5))
time.sleep(0.1) # durée d'établissement de la connexion sur le port série avec l'arduino
print("début de l'acquisition des mesures")
time.sleep(1)
# initialisation des variables et paramètres
m=0
N=100 # nombre de points de mesure
tau=0.00
Umax=5.000 # tension correspondant à l'état haut sur la broche numérique
Dt=0.0 # intervalle de temps supplémentaire entre deux mesures
# la boucle d'acqusition s'exécute entre 80 et 100 ms minimum
#------------------ lancement de l'acquisition ---------------------------------
t1=time.time() # date de début d'acquisition (temps machine)
carte.sortie_numerique(2,1) # place la sortie numérique 2 (D2) en état haut (1)
for i in range(N): # N points de mesure - intervalle Dt
    m=carte.entree_analogique(0) # lecture de la valeur numérique (1024 niveaux)
    t2=time.time()
    tension=round(Umax/1023*m,4) # conversion de la valeur numérique lue
    date=round(t2-t1,3)
    valeurs_t.append(date)
    valeurs_U.append(tension)
    drawnow(plotValues)
    time.sleep(Dt) # intervalle entre deux mesures successives
carte.sortie_numerique(2,0) # place la sortie numérique 2 (D2) en état bas (1)
carte.fermer() # fermeture du port de communication avec l'arduino
plt.ioff()
print("fin de l'acquisition des mesures")
print("durée de l'acquisition des mesures (s) : "+str(date)+" s")
#--------------- calcul de tau et affichage ------------------------------------
E=[]
for p in range(N):
    d=(valeurs_U[p]-0.63*Umax)**2
    E.append(d)
i=E.index(min(E))
tau=valeurs_t[i]
plt.text(0.5,0.5,'constante de temps : 'r'$\tau=%.3f$'%tau)
#-------------------affichage console de tau  ----------------------------------
print('temps caractéristique :'+str(tau)+' s')
#-------------- sauvegarde des données et de la courbe -------------------------
valeurs = {'date': valeurs_t,'tension': valeurs_U}
data = pd.DataFrame(valeurs)
print(data)
data.to_csv('charge_RC.csv',sep=';',index=False)
plt.savefig("charge_RC.png")
plt.show()
sys.exit()