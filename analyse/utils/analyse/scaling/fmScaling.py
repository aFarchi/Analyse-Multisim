#_____________
# fmScaling.py
#_____________

import numpy as np
from itertools     import product
from ..io.navigate import * 

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

def mergeFMScalings(simOutput, scalingFM, AOG):
    mergedScalings = {}

    for field in simOutput.fieldList[AOG]:
        mergedScalings[field.name] = {}
        for lol in LinOrLog():
            mean = 0.0
            for proc in simOutput.procList:
                mean += scalingFM[lol][field.name][proc]
            mergedScalings[field.name][lol] = mean / len(simOutput.procList)

    return mergedScalings

#__________________________________________________

def initScalingFM(simOutput, AOG):
    scalingFM = {}
    for lol in LinOrLog():
        scalingFM[lol] = {}
        for field in simOutput.fieldList[AOG]:
            scalingFM[lol][field.name] = {}
    return scalingFM

#__________________________________________________

def writeFMScaling(simOutput, scalingFM, species, AOG, printIO=False):

    for (field, lol) in product(simOutput.fieldList[AOG], LinOrLog()):
        fn = simOutput.fileFMScalingFieldSpecies(AOG, field, lol, species)
        if printIO:
            print ('Writing '+fn+' ...')
        np.save(fn, scalingFM[field.name][lol])

#__________________________________________________
