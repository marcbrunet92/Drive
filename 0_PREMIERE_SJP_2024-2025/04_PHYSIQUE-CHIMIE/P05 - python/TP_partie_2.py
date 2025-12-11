import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lire les données depuis le fichier CSV
data = pd.read_csv('donnees.csv', delimiter=';', decimal=',')

# Extraire les colonnes x et phi
subset = data[data['y'] == 0]
x, phi = subset['x'].values, subset['V'].values

# Calculer la pente de la droite de régression passant par l'origine
slope = np.sum(x * phi) / np.sum(x**2)

# Calculer les valeurs ajustées de phi
phi_fit = slope * x

# Tracer le graphique
plt.plot(x, phi, 'bo-', label="$f(x)=\\varphi$")
plt.plot(x, phi_fit, 'r-', label=f"f(x)={slope:.3f}*x")
plt.xlabel("Position $x$ (cm)")
plt.ylabel("$\\varphi(x)$ (V)")
plt.title("Potentiel électrique $f(x)=\\varphi$")
plt.legend()
plt.grid()
plt.show()
