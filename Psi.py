import json 
import numpy as np
def CreatePsi(x,parfile = "parameters.json"):
    '''
    Creates initial wavefunction based on input parameters
    
    Parameters:
        x (numpy array) : Spacial component of simulation box
        parfile (json) : Parameters for initial shape/kind of wavefunction

    Returns:
        psi (numpy array) : Wavefunction at t = 0
    '''
    parameters = open(parfile) # opens parfile
    parameters = json.load(parameters)

    if parameters["psi_0"] == "gaussian": # Imports parameters for gaussian wavepacket wavefunction
        b = parameters["gauss_param"][0]["b"]
        p_0 = parameters["gauss_param"][0]["p_0"]
        center = parameters["gauss_param"][0]["center"]
        psi = np.sqrt(2*b)/np.sqrt(np.sqrt(2*np.pi)) * np.exp(1j*p_0*(x-center))* np.exp(-(x-center)**2 *b**2)
        C = 1/np.sqrt(np.linalg.norm(np.abs(psi)**2))
        psi = psi*C
        return psi
    else:
        return "This type of psi_0 is not yet implememented"
    
    
    
    
    
    
    
    