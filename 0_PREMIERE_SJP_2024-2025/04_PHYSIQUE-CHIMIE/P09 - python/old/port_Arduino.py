#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Recherche d'un Arduino branché
à un port USB.
'''

#import serial
import serial.tools.list_ports
def port_Arduino():
    print("Recherche d'un port serie (USB)...")
    ports = serial.tools.list_ports.comports(include_links=False)
    if (len(ports) != 0): # on a trouvé au moins un port actif
        if (len(ports) > 1):     # affichage du nombre de ports trouvés
            print (str(len(ports)) + " ports USB actifs ont été trouvés:")
        else:
            print ("un port USB actif a été trouvé:")
        ligne = 1
        for port in ports :  # affichage du nom de chaque port
            print('n° '+str(ligne) + ' : ' + port.device + ' – type constructeur :  '+ str(port.manufacturer))
            if str(port.manufacturer)=="wch.cn":
                portTrouve=port.device
                return portTrouve
            else:
                ligne=ligne+1
        choix = int(input('Écrivez le numéro de la liste pour le port USB désiré : '))
        portChoisi=ports[choix - 1]
        return portChoisi.device
    else: # on n'a pas trouvé de port USB actif
        print("Aucun port USB actif n'a été trouvé\n")
        print(" Veuillez vérifier le branchement USB avec l'arduino")
# ---------- en tant que script --------------------------
if __name__ == "__main__":
    portUSB=port_Arduino()
    print(portUSB)
