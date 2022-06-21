import numpy as np

__all__ = [
    'decomp'
    ]

def decomp(uni: np.matrix):
    mat = ""
    #print(uni[1])
    for i in range(len(uni)):
        for j in range(len(uni[i])):
            mat += (str(uni[i][j]) + ',')
        mat += "\n"
    print(mat)
    
        
