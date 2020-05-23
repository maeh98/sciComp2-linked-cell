import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams, patches
import time
from itertools import product


def lj_potential(distance, c1=1e-15, c2=1e-5):
    return   (c1 / distance**12) - (c2 / distance**6)

def get_successor_neighbor_delta_coordinate(a=1):
    """Returns neighbor_delta_coordinate
    
    Parameters
    ---------
    a: int
        Variable linked-cell parameter
    """
    
    neighbor_delta_coordinate = []
    ############# Task 1.1 begins ##################
    mesh = np.array(np.meshgrid(range(a), range(a)))
    candidates = (1+mesh.T.reshape(-1, 2)).tolist()
    for c in candidates:
        minDist = np.sqrt((c[0]-1)**2 + (c[1]-1)**2) #distance to lower left corner in units of cell width
        if minDist <= a:
            neighbor_delta_coordinate.append(c)
    ############ Task 1.1 ends #####################
    return neighbor_delta_coordinate

def plot_all_cells(ax, list_cells, edgecolor='r',domain=1):
    for c in list_cells:
        c.plot_cell(ax, edgecolor=edgecolor)
    ax.tick_params(axis='both',labelsize=0, length = 0)
    plt.xlim(left=0, right=domain)
    plt.ylim(bottom=0, top=domain)
    ax.set_aspect('equal', adjustable='box')
    
def get_mean_relative_error(direct_potential, linked_cell_potential):
    return np.mean(np.abs((direct_potential - linked_cell_potential) / direct_potential))
