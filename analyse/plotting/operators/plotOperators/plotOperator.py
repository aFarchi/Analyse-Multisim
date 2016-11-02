#________________
# plotOperator.py
#________________

import numpy as np
from matplotlib import pyplot as plt

from ....utils.plotting.plotMatrix import plotMatrixBasic
from ....utils.plotting.saveFig    import saveFig
from ....utils.types.matrix        import permuteMatrix
from ....utils.io.files            import fileNameSuffix

#__________________________________________________

def plotOperator(fn, figDir, prefixFN, label, extensionsList, cmapName='gray', applyAbs=False, factor=1.0):

    matrix  = np.load(fn+'.npy')

    if applyAbs:
        matrix = abs(matrix)

    matrix *= factor

    figure  = plt.figure()
    ax      = plt.subplot(111)
    plotMatrixBasic(ax, matrix, cmapName)
    ax.set_xlabel(label)
    figName = figDir + prefixFN
    saveFig(plt, figName, extensionsList)

    ax.cla()
    matrix  = permuteMatrix(matrix)
    plotMatrixBasic(ax, matrix, cmapName)
    ax.set_xlabel(label)
    figName = figDir + 'permute_' + prefixFN
    saveFig(plt, figName, extensionsList)

    plt.close()
    plt.figure()
    line    = matrix[0, 1:]
    plt.plot(line)
    plt.xlabel(label)
    figName = figDir + 'line_' + prefixFN
    saveFig(plt, figName, extensionsList)
    plt.close()

#__________________________________________________

def plotStatisticalOperators(simOutput, AOG, field, LOL, species, nLevelsFM, nLevelsAlpha, cmapName, extensionsList):
    directory = simOutput.analyseFieldSeciesDir(AOG, field, LOL, species)
    figDir    = simOutput.plotOperatorsDir(AOG, field, LOL, species)

    operators = ['MSE', 'NFMmini', 'bias', 'BcMSE', 'TSS', 'PCC', 'FOEX']

    applyAbs  = ['bias']
    inverse   = ['NFMmini', 'PCC', 'TSS']

    for op in operators:
        resultFile = directory + op
        factor     = 1.0
        if op in inverse:
            factor = -1.0
        plotOperator(resultFile, figDir, op, op, extensionsList, cmapName, op in applyAbs, factor)

    for k in xrange(nLevelsFM):
        op = 'NFM' + fileNameSuffix(k, nLevelsFM)
        resultFile = directory + op
        plotOperator(resultFile, figDir, op, op, extensionsList, cmapName, False, -1.0)

    for k in xrange(nLevelsAlpha):
        op = 'FA' + fileNameSuffix(k, nLevelsAlpha)
        resultFile = directory + op
        plotOperator(resultFile, figDir, op, op, extensionsList, cmapName, False, -1.0)

#__________________________________________________

def plotL2WassersteinOT2D(simOutput, configName, AOG, field, LOL, species, cmapName, extensionsList):
    resultFile = simOutput.mergedResultsFileOT2DFieldSpecies(configName, AOG, field, LOL, species)
    figDir     = simOutput.plotOperatorsDir(AOG, field, LOL, species)
    plotOperator(resultFile, figDir, 'OT2D_'+configName, '$L^2$-Wasserstein\n'+configName, extensionsList, cmapName)

#__________________________________________________

def plotL2WassersteinOTGS(simOutput, configName, AOG, field, LOL, species, TS, cmapName, extensionsList):
    resultFile = simOutput.mergedResultsFileOTGSFieldSpecies(configName, AOG, field, LOL, species, TS)
    figDir     = simOutput.plotOperatorsDir(AOG, field, LOL, species)
    plotOperator(resultFile, figDir, 'OTGS_'+TS+configName, '$L^2$-Wasserstein (gray scales)\n'+configName, extensionsList, cmapName)

#__________________________________________________
