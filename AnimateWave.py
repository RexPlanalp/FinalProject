from Plot import *
from Grid import *
from Potential import *
from matplotlib import animation
import json


'''
Animates Wavefunction

Not as modular as other files since this
needs to be changed subtly/frequently


'''




x,t = CreateGrid() # Creates another copy of x,t for this file

PSI = np.load("psi_files/PSI.npy") # Opens saved wavefunction array
print("The shape of PSI is",PSI.shape) # Confirms size of wavefunction array
PSI_dens = np.abs(PSI)**2 # Computes the density at each time step

fig = plt.figure() # Constructs matplotlib figure, defining plot limits and figure size
ax = plt.axes(xlim=(-40,40), ylim=(-0.1, 0.1))
line, = ax.plot([], [], lw=2)


def init(): # Defines initialize function to draw each frame
    line.set_data([], [])
    return line,


def animate(i): # Defines animate function to retrieve data for each frame
    global x
    print(i,len(t))
    y = PSI_dens[:,i-1]
    line.set_data(x, y)
    return line,


print("Starting Animation") # Draws animation for as many time steps as frames
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=2999, interval=10, blit=True)
#y = np.max(PSI_dens[:,Nt-1])*np.exp(-0.15*x**2)
#plt.plot(x,y,label = "Exact")




plt.plot(x,np.real(CreateV(x)[1]),label = "Potential", color = "k") # Plots potential along with figure title and adds labels
plt.title("Gaussian Wavepacket")
plt.legend()
plt.show()


# Saves 
anim.save('./images/PartiallyReflected.mp4', fps=60,dpi =250) # Saves wavefunction animation as mp4 file
print("Finished Animating")