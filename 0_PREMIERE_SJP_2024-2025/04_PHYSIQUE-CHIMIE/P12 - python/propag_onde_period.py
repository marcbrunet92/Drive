'''simulation de la propagation d'une onde périodique sinusoidale
Leroy-Bury (2023)'''
##
# importation des bibliothèques
import sys
from math import cos, pi
from matplotlib import pyplot, animation
from numpy import zeros
##
# fonction de déroulement temporel
def incrementemps(i):
    courbe.set_ydata(mescourbes[i])
    return courbe,
##
# programme principal
Xmax=10.0
Tmax=10.0
fig=pyplot.figure("onde progressive périodique",figsize=(12,8))
ax=pyplot.axes(xlim=(0,Xmax),ylim=(-2,2))
NbEchantillons=100
positionsx=[i*Xmax/NbEchantillons for i in range(NbEchantillons)]
temps=[i*Tmax/NbEchantillons for i in range(NbEchantillons)]
T=2.0 # période
v=1.0 # célérité
mescourbes=[[cos(2*pi/T*(t-x/v)) for x in positionsx] for t in temps]
courbe, =ax.plot(positionsx,mescourbes[0])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title("propagation d'une onde périodique")
lin_ani=animation.FuncAnimation(fig,incrementemps,100,interval=50,blit=False)
pyplot.show()
##
if sys.platform.startswith('darwin'):
    sys.exit()