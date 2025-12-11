import numpy as np
import matplotlib.pyplot as plt
from math import log10

# Valeurs expérimentales (U en volts et L en lux)
U = [0.2, 0.48, 0.78, 1.02, 1.18, 1.36, 1.62, 1.76, 1.88, 1.96]  # Tension en V
L = [0, 30, 60, 110, 150, 180, 300, 310, 360, 400]  # Eclairement en lux

# Exclure L = 0 de l'analyse (car log(0) n'est pas défini)
U_filtered = [u for i, u in enumerate(U) if L[i] > 0]
L_filtered = [l for l in L if l > 0]

# Calcul de Log(L) = log10(L)
LogL = [log10(l) for l in L_filtered]

# Calcul des coefficients de la droite de régression linéaire
K = len(U_filtered)
Umoy = sum(U_filtered) / K
LogLmoy = sum(LogL) / K
N = sum((U_filtered[i] - Umoy) * (LogL[i] - LogLmoy) for i in range(K))
D = sum((U_filtered[i] - Umoy)**2 for i in range(K))
a = N / D  # Coefficient directeur de la droite
b = LogLmoy - a * Umoy  # Ordonnée à l'origine de la droite

# Création du graphique
plt.figure(figsize=(10, 6))

# Tracé des points expérimentaux
plt.scatter(U_filtered, LogL, color='blue', label='Données expérimentales', zorder=5)

# Tracé de la droite de régression
x_vals = np.linspace(min(U_filtered), max(U_filtered), 100)
y_vals = a * x_vals + b
plt.plot(x_vals, y_vals, 'r-', label=f'Log(L) = {a:.3f} * U + {b:.3f}', zorder=10)

# Paramètres du graphique
plt.title("Étalonnage d'une photorésistance", fontsize=16, color='darkred')
plt.xlabel('Tension U (V)', fontsize=14)
plt.ylabel('Log(L) (sans unité)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Affichage du graphique
plt.show()
