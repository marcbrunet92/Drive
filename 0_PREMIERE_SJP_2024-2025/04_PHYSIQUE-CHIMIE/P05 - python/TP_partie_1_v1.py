import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_field_and_equipotentials(data):
    x, y, V = data['x'], data['y'], data['V']
    print(data['x'], data['y'], data['V'])
    r = np.sqrt(x**2 + y**2)
    r[r < 1e-10] = 1e-10
    Ex, Ey = -x / r * V, -y / r * V
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.quiver(x, y, Ex, Ey, color='blue', angles='xy', scale_units='xy', scale=1)
    for rayon in np.sqrt(x**2 + y**2):
        ax.add_artist(plt.Circle((0, 0), rayon, color='black', fill=False, linestyle='dotted'))
    ax.set(xlabel='x', ylabel='y', title='Champ vectoriel (la source est au point (0, 0))', xlim=[0, 35], ylim=[-1, 10])
    ax.grid(True)
    ax.set_aspect('equal')
    plt.show()

plot_field_and_equipotentials(pd.read_csv('donnees.csv', delimiter=';', decimal=','))
