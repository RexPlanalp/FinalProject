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

    o = np.ones((Nx),complex)
    alp = (1j)*dt/(2*dx**2)*o # alpha from (3.11)
    xi = o + 1j*dt/2*(2/(dx**2)*o + V) # xi from (3.11)
    diags = np.array([-1,0,+1]) # positions of the vectors in the matrix
    vecs1 = np.array([-alp,xi,-alp])
    U1 = sparse.spdiags(vecs1,diags,Nx,Nx) # create tridiagonal sparse matrix
    U1 = U1.tocsc() # convert to different sparse format needed for further calculation


    o2 = np.ones((Nx),complex)
    alp = (1j)*dt/(2*dx**2)*o # alpha from (3.11)
    gum = o - 1j*dt/2*(2/(dx**2)*o + V) # xi from (3.11)
    diags = np.array([-1,0,+1]) # positions of the vectors in the matrix
    vecs2 = np.array([alp,gum,alp])
    U2 = sparse.spdiags(vecs2,diags,Nx,Nx) # create tridiagonal sparse matrix
    U2 = U2.tocsc() 


    PSI = np.zeros((Nx,Nt),complex)
    PSI[:,0] = psi_0

    LU = spsp.splu(U1)
    for n in range(0,Nt - 1): # loop over time-steps
        b = U2.dot(PSI[:,n]) # right hand side of eq. (3.9)
        PSI[:,n + 1] = LU.solve(b)
    
    return PSI,np.abs(PSI)**2,np.real(PSI),np.imag(PSI)
