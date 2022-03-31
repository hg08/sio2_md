import numpy as np
from load_r import load_r
from distance3 import distance3_squared
import matplotlib.pyplot as plt
from plot_msd import plot_msd

def msd3(r_arr,a,b,c):
    steps = r_arr.shape[0]
    natom = r_arr.shape[1]
    delta_r2 = np.zeros((steps,steps))
    for tw in range(steps):
        for t in range(steps-tw):
            delta_r2[tw,t] = 0
            for i in range(natom):
                delta_r2[tw,t] += distance3_squared(r_arr[t+tw][i][0],r_arr[t+tw][i][1],r_arr[t+tw][i][2], r_arr[tw][i][0],r_arr[tw][i][1],r_arr[tw][i][2],a,b,c)
            delta_r2[tw,t] =delta_r2[tw,t]/natom
    return delta_r2
def msd3_(r_arr,a,b,c,dt=80):
    steps = r_arr.shape[0]
    natom = r_arr.shape[1]
    num_tw = int((steps/dt)/2)
    delta_r2 = np.zeros((num_tw,steps))
    for tw in range(num_tw):
        for t in range(steps-tw*dt):
            delta_r2[tw,t] = 0
            for i in range(natom):
                delta_r2[tw,t] += distance3_squared(r_arr[t+tw*dt][i][0],r_arr[t+tw*dt][i][1],r_arr[t+tw*dt][i][2], r_arr[tw*dt][i][0],r_arr[tw*dt][i][1],r_arr[tw*dt][i][2],a,b,c)
            delta_r2[tw,t] =delta_r2[tw,t]/natom
    return delta_r2

if __name__ == "__main__":
    index = 1
    steps = 640
    natom = 512
    a = 28.640
    r_arr = load_r(index,steps,natom)
    print(r_arr[0])
    delta_r2 = msd3_(r_arr,a,a,a)
    plot_msd(delta_r2,index) 
