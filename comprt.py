#Author: Martín Manuel Gómez Míguez
#GitHub: @Correlo
#Date: 21/12/2019

import numpy as np
import matplotlib.pyplot as plt
import cmath

'''Input parameters'''

#Index of the root
n = 5

#Complex number
z = 1.3 + 4j

#-----------------------#
#    The code begins    #
#-----------------------#

if type(n) != int or n <= 0:
 
    raise ValueError('El indice introducido no es válido')

#Module
Z = np.sqrt(np.real(z*z.conjugate()))

if Z==0j: 
    
    raise ValueError('El numero complejo introducido no es válido')

#Phase 
phase_z = cmath.phase(z)

#Module of the n-root
mod_nrtz = Z**(1/n)

#Phase of the n-root
phase_nrtz = phase_z/n + 2*np.pi*np.arange(n+1)/n

#Angle range
phi=np.linspace(-np.pi,np.pi,200)

plt.figure(figsize=(6,6))
plt.plot(Z*np.cos(phi), Z*np.sin(phi), 'k-', label = 'module')
plt.plot(Z*np.cos(phase_nrtz), Z*np.sin(phase_nrtz), 'b-', label = 'root graph')
plt.xlabel('Re(z)', fontsize = 15)
plt.ylabel('Im(z)', fontsize = 15)
plt.minorticks_on()
plt.tick_params(axis='both',direction='inout',which='minor',length=3,width=.5,labelsize=14)
plt.tick_params(axis='both',direction='inout',which='major',length=8,width=1,labelsize=14)
plt.legend(frameon=False)
plt.show()
