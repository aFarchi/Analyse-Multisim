#______________________________
# preprocessRawDataBigMemory.py
#______________________________

import numpy as np

from itertools                          import product

from ...utils.analyse.scaling.scaling   import initScalingMaximum
from ...utils.analyse.scaling.scaling   import mergeScalings
from ...utils.analyse.scaling.scaling   import writeScaling
from ...utils.analyse.scaling.scaling   import arrayToScaling
from ...utils.analyse.scaling.fmScaling import initScalingFM
from ...utils.analyse.scaling.fmScaling import mergeFMScalings
from ...utils.analyse.scaling.fmScaling import writeFMScaling
from ...utils.analyse.io.navigate       import *

#__________________________________________________

def computeAOGFieldsBigMemory(rawData, 
                              simOutput,
                              AOG,
                              species,
                              analyseShape,
                              printIO):

    (scaling, maximum) = initScalingMaximum(simOutput, AOG)

    for (proc, field, lol) in product(simOutput.procList, simOutput.fieldList[AOG], LinOrLog()):

        (data, scale) = field.extract(rawData[proc], lol)
        try:
            maximum[lol][field.name] = np.maximum( maximum[lol][field.name] , data )
        except:
            maximum[lol][field.name] = data

        scaling[lol][field.name][proc] = scale
        data                           = field.interpolate(data, analyseShape)

        fn = simOutput.fileProcPreprocessedField(proc, AOG, field, lol, species)
        if printIO:
            print ('Writing '+fn+' ...')
        np.save(fn, data)

    scaling = mergeScalings(simOutput, scaling, maximum, AOG)
    writeScaling(simOutput, scaling, species, AOG, printIO)

#__________________________________________________

def computeFMScalingMakeGSAOGFieldsBigMemory(rawData,
                                             simOutput,
                                             AOG,
                                             species,
                                             nLevelsAnalyse,
                                             printIO):

    scalingFM = initScalingFM(simOutput, AOG)

    for (field, lol) in product(simOutput.fieldList[AOG], LinOrLog()):

        fn      = simOutput.fileScalingFieldSpecies(AOG, field, lol, species)
        array   = np.load(fn)
        scaling = arrayToScaling(array)

        for proc in simOutput.procList:

            (FMScaling, GSNT, GST)           = field.computeFMScalingMakeGrayScale(rawData[proc], lol, scaling.mini, scaling.maxi, nLevelsAnalyse)
            scalingFM[lol][field.name][proc] = FMScaling

            fn = simOutput.fileProcPreprocessedFieldGS(proc, AOG, field, lol, species, 'Threshold')
            if printIO:
                print ('Writing '+fn+' ...')
            np.save(fn, GST)
                                
            fn = simOutput.fileProcPreprocessedFieldGS(proc, AOG, field, lol, species, 'NoThreshold')
            if printIO:
                print ('Writing '+fn+' ...')
            np.save(fn, GSNT)
                                            
    scalingFM = mergeFMScalings(simOutput, scalingFM, AOG)
    writeFMScaling(simOutput, scalingFM, species, AOG, printIO)

#__________________________________________________
