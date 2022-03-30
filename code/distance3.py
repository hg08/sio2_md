import numpy as np

def distance3(x1,y1,z1,x2,y2,z2,a,b,c):
    delta_x = distance(x1,x2,a)
    delta_y = distance(y1,y2,b)
    delta_z = distance(z1,z2,c)
    d = np.sqrt(delta_x**2 + delta_y**2 + delta_z**2)
    return d
def distance3_squared(x1,y1,z1,x2,y2,z2,a,b,c):
    delta_x = distance(x1,x2,a)
    delta_y = distance(y1,y2,b)
    delta_z = distance(z1,z2,c)
    d2 = delta_x**2 + delta_y**2 + delta_z**2
    return d2
def distance(x1,x2,a):
    abs12 = np.abs(x1-x2)
    if abs12 > a/2:
        dist = a - abs12
    else:
        dist = x1-x2
    return dist

if __name__ == "__main__":
    x1,y1,z1 = 0,0,0
    x2,y2,z2 = 10,10,10
    a,b,c = 12,12,12
    d1= distance(x1,x2,a)
    print(d1)
    d = distance3(x1,y1,z1,x2,y2,z2,a,b,c)
    print(np.sqrt(12**2 + 12**2 + 12**2)-17.3)
    print(d)
