
import numpy as np
from numpy.linalg import eig, inv
import sys

__all__ = [
    'unitary'
    ]

_debug = False

def unitary(filename: str):
    #load data in
    h = np.genfromtxt(filename)
    print(h)
    #generate diaganol to check
    e = eig(h)[1].transpose()
    diag = e * h * inv(e)
    
    #print diaganol for debug
    if _debug:
        print(diag)
        print("Identity matrix")
        print ( e.transpose() * inv(e).transpose() )

    #return unitary transpoition
    return e.transpose()

#### debug ####
def main():
    unitary(sys.argv[1])

if __name__ == '__main__':
    _debug = True
    main()



