import numpy as np
import matplotlib.pyplot as plt
from plot_msd import plot_msd

if __name__ == "__main__":
    a = 28.640
    steps = 1000
    index_list = [1,2]
    # Import the  MSD and plot
    for j in range(2):
        delta_r2 = np.load("../data/msd_atom{}.npy".format(index_list[j]))
        plot_msd(delta_r2,index_list[j]) 
