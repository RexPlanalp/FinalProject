import json
import numpy as np

def CreateGrid(gridfile = "sim_box.json"):
    grid_data = open(gridfile)
    grid_data = json.load(grid_data)

    x = np.linspace(grid_data["x_min"],grid_data["x_max"],grid_data["Nx"])
    t = np.linspace(0,grid_data["t_max"],grid_data["Nt"])

    return x,t
