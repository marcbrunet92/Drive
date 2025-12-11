''' Programme développé pour réaliser la construction de Bouasse pour
    déterminer la valeur de la distance focale d'une lentille sphérique mince

    Leroy-Bury (2023)

    # les données à traiter OF et OF' sont disponibles dans un fichier au
    format csv et la distance focale est mesurée sur le graphique'''
from matplotlib.pyplot import *
from mpl_toolkits.axes_grid1 import host_subplot
import pandas as pd
import numpy as np
from Lecture_csv import LectureCSV
import sys
##
nom_fichier=input("Quel est le nom du fichier de pointage (sans l'extension .csv)? : ")+".csv"
objet,image=LectureCSV(nom_fichier)
fig, ax = subplots(num="construction de Bouasse",nrows=1, ncols=1,figsize=(12,6))
grid(visible=True, which='major', color='b', linestyle='-')
grid(visible=True, which='minor', color='g', linestyle='--')
ax.axis("equal")
minorticks_on()
title('construction de Bouasse')
xlabel(r'$\overline{OA}$ en m')
ylabel(r"$\overline{OA'}$ en m")
for i in range(0,len(objet),1):
    axline((objet[i], 0), (0, image[i]),linewidth=1, color='r')
savefig("bouasse.png")
show()
if sys.platform.startswith('darwin'):
    sys.exit()