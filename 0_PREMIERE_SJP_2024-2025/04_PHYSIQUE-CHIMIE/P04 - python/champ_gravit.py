""" Illustration d'un champ gravitationnel
https://glq2200.clberube.org/ - 2023"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as patches
import sys
##
def equal_aspect_plot(vmin=-1, vmax=1, figsize=(6, 5)):
    """Crée un gabarit pour dessiner le champ g."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlim([vmin, vmax])
    ax.set_ylim([vmin, vmax])
    ax.set_aspect('equal')
    ax.plot([0], [0], 'ko')
    ax.annotate('$m$', (0.05, 0), va='center')
    return fig, ax
##
def champ_g(x, y, m=1):
    """Retourne g pour une masse quelconque."""
    G = 6.67408e-11  # m^3 kg^-1 s^-2
    r = np.sqrt(x*x + y*y)
    theta = np.arctan2(y, x)
    r[r < 0.2] = np.nan  # évite division par 0
    F = -G*m/r**2
    return F*np.cos(theta), F*np.sin(theta)  # gx, gy
##
def potentiel_g(x, y, m=1):
    """Retourne le potentiel gravitationnel
    pour une paire de coordonnées (x, y)"""
    G = 6.67408e-11  # m^3 kg^-1 s^-2
    r = np.sqrt(x**2 + y**2)
    r[r == 0] = np.nan  # évite division par 0
    return -G*m/r
##
# Préparer une grille
x = np.linspace(-1, 1, 10)
y = np.linspace(-1, 1, 10)
X, Y = np.meshgrid(x, y)
# Calcul de g sur la grille
gx, gy = champ_g(X, Y)
# Tracer le gabarit
fig1, ax = equal_aspect_plot()
# On ajoute les flèches du champ g
arrows = ax.quiver(X, Y,
                   gx/np.sqrt(gx**2 + gy**2),
                   gy/np.sqrt(gx**2 + gy**2),
                   np.sqrt(gx**2 + gy**2),
                   cmap='binary', width=0.01, scale=10)
plt.colorbar(arrows, label=r'$g$ (m/s$^2$)')
##
fig2, ax = equal_aspect_plot()
# On remet les flèches du champ g
arrows = ax.quiver(X, Y,
                   gx/np.sqrt(gx**2 + gy**2),
                   gy/np.sqrt(gx**2 + gy**2),
                   np.sqrt(gx**2 + gy**2),
                   cmap='binary', width=0.005, scale=10)
# Nouvelle grille plus fine pour le potentiel
xu, yu = np.linspace(-1, 1), np.linspace(-1, 1)
XX, YY = np.meshgrid(xu, yu)
# Calculer le potentiel sur la grille
U = potentiel_g(XX, YY)
# Tracer le potentiel avec une carte de contour
contours = ax.contourf(XX, YY, U, cmap='viridis_r',
                       norm=colors.PowerNorm(gamma=4),
                       levels=25,
                       zorder=0, alpha=1)
# Ajouter une barre de couleurs
plt.colorbar(contours, label=r'$U$ (J/kg)')
##
plt.show()
if sys.platform.startswith('darwin'):
    sys.exit()