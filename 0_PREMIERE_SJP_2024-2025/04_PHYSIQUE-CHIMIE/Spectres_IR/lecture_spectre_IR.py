''' Lecture de spectres infrarouge en transmittance - fichier format jdx
    possibilité de lire un ou deux spectres simultanément (comparaison)
    Leroy-Bury (2024)
    une banque de spectres IR est disponible à https://webbook.nist.gov/chemistry/inchi-ser/'''
import sys
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from tkinter import filedialog as fd
from pathlib import Path
from numpy import array,log10
from jcamp import jcamp_calc_xsec, jcamp_readfile
# -------------------------------------------------------
def select_files(): # fonction ouvrant une boite de dialogue pour sélectionner un fichier
    global filename
    tk.Tk().withdraw()
    filetypes = (
        ('spectres IR','*.jdx'),
        ('fichiers texte', '*.txt'),
        ('tout type', '*.*')
    )
    filename = fd.askopenfilename(
        title='Sélection du fichier',
        initialdir='.',
        filetypes=filetypes)
# -------------------------------------------------------
def convert_AT(jcamp_dict): # conversion d'absorbance en tranmittance
    y = array(jcamp_dict['y'])
    if (jcamp_dict['yunits'].lower() == 'absorbance' or jcamp_dict['yunits'].lower() == 'ABSORBANCE'):
        jcamp_dict['yunits']='TRANSMITTANCE'
        y[y > 3.0] = 3.0
        y = 10**(2-y)
        jcamp_dict['y'] = y
    elif (jcamp_dict['yunits'].lower() == '% transmittance' or jcamp_dict['yunits'].lower() == '% TRANSMITTANCE'):
        jcamp_dict['yunits']='TRANSMITTANCE'
        y[y>1]=y[y>1]/100
        jcamp_dict['y'] = y
# -------------------------------------------------------
def visu_2_spectres (filename1,filename2):
    nom1=Path(filename1).stem # récupération du nom de fichier sans extension à partir du chemin
    nom2=Path(filename2).stem
    jcamp_dict1 = jcamp_readfile(filename1)
    jcamp_dict2 = jcamp_readfile(filename2)
    convert_AT(jcamp_dict1)
    convert_AT(jcamp_dict2)
    fig, ax = plt.subplots(num='spectres infrarouges',figsize=(14,6))
    ax.set_xlabel(jcamp_dict1['xunits'])
    ax.set_ylabel(jcamp_dict1['yunits'])
    ax.minorticks_on()
    ax.margins(0.01, 0.05)
    ax.set_ylim([0, 1.1])
    ax2 = ax.twinx()
    ax2.set_ylabel(jcamp_dict2['yunits'])
    ax2.set_ylim([0, 1.1])
    ax.plot(jcamp_dict1['x'], jcamp_dict1['y'],"b",label=nom1)
    ax2.plot(jcamp_dict2['x'], jcamp_dict2['y'],"r",label=nom2)
    ax.invert_xaxis()
    ax.grid( which='major', color='g', linestyle='-.',alpha=0.5)
    ax.grid( which='minor', color='g', linestyle=':', alpha=0.2)
    lines = [ax.get_lines()[0], ax2.get_lines()[0]]
    plt.legend(lines, [nom1, nom2], loc="best")
    rect = patches.Rectangle((450, 0), 1050, 100, linewidth=1, edgecolor="cyan",facecolor='cyan', fill=True,alpha=0.2)
    ax.add_patch(rect)
# -------------------------------------------------------
def visu_1_spectre (filename1):
    nom=Path(filename1).stem # récupération du nom de fichier sans extension à partir du chemin
    print(nom)
    jcamp_dict = jcamp_readfile(filename1)
    convert_AT(jcamp_dict)
    fig, ax = plt.subplots(num='spectres infrarouges',figsize=(14,6))
    ax.set_xlabel(jcamp_dict['xunits'])
    ax.set_ylabel(jcamp_dict['yunits'])
    ax.minorticks_on()
    ax.margins(0.01, 0.05)
    ax.plot(jcamp_dict['x'], jcamp_dict['y'],"b",label=str(nom))
    ax.invert_xaxis()
    ax.grid( which='major', color='g', linestyle='-.',alpha=0.5)
    ax.grid( which='minor', color='g', linestyle=':', alpha=0.2)
    lines = [ax.get_lines()[0]]
    plt.legend(lines, [nom], loc="best")
    rect = patches.Rectangle((450, 0), 1050, 100, linewidth=1, edgecolor="cyan",facecolor='cyan', fill=True,alpha=0.2)
    ax.add_patch(rect)

##
# programme principal
filename=''
filenames=['','']
rep=input("Combien de spectres souhaitez-vous visualiser (1 ou 2) ?")
if rep=="2":
    for i in(0,1):
        select_files()
        filenames[i]=filename
    visu_2_spectres (filenames[0],filenames[1])
else : # par défaut 1 seul spectre visualisé
    select_files()
    visu_1_spectre(filename)
plt.savefig('spectre_IR.png')
plt.show()
sys.exit() # pour fermer les fenêtres Tkinter