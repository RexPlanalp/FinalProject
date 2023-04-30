import json 
import numpy as np
def CreatePsi(x):
    parameters = open("parameters.json")
    parameters = json.load(parameters)

    if parameters["psi_0"] == "gaussian":
        b = parameters["gauss_param"][0]["b"]
        p_0 = parameters["gauss_param"][0]["p_0"]
        psi = np.sqrt(2*b)/np.sqrt(np.sqrt(2*np.pi)) * np.exp(1j*p_0*x)* np.exp(-(x)**2 *b**2)
        return psi,np.abs(psi)**2,np.real(psi),np.imag(psi)
    else:
        return "This type of psi_0 is not yet implememented"
    
    
    
    
    
    
    
    