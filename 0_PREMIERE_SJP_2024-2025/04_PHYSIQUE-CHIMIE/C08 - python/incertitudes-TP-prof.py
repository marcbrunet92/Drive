'''' résultats du titrage d'oxydoréduction (leroy-bury 2023)
calcul des incertitudes par la méthode de propagation'''
import numpy as np
##
# Données, à compléter de la manière suivante : [valeur , incertitude type sur la valeur]
#
Vfiole=[50, 0.05]    # exemple [50,0.05] en mL pour la dilution
Vpipette=[5,0.01]   # exemple [5,0.01] en mL pour la dilution
#
Vpreleve=[20,0.03]    # exemple [20,0.03]  en mL pour l'échantillon titré
Vburette=[25,0.03]   # exemple [25,0.03] en mL
Ctitra=[2e-2,5e-5]     # concentration de la solution titrante en mol.L-1
#
VE= 14.2    # volume à l'équivalence en mL
##
ulect=0.05 # incertitude de lecture 1/2 graduation en mL
ugoutte=0.05 # incertitude liée au volume d'une goutte (à la goutte près) en mL
utitrage=0 # incertitude estimée sur la détermination de VE par la méthode de titrage en mL
##
# Calcul de l'incertitude type sur le volume à l'équivalence (méthode des propagation)
uVE=np.sqrt((ulect)**2+(ulect+2*Vburette[1]+ugoutte+utitrage)**2)
##
# Calcul de la concentration de l'échantillon titré - a et b sont les nombres stœchiométriques
a=float(5)  # nombre stoechio réactif titré
b= float(1) # nombre stoechio réactif titrant
Cech=(a/b)*Ctitra[0]*(VE/Vpreleve[0])
##
# Calcul de l'incertitude type sur la concentration de l'échantillon titré (dilué)
uCech=Cech*np.sqrt((Ctitra[1]/Ctitra[0])**2+(Vpreleve[1]/Vpreleve[0])**2+(uVE/VE)**2)
##
# Calcul de la concentration en quantité et de son incertitude pour la solution concentrée
F=Vfiole[0]/Vpipette[0] # facteur de dilution
C0=F*Cech
UC0=2*C0*np.sqrt((uCech/Cech)**2+(Vpipette[1]/Vpipette[0])**2+(Vfiole[1]/Vfiole[0])**2)
##
# calcul de l'écart type et du Z-score
w=0.04 # teneur massique (g/g)
d=1.0 # densité
rho =998 # masse volumique de l'eau (g/L)
MFe=55.85 # masse molaire du fer (g/mol)
Cphyto=d*rho*w/MFe # concentration du produit phytosanitaire en ions Fe II
E=abs((Cphyto-C0)/Cphyto)*100 # écart-relatif
Z = abs((Cphyto-C0)/UC0) # Z-score
##
# affichage des résultats
print("\n _________________________________")
print("incertitude type sur le volume à l équivalence : %1.0e mL"% uVE)
print("concentration en quantité de l'échantillon titré : %.2e mol/L"% Cech)
print("incertitude type sur la concentration de l'échantillon titré : %1.0e mol/L"% uCech)
print("facteur de dilution : ",F)
print("\n concentration en quantité de la solution : %.2e mol/L"% C0)
print("incertitude sur la concentration de la solution : %1.0e mol/L"% UC0)
print("\n concentration théorique du produit phytosanitaire : %.2e mol/L"% Cphyto)
print("\n écart-relatif : %.1f"% E)
print("Z-score : %1.1f"% Z)
if Z<2 :
    print("\n l'écart relatif n'est pas significatif \n le titrage confirme la concentration de la solution commerciale")
else :
    print("l'écart relatif est significatif \n le titrage ne confirme pas la concentration de la solution commerciale")