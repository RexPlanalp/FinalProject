import numpy as np
import matplotlib.pyplot as plt

def CreatePlot(x_like,y_like,labels,title,name):
    '''
    Helper Function for making detailed plots

    Paramters:
        x_like/y_like (list) : x,y data to plot
        labels (list) : labels for individual x,y data
        title (string) : title of plot
        name (string) : name of file figure is saved to

    Returns:
        jpg file of figure
    
    '''
    if type(x_like) != type(y_like): # Checks to make sure x_like and y_like are the 
        return "x and y must be the same type" # same type(ideally arrays or lists)
    if type(x_like) == list: # If they are iterable then loops over all x,y data pairs and labels,
        for x,y,lab in zip(x_like,y_like,labels): # plotting on the same figure
            plt.plot(x,y,label = f"{lab}")
            plt.legend()
            plt.title(title)
            plt.savefig(name)
    return



   