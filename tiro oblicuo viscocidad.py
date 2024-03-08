#simulación de Tiro parabólico con y sin viscosidad

import matplotlib.pyplot as plt
import math as m
dt = 0.01
visco=0.0000174
densidad=1,2
g=9.8
r=0.3
ma=0.5
y0=10
y=y0
x0=0
x=x0
v0x=20
vx=v0x
v0y=10
vy=v0y
Cd=0.5
A=m.pi*r**2
ax=-(0.5*Cd*A*m.sqrt((vx**2)+(vy**2))*vx)/ma
ay=-g-(0.5*Cd*A*m.sqrt((vx**2)+(vy**2))*vy)/ma
t=0
 
while y>0: 
    xideal=x+v0x*t
    yideal=y0+v0y*t-4.9*t**2    
    plt.figure(1)
    plt.plot(t,y,"ro")
    plt.figure(2)
    plt.plot(t,vy,"bx")
    plt.figure(3)
    plt.plot(x,y,"yx")
    plt.plot(xideal,yideal,"rx")
    y=y+vy*dt
    vy=vy+ay*dt
    ay=-g-(0.5*Cd*A*m.sqrt((vx**2)+(vy**2))*vy)/ma
    x=x+vx*dt
    vx=vx+ax*dt
    ax=-(0.5*Cd*A*m.sqrt((vx**2)+(vy**2))*vx)/ma
    t = t+dt
    
plt.figure(1)
plt.show()
plt.figure(2)
plt.show()
plt.figure(3)
plt.show()
print (t)