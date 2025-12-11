# importation des bibliotheques
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
M = 0.200 # la masse (kg) du pendule
L = 0.489 # la longueur (m) du pendule
g = 9.81 # l'intensité de la pesanteur (N/kg)

# Les fonctions------------------------------------------------------
def graphique_angle(t,theta):
    plt.figure(num="oscillation angulaire",figsize=(16,8))
    plt.title("Oscillation du pendule autour de la position d'équilibre")
    plt.xlabel('t en (s)')
    plt.ylabel('angles en (rad)')
    plt.xlim(0,1.2*max(t))
    plt.ylim=(0,1.2*np.max(theta))
    plt.plot(t,theta,'r.-',label=r'$\theta$')
    plt.legend()

# noinspection PyBroadException
def lectureCSV(fichier):
    try:
        # Lecture du fichier CSV en passant directement les arguments nécessaires
        data = pd.read_csv(fichier, sep=';', skiprows=[0, 1], names=['x', 'y'], dtype={'x': str, 'y': str})
        data = data.replace({',': '.'}, regex=True).astype(float)
        print(data['x'].tolist(), data['y'].tolist())
        return data['x'].tolist(), data['y'].tolist()
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")
        return [], []

def graphique_energie(Ec, Epp, Em, t):
    plt.figure(num="transferts d'énergie",figsize=(16,8))
    plt.title("Evolution des formes d'énergies du pendule")
    plt.xlabel('t en (s)')
    plt.ylabel('Energies en (J)')
    plt.xlim(0,1.2*max(t))
    plt.ylim=(0,1.2*np.max(Em))
    plt.plot(t,Ec,'r.-',label=r'$E_c$')
    plt.plot(t,Epp,'b.-',label=r'$E_{pp}$')
    plt.plot(t,Em,'g.-',label=r'$E_m$')
    plt.legend()
# calcul de vitesse - méthode par l'aval
def calcul_vitesses_aval(temps,angle,rayon):
    omega=np.array([])
    temps=np.array(temps)
    angle=np.array(angle)
    omega=(angle[1:]-angle[:-1])/(temps[1:]-temps[:-1])
    v=rayon*omega
    temps=temps[:-1]
    angle=angle[:-1]
    return v,temps,angle
# calcul de vitesse - méthode centrée
def calcul_vitesses_centre(temps,angle,rayon):
    omega=np.array([])
    temps=np.array(temps)
    angle=np.array(angle)
    omega=(angle[2:]-angle[:-2])/(temps[2:]-temps[:-2])
    v=rayon*omega
    temps=temps[1:-1]
    angle=angle[1:-1]
    return v,temps,angle

t,theta=lectureCSV('pendule_polaire.csv')
theta=np.radians(np.array(theta)) # conversion deg—>rad

# calcul de la vitesse (méthode aval) ###############
v, temps_v,theta_z = calcul_vitesses_aval(t,theta,L)
# calcul de la vitesse (méthode centrée) ############
v, temps_v,theta_z = calcul_vitesses_centre(t,theta,L)

Ec=0.5*M*v**2

z=L*(1-np.cos(theta_z))
Epp=M*g*z

Em=Ec+Epp
Emoy=np.mean(Em)
Estd=np.std(Em)
print("valeur moyenne de l'énergie mécanique : ",round(Emoy,3)," J")
print("déviation standard de l'énergie mécanique : ",round(Estd,3)," J")

graphique_angle(t,theta)
plt.savefig("oscillations.png")
graphique_energie(Ec, Epp, Em, temps_v)
plt.savefig("transferts-energie.png")
plt.show()
if sys.platform.startswith('darwin'):
    sys.exit()