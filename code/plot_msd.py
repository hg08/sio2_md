import numpy as np
import matplotlib.pyplot as plt

def plot_msd(arr,index):
    steps = arr.shape[1]
    time_arr = np.arange(steps)
    fig = plt.figure()
    ax = fig.add_subplot(111) # add_subplot() adds an axes to a figure, it returns a (subclass of a) matplotlib.axes.Axes object.
    ax.set_xlim(0.1, 300)
    ax.set_ylim(0.001, 1.0)
    ax.set_xscale('log')
    ax.set_yscale('log')
    tw_list = [0,2,4,8]
    for i, term in enumerate(tw_list):
        ax.plot(time_arr[1:60],arr[i][1:60],label=r"$tw=${}".format(term))
    plt.legend(loc="lower left")
    plt.xlabel("t")
    plt.ylabel("MSD")
    ax.set_title("MSD of atom type {:d}".format(index))
    #
    plt.savefig("../imag/MSD_{:d}_loglog.pdf".format(index),format='pdf')

if __name__ == "__main__":
    msd_arr = np.random.random((100,100)) 
    print(msd_arr[0])
    plot_msd(msd_arr) 
