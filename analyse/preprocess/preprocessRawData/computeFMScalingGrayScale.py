#_____________________________
# computeFMScalingGrayScale.py
#_____________________________

import numpy as np

from itertools                                      import product

from ...utils.analyse.scaling.scaling               import arrayToScaling
from ...utils.analyse.scaling.fmScaling             import initScalingFM
from ...utils.analyse.scaling.fmScaling             import computeFMScaling
from ...utils.analyse.scaling.fmScaling             import mergeFMScalings
from ...utils.analyse.scaling.fmScaling             import writeFMScaling
from ...utils.analyse.scaling.grayScale             import makeGrayScale
from ...utils.analyse.filters.zeroFilterLog10       import halfMinValueFiltered
from ...utils.analyse.io.navigate                   import *

#__________________________________________________

def computeFMScalingMakeGSAOGFields(simOutput,
                                    AOG,
                                    species,
                                    nLevelsFM,
                                    nLevelsGrayScale,
                                    printIO):

    scalingFM = initScalingFM(simOutput, AOG)

    for (proc, field, LOL) in product(simOutput.procList, simOutput.fieldList[AOG], LinOrLog()):

        fn      = simOutput.fileScalingFieldSpecies(AOG, field, LOL, species)
        array   = np.load(fn)
        scaling = arrayToScaling(array)
        
        for TS in ThresholdNoThreshold():

            fn   = simOutput.fileProcPreprocessedField(proc, AOG, field, LOL, species, TS)
            data = np.load(fn)

            if TS == 'Threshold':
                scalingFM[LOL][field.name][proc] = computeFMScaling(data, mini=scaling.mini, maxi=scaling.maxi, nLevels=nLevelsFM)
                threshold = halfMinValueFiltered()
            else:
                threshold = None

            grayScale = makeGrayScale(data, mini=scaling.mini, maxi=scaling.maxi, nLevels=nLevelsGrayScale, threshold=threshold)
            fn        = simOutput.fileProcPreprocessedFieldGS(proc, AOG, field, LOL, species, TS)
            if printIO:
                print ('Writing '+fn+' ...')
            np.save(fn, grayScale)

    scalingFM = mergeFMScalings(simOutput, scalingFM, AOG)
    writeFMScaling(simOutput, scalingFM, species, AOG, printIO)

#__________________________________________________
