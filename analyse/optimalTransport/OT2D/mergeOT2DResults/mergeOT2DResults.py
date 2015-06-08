#____________________
# mergeOT2DResults.py
#____________________

import numpy   as np
import cPickle as pck

from ....utils.io.write import saveSymMatrixEig

#__________________________________________________

def mergeOT2DResultsForField(simOutput,
                             configName,
                             AOG,
                             species,
                             field,
                             LOL,
                             printIO):


    nbrProc = len(simOutput.procList)
    results = np.zeros(shape=(nbrProc,nbrProc))

    for p1 in xrange(nbrProc):
        for p0 in xrange(p1):
            
            resFile        = simOutput.resultsFileOT2DP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species)
            f              = open(resFile, 'rb')
            p              = pck.Unpickler(f)
            results[p0,p1] = p.load()
            results[p1,p0] = results[p0,p1]
            f.close()

    mergedResFile = simOutput.mergedResultsFileOT2DFieldSpecies(configName, AOG, field, LOL, species)
    saveSymMatrixEig(mergedResFile, results)
    if printIO:
        print('Written '+mergedResFile+'*.npy ...')
   
#__________________________________________________
