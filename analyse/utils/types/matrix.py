#__________
# matrix.py
#__________

import numpy as np

#__________________________________________________

def permuteMatrix(matrix):

    N = matrix.shape[0]
    P = int(np.round(np.sqrt(N)))

    if not matrix.shape == (N,N):
        return matrix

    if not P**2 == N:
        return matrix

    permutedMatrix = np.zeros(shape=(N,N))
    permutation    = np.arange(N).reshape((P,P), order='F').reshape(N)

    # non vectorized version for testing
    #for i in xrange(N):
    #     for j in xrange(N):
    #        permutedMatrix[i,j] = matrix[permutation[i],permutation[j]]
 
    # vectorized version
    temp = matrix[permutation[:],:]
    return temp[:,permutation[:]]

#__________________________________________________
