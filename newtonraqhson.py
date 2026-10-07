import numpy as np


# f(x, y) = x^2 + 2y^2 - 4x + 6y +13
#cho sai so la 10^-8

def fg(x, y) :
    return np.array([2*x-4, 4*y +6],dtype = float)
def fh(x, y) : 
    return np.array([[2,0],[0, 4]],dtype =float)
saiso = pow(10,-8)

def cuctrihamso(x,y, saiso) :
    toa_do = np.array([float(x), float(y)])
    for i in range(1000) :
        x , y = toa_do
        g = fg(x,y)
        h = fh(x,y)
        t = -(np.linalg.inv(h))@g
        toa_do_new = toa_do + t
        khoang_cach = np.linalg.norm(toa_do_new - toa_do)
        if khoang_cach <= saiso :
            return toa_do_new
        toa_do = toa_do_new
    return toa_do
ketqua = cuctrihamso(0, 0 ,saiso)
print("Diem cuc tri la ",ketqua)

   
    

    