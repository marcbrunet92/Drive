import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Lire les données depuis le fichier CSV
data = pd.read_csv('donnees.csv', delimiter=';', decimal=",")

# Extraire les colonnes et ajouter les points symétriques par rapport à l'axe Ox
x_sym = np.concatenate((data['x'].values, data['x'].values))
y_sym = np.concatenate((data['y'].values, -data['y'].values))
V_sym = np.concatenate((data['V'].values, data['V'].values))

# Définir une grille pour l'interpolation
xi = np.linspace(min(x_sym), max(x_sym), 100)
yi = np.linspace(min(y_sym), max(y_sym), 100)
xi, yi = np.meshgrid(xi, yi)

# Interpoler les données sur la grille
Vi = griddata((x_sym, y_sym), V_sym, (xi, yi), method='linear')

# Tracer les équipotentielles
plt.figure(figsize=(10, 6))
contour = plt.contour(xi, yi, Vi, levels=14, colors='black')
plt.clabel(contour, inline=1, fontsize=10)
plt.title('Cartographie du champ électrique')
plt.xlabel('x')
plt.ylabel('y')

# Définir les limites des axes
plt.xlim(0, 35)
plt.ylim(-10, 10)

# Ajouter les lignes en pointillés
for y_val in [3, 6, 9, -3, -6, -9]:
    plt.axhline(y=y_val, color='gray', linestyle='--', linewidth=0.5)

for x_val in [5, 10, 15, 20, 25, 30]:
    plt.axvline(x=x_val, color='gray', linestyle='--', linewidth=0.5)

# Ajouter les axes Ox et Oy
plt.axhline(y=0, color='black', linewidth=1)
plt.axvline(x=0, color='black', linewidth=1)

plt.show()
