'''# Travaux pratiques P03 - Vecteur variation-de-vitesse et PFD
Leroy-Bury (2023)'''
import sys
from matplotlib.pyplot import *
from mpl_toolkits.axes_grid1 import host_subplot
import pandas as pd
import numpy as np
from fonctions_cinematique import *
##
# Le programme principal
nom_fichier=input("Quel est le nom du fichier de pointage (sans l'extension .csv)? : ")+".csv"
t0,x,y=LectureCSV(nom_fichier)
graphXY(t0,x,y)
vx,vy,v=calcul_vitesses_aval(t0,x,y)
t1=t0[:-1]
graphVxVy(t1,vx,vy)
representation_graphique(x,y,vx,vy)
show()
if sys.platform.startswith('darwin'):
    sys.exit()