# Affichage du nom du programme
print("_________________________________________________________")
print("Etalonnage d'une photorésistance")
print("_________________________________________________________")

# Importation des bibliothèques
import matplotlib.pyplot as plt
import numpy as np
from math import log10

# Valeurs expérimentales (U en volts et L en lux)
U = [0.2, 0.48, 0.78, 1.02, 1.18, 1.36, 1.62, 1.76, 1.88, 1.96]  # Tension en V
L = [0, 30, 60, 110, 150, 180, 300, 310, 360, 400]  # Eclairement en lux

# Exclure L = 0 de l'analyse (car log(0) n'est pas défini)
U_filtered = [u for i, u in enumerate(U) if L[i] > 0]
L_filtered = [l for l in L if l > 0]

# Nombre de points expérimentaux après exclusion
K = len(U_filtered)

# Calcul de Log(L) = log10(L)
LogL = [log10(l) for l in L_filtered]

# Affichage des valeurs expérimentales et du nombre de points
print("**********************************************")
print("valeurs de U : ", U_filtered)
print("valeurs de Log(L) : ", LogL)
print("Il y a ", K, " couples de points")
print("**********************************************")

# Initialisation des variables pour le calcul de la droite de régression
Umoy = sum(U_filtered) / K
LogLmoy = sum(LogL) / K
N = sum((U_filtered[i] - Umoy) * (LogL[i] - LogLmoy) for i in range(K))
D = sum((U_filtered[i] - Umoy)**2 for i in range(K))
a = N / D  # Coefficient directeur de la droite
b = LogLmoy - a * Umoy  # Ordonnée à l'origine de la droite

# Calcul de la constante C pour la formule L = C * 10^(a * U)
C = 10**b
A = round(a, 3)
B = round(b, 3)
C = round(C, 3)

# Affichage de l'équation
print("L'équation de la droite est: Log(L) = ", A, "x U +", B)
print("La formule à utiliser est: L = ", C, "x 10^(", A, "x U)")

# Initialisation de la figure pour le graphique
fig, ax = plt.subplots()

# Tracé des axes, labels et titre du graphique
plt.axis([min(U_filtered), max(U_filtered), min(LogL), max(LogL)])
plt.xlabel('U (V)', color='green', fontsize=20)
plt.ylabel('Log(L) (sans unité)', color='green', fontsize=20)
plt.title("Etalonnage d'une photorésistance", color='red', fontsize=10)
plt.grid()

# Tracé des points expérimentaux
plt.scatter(U_filtered, LogL, marker='o', color='r', linewidth=4)

# Tracé de la droite de régression
x = np.linspace(min(U_filtered), max(U_filtered), 200)
y = a * x + b
plt.plot(x, y, linewidth=2)

# Ecriture de l'équation de la droite sur le graphique
plt.text((max(U_filtered) + min(U_filtered)) / 2, max(LogL) - (max(LogL) - min(LogL)) * 0.1,
         f"Log(L) = {A} x U + {B}", color='green', fontsize=10, horizontalalignment='center')

# Affichage du graphique
plt.show()

# Sauvegarde de la figure dans le dossier où se trouve le programme
fig.savefig("Etalonnage_d'une_photorésistance.png")

print("********************************************************")
print("Fin du programme")
