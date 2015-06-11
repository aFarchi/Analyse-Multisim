#_____________________________
# performStatisticalAnalyse.py
#_____________________________

import numpy as np

from analyseResults                           import AnalyseResults
from ...utils.analyse.io.extractProcessedData import extractProcessedDataFullScaling

#__________________________________________________

def analyseFieldSpecies(simOutput,
                        AOG,
                        field,
                        LOL,
                        species,
                        nLevelsAlpha,
                        chooseScaling,
                        printIO=False):

    (data, scaling, scalingFM) = extractProcessedDataFullScaling(simOutput, AOG, field, LOL, species, 'NoThreshold', printIO)
    analyse                    = AnalyseResults(len(simOutput.procList), scaling, scalingFM, nLevelsAlpha, chooseScaling)
    applyScaling               = ( LOL == 'lin' )

    for p1 in xrange(len(simOutput.procList)):
        for p0 in xrange(p1):
            data0 = data[simOutput.procList[p0]]
            data1 = data[simOutput.procList[p1]]
            analyse.applyOperators(p0, p1, data0, data1, applyScaling)

    analyse.fill()
    analyse.toFiles(simOutput.analyseFieldSeciesDir(AOG, field, LOL, species), printIO)

#__________________________________________________

