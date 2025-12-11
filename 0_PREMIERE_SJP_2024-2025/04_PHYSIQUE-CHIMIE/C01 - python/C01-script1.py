# calcul de l'incertitude élargie sur la concentration en masse obtenue par dissolution - script 1
# importation de numpy alias np
import numpy as np
# incertitude sur la pesée
def inc_pesee(r):
    u=np.sqrt(2/3)*r # r est la résolution de la balance
    return u
# incertitude sur le volume jaugée
def inc_jauge(t):
    u=np.sqrt(1/3)*t #t est la tolérance de la verrerie
    return u
# programme principal ----------------------
print("Calcul de l'incertitude sur la concentration massique d'une solution préparée par dissolution d'un soluté solide")
m=float(input("Saisir la masse pesée en g : m = ")) # saisie de la masse
rm=float(input("Saisir la résolution de la balance en g : r = ")) # saisie de la résolution
V=float(input("Saisir le volume préparé en mL : V = ")) # saisie du volume de la fiole
tv=float(input("Saisir la tolérance de la jauge en mL : t = ")) # saisie de la tolérance de la fiole
# Calcul la concentration massique et de l'incertitude-type élargie
Cm=m/(V*1E-3) # concentration massique
Um=inc_pesee(rm)
UV=inc_jauge(tv)
UCm=2*Cm*np.sqrt((Um/m)**2+(UV/V)**2) # incertitude élargie sur la concentration massique
# affichage du résultat
print('Concentration massique de la solution : Cm= ',round(Cm,3),' ± ',round(UCm,3),' g/L')