##
# importation des bibliothèques
import matplotlib.pyplot as plt
import pandas as pd
import sys
##
# Les fonctions
# calcul de l'avancement maximal
def avancement_maximal(a,n_Ai,b,n_Bi):
    x_max=min(n_Ai/a, n_Bi/b)
    return x_max
# calcul de la composition de l'état final
def etat_final(a,n_Ai,b,n_Bi,x_max):
    n_A=n_Ai-a*x_max
    n_B=n_Bi-b*x_max
    if (n_A<1E-10 and n_B<1E-10):
        print("Nous sommes dans les conditions stoechiométriques")
        print("x_max = {0:1.2E} mol.".format(x_max))
    elif n_A<1E-10 :
        n_A=0
        print("A est le réactif limitant.")
        print("x_max = {0:1.2E} mol.".format(x_max))
        print("A la fin de la transformation, il n'y a plus de A.")
        print("Il reste {0:1.2E} mol de B.".format(n_B))
    else :
        n_B=0
        print("B est le réactif limitant.")
        print("x_max = {0:1.2E} mol.".format(x_max))
        print("A la fin de la transformation, il n'y a plus de B.")
        print("Il reste {0:1.2E} mol de A.".format(n_A))
# affichage des courbes
def courbes(a,b,c,d,n_Ai,n_Bi,n_Ci,n_Di,A,B,C,D):
    x=0
    xT=[]
    n_AT=[]
    n_BT=[]
    n_CT=[]
    n_DT=[]
    n_A, n_B, n_C, n_D = n_Ai, n_Bi, n_Ci, n_Di
    dx=(min(n_A,n_B)/50)
    plt.ion()
    x_max=min(n_Ai/a,n_Bi/b)
    plt.xlim(0,1.2*x_max)
    plt.xlabel('Avancement x (mol)')
    plt.ylabel('n (en mol)')
    plt.grid()
    plt.plot(x,n_A,'b.',label=A)
    plt.plot(x,n_B,'r+',label=B)
    plt.plot(x,n_C,'c.',label=C)
    plt.plot(x,n_D,'m+',label=D)
    plt.legend()
    while (n_A>0) and (n_B>0):
        plt.plot(x,n_A,'b.')
        plt.plot(x,n_B,'r+')
        plt.plot(x,n_C,'c.')
        plt.plot(x,n_D,'m+')
        plt.pause(0.01)
        x=x+dx
        n_A=n_Ai-a*x
        n_B=n_Bi-b*x
        n_C=n_Ci+c*x
        n_D=n_Di+d*x
        xT.append(x)
        n_AT.append(n_A)
        n_BT.append(n_B)
        n_CT.append(n_C)
        n_DT.append(n_D)
        plt.ylim(0,1.2*max(n_A,n_B,n_C,n_D))
    return xT,n_AT,n_BT,n_CT,n_DT
##
# Le programme principal
# Equation du type aA + bB -> cC +  dD
print("Equation du type :  aA + bB -> cC +  dD")
a=float(input("Entrez le nombre stoechiométrique a :"))
n_Ai=float(input("n_Ai = "))
b=float(input("Entrez le nombre stoechiométrique b :"))
n_Bi=float(input("n_Bi = "))
c=float(input("Entrez le nombre stoechiométrique c :"))
n_Ci=float(input("n_Ci = "))
d=float(input("Entrez le nombre stoechiométrique d :"))
n_Di=float(input("n_Di = "))
A, B, C, D = "réactif A", "réactif B", "produit C", "produit D"
x_max=avancement_maximal(a,n_Ai,b,n_Bi)
etat_final(a,n_Ai,b,n_Bi,x_max)
xT,n_AT,n_BT,n_CT,n_DT=courbes(a,b,c,d,n_Ai,n_Bi,n_Ci,n_Di,A,B,C,D)
plt.ioff()
tableau_av = pd.DataFrame(list(zip(xT,n_AT,n_BT,n_CT,n_DT)), columns=["x","réactif A","réactif B","produit C","produit D"])
print(tableau_av)
plt.show()
if sys.platform.startswith('darwin'):
    sys.exit()
