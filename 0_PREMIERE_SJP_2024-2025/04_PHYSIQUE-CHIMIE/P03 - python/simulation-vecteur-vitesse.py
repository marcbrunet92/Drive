#Modelisation du mouvement parabolique d une balle lancee

import numpy as np
from scipy import *
import matplotlib.pyplot as plt

#Preciser la duree de la sequence
T=

#preciser les coefficient de l equation de la parabole de la forme y=ax2+bx+c
a=
b=
c=

#Trace des points modelisant la trajectoire etudiee

t=np.linspace(0,T,22)
g=9.8
x=0-g/2/a*t
y=a*x**2+b*x+c
plt.figure(1,figsize=(10,12))
plt.plot(x,y,"o")
plt.grid()



#traces des vecteurs vitesse au cours de la trajectoire de la balle

n=np.arange(21)

for i in n :
    plt.arrow(x[i],y[i],0.2*(x[i+1]-x[i])/(t[i+1]-t[i]),0.2*(y[i+1]-y[i])/(t[i+1]-t[i]),fc="k",ec="k",head_width=0.05, head_length=0.1)
plt.figure(2,figsize=(10,12))
plt.plot(x,y,"ro")
plt.grid()


#Traces des vecteurs variation de vitesse pour les points de la parabole

vy=np.diff(y,1)
vx=np.diff(x,1)
ay=np.diff(vy,1)
ax=np.diff(vx,1)
X=x[0:21]
Y=y[0:21]
n=np.arange(20)
for i in n :
    plt.arrow(x[i],y[i],10*ax[i],10*ay[i],fc="k",ec="k",head_width=0.05, head_length=0.1)
plt.figure(3,figsize=(10,12))
plt.plot(x,y,"ro")
plt.grid()
plt.show()
sys.exit()
