import matplotlib.pyplot as plt
from scipy.integrate import trapezoid as simps
import serial.tools.list_ports
import time
import numpy as np
import pandas as pd
import serial

def port_Arduino():
    print("Recherche d'un port serie (USB)...")
    ports = serial.tools.list_ports.comports(include_links=False)
    if (len(ports) != 0):
        if (len(ports) > 1):
            print (str(len(ports)) + " ports USB actifs ont été trouvés:")
        else:
            print ("un port USB actif a été trouvé:")
        ligne = 1
        for port in ports :
            print('n° '+str(ligne) + ' : ' + port.device + ' – type constructeur :  '+ str(port.manufacturer))
            if str(port.manufacturer)=="wch.cn":
                portTrouve=port.device
                return portTrouve
            else:
                ligne=ligne+1
        choix = int(input('Écrivez le numéro de la liste pour le port USB désiré : '))
        portChoisi=ports[choix - 1]
        return portChoisi.device
    else:
        print("Aucun port USB actif n'a été trouvé\n")
        print(" Veuillez vérifier le branchement USB avec l'arduino")

class arduino():
    def __init__(self,port):
        self.serie = serial.Serial(port,baudrate=115200)
        synchro = ord(self.serie.read())
        while synchro != 0:
            synchro = ord(self.serie.read())

    def sortie_numerique(self,pin,etat):
        self.serie.write(chr(1).encode('latin-1'))
        self.serie.write(chr(pin).encode('latin-1'))
        self.serie.write(chr(etat).encode('latin-1'))

    def entree_numerique(self,pin):
        self.serie.write(chr(2).encode('latin-1'))
        self.serie.write(chr(pin).encode('latin-1'))
        val=ord(self.serie.read())
        return val

    def sortie_analogique(self,pin,val):
        self.serie.write(chr(3).encode('latin-1'))
        self.serie.write(chr(pin).encode('latin-1'))
        self.serie.write(chr(val).encode('latin-1'))

    def entree_analogique(self,pin):
        self.serie.write(chr(4).encode('latin-1'))
        self.serie.write(chr(pin).encode('latin-1'))
        val1=ord(self.serie.read())
        val2=ord(self.serie.read())
        return val1*256 + val2

    def son(self,pin,freq,duree=0):
        self.serie.write(chr(5).encode('latin-1'))
        self.serie.write(chr(pin).encode('latin-1'))
        self.serie.write(chr(freq>>8 & 255).encode('latin-1'))
        self.serie.write(chr(freq & 255).encode('latin-1'))
        self.serie.write(chr(duree>>8 & 255).encode('latin-1'))
        self.serie.write(chr(duree & 255).encode('latin-1'))
        time.sleep(duree/1000)

    def module_us(self,echo,trig):
        self.serie.write(chr(6).encode('latin-1'))
        self.serie.write(chr(echo).encode('latin-1'))
        self.serie.write(chr(trig).encode('latin-1'))
        val1=ord(self.serie.read())
        val2=ord(self.serie.read())
        return val1*256 + val2

    def resistance_pt100(self,cs,di,do,clk):
        self.serie.write(chr(7).encode('latin-1'))
        self.serie.write(chr(cs).encode('latin-1'))
        self.serie.write(chr(di).encode('latin-1'))
        self.serie.write(chr(do).encode('latin-1'))
        self.serie.write(chr(clk).encode('latin-1'))
        val1=ord(self.serie.read())
        val2=ord(self.serie.read())
        return 430*(val1*256 + val2)/32768

    def fermer(self):
        self.serie.close()

carte=arduino(port_Arduino())

def plotValues():
    plt.grid ()
    plt.title("fonctionnement du moteur")
    plt.xlabel('date (s)')
    plt.ylabel('Puissance (W)')
    plt.plot(valeurs_t[:-1], valeurs_P[:-1])

valeurs_t = []
valeurs_P = []
valeurs_Im = []
valeurs_Um = []
plt.figure(figsize=(5,5))
time.sleep(0.1)
m0=0
m1=0
Umax=5.0
R0= 5
R1= 10000
R2= 5000
F= R2/(R1+R2)

seuil=25
Dt=0.10
ecoute=True
print("attente du déclenchement...")
while ecoute :
    m0=carte.entree_analogique(0)
    if m0>seuil :
        print("déclenchement de l'acquisition")
        ecoute = False
t1=time.perf_counter()

while m0>seuil:
    m0=carte.entree_analogique(0)
    m1=carte.entree_analogique(2)
    t2=time.perf_counter()
    date=round(t2-t1,3)
    U0=round(Umax/1023*m0,4)
    U2=round(Umax/1023*m1,4)
    P = (U2 / F - U0) * (U0 / R0)
    valeurs_t.append(date)
    valeurs_Um.append(U2/F-U0)
    valeurs_Im.append(U0/R0)
    valeurs_P.append(P)
    print("t = ",date," s \t Um = ",U2/F-U0," V \t Im = ",U0/R0," A")
    time.sleep(Dt)
carte.fermer()
print("fin de l'acquisition des mesures")
print("durée de l'acquisition des mesures (s) : "+str(date)+" s")
U=np.array(valeurs_Um)
I=np.array(valeurs_Im)
t=np.array(valeurs_t)
P=U*I
E=simps(y=P[:-1], x=t[:-1])

print("Energie totale délivrée au moteur E = ", round(E,2)," J")
fichier=input("Nom du fichier de sauvegarde (sans.csv)")
valeurs = {'date': t[:-1],'Um': U[:-1],'Im': I[:-1]}
data = pd.DataFrame(valeurs)
print(data)
data.to_csv(fichier+'.csv',sep=';',index=False)
plotValues()
plt.savefig(fichier+'.png')
plt.show()