import numpy as np
import matplotlib.pyplot as plt
import math

v0 = float(input("Podaj predkosc poczatkowa "))
alpha = float(input("Podaj kat rzutu "))

v0y = np.sin(math.radians(alpha))*v0
v0x = np.cos(math.radians(alpha))*v0
g=9.81

hmax = ((v0*v0)/(2*g)) * ((np.sin(math.radians(alpha)))**2)
t = 2*(v0y/g)
R = v0x*t
print("Maksymalna wysokość: ",hmax,"\nZasięg rzutu: ",R,"\nCzas lotu: ",t)

czas = np.linspace(0,t,100)
y = (-g*czas*czas)/2 + v0y*czas #z wzoru na h

vy = -g*czas +v0y
vx = np.linspace(v0x,v0x,100)

x = vx*czas
y = v0 * czas * np.sin(math.radians(alpha)) - 9.81 * czas * czas / 2

plt.subplot(3,1,1)
plt.grid(color='k',linewidth='0.2')
plt.plot(czas,vy)
plt.plot(czas,vx)
plt.title('Predkosc chwilowa po czasie t')
plt.ylabel('v [m/s]')
plt.xlabel('t [s]')

plt.subplot(3,1,2)
plt.grid(color='k',linewidth='0.2')
plt.plot(czas,y)
plt.title('Położenie w funkcji czasu')
plt.xlabel('t [s]')
plt.ylabel('y [m]')

plt.subplot(3,1,3)
plt.grid(color='k',linewidth='0.2')
plt.plot(x,y)
plt.title('Wykres toru')
plt.ylabel('y [m]')
plt.xlabel('x [m]')

plt.tight_layout()
plt.show()