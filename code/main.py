import numpy as np
from load_r import load_r
from distance3 import distance3_squared
import matplotlib.pyplot as plt
from plot_msd import plot_msd
from msd3 import msd3

if __name__ == "__main__":
    a = 28.640
    steps = 1000
    index_list = [1,2]
    natom_list = [512,1024]
    # Calculat the MSD and plot
    for j in range(2):
        r_arr = load_r(index_list[j],steps,natom_list[j])
        print(r_arr[0])
        delta_r2 = msd3(r_arr,a,a,a)
        plot_msd(delta_r2,index_list[j]) 
