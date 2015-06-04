#_________________________________
# interpolateIntoOT2DResolution.py
#_________________________________

import numpy as np

from itertools                     import product

from ....utils.analyse.io.navigate import *

#__________________________________________________

def interpolateAOGFieldsIntoOT2DResolution(simOutput,
                                           AOG,
                                           species,
                                           OTShape,
                                           printIO):
    
    for (proc, field, lol) in product(simOutput.procList, simOutput.fieldList[AOG], LinOrLog()):

        fn   = simOutput.fileProcPreprocessedField(proc, AOG, field, lol, species)
        if printIO:
            print ('Reading '+fn+' ...')
        data = np.load(fn)
        data = field.interpolate(data, OTShape)

        fn = simOutput.fileProcPreprocessedFieldOTResolution(proc, AOG, field, lol, species)
        if printIO:
            print ('Writing '+fn+' ...')
        np.save(fn, data)

#__________________________________________________
