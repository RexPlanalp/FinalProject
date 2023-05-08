from scipy import linalg
from scipy import sparse
import numpy as np
import json
import scipy.sparse.linalg as spsp


def CreateCNTimeEvol(x,t,psi_0,V):
    Nx = len(x)
    Nt = len(t)
    dx = x[1] - x[0]
    dt = t[1] - t[0]


    I = np.ones_like(x,complex)
    alpha = (1j)*dt/(2*dx**2)*I

    zeta = I + ((1j)*dt/2)*(V+2*I/(dx**2))
    gamma = I - ((1j)*dt/2)*(V+2*I/(dx**2))

    diags = np.array([-1,0,1])

    vecs1 = np.array([-alpha,zeta,-alpha])
    vecs2 = np.array([alpha,gamma,alpha])

    U1 = sparse.spdiags(vecs1,diags,Nx,Nx)
    U2 = sparse.spdiags(vecs2,diags,Nx,Nx)

    U1.tocsc()
    U2.tocsc()

    PSI = np.zeros((Nx,Nt),complex)
    PSI[:,0] = psi_0

    LU = spsp.splu(U1)
    for n in range(0,Nt - 1): # loop over time-steps
        b = U2.dot(PSI[:,n]) # right hand side of eq. (3.9)
        PSI[:,n + 1] = LU.solve(b)
        print(n,Nt)
    
    return PSI