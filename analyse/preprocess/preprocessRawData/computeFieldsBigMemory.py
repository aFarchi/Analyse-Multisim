#__________________________
# computeFieldsBigMemory.py
#__________________________

import numpy as np

from itertools                        import product

from ...utils.analyse.scaling.scaling import initScalingMaximum
from ...utils.analyse.scaling.scaling import mergeScalings
from ...utils.analyse.scaling.scaling import writeScaling
from ...utils.analyse.io.navigate     import *

#__________________________________________________

def computeAOGFieldsBigMemory(rawData, 
                              simOutput,
                              AOG,
                              species,
                              printIO):

    (scaling, maximum) = initScalingMaximum(simOutput, AOG)

    for (proc, field, LOL) in product(simOutput.procList, simOutput.fieldList[AOG], LinOrLog()):

        (dataFiltered, scale) = field.extract(rawData[proc], LOL, copy=False)

        try:
            maximum[LOL][field.name] = np.maximum(maximum[LOL][field.name], dataFiltered)
        except:
            maximum[LOL][field.name] = dataFiltered

        scaling[LOL][field.name][proc] = scale

        fn = simOutput.fileProcPreprocessedField(proc, AOG, field, LOL, species, 'Threshold')
        if printIO:
            print ('Writing '+fn+' ...')
        np.save(fn, dataFiltered)

        data = field.removeFilter(dataFiltered, LOL)
        fn   = simOutput.fileProcPreprocessedField(proc, AOG, field, LOL, species, 'NoThreshold')
        if printIO:
            print ('Writing '+fn+' ...')
        np.save(fn, data)

    scaling = mergeScalings(simOutput, scaling, maximum, AOG)
    writeScaling(simOutput, scaling, species, AOG, printIO)

#__________________________________________________

