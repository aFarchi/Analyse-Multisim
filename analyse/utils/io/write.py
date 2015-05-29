#_________
# write.py
#_________

import numpy as np
from scipy.linalg import eigh

from ..sys.run    import runCommand

#__________________________________________________

def createDirectories(dirList, printIO=False):
    for d in dirList:
        runCommand('mkdir -p '+d, printIO)

#__________________________________________________

def saveSymMatrixEig(prefixFileName, matrix):
    n = matrix.shape[0]

    (eigVals,eigVects) = eigh(matrix)

    indexes            = np.argsort(abs(eigVals))
    i                  = np.arange(n)

    sortedEigVals      = eigVals[indexes[n-1-i]]
    sortedEigVects     = eigVects[:, indexes[n-1-i]]

    np.save(prefixFileName+'.npy', matrix)
    np.save(prefixFileName+'_eigVals.npy', sortedEigVals)
    np.save(prefixFileName+'_eigVects.npy', sortedEigVects)

#__________________________________________________
