''' Bibliothèque d'instructions permettant de contrôler un microcontroleur
Arduino UNO grâce à Python
– Frédéric Guérinet 2020 - adaptation J.L. Leroy-Bury 2024'''
import serial,time, sys
import serial.tools.list_ports
##
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

    def lecture_Vcc(self):
    # Idéalement : VCC = 5 volts = 1023
    # Référence interne = 1.1 volts = (1023 * 1.1) / 5 = 225
    # En mesurant la référence à 1.1 volts, on peut déduire la tension d'alimentation réelle du microcontrôleur
    # VCC = (1023 * 1.1) / analogReadReference()
        self.serie.write(chr(8).encode('latin-1'))
        val1=ord(self.serie.read())
        val2=ord(self.serie.read())
        val=float(val1*256 + val2)
        Vcc=round(1023*1.1/val,3)
        return Vcc

    def entree_analogdec(self,pin):
        self.serie.write(chr(9).encode('latin-1'))
        self.serie.write(chr(pin).encode('latin-1'))
        val1=ord(self.serie.read())
        val2=ord(self.serie.read())
        valRef1=ord(self.serie.read())
        valRef2=ord(self.serie.read())
        valdec= (val1*256 + val2)*1.085/((valRef1*256 + valRef2))
        return round(valdec,3)

    def fermer(self):
        self.serie.close()
##
def port_Arduino():
    print("\n Recherche d'un port série (USB) pour la connexion avec le microcontroleur Arduino... \n")
    portsUSB = serial.tools.list_ports.comports(include_links=False)
    if (len(portsUSB) != 0): # on a trouvé au moins un port actif
        if (len(portsUSB) > 1):     # affichage du nombre de ports trouvés
            print (str(len(portsUSB)) + " ports USB actifs ont été trouvés:")
        else:
            print ("un port USB actif a été trouvé :")
        ligne = 1
        portArduino=""
        for port in portsUSB :  # affichage du nom de chaque port
            print('n° '+str(ligne) + ' : ' + port.device + ' – type constructeur :  '+ str(port.manufacturer))
            if str(port.manufacturer)=="wch.cn" or str(port.manufacturer)=="Arduino (www.arduino.cc)":
                portArduino=port.device
            ligne=ligne+1
        if portArduino =="":
            print("\n Aucun microcontroleur Arduino n'a été détecté sur un port USB")
            print("Veuillez vérifier le branchement USB avec le microcontroleur Arduino")
            sys.exit()
        else :
            return portArduino
    else: # on n'a pas trouvé de port USB actif
        print("\n Aucun port USB actif n'a été trouvé")
        print("Veuillez vérifier toutes les connexions USB")
        sys.exit()
##
# Recherche du port sur lequel est connecté le mricrocontroleur en tant que script autonome --------------------------
if __name__ == "__main__":
    portUSB=port_Arduino()
    print("le microcontroleur est connecté sur le port USB ",portUSB)
    carte = arduino(portUSB)
    time.sleep(0.1) # durée d'établissement de la connexion sur le port série avec l'arduino
    Valim=carte.lecture_Vcc()
    print("le microcontrôleur est alimenté sous une tension de  ",Valim,' V')
    carte.fermer()