""" étude de la charge d'un condensateur et mesure de la constante tau=RC
avec AFFICHAGE FINAL de la courbe de charge
Leroy-Bury (2022)"""

# Lecture de la tension aux borne du condensateur sur la broche A0
# Envoi de la tension de charge sur la broche D2
# Impédance de sortie de la carte R = 1 kohm - il faut ajouter +1k pour le calcul de C
#
# téléversement de "microcontroleurs.ino" dans l'arduino via l'IDE
# placer "microcontroleurs.py" dans le répertoire de travail de python
#-------------------------------------------------------------------------------
# bibliothèques nécessaires pour les acquisitions et le tracé du graphique
import matplotlib.pyplot as plt
from microcontroleurs import arduino
import time, sys
import numpy as np
import pandas as pd
#----------------- paramétrage de la communication -----------------------------
carte=arduino("/dev/cu.usbmodem14701") # à modifier en  fonction de la liaison USB vers l'arduino
#----------------- fonction d'affichage des valeurs ---------------------------
def plotValues(valeurs_t,valeurs_U,tau):
    plt.grid ()
    plt.title("Charge d'un condensateur - circuit RC")
    plt.xlabel('Temps en secondes')
    plt.ylabel('tension')
    plt.plot(valeurs_t,valeurs_U,'r+')
    plt.text(0.2,0.05,'constante de temps : 'r'$\tau=%.3f$'%tau)
#------------- programme principal ---------------------------------------------
valeurs_t = [] # dates en abcisse
valeurs_m = [] # tensions en ordonnée
plt.figure(figsize=(5,5))
time.sleep(0.1) # durée d'établissement de la connexion sur le port série avec l'arduino
print("début de l'acquisition des mesures")
time.sleep(1)
# -------  initialisation des variables et paramètres --------------------------
m=0
N=10 # nombre de points de mesure
tau=0.00
Umax=5.000 # tension correspondant à l'état haut sur la broche numérique
Dt=0.5 # intervalle de temps supplémentaire entre deux mesures
# la boucle d'acqusitions s'exécute entre 8 et 9 ms minimum
#------------------- lancement de l'acquisition --------------------------------
t1=time.time() # date de début d'acquisition (temps machine)
carte.sortie_numerique(2,1) # place la sortie numérique 2 (D2) en état haut (1)
for i in range(N): # N points de mesure - intervalle Dt
    m=carte.entree_analogique(0) # lecture de la valeur numérique (1024 niveaux)
    t2=time.time()
    date=round(t2-t1,3)
    valeurs_t.append(date)
    valeurs_m.append(m)
    time.sleep(Dt) # intervalle entre deux mesures successives
carte.sortie_numerique(2,0) # place la sortie numérique 2 (D2) en état bas (1)
carte.fermer() # fermeture du port de communication avec l'arduino
print("fin de l'acquisition des mesures")
print("durée de l'acquisition des mesures (s) : "+str(date)+" s")
# ----------------conversion de la valeur numérique lue en tension -------------
MesNum=np.array(valeurs_m)
tension=np.round(Umax/1023*MesNum,4)
#-------------------------------------------------------------------------------
E=[]
for p in range(N):
    d=(valeurs_m[p]-int(0.63*1023))**2
    E.append(d)
i=E.index(min(E))
tau=valeurs_t[i]
#-------------------------------------------------------------------------------
print('temps caractéristique :'+str(tau)+' s')
plotValues(valeurs_t,tension,tau)
#-------------------------------------------------------------------------------
valeurs = {'date': valeurs_t,'tension': tension}
data = pd.DataFrame(valeurs)
print(data)
data.to_csv('charge_RC_2.csv',sep=';',index=False)
plt.savefig("charge_RC_2.png")
plt.show()
sys.exit()