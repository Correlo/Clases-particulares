#Author: Martín Manuel Gómez Míguez
#GitHub: @Correlo
#Date: 14/12/2019

import numpy as np
import matplotlib.pyplot as plt

'''Input parameters'''

#Charge
q1, q2 = 1.,-1. #C
#Center in space grid units (h)
r1,r2 = (-1,0),(1,0)
#number of grid boxes
ngrid=10
#Size of the box in meters
scale=1. #m

#-----------------------#
#    The code begins    #
#-----------------------#


e0=8.8541878176e-12 #C^2/(N m^2)

def E(q, X, Y, h):

    #Coulomb constant
    k=1/(4*np.pi*e0)
    #Distance (plus smoothing lenght)
    r=np.sqrt(X**2 + Y**2) + h*1e-5
    #Module
    E_m=k*q/r**2
    #Components
    Cos, Sen = X/r, Y/r
    Ex, Ey = E_m*Cos, E_m*Sen

    return [Ex,Ey]

#Build the box
l,h=np.linspace(-0.5*scale,0.5*scale,ngrid,retstep=True) #m
X,Y = np.meshgrid(l,l)

#Shift mesh
X1 = X - r1[0]*h
Y1 = Y - r1[1]*h

X2 = X - r2[0]*h
Y2 = Y - r2[1]*h

#Obtain the Electric field
E1x,E1y = E(q1, X1, Y1, h)
E1_m= np.sqrt(E1x**2 + E1y**2)

E2x,E2y = E(q2, X2, Y2, h)
E2_m= np.sqrt(E2x**2 + E2y**2)

Ex,Ey = E1x + E2x, E1y + E2y
E_m= np.sqrt(Ex**2 + Ey**2)

#Vector plot
plt.figure(1, figsize=(6,6))
#Draw the normalized vector
plt.quiver(X,Y,Ex/E_m,Ey/E_m, E_m)
plt.colorbar(fraction=0.046, pad=0.04).ax.set_ylabel(r'$\vec{E}$ (N/C)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()
plt.close()

#Streamline plot
plt.figure(2, figsize=(6,6))
#Draw the normalized vector
plt.streamplot(X,Y,Ex/E_m,Ey/E_m, color=E_m)
plt.plot(X,Y,'.w')
plt.colorbar(fraction=0.046, pad=0.04).ax.set_ylabel(r'$\vec{E}$ (N/C)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()
plt.close()


