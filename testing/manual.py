import numpy as np
import scipy.linalg as sla
from numpy.linalg import eig, inv


def main():
    time = 0.0
    E_0 = 13000
    E_1 = 12900

    A = 1.0 / 8.0
    T2 = 0.25
    omega = 100.0

    photon = A * np.e ** (time/T2) * np.cos(omega * time)

    off_diag = np.matrix('0, 1; 1, 0')
    H_I = photon * off_diag
    H_s = np.matrix(str(E_0)+', 0; 0,'+str(E_1))
    H_f = H_I + H_s

    T, H_fd = diagonal(H_f)
    print(H_fd)
    print(T)

def diagonal(mat):
    e = eig(mat)[1].transpose()

    diag = e * mat * inv(e)
    print( e * inv(e))

    return e, np.diag(np.diag(diag))



if __name__ == '__main__':
    main()