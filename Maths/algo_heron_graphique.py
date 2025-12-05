# determiner la racine carré de a revient a trouver un carré dont l'aire est a

def heron_visuel(a:int, p:float=10**-9, pause:float = 0.5):
    import matplotlib.pyplot as plt
    import numpy as np
    x = a/2

    _, ax = plt.subplots(figsize=(6, 6))
    plt.ion()
    while not abs(x**2-a) < p:
        x = (x + a/x) / 2
        ax.clear()
        x_id = np.linspace(0, a * 1.1, 100)
        plt.plot(x_id, x_id, label='y = x', color='lightgray')
        ax.add_patch(plt.Rectangle((0, 0), x, a/x, fill=None, edgecolor='blue', linewidth=2, label='Carré de côté a'))
        plt.grid(True)
        plt.pause(pause)
    plt.show(block=False)
    return x

print(f"Racine carrée trouvée : {heron_visuel(15)}")