#_________________________________
# interpolateIntoOTGSResolution.py
#_________________________________

import numpy as np

from fractions                     import gcd
from scipy.interpolate             import interp1d

#__________________________________________________

def interpolateProcPreprocessedDieldGSIntoOTGSResolution(simOutput,
                                                         AOG,
                                                         species,
                                                         field,
                                                         LOL,
                                                         TS,
                                                         proc,
                                                         OTGSResolution,
                                                         printIO):
    
    fn   = simOutput.fileProcPreprocessedFieldGS(proc, AOG, field, LOL, species, TS)
    if printIO:
        print ('Reading '+fn+' ...')
    data = np.load(fn)
    data = interpolateGS(data, OTGSResolution+1)

    data[1]                += data[0]
    data[0]                 = 0.0
    data[OTGSResolution-2] += data[OTGSResolution-1]
    data[OTGSResolution-1]  = 0.0

    fn = simOutput.fileProcPreprocessedFieldGSOTResolution(proc, AOG, field, lol, species, TS)
    if printIO:
        print ('Writing '+fn+' ...')
    np.save(fn, data)

#__________________________________________________

def interpolateGS(grayScale, OTGSResolution):

    oldSize = grayScale.size

    if not oldSize == OTGSResolution:

        oldX     = np.linspace(0.0, 1.0, oldSize)
        gsInterp = interp1d(oldX, grayScale, kind='linear', axis=0, copy=False, bounds_error=False, fill_value=0.0)

        if oldSize < OTGSResolution or not gcd(oldSize-1, OTGSResolution-1) == (OTGSResolution-1):
            fineResolution = 1 + (oldSize-1) * int( (OTGSResolution-1) / gcd(oldSize-1, OTGSResolution-1) )
            fineX          = np.linspace(0.0, 1.0, fineResolution)
            gsFine         = gsInterp(fineX)
        else:
            fineResolution = oldSize
            gsFine         = grayScale

        ratio              = int( (float(fineResolution)-1.0) / (float(OTGSResolution)-1.0) )
        if ratio == 1:
            return gsFine

        gsOTGSResolution   = np.zeros(OTGSResolution)

        for i in xrange(OTGSResolution-1):
            jStart = ratio * i
            jEnd   = ratio * (i+1)

            if np.mod(ratio,2) == 0:
                jMiddle = int(ratio*(i+0.5))

                gsOTGSResolution[i]   = ( gsFine[jStart:jMiddle+1].sum() -
                                          gsFine[jStart] / 2.0 -
                                          gsFine[jMiddle] / 2.0 ) / ratio

                gsOTGSResolution[i+1] = ( gsFine[jMiddle:jEnd+1].sum() -
                                          gsFine[jMiddle] / 2.0 -
                                          gsFine[jEnd] / 2.0 ) / ratio

            else:
                jMiddle = ratio * i + int((ratio-1.0)/2.0)

                gsOTGSResolution[i]   = ( gsFine[jStart:jMiddle+1].sum() -
                                          gsFine[jStart] / 2.0 ) / ratio

                gsOTGSResolution[i+1] = ( gsFine[jMiddle+1:jEnd+1].sum() -
                                          gsFine[jEnd] / 2.0 ) / ratio
        return gsOTGSResolution

#__________________________________________________
