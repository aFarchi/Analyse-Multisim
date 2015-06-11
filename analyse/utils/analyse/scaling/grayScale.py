#_____________
# grayScale.py
#_____________

import numpy as np

#__________________________________________________

def makeGrayScale(matrix, levels=None, mini=None, maxi=None, nLevels=32, threshold=None):

    # make levels
    if levels is None:
        levels  = np.linspace(mini, maxi, nLevels)
    else:
        nLevels = len(levels)

    # threshold
    if threshold is None:
        threshold = matrix.min() - 1

    # compute CDF
    CDF = np.zeros(nLevels)
    for i in xrange(nLevels-1):
        CDF[i] = ( ( matrix < levels[i] ) * ( matrix > threshold ) ).mean()

    CDF[0]     = 0.0 # should be aready the case, but just to make sure...
    CDF[-1]    = ( matrix > threshold ).mean()


    # rescale CDF
    if CDF[-1] == 0.0:
        PDF    = np.zeros(nLevels)
        PDF[0] = 1.0
        return PDF

    CDF /= CDF[-1]

    # derivate CDF
    dCDF = ( CDF[1:] - CDF[:-1] )

    # interpolate PDF = derivate(CDF)
    PDF       = np.zeros(nLevels)
    PDF[0]    = dCDF[0] / 2.0
    PDF[1:-1] = ( dCDF[1:] + dCDF[:-2] ) / 2.0
    PDF[-1]   = dCDF[-2] / 2.0

    return PDF

#__________________________________________________
