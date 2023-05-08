from scipy import linalg
from scipy import sparse
import numpy as np
import json
import scipy.sparse.linalg as spsp

'''
Selects Propagator for time evolution

The input file parameters decides what kind of evolution.
Currently only Crank-NicholsonO3,Crank-NicholsonO4, and Imaginary
are implemented. 

Note CN_2nd is the same as CN_4th but with less diagonal elements.
Additionally for Imaginary, its equivalent to t = -it for CN_4th
'''


parameters = open("parameters.json")
parameters = json.load(parameters)

if parameters["prop"] == "CN_4th":
    def CreateCNTimeEvol(x,t,psi_0,V):
        Nx = len(x) # Counts number of x/t points
        Nt = len(t)
        dx = x[1] - x[0] # Finds x/t resolution
        dt = t[1] - t[0]

        I = np.ones_like(x,complex) # Creates identity vector
        alpha1 = ((1j)*dt/2)*(4/(3*dx**2))*I # Creates first off diagonal values
        alpha2 = ((1j)*dt/2)*(-1/(12*dx**2))*I # Creates second off diagonal values

        zeta = I - ((1j)*dt/2)*(V+5*I/(2*dx**2)) # Creates diagonal values for inverse U
        gamma = I + ((1j)*dt/2)*(V+5*I/(2*dx**2)) # Creates diagonal values for U 

        diags = np.array([-2,-1,0,1,2]) # Defines how the diagonal info will be distributed wrt main diagonal

        vecs1 = np.array([-alpha2,-alpha1,zeta,-alpha1,-alpha2]) # Constructs vectors of diagonal values 
        vecs2 =  np.array([alpha2,alpha1,gamma,alpha1,alpha2]) # corresponding to the diags vector

        U1 = sparse.spdiags(vecs1,diags,Nx,Nx) # Uses scipy.sparse package to create sparse quintuple diagonal matrices
        U2 = sparse.spdiags(vecs2,diags,Nx,Nx)

        U1.tocsc() # Converts to compresssed sparse column matrices for linear solver
        U2.tocsc()

        PSI = np.zeros((Nx,Nt),dtype =complex) # Creates empty Nx X Nt array to store wavefunction history
        PSI[:,0] = psi_0 # Sets initial wavefunction value 

        LU = spsp.splu(U1) # Factors U1 into lower and upper diagonal matrices for more efficient linear solving
        
        #for n in range(0,Nt - 1): # loop over time-steps
            #b = U2.dot(PSI[:,n]) # right hand side of eq. (3.9)
            #PSI[:,n + 1] = LU.solve(b)
            #print(n,Nt)
        
        for n in range(0,Nt - 1): # Iterates over all time steps
            b = U2.dot(PSI[:,n]) # computes the RHS of CN Equation
            sol = LU.solve(b) # Solves linear system for updated wavefunction
            PSI[:,n + 1] = sol/np.sqrt(np.linalg.norm(sol**2)) # Normalizes and sets value of next wavefunction step
            print(n,Nt) # Prints current step 
        return PSI

if parameters["prop"] == "CN_2nd":
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
        for n in range(0,Nt - 1): 
            b = U2.dot(PSI[:,n]) 
            PSI[:,n + 1] = LU.solve(b)
            print(n,Nt)
        #for n in range(0,Nt - 1): 
            #b = U2.dot(PSI[:,n]) 
            #sol = LU.solve(b)
            #PSI[:,n + 1] = sol/np.sqrt(np.linalg.norm(sol**2))
            #print(n,Nt)
        return PSI

if parameters["time"] != "real":
    def CreateCNTimeEvol(x,t,psi_0,V):
        Nx = len(x)
        Nt = len(t)
        dx = x[1] - x[0]
        dt = t[1] - t[0]

        I = np.ones_like(x,complex)
        alpha1 = (dt/2)*(4/(3*dx**2))*I
        alpha2 = (dt/2)*(-1/(12*dx**2))*I

        zeta = I + (dt/2)*(V+5*I/(2*dx**2))
        gamma = I - (dt/2)*(V+5*I/(2*dx**2))

        diags = np.array([-2,-1,0,1,2])

        vecs1 = np.array([-alpha2,-alpha1,zeta,-alpha1,-alpha2])
        vecs2 =  np.array([alpha2,alpha1,gamma,alpha1,alpha2])

        U1 = sparse.spdiags(vecs1,diags,Nx,Nx)
        U2 = sparse.spdiags(vecs2,diags,Nx,Nx)

        U1.tocsc()
        U2.tocsc()

        PSI = np.zeros((Nx,Nt),dtype = complex)
        PSI[:,0] = psi_0

        LU = spsp.splu(U1)
        for n in range(0,Nt - 1): 
            b = U2.dot(PSI[:,n]) 
            sol = LU.solve(b)
            PSI[:,n + 1] = sol/np.sqrt(np.linalg.norm(sol**2))
            print(n,Nt)
    
        return PSI
 


if parameters["prop"] == "TEST":
    def CreateCNTimeEvol(x,t,psi_0,V):
        Nx = len(x)
        Nt = len(t)
        dx = x[1] - x[0]
        dt = t[1] - t[0]

        I = np.ones_like(x,complex)
        alpha1 = ((1j)*dt/2)*(4/(6*dx**2))*I
        alpha2 = ((1j)*dt/2)*(-1/(24*dx**2))*I

        zeta = I + ((1j)*dt/2)*(V-5*I/(4*dx**2))
        gamma = I - ((1j)*dt/2)*(V-5*I/(4*dx**2))

        diags = np.array([-2,-1,0,1,2])

        vecs1 = np.array([-alpha2,-alpha1,zeta,-alpha1,-alpha2])
        vecs2 =  np.array([alpha2,alpha1,gamma,alpha1,alpha2])

        U1 = sparse.spdiags(vecs1,diags,Nx,Nx)
        U2 = sparse.spdiags(vecs2,diags,Nx,Nx)

        U1.tocsc()
        U2.tocsc()

        PSI = np.zeros((Nx,Nt),complex)
        PSI[:,0] = psi_0

        LU = spsp.splu(U1)
        
        #for n in range(0,Nt - 1): # loop over time-steps
            #b = U2.dot(PSI[:,n]) # right hand side of eq. (3.9)
            #PSI[:,n + 1] = LU.solve(b)
            #print(n,Nt)
        
        for n in range(0,Nt - 1): # loop over time-steps
            b = U2.dot(PSI[:,n]) # right hand side of eq. (3.9)
            sol = LU.solve(b)
            PSI[:,n + 1] = sol/np.sqrt(np.linalg.norm(sol**2))
            print(n,Nt)

        return PSI