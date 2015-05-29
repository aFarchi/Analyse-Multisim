#_____________
# grayScale.py
#_____________

import numpy as np

#__________________________________________________

def makeGrayScale(matrix, levels=None, mini=None, maxi=None, nLevels=32, threshold=None):

    if levels is None:
        levels = np.linspace(mini, maxi, nLevels)
    else:
        nLevels = len(levels)

    if threshold is None:
        threshold = matrix.min() - 1

    CDF = np.zeros(nLevels+1)

    for i in xrange(nLevels-1):
        CDF[i+1] = ( ( matrix < levels[i] ) * ( matrix > threshold ) ).mean()

    CDF[nLevels] = ( matrix > threshold ).mean()

    if CDF[nLevels] == 0:
        CDF    = np.ones(nLevels+1)
        CDF[0] = 0.0
    else:
        CDF /= CDF[nLevels]

    PDF = CDF[1:nLevels+1] - CDF[0:nLevels]
    return PDF

#__________________________________________________
