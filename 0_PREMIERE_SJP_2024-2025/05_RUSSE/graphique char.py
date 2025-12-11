import matplotlib.pyplot as plt
import numpy as np

# Données approximatives sur le nombre de chars durant la guerre froide (en milliers)
années = np.arange(1947, 1991, 5)
chars_soviétiques = [10, 18, 30, 45, 60, 55, 60, 65, 70, 65, 55, 50, 45, 40, 35]  # Estimations approximatives
chars_américains = [8, 15, 22, 30, 35, 40, 40, 45, 50, 60, 58, 60, 58, 57, 50]  # Estimations approximatives

# Création du graphique
plt.figure(figsize=(10, 6))
plt.plot(années, chars_soviétiques, label="Chars Soviétiques")
plt.plot(années, chars_américains, label="Chars Américains")

# Ajout de titres et légendes
plt.title("Évolution du nombre de chars soviétiques et américains pendant la Guerre froide")
plt.xlabel("Années")
plt.ylabel("Nombre de chars (en milliers)")
plt.legend()

# Affichage du graphique
plt.grid(True)
plt.tight_layout()
plt.show()
