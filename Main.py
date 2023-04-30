from Grid import *
from Psi import * 
from Potential import * 
from Plot import * 
from CNTimeStep import *


x,t = CreateGrid()
psi_0,psi_dens,psi_real,psi_imag = CreatePsi(x)
V,V_norm= CreateV(x)

CreatePlot(x,V_norm,"images/Potential.jpg")
CreatePlot(x,psi_dens,"images/Psi_Dens.jpg")

PSI,PSI_dens,PSI_real,PSI_imag = CreateCNTimeEvol(x,t,psi_0,V)

print(PSI_dens.shape)
CreatePlot(x,PSI_dens[:,4000],"images/Psi_Dens_Evolved.jpg")












