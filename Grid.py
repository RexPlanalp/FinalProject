import json
import numpy as np

def CreateGrid(gridfile = "sim_box.json"):
    '''
    Constructs the simulation box in time and space

    Parameters:
        gridfile (json) : Input file to determine grid characteristics
        
    
    Returns:
        x,t (tuple) : Tuple of numpy arrays for discretized space/time
    '''
    grid_data = open(gridfile) # Opens gridfile
    grid_data = json.load(grid_data)

   

    x = np.linspace(grid_data["x_min"],grid_data["x_max"],grid_data["Nx"]) # Defines x,t using imported parameters
    t = np.linspace(0,grid_data["t_max"],grid_data["Nt"]) # and np.linspace

    ECS = grid_data["ECS"]
    if ECS != 0:
        Nx_ECS = int(len(x)*ECS)
        x[Nx_ECS:] = x[Nx_ECS:] * np.exp(-1j*np.pi/4)
    else:
        pass

    return x,t

