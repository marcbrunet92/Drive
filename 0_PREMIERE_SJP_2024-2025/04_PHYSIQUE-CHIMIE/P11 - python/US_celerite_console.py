'''' programme d'utilisation du Télémètre Ultrason (Console)
     pour déterminer la vitesse de propagation des ondes
     ultrasonores, la distance à l'écran étant connue.

    S'utilise avec :
     - Sciencethic 651 049 - Télémètre Ultrason fixe
     - Grove - Ultrasonic Ranger 101020010

     Leroy-Bury (2022)'''
##
# importations des bibliothèques et modules
import time
from microcontroleurs import arduino
from port_Arduino import port_Arduino
##
# fonction de conversion intervalle de temps vers distance
def convertirIntervalTempsEnCelerite(tempsAllerRetour,distanceEcran):
    # celerite: distance (en m) /durée (en s)
    try :
        celerite = 2*distanceEcran / ( tempsAllerRetour *1e-6 ) # temps en µs
    except :
        print("calcul de la célérité impossible")
        celerite=0.0
    return celerite
##
# programme principal
# paramétrage de la communication avec Plug'Uino
port=port_Arduino()
carte=arduino(port)
time.sleep(0.1) # durée d'établissement de la connexion sur le port série avec l'arduino
time.sleep(0.1)
# définition des broches de connexion entre le mcirocontroleur et le module US
broche_echo=2
broche_trig=2
# début de la boucle de lecture à la demande (en console)
while True :
    if input(
            "\n"
            "Appuyer sur \"entrée\" pour effectuer une mesure."
            "\n"
            "Saisir \"stop\" pour mettre fin à l'exécution du programme."
            "\n"
    ) == "stop" :
        # Termine l'execution de la boucle d'acquisition.
        break
    distance=float(input("\n quelle est la distance à l'écran (en cm) ? : "))*1e-2
    Nmoy=5 # nombre de mesures à moyenner pour le calcul
    dureeAllerRetour=0
    for i in range(Nmoy) :
        # lecture de l'intervalle de temps mesuré par le télémètre ultrason (en µs)
        dureeAllerRetour=dureeAllerRetour+carte.module_us(broche_echo,broche_trig)
    # calcul de la valeur moyenne de la mesure sur Nmoy valeurs
    dureeAllerRetourMoy=dureeAllerRetour/Nmoy
    print(
        "\n Valeur brute : ",
        dureeAllerRetourMoy," µs"
        " (soit ",
        "{:.1f}".format( convertirIntervalTempsEnCelerite(dureeAllerRetourMoy,distance)),
        " m/s sur la distance de ","{:.1f}".format(distance*1e2)," cm)"
    )
# Fermer la connexion à Plug'Uino avant de quitter.
carte.fermer()
##
if sys.platform.startswith('darwin'):
    sys.exit()
