#importation des modules
import numpy as np
import matplotlib.pylab as plt
import csv
import sys

#initialisation du pointage
table = []
#initialisation du temps en seconde
temps = []
#initialisation des abscisses
x = []
#initialisation des ordonnées
y = []

with open('roue.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        table.append(row)

#taille du tableau importé
N = len(table)
M = len(table[0])

#initialisation des constantes du problème
R = 0.26        #Rayon de la centrifugeuse en m
k = 6.26        #constante k en m.s-2
v0 = 0.33       #constante v0 en m.s-1
Dt = 0.040      #pas de temps en s

#Initialisation des vitesses
vx =np.zeros(N-2)       #vitesse calculée selon l'axe des abscisses
vy =np.zeros(N-2)       #vitesse calculée selon l'axe des ordonnées


#Initialisation des accélérations
ax =np.zeros(N-2)       #accélération calculée selon l'axe des abscisses
ay =np.zeros(N-2)       #accélération calculée selon l'axe des ordonnées


#Vérification de la structure de ce tableau (3 colonnes ont été exportées : temps, X et Y)
if M != 3 :
    print("Problème dans la réalisation de votre pointage. Reprenez le travail et exportez uniquement deux courbes (Mouvement_X et Mouvement_Y)")
    sys.exit()

#importation des coordonnées X, Y et temps
for i in range(1,N):
    #Génération des listes, avec transformation des données
    temps.append(float(table[i][0].replace(',','.')))
    x.append(float(table[i][1].replace(',','.')))
    y.append(float(table[i][2].replace(',','.')))

#Création d'une fonction permettant de tracer les vecteurs
def trace_vect(x,y,Vectx,Vecty,titre,couleur,position):
    q = plt.quiver(x,y,Vectx,Vecty,color = couleur,width=0.003,scale=20)
    plt.quiverkey(q, X=0.5, Y=position, U=1,label=titre, labelpos='E', color=couleur)

###########################################################
###         DEBUT DE LA PARTIE A MODIFIER               ###
###########################################################

#Calculs approchés des coordonnées des vitesses
for i in range(1,N-2):
    vx[i] =
    vy[i] =

#Calculs approchés des coordonnées des accélérations
for i in range(2,N-3):
    ax[i] =
    ay[i] =

###########################################################
###         FIN DE LA PARTIE A MODIFIER                 ###
###########################################################


#imposer la taille de la zone de travail
plt.figure(1, figsize=(9, 9))


if ay[N-4]!= 0 :
    #tracer les vecteurs vitesses calculées
    trace_vect(x[1:],y[1:],vx,vy,"Vecteur vitesse calculée",'g',1.09)

    #tracer les vecteurs accélérations calculées
    trace_vect(x[1:],y[1:],ax,ay,"Vecteur accélération calculée",'r',1.06)


#tracer les positions
plt.plot(x,y,"r.",label="Positions de la cabine")

#tracer le centre de rotation
plt.plot(0,0,"bo")

#tracer les rayons
for i in range(0,N-1):
    plt.plot([0, x[i]], [0, y[i]], 'k--', lw=0.2)

#position du bloc légende
plt.legend(loc='upper right')

#étiquettes des axes
plt.xlabel(r'$ x $'+' (m)')
plt.ylabel(r'$ y $'+' (m)')

#Titre du graphique
# plt.title('Positions et accélération de la cabine',loc='left')
plt.show()
if sys.platform.startswith('darwin'):
    sys.exit()