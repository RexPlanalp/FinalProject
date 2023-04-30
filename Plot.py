import numpy as np
import matplotlib.pyplot as plt

def CreatePlot(x_like,y_like,name):
    plt.plot(x_like,y_like)
    plt.savefig(name)
    return