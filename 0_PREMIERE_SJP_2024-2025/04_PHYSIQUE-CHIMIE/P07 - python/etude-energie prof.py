''''# Etude des transferts d'énergie - oscillation d'un pendule
Leroy-Bury - 2023'''
##
# importation des bibliotheques
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Les fonctions------------------------------------------------------
def LectureCSV(fichier):
    # Récupération et lecture des données en évitant la ligne d'entête à partir
    # des données du fichier CSV sur deux colonnes
    try :
        data = pd.read_csv(fichier, sep = ';',skiprows=[0,1],names = ['x','y'])
    except :
        print("fichier de données absent ou non reconnu")
        # initialisation avec des zéros sur deux lignes et deux colonnes
        data = pd.DataFrame(0, index = [0, 1], columns = ['x', 'y'])

# Conversion en flottant avec le point en séparateur décimal
    L="xy"
    for var in L :
        try :
             data[var] = [x.replace(',', '.') for x in data[var]]
        except :
            pass
        data[var] = data[var].astype(np.float64)
# Création des listes des variables
    donnee1=data['x'].values.tolist()
    donnee2=data['y'].values.tolist()
# affichage du résultat sous forme d'un tableau
    print(data)
    return donnee1,donnee2

def graphique_angle(t,theta):
    plt.figure(num="oscillation angulaire",figsize=(16,8))
    plt.title("Oscillation du pendule autour de la position d'équilibre")
    plt.xlabel('t en (s)')
    plt.ylabel('angles en (rad)')
    plt.xlim(0,1.2*max(t))
    plt.ylim=(0,1.2*np.max(theta))
    plt.plot(t,theta,'r.-',label=r'$\theta$')
    plt.legend()
#
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
##
# Le programme principal
# récupération des données du pointage sous LatisPro
t,theta=LectureCSV('pendule_polaire.csv') # le nom du fichier
theta=np.radians(np.array(theta)) # conversion deg—>rad
M = 0.200 # la masse (kg) du pendule # à compléter avec la valeur
L = 0.489 # la longueur (m) du pendule # à compléter avec la valeur
g = 9.81 # l'intensité de la pesanteur (N/kg)
##
# calcul de la vitesse (méthode aval) ###############
# v, temps_v,theta_z = calcul_vitesses_aval(t,theta,L)
# calcul de la vitesse (méthode centrée) ############
v, temps_v,theta_z = calcul_vitesses_centre(t,theta,L)
##
Ec=np.array([]) # énergie cinétique
Ec=0.5*M*v**2 # à compléter avec l'expression correcte
##
Epp=np.array([]) # énergie potentielle de pensanteur
z=np.array([])
z=L*(1-np.cos(theta_z)) # à compléter avec l'expression correcte en theta_z
Epp=M*g*z # à compléter avec l'expression correcte
##
Em=np.array([]) # énergie mécanique
Em=Ec+Epp # à compléter avec l'expression correcte
Emoy=np.mean(Em)
Estd=np.std(Em)
print("valeur moyenne de l'énergie mécanique : ",round(Emoy,3)," J")
print("déviation standard de l'énergie mécanique : ",round(Estd,3)," J")
##
graphique_angle(t,theta)
plt.savefig("oscillations.png")
graphique_energie(Ec, Epp, Em, temps_v)
plt.savefig("transferts-energie.png")
plt.show()