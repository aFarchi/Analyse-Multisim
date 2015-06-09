#____________________
# applyGSTransport.py
#____________________

import numpy   as np

from scipy.interpolate                         import interp1d
from ....utils.analyse.io.extractProcessedData import extractProcessedDataFullScaling
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

    (data, scaling, scalingFM) = extractProcessedDataFullScaling(simOutput, AOG, field, LOL, species, printIO)

    def normalize(x):
        return ( x - scaling.mini ) / ( scaling.maxi - scaling.mini )

    def inverseNormalize(x):
        return scaling.mini + x * ( scaling.maxi - scaling.mini )

    for p1 in xrange(len(simOutput.procList)):
        for p0 in xrange(p1):

            Tarray              = np.load(simOutput.TmapFileOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS))
            (Tmap, inverseTmap) = buildTmap(Tarray, error)
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

def buildTmap(Tarray, error):
    N             = Tarray.size

    # Filters T to make it stricly growing
    TFiltered     = np.minimum(1.0, Tarray)
    TFiltered[0]  = 0.0
    DT            = TFiltered[1:] - TFiltered[:N-1]
    DT            = np.maximum(error/N, DT)

    TFiltered[1:] = DT.cumsum()

    TFiltered    /= TFiltered[N-1]

    # Extends X and T arrays to avoid boundary errors
    XTmap         = np.zeros(N+2)
    TTmap         = np.zeros(N+2)

    XTmap[0]      = - 1.0
    XTmap[1:N+1]  = np.linspace(0.0, 1.0, N)
    XTmap[N+1]    = 2.0

    TTmap[0]      = 0.0
    TTmap[1:N+1]  = TFiltered[:]
    TTmap[N+1]    = 1.0

    # Interpolates Tmap 
    Tmap          = interp1d(XTmap, TTmap)

    XTmap[0]      = 0.0
    XTmap[N+1]    = 1.0
    TTmap[0]      = - 1.0
    TTmap[N+1]    = 2.0

    # Interpolates inverse Tmap
    inverseTmap   = interp1d(TTmap, XTmap, copy=False)

    return (Tmap, inverseTmap)

#__________________________________________________
