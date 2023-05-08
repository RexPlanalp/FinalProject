from Grid import *
from Psi import * 
from Potential import * 
from Plot import * 
from Propagator import *


'''
Main loop for TDSE simulation

1. Creates simulation box

2. Initializes wavefunction

3. Confirms wavefunction normalization

4. Initializes the potential

5. Creates Useful plots

6. Evolves wavefunction over each step and saves
'''


print("Creating Grid")
x,t = CreateGrid()
print("Initializing Wavefunction")
psi_0 = CreatePsi(x)
psi_dens = np.abs(psi_0)**2

print("The wavefunction is normalized to",np.linalg.norm(np.abs(psi_0)**2))

print("Constructing Potential")
V,V_norm= CreateV(x)


CreatePlot(x,V_norm,"Potential","Potential",name = "images/Potential.jpg")
CreatePlot(x,psi_dens,"Psi_Dens","Psi_Dens","images/Psi_Dens.jpg")
print("Evolving Wavefunction")
PSI = CreateCNTimeEvol(x,t,psi_0,V)

np.save("psi_files/PSI.npy",PSI)

print("Done Evolving Wavefunction")













