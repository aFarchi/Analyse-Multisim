#_____________
# fmScaling.py
#_____________

import numpy as np
from itertools            import product

from ...path.absolutePath import *

#__________________________________________________

def computeFMScaling(matrix, levels=None, mini=None, maxi=None, nLevels=32):
    if levels is None:
        levels = np.linspace(mini, maxi, nLevels)
    else:
        nLevels = len(levels)

    FMScaling = np.zeros(nLevels)
    for i in xrange(nLevels):
        FMScaling[i] = ( matrix > levels[i] ).sum()

    return FMScaling

#__________________________________________________

def mergeFMScalings(scalingFM, fieldList, procList):
    mergedScalings = {}

    for field in fieldList:
        mergedScalings[field] = {}

        for lol in ['lin','log']:
            mean = 0.0

            for proc in procList:
                mean += scalingFM[lol][field][proc]
            mergedScalings[field][lol] = mean / len(procList)

    return mergedScalings

#__________________________________________________

def initScalingFM(fieldList):
    scalingFM = {}
    for lol in ['lin','log']:
        scalingFM[lol] = {}
        for field in fieldList:
            scalingFM[lol][field] = {}
    return scalingFM

#__________________________________________________

def writeFMScaling(scalingFM, species, AOG, fieldList, outputDir, sessionName, printIO=False):

    for (field, lol) in product(fieldList, ['lin','log']):
        fn = fileFMScaling(outputDir, sessionName, AOG, field.name, lol, species)
        if printIO:
            print ('Writing '+fn+' ...')
        np.save(fn, scalingFM[field][lol])

#__________________________________________________
