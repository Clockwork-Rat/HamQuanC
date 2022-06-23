
import numpy as np
from numpy.linalg import eig, inv
import sys

__all__ = [
    'unitary'
    ]

_debug = False

def unitary(filename: str):
    #load data in
    #h = np.genfromtxt(filename, delimeter=',')
    h = np.genfromtxt(filename, delimeter=",")
    print(h)
    #generate diaganol to check
    e = eig(h)[1].transpose()
    v = eig(h)[0]
    print(v)
    diag = e * h * inv(e)
    
    #print diaganal for debug
    if _debug:
        print(diag)
        print("Identity matrix")
        print ( e.transpose() * inv(e).transpose() )

    #return unitary transpoition
    return e.transpose()

def _unitary(mtrx: np.matrix):
    e = eig(mtrx)[1].transpose()
    #diag = e * mtrx * inv(e)

    return e.transpose()

def m_unitary(filename: str, size: int):
    h = np.genfromtxt(filename, delimiter=",")
    #print(h)
    
    ret = []
    #out_tmp = []

    for i in range(len(h)):
        for j in range(len(h[i])):
            if j + size < (len(h[i]) + 1) and i + size < (len(h[i]) + 1):
                temp = []
                for k in range(size):
                    temp.append(h[i+k][j : j + size])
                #print(h[i+j][i : i+ size])
                print(np.matrix(temp))
                #temp.append(h[i+j][i : i + size])

                
            #print(temp)
            #print(np.matrix(temp))
            ret.append(_unitary(np.matrix(temp)))
            #print(ret[i])
    return ret

    


#### debug ####
def main():
    unitary(sys.argv[1])

if __name__ == '__main__':
    _debug = True
    main()



