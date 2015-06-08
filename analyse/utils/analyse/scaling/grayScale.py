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

    try:
        spacing = levels[1] - levels[0]
    except:
        spacing = 1.0
    if spacing == 0.0:
        spacing = 1.0

    # threshold
    if threshold is None:
        threshold = matrix.min() - 1

    # compute CDF
    CDF = np.zeros(nLevels)
    for i in xrange(nLevels-2):
        CDF[i+1]   = ( ( matrix < levels[i] ) * ( matrix > threshold ) ).mean()
    CDF[nLevels-1] = ( matrix > threshold ).mean()

    # rescale CDF
    if CDF[nLevels-1] == 0.0:
        PDF = np.zeros(nLevels)
        PDF[0] = 1.0# / spacing
        return PDF

    CDF /= CDF[nLevels-1]

    # derivate CDF
    dCDF = ( CDF[1:] - CDF[:nLevels-1] )# / spacing

    # interpolate PDF = derivate(CDF)
    PDF              = np.zeros(nLevels)
    PDF[0]           = dCDF[0] / 2.0
    PDF[1:nLevels-1] = ( dCDF[1:] + dCDF[:nLevels-2] ) / 2.0
    PDF[nLevels-1]   = dCDF[nLevels-2] / 2.0

    return PDF

#__________________________________________________
