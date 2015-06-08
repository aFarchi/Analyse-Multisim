#____________________
# mergeOTGSResults.py
#____________________

import numpy   as np
import cPickle as pck

from ....utils.io.write import saveSymMatrixEig

#__________________________________________________

def mergeOTGSResultsForField(simOutput,
                             configName,
                             AOG,
                             species,
                             field,
                             LOL,
                             TS,
                             printIO):


    nbrProc = len(simOutput.procList)
    results = np.zeros(shape=(nbrProc,nbrProc))

    for p1 in xrange(nbrProc):
        for p0 in xrange(p1):
            
            resFile        = simOutput.resultsFileOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS)
            f              = open(resFile, 'rb')
            p              = pck.Unpickler(f)
            results[p0,p1] = p.load()
            results[p1,p0] = results[p0,p1]
            f.close()

    mergedResFile = simOutput.mergedResultsFileOTGSFieldSpecies(configName, AOG, field, LOL, species, TS)
    saveSymMatrixEig(mergedResFile, results)
    if printIO:
        print('Written '+mergedResFile+'*.npy ...')
   
#__________________________________________________
