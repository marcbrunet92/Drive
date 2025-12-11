'''Travaux pratiques P03 - vecteur cinematique
fournit les principales fonctions pour le calcul et l'affichage
Leroy-Bury (2023) '''
from matplotlib.pyplot import *
from mpl_toolkits.axes_grid1 import host_subplot
import pandas as pd
import numpy as np
##
# Les fonctions
#––––––––––––––––––––––––––––––––––––––––––––––––––
def LectureCSV(fichier):
    # Récupération et lecture des données en évitant deux lignes d'entête à partir
    # des données du fichier CSV sur trois colonnes
    try :
        data = pd.read_csv(fichier, decimal=",",sep = ';',skiprows=[0,1],names = ['x','y','z'])
    except :
        print("fichier de données absent ou non reconnu")
        # initialisation avec des zéros sur deux lignes et trois colonnes
        data = pd.DataFrame(0, index = [0, 1], columns = ['x', 'y','z'])
    # Conversion en flottant avec le point en séparateur décimal
    L="xyz"
    for var in L :
        try :
             data[var] = [x.replace(',', '.') for x in data[var]]
        except :
            pass
        data[var] = data[var].astype(np.float64)
    # Création des listes des variables
    abscisse=data['x'].values.tolist()
    ordonnee1=data['y'].values.tolist()
    ordonnee2=data['z'].values.tolist()
    # affichage du résultat sous forme d'un tableau
    print(data)
    return abscisse,ordonnee1,ordonnee2
#–––––––––––––––––––––––––––––––––––––––––––––––––
def calcul_vitesses_aval(date,abscisses,ordonnees):
    x=np.array(abscisses) #
    y=np.array(ordonnees) #
    t=np.array(date) #
    v=[] # valeur approchée du module de la vitesse
    v_x=np.round((x[1:]-x[:-1])/(t[1:]-t[:-1]),2)   # abscisse de la vitesse
    v_y=np.round((y[1:]-y[:-1])/(t[1:]-t[:-1]),2)   # ordonnées de la vitesse
    v=np.round_(np.sqrt(v_x**2+v_y**2),2)           # norme de la vitesse
    t=t[:-1] # on enlève la dernière date pour laquelle il n'y a de valeur
    vitesse_data=pd.DataFrame({'Vx':v_x,'Vy':v_y,'V':v},index=t,dtype=float)
    print("valeurs de la vitesse - méthode par l'aval")   # affichage du résultat sous forme d'un tableau
    print(vitesse_data)
    return v_x,v_y,v
#–––––––––––––––––––––––––––––––––––––––––––––––––
def calcul_vitesses_cent(date,abscisses,ordonnees):     # méthode de calcul centrée [n+1]-[n-1]
    x=np.array(abscisses) #
    y=np.array(ordonnees) #
    t=np.array(date) #
    v=[] # valeur approchée du module de la vitesse
    v_x=np.round((x[2:]-x[:-2])/(t[2:]-t[:-2]),2)   # abscisse de la vitesse
    v_y=np.round((y[2:]-y[:-2])/(t[2:]-t[:-2]),2)   # ordonnées de la vitesse
    v=np.round_(np.sqrt(v_x**2+v_y**2),2)           # norme de la vitesse
    t=t[1:-1] # on enlève la première et la dernière date pour lesquelles il n'y a de valeur
    vitesse_data=pd.DataFrame({'Vx':v_x,'Vy':v_y,'V':v},index=t,dtype=float)
    print("valeurs de la vitesse - méthode centrée")   # affichage du résultat sous forme d'un tableau
    print(vitesse_data)
    return v_x,v_y,v
#–––––––––––––––––––––––––––––––––––––––––––––––––
def representation_graphique(x,y,v_x,v_y): # représentation des vecteurs
    fig, (ax1,ax2,ax3) = subplots(nrows=1, ncols=3,figsize=(12,6))
    #------------------------------
    subplot(1,2,1)
    g1, = ax1.plot(x, y, "g+")
    title('Vecteur vitesse instantannée')
    xlabel('x en (m)')
    ylabel('Altitude z en (m)')
    ax1.axis("equal")     # orthonormé
    xlim(min(x)-2,1.2*max(x))
    for i in range(0,len(v_x),1):
        V=quiver(x[i],y[i],v_x[i],v_y[i],units='xy',
         scale_units='xy',angles='xy', scale=10)
    #------------------------------
    subplot(1,2,2)
    g2, = ax2.plot(x, y, "g+")
    title('Variation du vecteur vitesse')
    xlabel('x en (m)')
    ylabel('Altitude z en (m)')
    xlim(min(x)-2,1.2*max(x))
    ax2.axis("equal")     # orthonormé
    for i in range(0,len(v_x)-1,1):
        DV=quiver(x[i],y[i],v_x[i+1]-v_x[i],v_y[i+1]-v_y[i],units='xy',
        scale_units='xy',angles='xy', scale=10, color='red')
    #------------------------------
    fig.tight_layout()
