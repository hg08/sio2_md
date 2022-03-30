import numpy as np
from load_r import load_r
from distance3 import distance3_squared
import matplotlib.pyplot as plt

def mds3(r_arr,a,b,c):
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

def plot(arr):
    time_arr = np.arange(steps)
    fig = plt.figure()
    ax = fig.add_subplot(111) # add_subplot() adds an axes to a figure, it returns a (subclass of a) matplotlib.axes.Axes object.
    ax.set_xlim(0.1, 300)
    ax.set_ylim(0.01, 1.0)
    ax.set_xscale('log')
    ax.set_yscale('log')
    tw_list = [0,2,4,8]
    for i, term in enumerate(tw_list):
        ax.plot(time_arr[1:60],arr[i][1:60],label=r"$tw=${}".format(term))
    plt.legend(loc="lower left")
    plt.xlabel("t")
    plt.ylabel("MSD")
    ax.set_title("MDS")
    #
    plt.savefig("../imag/MSD_loglog.pdf",format='pdf')

if __name__ == "__main__":
    index = 1
    steps = 100
    natom = 512
    a = 2.7
    r_arr = load_r(index,steps,natom)
    print(r_arr[0])
    delta_r2 = mds3(r_arr,a,a,a)
    plot(delta_r2) 
