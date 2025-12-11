''' Programme de filtrage d'une image RVB
Leroy_Bury (2023)'''
# importation des bibliothèques et modules
import matplotlib.image as mpimg                # ou "import imageio as mpimg"
import matplotlib.pyplot as plt
import numpy as np
import sys
##
# Définition de la fonction filtre_vert
def filtre_vert( image ):
    photo = np.copy(image)                      # copie de l'image à filtrer
    for i in range(photo.shape[0]):             # i indique la ligne sur laquelle se trouve le pixel
        for j in range(photo.shape[1]):         # j indique la colonne sur laquelle se trouve le pixel
            r, v, b = photo[i, j]               # valeurs des composantes rouge, verte et bleue du pixel situé sur la ligne i et la colonne j
            photo[i, j] = (0,v,0)              # conserve la valeur de la composante verte et annule les composantes rouge et bleue
    return photo
##
# Définition de la fonction filtre_rouge
def filtre_rouge( image ):
    photo = np.copy(image)                      # copie de l'image à filtrer
    for i in range(photo.shape[0]):             # i indique la ligne sur laquelle se trouve le pixel
        for j in range(photo.shape[1]):         # j indique la colonne sur laquelle se trouve le pixel
            r, v, b = photo[i, j]               # valeurs des composantes rouge, verte et bleue du pixel situé sur la ligne i et la colonne j
            photo[i, j] = (r,0,0)              # conserve la valeur de la composante rouge et annule les composantes verte et bleue
    return photo
##
# Définition de la fonction filtre_bleu
def filtre_bleu( image ):
    photo = np.copy(image)                      # copie de l'image à filtrer
    for i in range(photo.shape[0]):             # i indique la ligne sur laquelle se trouve le pixel
        for j in range(photo.shape[1]):         # j indique la colonne sur laquelle se trouve le pixel
            r, v, b = photo[i, j]               # valeurs des composantes rouge, verte et bleue du pixel situé sur la ligne i et la colonne j
            photo[i, j] = (0,0,b)              # conserve la valeur de la composante bleue et annule les composantes rouge et verte
    return photo
##
# programme principal
# Lecture de l'image sous forme d'un tableau de nombres
photoOriginale = mpimg.imread("cercle_chroma_addit.jpg")   # image placée dans le même dossier que le fichier python ou copier le chemin d'accès
#création d'une figure
fig=plt.figure(num="filtrage d'une image", figsize=(16,8))
# Application de la fonction filtre_rouge à la photo choisie
photoFiltreR = filtre_rouge(photoOriginale)
# Application de la fonction filtre_vert à la photo choisie
photoFiltreV = filtre_vert(photoOriginale)
# Application de la fonction filtre_rouge à la photo choisie
photoFiltreB = filtre_bleu(photoOriginale)
# position de l'image originale avec un titre
fig.add_subplot(2, 2, 1) # sous-figures en 2x2 on crée une première sous-figure en (1,1)
plt.imshow(photoOriginale)
plt.title('Photo originale')
# création des photos filtrées avec titre
fig.add_subplot(2, 2, 2) # sous-figures en 2x2 on crée une deuxième sous-figure en (1,2)
plt.imshow(photoFiltreV)
plt.title('Photo avec un filtre vert')
fig.add_subplot(2, 2, 3) # sous-figures en 2x2 on crée une troisième sous-figure en (2,1)
plt.imshow(photoFiltreR)
plt.title('Photo avec un filtre rouge')
fig.add_subplot(2, 2, 4) # sous-figures en 2x2 on crée une quatrième sous-figure en (2,2)
plt.imshow(photoFiltreB)
plt.title('Photo avec un filtre bleu')
# Affichage de la figure
fig.tight_layout() # ajuste les sous-figures les unes par rapport aux autres
plt.savefig("photo_filtree.png")
plt.show()
if sys.platform.startswith('darwin'):
    sys.exit()