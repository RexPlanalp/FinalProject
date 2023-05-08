from Plot import *
from Grid import *
import json

'''
Displays density at chosen times

Not as modular as other files since this
needs to be changed subtly/frequently

'''

x,t = CreateGrid() # Creates local copy of x,y and measures time steps
Nt = len(t)


t_frac = 0.8 # Fraction to determine at what percentage of the total time to plot
Nt_anal = int(t_frac*Nt)

PSI = np.load("psi_files/PSI.npy") # Opens wavefunction array, confirms the size of PSI, and computes 
print("The shape of PSI is",PSI.shape) # the density
PSI_dens = np.abs(PSI)**2


lab = ["t = 0",r"t = 3","t = 6"] # Defines the labels for each x,y data plot
#x_like = [x,x,x] # Creates copy of x for each plotted wavefunction
#y_like = [PSI_dens[:,0],PSI_dens[:,Nt_anal],PSI_dens[:,Nt-1]] # Defines wavefunction times to plot
x_like =[x]
y_like = [PSI_dens[:,Nt_anal]]


# Plots all x,y datasets on the same plot
CreatePlot(x_like,y_like,lab,"Gaussian Wavepacket: T = 6",name = "images/Psi_Dens_Evolved.jpg")

# Confirms the normalization of wavefunction times in y_like
print("The Norm at this time is:",np.linalg.norm(y_like[0]))







