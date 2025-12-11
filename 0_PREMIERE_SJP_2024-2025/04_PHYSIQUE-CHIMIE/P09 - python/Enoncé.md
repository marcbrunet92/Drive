**P09 Travaux Pratiques**  

**Conversion d’énergie : alimentation d’un monte-charge par un moteur électrique**  

Les moteurs électriques sont des convertisseurs d’énergie : ils convertissent de l’énergie électrique en énergie mécanique (cinétique et potentielle).  

Afin de rendre compte de changements de forme de l’énergie, par exemple dans une machine telle qu’un monte-charge, on fait appel à une représentation graphique : la chaîne énergétique. Dans une chaîne énergétique, on peut faire apparaître (mais c’est facultatif) les réservoirs d’énergie sous la forme de rectangles, mais cela ne peut concerner que des formes stockables de l’énergie.  

Les convertisseurs d’énergie assurent la conversion d’une forme d’énergie en une ou plusieurs autres utiles ou non. Par convention, un convertisseur se note par un cercle, par lequel va transiter des transferts d’énergie, indiqués par des flèches. Un convertisseur n’emmagasine ni ne crée d’énergie.  

D’après le principe de conservation de l’énergie, l’énergie totale sortant d’un convertisseur est strictement égale à l’énergie entrante. À chaque convertisseur, il y a possibilité de « pertes » d’énergie. Cette énergie est dite perdue, ou dégradée, car elle est sous une forme non exploitable par la chaîne, comme par exemple la chaleur dissipée par des frottements. En conséquence, quand on fournit une quantité d’énergie à un convertisseur, seule une partie sera utilisable en sortie.  

De manière générale, le rendement d’un convertisseur est le rapport de l’énergie utile sur l’énergie apportée : le rendement est donc un nombre sans dimension compris entre 0 et 1, et peut s’exprimer sous la forme d’un pourcentage.  

**Le rendement du monte-charge dépend-il de la masse de la charge soulevée ?**  

### **I – Étude du montage avec le moteur monte-charge**

#### 1°/ Étude théorique du montage électrique avec le moteur

— Établir l’expression de l’intensité du courant $ I_0 $ traversant le moteur en fonction de $ U_0 $ et $ R_0 $.  
— Établir l’expression de la tension $ U_2 $ en fonction de la tension $ e $ et des résistances $ R_1 $ et $ R_2 $.  
— Établir l’expression de la tension $ U_M $ aux bornes du moteur en fonction de $ e $ et de $ U_0 $.  
— En déduire une expression de la puissance électrique $ P_M $ délivrée au moteur en fonction de $ U_0, U_2, R_0, R_1 $ et $ R_2 $.  
— Sachant que les entrées analogiques du microcontrôleur ne supportent pas des tensions supérieures à 5,0 V (tension d’alimentation de la carte via le port de communication série USB de l’ordinateur), quel est l’intérêt du montage pont diviseur réalisé avec les résistors $ R_1 $ et $ R_2 $ ?  
— Quelle est l’intensité maximale admissible $ I_{0,\max} $ dans la branche contenant le moteur ?  
— Quelle est la valeur moyenne de l’énergie électrique $ E_M (t) $ délivrée au moteur pendant l’intervalle de temps $ \Delta t $ entre deux mesures aux dates $ t $ et $ t+\Delta t $ ?  
— Comment obtenir l’énergie totale délivrée au moteur pendant toute la durée de l’expérience ?  

#### 2°/ Étude théorique du montage mécanique avec la charge de masse $ m $

On considère le système {charge de masse $ m $} en interaction avec le champ de pesanteur en négligeant toutes les autres forces. On se place dans le référentiel du laboratoire considéré comme galiléen.  

— Donner l’expression de l’énergie cinétique de la charge levée par le monte-charge.  
— Donner l’expression de l’énergie potentielle de pesanteur de la charge levée par le monte-charge en fonction de son altitude $ z $. Précisez le choix de l’origine des altitudes.  
— En déduire une expression de son énergie mécanique.  
— Quelle est la puissance mécanique fournie en moyenne à la charge par le monte-charge ?  
— Quelle est la force qui travaille ? Est-elle constante pendant toute la remontée ?  

#### 3°/ Étude expérimentale

— Faire monter une première charge de masse $ m = 100 g $ en enregistrant son mouvement à l’aide d’une webcam et les valeurs des tensions $ U_0 $ et $ U_1 $ à l’aide du microcontrôleur Arduino.  
— Relever les différentes positions occupées par la charge au cours du temps (pointage avec le tableur-grapheur Regressi) et construire la courbe représentative de l’énergie potentielle de pesanteur $ E_{pp} $ de cette charge au cours du temps.  
— Déterminer la vitesse ascensionnelle de la charge et en déduire la valeur de son énergie cinétique $ E_c $ au cours du temps. Construire sa courbe représentative.  
— Construire la courbe représentative de l’évolution de l’énergie mécanique $ E_{\text{meca}} $ de la charge au cours du temps. Quelle est sa valeur finale ?  
— Quelle est la valeur de l’énergie électrique $ E_{\text{moteur}} $ fournie au moteur pendant l’ascension de la charge ?  
— En déduire le rendement $ r $ du moteur du monte-charge.  
— Reprendre votre étude pour d’autres valeurs de la masse $ m $.  

Regrouper vos résultats dans un tableau :  

| $ m $ (g)                                        | 100 | 150 | 200 | 250 |
| ------------------------------------------------ | --- | --- | --- | --- |
| $r = \frac{E_{\text{meca}}}{E_{\text{moteur}}} $ |     |     |     |     |
| $E_{\text{meca}} $ (J)                           |     |     |     |     |
| $E_{\text{moteur}}$ (J)                          |     |     |     |     |

— Répondre à la question introductive au TP.  
— Pensez-vous que le moteur puisse augmenter son rendement indéfiniment ? Pourquoi ?  
— Représenter la chaîne énergétique correspondant à ce convertisseur.  


