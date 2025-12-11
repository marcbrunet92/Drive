import numpy as np
import matplotlib.pyplot as plt

# Données
r = np.array([125, 250, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000])  # Résistance en Ω
I = np.array([4.41, 3.98, 3.32, 2.49, 1.66, 1.00, 0.55, 0.295, 0.152, 0.077])  # Courant en mA
Us = np.array([0.55, 0.98, 1.65, 2.48, 3.32, 4.00, 4.40, 4.69, 4.85, 4.93])  # Tension en V

# Paramètres du pont diviseur
Ue = 5.00  # Tension d'entrée en V
Rp = 1000  # Résistance fixe en Ω

# Modèles théoriques
r_fit = np.logspace(np.log10(min(r)), np.log10(max(r)), 100)
Us_fit = Ue * r_fit / (r_fit + Rp)
I_fit = (Ue / (r_fit + Rp)) * 1000  # Conversion en mA

# Création de la figure et des sous-graphiques
fig, ax1 = plt.subplots()

# Tracé de Us en fonction de r
ax1.plot(r, Us, 'o', color='b', label='Us (mesuré)')
ax1.plot(r_fit, Us_fit, '--', color='b', label='Modèle Us')
ax1.set_xscale('log')
ax1.set_xlabel('Résistance (Ω)')
ax1.set_ylabel('Tension Us (V)', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

# Création d'un second axe pour I
ax2 = ax1.twinx()
ax2.plot(r, I, 's', color='r', label='I (mesuré)')
ax2.plot(r_fit, I_fit, '--', color='r', label='Modèle I')
ax2.set_ylabel('Courant I (mA)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Ajout des formules sur le graphique avec valeurs numériques
us_formula = f'$U_s = {Ue} \\cdot \\frac{{r}}{{r + {Rp}}}$'
i_formula = f'$I = \\frac{{{Ue}}}{{r + {Rp}}}$'
ax1.text(2000, 3, us_formula, fontsize=12, color='b')
ax2.text(2000, 0.5, i_formula, fontsize=12, color='r')


# Légende
ax1.legend(loc='center left')
ax2.legend(loc='center right')

# Titre et affichage
plt.title('Graphes Us = f(r) et I = g(r) avec modèles théoriques')
plt.show()
