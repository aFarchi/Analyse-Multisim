#_________
# write.py
#_________

import numpy as np
from scipy.linalg import eigh

from ..sys.run    import runCommand

#__________________________________________________

def writeLinesFillingWithArgs(lines, fileName, args):
    f = open(fileName, 'w')
    for line in lines:
        for arg in args:
            line = line.replace(arg, args[arg])
        f.write(line)
    f.close()

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
