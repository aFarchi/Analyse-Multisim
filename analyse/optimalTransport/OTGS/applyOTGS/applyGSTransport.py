#____________________
# applyGSTransport.py
#____________________

import numpy   as np

from ....utils.analyse.io.extractProcessedData import extractProcessedDataFullScaling
from ....utils.analyse.io.extractProcessedData import extractTmapOTGSP0P1FieldSpecies
from ....utils.io.write                        import saveSymMatrixEig

#__________________________________________________

def applyGSTransportForField(simOutput,
                             configName,
                             AOG,
                             species,
                             field,
                             LOL,
                             TS,
                             error,
                             printIO=False):

    (data, scaling, scalingFM) = extractProcessedDataFullScaling(simOutput, AOG, field, LOL, species, 'Threshold', printIO)

    def normalize(x):
        return ( x - scaling.mini ) / ( scaling.maxi - scaling.mini )

    def inverseNormalize(x):
        return scaling.mini + x * ( scaling.maxi - scaling.mini )

    for p1 in xrange(len(simOutput.procList)):
        for p0 in xrange(p1):

            (Tmap, inverseTmap) = extractTmapOTGSP0P1FieldSpecies(simOutput, configName, p0, p1, AOG, field, LOL, species, TS, error, printIO)
            data0               = data[simOutput.procList[p0]]
            data1               = data[simOutput.procList[p1]]

            (forwardInterpolate, backwardInterpolate) = applyGSTransport(data0, data1, normalize, inverseNormalize, Tmap, inverseTmap)

            fileForward  = simOutput.applyOTGSForwardP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS)
            fileBackward = simOutput.applyOTGSBackwardP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS)

            if printIO:
                print('Writing '+fileForward+' ...')
                print('Writing '+fileBackward+' ...')

            np.save(fileForward, forwardInterpolate)
            np.save(fileBackward, backwardInterpolate)
            
#__________________________________________________

def applyGSTransport(data0, data1, Nmap, iNmap, Tmap, inverseTmap):
    
    forwardInterpolate  = iNmap( inverseTmap( Nmap( data0 ) ) )
    backwardInterpolate = iNmap(        Tmap( Nmap( data1 ) ) )

    return (forwardInterpolate, backwardInterpolate)

#__________________________________________________
