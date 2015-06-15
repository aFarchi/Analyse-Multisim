#__________________
# analyseResults.py
#__________________

import numpy as np

from ...utils.io.write                        import saveSymMatrixEig
from ...utils.io.files                        import fileNameSuffix
from ...utils.analyse.statisticalOperators    import statisticalOperators as stats

#__________________________________________________

class AnalyseResults:

    def __init__(self, nbrProc, scaling, scalingFM, nLevelsAlpha, chooseScaling='mean'):
        self.scaling      = scaling
        self.scalingFM    = scalingFM
        self.nLevelsFM    = len(scalingFM)
        self.levelsNFM    = np.linspace(scaling.mini, scaling.maxi, self.nLevelsFM)
        self.levelsAlpha  = np.power(10. , 0.1*np.arange(nLevelsAlpha))
        self.nLevelsAlpha = nLevelsAlpha

        if chooseScaling == 'geomMean':
            self.scaling.generalScale = self.scaling.geomMeanMeans
        elif chooseScaling == 'var':
            self.scaling.generalScale = self.scaling.meanVars
        else:
            self.scaling.generalScale = self.scaling.meanMeans
                        
        self.MSE     = np.zeros(shape=(nbrProc,nbrProc))
        self.NFMmini = np.zeros(shape=(nbrProc,nbrProc))
        self.bias    = np.zeros(shape=(nbrProc,nbrProc))
        self.BcMSE   = np.zeros(shape=(nbrProc,nbrProc))
        self.TSS     = np.zeros(shape=(nbrProc,nbrProc))
        self.PCC     = np.zeros(shape=(nbrProc,nbrProc))
        self.FOEX    = np.zeros(shape=(nbrProc,nbrProc))
        
        self.NFM     = np.zeros(shape=(nbrProc,nbrProc,self.nLevelsFM))
        self.FAalpha = np.zeros(shape=(nbrProc,nbrProc,self.nLevelsAlpha))

        self.correctZeroScalings()

    #_________________________

    def correctZeroScalings(self):
        if self.scaling.generalScale == 0.0:
            self.scaling.generalScale = 1.0
        if self.scaling.sumMaximum == 0.0:
            self.scaling.sumMaximum = 1.0

        for k in xrange(self.nLevelsFM):
            if self.scalingFM[k] == 0.0:
                self.scalingFM[k] = 1.0

    #_________________________

    def applyOperators(self, i, j, field0, field1, applyScaling=True):
        if not applyScaling :
            self.MSE[i,j]     = stats.MSE(    field0, field1)
            self.NFMmini[i,j] = stats.NFMmini(field0, field1)
            self.bias[i,j]    = stats.bias(   field0, field1)
            self.BcMSE[i,j]   = stats.BcMSE(  field0, field1)
            self.TSS[i,j]     = stats.TSS(    field0, field1)
            for k in xrange(self.nLevelsFM):
                self.NFM[i,j,k]     = stats.NFM(field0, field1, self.levelsNFM[k])
        else:
            self.MSE[i,j]     = stats.NMSE_corrected(   field0, field1, self.scaling.generalScale)
            self.NFMmini[i,j] = stats.NFMmini_corrected(field0, field1, self.scaling.sumMaximum)
            self.bias[i,j]    = stats.Nbias_corrected(  field0, field1, self.scaling.generalScale)
            self.BcMSE[i,j]   = stats.BcNMSE_corrected( field0, field1, self.scaling.generalScale)
            self.TSS[i,j]     = stats.TSS_corrected(    field0, field1, self.scaling.generalScale)
            for k in xrange(self.nLevelsFM):
                self.NFM[i,j,k]     = stats.NFM_corrected(field0, field1, self.levelsNFM[k], self.scalingFM[k])

        self.PCC[i,j]     = stats.PCC( field0, field1)
        self.FOEX[i,j]    = stats.FOEX(field0, field1)
        for k in xrange(self.nLevelsAlpha):
            self.FAalpha[i,j,k] = stats.FA(field0, field1, self.levelsAlpha[k])

    #_________________________

    def fill(self):
        for j in xrange(self.MSE.shape[0]):
            for i in xrange(i):
                self.MSE[j,i]     = self.MSE[i,j]
                self.NFMmini[j,i] = self.NFMmini[i,j]
                self.bias[j,i]    = self.bias[i,j]
                self.BcMSE[j,i]   = self.BcMSE[i,j]
                self.TSS[j,i]     = self.TSS[i,j]
                self.PCC[j,i]     = self.PCC[i,j]
                self.FOEX[j,i]    = self.FOEX[i,j]
                for k in xrange(self.nLevelsFM):
                    self.NFM[j,i,k]     = self.NFM[i,j,k]
                for k in xrange(self.nLevelsAlpha):
                    self.FAalpha[j,i,k] = self.FAalpha[i,j,k]

            self.MSE[i,i]     = 0.0
            self.NFMmini[i,i] = 1.0
            self.bias[i,i]    = 0.0
            self.BcMSE[i,i]   = 0.0
            self.TSS[i,i]     = 1.0
            self.PCC[i,i]     = 1.0
            self.FOEX[i,i]    = 0.0
            for k in xrange(self.nLevelsFM):
                self.NFM[i,i,k]     = 1.0
            for k in xrange(self.nLevelsAlpha):
                self.FAalpha[i,i,k] = 1.0

    #_________________________

    def toFiles(self, directory, printIO):
        if printIO:
            print ('Writing analyse result in '+directory+' ...')
        saveSymMatrixEig(directory+'MSE',     self.MSE)
        saveSymMatrixEig(directory+'NFMmini', self.NFMmini)
        saveSymMatrixEig(directory+'bias',    self.bias)
        saveSymMatrixEig(directory+'BcMSE',   self.BcMSE)
        saveSymMatrixEig(directory+'TSS',     self.TSS)
        saveSymMatrixEig(directory+'PCC',     self.PCC)
        saveSymMatrixEig(directory+'FOEX',    self.FOEX)

        for k in xrange(self.nLevelsFM):
            saveSymMatrixEig(directory+'NFM'+fileNameSuffix(k,self.nLevelsFM), self.NFM[:,:,k])
        for k in xrange(self.nLevelsAlpha):
            saveSymMatrixEig(directory+'FA'+fileNameSuffix(k,self.nLevelsAlpha), self.FAalpha[:,:,k])

#__________________________________________________
