#____________________
# plotTransportMap.py
#____________________

import numpy as np

from matplotlib import pyplot as plt

from ....utils.analyse.io.extractProcessedData import extractScalingFieldSpecies
from ....utils.plotting.plotting               import adaptAxesExtent
from ....utils.plotting.plotting               import addTitleLabelsGrid
from ....utils.plotting.plotting               import tryAddCustomLegend
from ....utils.plotting.saveFig                import saveFig
from ....utils.analyse.scaling.buildTmap       import buildTmap

#__________________________________________________

def plotTransportMap(simOutput,
                     configName,
                     p0,
                     p1,
                     AOG,
                     field,
                     LOL,
                     species,
                     TS,
                     TmapError,
                     TmapResolution,
                     extensionsList,
                     optionsForward,
                     optionsBackward,
                     extendX,
                     extendY,
                     nbrXTicks,
                     nbrYTicks,
                     xTicksDecimals,
                     yTicksDecimals,
                     printIO,
                     EPSILON):

    Tarray              = np.load(simOutput.TmapFileOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS))
    (Tmap, inverseTmap) = buildTmap(Tarray, TmapError)

    scaling             = extractScalingFieldSpecies(simOutput, AOG, field, LOL, species, printIO)

    def normalize(x):
        return ( x - scaling.mini ) / ( scaling.maxi - scaling.mini )

    def inverseNormalize(x):
        return scaling.mini + x * ( scaling.maxi - scaling.mini )

    X  = np.linspace(scaling.mini, scaling.maxi, TmapResolution)
    T  = inverseNormalize(Tmap(normalize(X)))
    iT = inverseNormalize(inverseTmap(normalize(X)))

    figure = plt.figure()
    plt.clf()
    ax = plt.subplot(111)
    ax.plot(X, T,  optionsForward,  label='$T$')
    ax.plot(X, iT, optionsBackward, label='$T^{-1}$')

    adaptAxesExtent(ax,
                    scaling.mini,
                    scaling.maxi,
                    scaling.mini,
                    scaling.maxi,
                    extendX,
                    extendY,
                    nbrXTicks,
                    nbrYTicks,
                    xTicksDecimals,
                    yTicksDecimals,
                    EPSILON)

    addTitleLabelsGrid(ax,
                       title='Transport maps',
                       xLabel='',
                       yLabel='',
                       grid=True)

    tryAddCustomLegend(ax, True)

    figName = simOutput.plotApplyGSTransportP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS) + 'TransportMap'
    saveFig(plt, figName, extensionsList)
    plt.close()

#__________________________________________________
