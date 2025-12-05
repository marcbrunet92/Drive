# determiner la racine carré de a revient a trouver un carré dont l'aire est a

def heron_visuel(a:int, p:float=10**-9, pause:float = 0.5):
    import matplotlib.pyplot as plt
    import numpy as np

    x = a
    _, ax = plt.subplots(figsize=(6, 6))
    plt.ion()

    while not abs(x**2-a) < p:
        x = (x + a/x) / 2
        max_side = max(x, a/x)

        x_id = np.linspace(0, max_side, 100)

        ax.clear()
        ax.set_aspect('equal', adjustable='box')
        plt.plot(x_id, x_id, label='y = x', color='lightgray')
        ax.add_patch(plt.Rectangle((0, 0), x, a/x, fill=None, edgecolor='blue', linewidth=2, label='Carré de côté a'))
        plt.grid(True)
        plt.pause(pause)

    plt.show(block=False)
    return x

# Programme principal
try:
    a = int(input('Entrez un nombre pour calculer sa racine carrée: '))
    assert a >= 0, "Le nombre doit être positif"
    print(f"Racine carrée trouvée : {heron_visuel(a):.6f}, racine carrée exacte : {a**0.5:.6f}")
except ValueError:
    print("Erreur: veuillez entrer un nombre entier valide")