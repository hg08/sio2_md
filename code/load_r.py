import numpy as np


def load_r(index,steps,natom):
    skiprows = 2
    r = np.zeros((steps,natom,3))
    for t in range(steps):    
        # Load data from a text file.
        fname = '../data/new_{:d}.xyz'.format(index)
        skip_t = skiprows + t*(natom+skiprows)
        print("{}".format(skip_t))
        # Read the j-th column as an array
        r[t]  = np.loadtxt(fname, dtype='float32', delimiter=" ", skiprows=skip_t, max_rows=natom, usecols=np.arange(1,4))
    return r

if __name__ == "__main__":
    index = 1
    steps = 10
    natom = 512
    r_arr = load_r(index,steps,natom)
    print(r_arr[0])
