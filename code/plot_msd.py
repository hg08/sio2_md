import numpy as np
import matplotlib.pyplot as plt

def plot_msd(arr,index,dt=80, unit=10):
    steps = arr.shape[1]
    step_list = range(steps)
    time = [t * unit for t in step_list]
    print(len(time))
    print(time)
    print(arr.shape)
    print(arr)
    fig = plt.figure()
    ax = fig.add_subplot(111) # add_subplot() adds an axes to a figure, it returns a (subclass of a) matplotlib.axes.Axes object.
    ax.set_xlim(0.01, 500)
    ax.set_ylim(0.0001, 20.0)
    ax.set_xscale('log')
    ax.set_yscale('log')
    tw_index_list = [0,2,4,8]
    tw_list = [tw*dt for tw in tw_index_list]
    for i, term in enumerate(tw_list):
        ax.plot(time,arr[i],label=r"$tw=${}".format(term))
    plt.legend(loc="lower left")
    plt.xlabel("t")
    plt.ylabel("MSD")
    ax.set_title("MSD of atom type {:d}".format(index))
    #
    plt.savefig("../imag/MSD_{:d}_loglog.pdf".format(index),format='pdf')

if __name__ == "__main__":
    msd_arr = np.random.random((1000,100)) 
    print(msd_arr[0])
    plot_msd(msd_arr,1) 
