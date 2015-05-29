#______________________
# interpolateRawData.py
#______________________

import numpy as np

from scipy.interpolate import interp1d

#__________________________________________________

def interpolate(array, axis, newN):
    oldN         = array.shape[axis]
    oldX         = ( np.arange(oldN) ) / ( oldN - 1. )
    newX         = ( np.arange(newN) ) / ( newN - 1. )
    interpolator = interp1d(oldX, array, axis=axis, bounds_error=False, fill_value=0.)
    return interpolator(newX)

#__________________________________________________

def interpolateRawData(rawData, targetShape):
    currentShape = rawData.shape
    result       = rawData.copy()
    
    for axis in xrange(len(currentShape)):
        oldN = currentShape[axis]
        newN = targetShape[axis]

        if not oldN == newN:
            result = interpolate(result, axis, newN)

    return result

#__________________________________________________