#----------------------------------------
def graphXY(t,x,y):          # Affichage des lois horaires du mouvement et de la trajectoire
    fig, (ax1,ax2) = subplots(nrows=1, ncols=2,figsize=(12,6))
    #------------
    subplot(1,2,1)
    grid()
    twin = ax1.twinx() # même axe des abscisses
    p1, = ax1.plot(t, x, "b+", label="coord. X")   # graphique n°1 - axe des ordonnées =ax1
    p2, = twin.plot(t, y, "r+", label="coord. Y")  # graphique n°2 - axe des ordonnées =twin
    min_axe=min(min(x),min(y))    # calcul des échelles graphiques
    max_axe=1.2*max(max(x),max(y))
    ax1.set_title('Coordonnées')   # paramétrage de la représentation graphique
    ax1.set_xlim(min(t), max(t)+t[1])
    ax1.set_ylim(min_axe, max_axe)
    ax1.set_xlabel("$date \; t$")
    ax1.set_ylabel("$x(t)$")
    ax1.yaxis.label.set_color(p1.get_color())
    twin.set_ylim(min_axe,max_axe)
    twin.set_ylabel("$y(t)$")
    twin.yaxis.label.set_color(p2.get_color())
    tkw = dict(size=4, width=1.5)
    ax1.tick_params(axis='y', colors=p1.get_color(), **tkw)
    ax1.tick_params(axis='x', **tkw)
    ax1.legend(handles=[p1, p2],loc='upper left')
    twin.tick_params(axis='y', colors=p2.get_color(), **tkw)
    #-------------
    subplot(1,2,2)
    grid()
    p3, = ax2.plot(x, y, "g+")    # graphique n°3 - axe des ordonnées =ax2
    ax2.set_title('Trajectoire')
    ax2.set_xlabel('x en (m)')
    ax2.set_ylabel('y en (m)')
    ax2.xaxis.label.set_color(p3.get_color())
    ax2.yaxis.label.set_color(p3.get_color())
    ax2.tick_params(axis='x', colors=p3.get_color(), **tkw)
    ax2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    ax2.set_xlim(min(x)-x[1],1.2*max(x))
    ax2.axis("equal")     # orthonormé
    #-------------
    fig.tight_layout()
#-------------------------------------
def graphVxVy(t,vx,vy):          # Affichage des lois horaires de la vitesse et de l'hodographe
    fig, (ax1,ax2) = subplots(nrows=1, ncols=2,figsize=(12,6))
    #------------
    subplot(1,2,1)
    grid()
    twin = ax1.twinx() # même axe des abscisses
    p1, = ax1.plot(t, vx, "b+", label="coord. Vx")   # graphique n°1 - axe des ordonnées =ax1
    p2, = twin.plot(t, vy, "r+", label="coord. Vy")   # graphique n°2 - axe des ordonnées =twin
    min_axe=min(min(vx),min(vy))    # calcul des échelles graphiques
    max_axe=1.2*max(max(vx),max(vy))
    ax1.set_title('Coordonnées')    # paramétrage de la représentation graphique
    ax1.set_xlim(min(t), max(t)+t[1])
    ax1.set_ylim(min_axe, max_axe)
    ax1.set_xlabel("$date \; t$")
    ax1.set_ylabel("$V_x(t)$")
    ax1.yaxis.label.set_color(p1.get_color())
    twin.set_ylim(min_axe,max_axe)
    twin.set_ylabel("$V_y(t)$")
    twin.yaxis.label.set_color(p2.get_color())
    tkw = dict(size=4, width=1.5)
    ax1.tick_params(axis='y', colors=p1.get_color(), **tkw)
    ax1.tick_params(axis='x', **tkw)
    ax1.legend(handles=[p1, p2],loc='upper left')
    twin.tick_params(axis='y', colors=p2.get_color(), **tkw)
    #-------------
    subplot(1,2,2)
    grid()
    p3, = ax2.plot(vx, vy, "g-+")    # graphique n°3 - axe des ordonnées =ax2
    for i in range(0,len(t),1):
        V=quiver(0,0,vx[i],vy[i],units='xy',scale_units='xy',angles='xy', scale=1)
    ax2.set_title('Hodographe')
    ax2.set_xlabel('Vx en (m)')
    ax2.set_ylabel('Vy en (m)')
    ax2.yaxis.label.set_color(p3.get_color())
    ax2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    ax2.xaxis.label.set_color(p3.get_color())
    ax2.tick_params(axis='x', colors=p3.get_color(), **tkw)
    ax2.set_xlim(-1.2*abs(min(vx)),1.2*abs(max(vx)))
    ax2.set_ylim(-1.2*abs(min(vy)),1.2*abs(max(vy)))
    ax2.axis("equal")     # orthonormé
    #-------------
    fig.tight_layout()
##