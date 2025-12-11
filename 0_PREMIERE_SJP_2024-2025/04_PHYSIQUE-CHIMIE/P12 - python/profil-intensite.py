''' ----- LEROY-BURY (2022) -- Profil d'intensité'''
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from PIL import Image
# Fonction d'actualisation des courbes
def update(val):
    y2=H.val
    valeurs = obt_valeurs(img,y2)
    p2.set_ydata(y2)
    p3.set_ydata(valeurs)
# Fonction de lecture des pixels de l'image
def obt_valeurs(image,H):
    h = image.height
    w = image.width
    sortie = list()
    for i in range(w):
        pixel = image.getpixel((int(i),int(H) ))
        intensite=int((pixel[0]+pixel[1]+pixel[2])/755*100)
        sortie.append(intensite)
    return sortie
# Chargement de l'image
fichier=input("Quel est le nom du fichier image (sans extension) ? ")
try :
    img = Image.open(fichier+".png")
except :
    try :
        img = Image.open(fichier+".jpg")
    except :
        fichier=input("Quel est le nom du fichier image avec son extension (.png ,.jpg , .gif...) ? ")
        img = Image.open(fichier)
# Lecture de l'image
NbVals = img.width
hauteur=img.height
print("hauteur de l'image en pixels : ",hauteur)
print("largeur de l'image en pixels : ",NbVals)
H_init=int(hauteur/2)
H=H_init
#Tracé des courbes
fig,(ax0,ax1) = plt.subplots(nrows=2, ncols=1,figsize=(12,8),sharey=False,sharex=True)
plt.subplots_adjust(left=0.25, bottom=0.25)
# ------------- Affichage image
plt.subplot(2,1,1)
p1 = plt.imshow(img)
p2 = plt.axhline(y=H,color='white',linestyle='--')
rectangle_a = plt.axes([0.25, 0.1, 0.5, 0.02])
H = Slider(rectangle_a, 'hauteur de la ligne de profil', valmin=0,valmax=hauteur,valinit=H_init)
H.on_changed(update)
#----------- Affichage profil
plt.subplot(2,1,2)
plt.xlabel("largeur de la figure (pixels)")
plt.ylabel("intensité (en %)")
plt.grid()
plt.title ("profil d'intensité– interférences")
Hval=H.val
valeurs = obt_valeurs(img, Hval)
ax1.set_ylim(ymin=0,ymax=int(800/755*100))
p3, = ax1.plot(range(NbVals), valeurs,label="$I$")
plt.legend()
plt.show()