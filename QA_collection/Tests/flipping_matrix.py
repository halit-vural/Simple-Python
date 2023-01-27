import numpy as np
import itertools

def m_sum(matrix):
    coll = 0
    for num in matrix:
        coll += num
    return coll

def inverse(matrix):
    n = len(matrix)//2
    for i in range(n):
        matrix[i], matrix[-i] = matrix[-i], matrix[i]
    
def flippingMatrix(matrix):
    # mtx = np.matrix(matrix)
    mtx = matrix
    n = len(matrix)
    
    for col in zip(*mtx):           # transpose matrix
        print(col)
        n_2 = n//2
        first_half = m_sum(col[:n_2])
        second_half = m_sum(col[n_2:])
        if first_half < second_half:
            print('unchanged:', col)
            inverse(col)
            print('changed:', col)
   

    return matrix
    


array = [[1,2,9,13],
        [3,4,10,14],
        [5,6,11,15],
        [7,8,12,16]]

res = flippingMatrix(array)
print(res)