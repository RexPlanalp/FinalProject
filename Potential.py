import json
import numpy as np 
def CreateV(x):
    parameters = open("parameters.json")
    parameters = json.load(parameters)

    if parameters["potential"] == "barrier":
        center = parameters["barrier_param"][0]["center"]
        width = parameters["barrier_param"][0]["width"]
        height = parameters["barrier_param"][0]["height"]

        V_0 = np.zeros_like(x)
        V_0[np.logical_and((x<center+width/2),(x>center-width/2))] = height
        return V_0,V_0/np.max(V_0)