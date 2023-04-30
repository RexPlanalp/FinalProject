import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
from scipy import sparse 
from scipy.sparse.linalg import splu
from matplotlib import animation

N = 3000
t = np.linspace(0,0.6,N)
x = np.linspace(-4,8,N)
dx = x[1] -x[0]
dt = t[1] -t[0]
b = 1
p_0 = 40



def psi(x):
    return np.sqrt(2*b)/np.sqrt(np.sqrt(2*np.pi)) * np.exp(1j*p_0*x)* np.exp(-(x)**2 *b**2)


'''
Now we define our potential 
'''
def V(x):
    vvals = []
    for i in x:
        if 2.99<= i<= 3:
            vvals.append(6000)
        else:
            vvals.append(0)
    return vvals

'''
We use the Crank-Nicholsom scheme to construct our propagator
'''
o = np.ones((N),complex)
alp = (1j)*dt/(2*dx**2)*o # alpha from (3.11)
xi = o + 1j*dt/2*(2/(dx**2)*o + V(x)) # xi from (3.11)
diags = np.array([-1,0,+1]) # positions of the vectors in the matrix
vecs1 = np.array([-alp,xi,-alp])
U1 = sparse.spdiags(vecs1,diags,N,N) # create tridiagonal sparse matrix
U1 = U1.tocsc() # convert to different sparse format needed for further calculation

o2 = np.ones((N),complex)
alp = (1j)*dt/(2*dx**2)*o # alpha from (3.11)
gum = o - 1j*dt/2*(2/(dx**2)*o + V(x)) # xi from (3.11)
diags = np.array([-1,0,+1]) # positions of the vectors in the matrix
vecs2 = np.array([alp,gum,alp])
U2 = sparse.spdiags(vecs2,diags,N,N) # create tridiagonal sparse matrix
U2 = U2.tocsc() 

PSI = np.zeros((N,N),complex)
PSI[:,0] = psi(x)
LU = splu(U1) # compute LU-decomposition of U1
for n in range(0,N - 1): # loop over time-steps
    b = U2.dot(PSI[:,n]) # right hand side of eq. (3.9)
    PSI[:,n + 1] = LU.solve(b)
'''
Now we animate our solution
'''

par = 0.00001

fig = plt.figure()
ax = plt.axes(xlim=(-4,8), ylim=(-1.8, 1.8))
line, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return line,


def animate(i):
    x = np.linspace(-4, 8, N)
    y = PSI[:,i]
    line.set_data(x, np.abs(y)**2)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=600, interval=30, blit=True)
plt.plot(x,V(x))
plt.show()

anim.save('PartiallyReflected.mp4', fps=60,dpi =250)


