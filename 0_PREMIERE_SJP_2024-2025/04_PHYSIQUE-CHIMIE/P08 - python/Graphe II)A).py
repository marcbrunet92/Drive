import numpy as np
import matplotlib.pyplot as plt

# Données mesurées
I = np.array([1.04, 1.01, 0.97, 0.88, 0.75, 0.571, 0.391, 0.24, 0.136, 0.072])  # Courant en mA
Us = np.array([4.87, 4.75, 4.52, 4.12, 3.5, 2.67, 1.85, 1.14, 0.63, 0.34])  # Tension en V

# Conversion du courant en A pour le calcul de la résistance
I_A = I / 1000  # Conversion de mA en A

# Calcul de la résistance de la photorésistance (R_photo = Us / I)
R_photo = Us / I_A  # Résistance en Ohms

# Calcul du modèle linéaire (ajustement)
coefficients = np.polyfit(I_A, Us, 1)  # Ajustement linéaire : Us = R_photo * I
slope = coefficients[0]  # Coefficient directeur (la résistance)
intercept = coefficients[1]  # L'ordonnée à l'origine (devrait être proche de zéro si le modèle est linéaire)

# Générer la courbe ajustée pour Us = R_photo * I
I_A_fit = np.linspace(min(I_A), max(I_A), 100)
Us_fit = slope * I_A_fit + intercept

# Création du graphique
plt.figure(figsize=(8, 6))

# Tracé des points mesurés
plt.scatter(I, Us, color='blue', label='Données mesurées', zorder=5)

# Tracé de la courbe linéaire ajustée
plt.plot(I_A_fit * 1000, Us_fit, 'r-', label=f'Modèle linéaire \n Us = R_photo * I = {slope:.2f} * I', zorder=10)

# Paramètres du graphique
plt.title('Relation entre la tension Us et le courant I avec modèle linéaire \n (condition d\'éclairage intense)')
plt.xlabel('Courant I (mA)')
plt.ylabel('Tension Us (V)')
plt.legend()
plt.grid(True)

# Affichage du graphique
plt.show()

# Affichage des résultats
print(f"Modèle linéaire : Us = {slope:.2f} * I + {intercept:.2f}")
