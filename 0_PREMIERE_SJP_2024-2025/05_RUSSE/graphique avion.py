import matplotlib.pyplot as plt

# Données des avions (en milliers)
années = [1950, 1960, 1970, 1980, 1990]
chars_soviétiques = [10, 18, 30, 45, 60, 55, 60, 65, 70, 65, 55, 50, 45, 40, 35]  # Estimations approximatives
chars_américains = [8, 15, 22, 30, 35, 40, 40, 45, 50, 60, 58, 60, 58, 57, 50]  # Estimation approximative pour l'URSS

# Création du graphique
plt.figure(figsize=(10, 6))
plt.plot(années, chars_américains, label='USA', color='blue', marker='o', linestyle='-', linewidth=2, markersize=8)
plt.plot(années, chars_soviétiques, label='URSS', color='red', marker='o', linestyle='-', linewidth=2, markersize=8)

# Ajouter des labels et un titre
plt.title("Nombre d'avions militaires pendant la Guerre froide", fontsize=14)
plt.xlabel("Années", fontsize=12)
plt.ylabel("Nombre d'avions (en milliers)", fontsize=12)

# Ajouter une légende
plt.legend()

# Afficher la grille et le graphique
plt.grid(True)
plt.tight_layout()
plt.show()
