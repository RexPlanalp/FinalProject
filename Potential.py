import json
import numpy as np 
def CreateV(x,parfile = "parameters.json"):
    '''
    Constructs the potential that the wavefunction will interact with

    Parameters:
        x (numpy array) : spacial component of simulation box
        parfile (json) : Input file to determine nature/kind of potential
    
    Returns:
        V,V (tuple) : Returns potential, with optional normalized version for easier plotting
    '''
    parameters = open(parfile)
    parameters = json.load(parameters)

    if parameters["potential"] == "barrier": # Imports parameters for finite/infinite barrier potential
        center = parameters["barrier_param"][0]["center"]
        width = parameters["barrier_param"][0]["width"]
        height = parameters["barrier_param"][0]["height"]
        sign = int(parameters["barrier_param"][0]["sign"])
        V_0 = np.zeros_like(x)
        V_0[np.logical_and((x<center+width/2),(x>center-width/2))] = height
        return sign*V_0,sign*V_0/np.max(V_0)
    elif parameters["potential"] == "harmonic": # Imports parameters for harmonic potential
        omega = parameters["harmonic_param"][0]["omega"]
        center = parameters["harmonic_param"][0]["center"]
        return 0.5*omega**2 * (x-center)**2,0.5*(x-center)**2
    elif parameters["potential"] == "None": # Defines free particle potential
        return 0*x,0*x
    

    
        
