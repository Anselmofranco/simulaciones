#Realizar una función "function y=tirovertical(t,y0,v0)" que reciba un vector
# tiempo, la altura inicial y la velocidad inicial y devuelva un vector
#con las posiciones correspondientes.


import matplotlib.pyplot as plt
import numpy as np

t=np.arange(0,3.28378,0.00001)

def TiroVertical(t,y0,v0):
    return y0+v0*t-4.9*t**2

y=TiroVertical(t, 20, 10)

def TiempoDeVuelo(x):
    tv=0
    i=0
    while i<y.size:
            if y[i]>0:
                tv=t[i]
                i=i+1
            else:
                i=i+1
    return tv

def AlturaMax(x):
    ymax=0
    i=0
    while i<y.size-1:
        if (y[i+1]-y[i])>0:
            ymax=y[i]
            i=i+1
        else:
            i=i+1
    return ymax

def integral (y,x):
 
    S=0
    i=0
    dx=x[1]-x[0]
    while i<y.size-1:
        S=S+y[i]*dx
        i=i+1
    return S

def derivada(y,x):  #derivada de y en función de x
    dy=y.copy()  #arreglo nuevo para no sobreescribir y
    # dy= np.empty_like(y) arma el array con valores none, de esa forma no hace falta  dy[i]=None
    i=0
    while i<y.size-1:
        dy[i]=(y[i+1]-y[i])/(t[i+1]-t[i])
        i=i+1
    dy[i]=None #valor nulo a la última posición
    return dy

v=derivada(y,t)
d=integral(v,t)

#print(v)
print(TiempoDeVuelo(y))
print(d)
print(AlturaMax(y))
#print(y)
#print(d_vuelo)

plt.plot(t,y)
plt.plot(t,v)

plt.show()


