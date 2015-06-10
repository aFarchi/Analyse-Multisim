#_____________________________
# plotFieldsAttachGrayScale.py
#_____________________________

from matplotlib import pyplot as plt

from itertools                                 import product

from ....utils.analyse.io.extractProcessedData import extractProcessedData
from ....utils.analyse.io.extractProcessedData import extractGrayScales
from ....utils.plotting.plotting               import makeAxesGridAttachGrayScale
from ....utils.plotting.plotMatrix             import plotMatrix
from ....utils.plotting.plotting               import adaptAxesExtent
from ....utils.plotting.plotting               import addTitleLabelsGrid
from ....utils.plotting.plotMatrix             import plotGrayScale
from ....utils.plotting.saveFig                import saveFig
from ....utils.plotting.positions              import figureRect

#__________________________________________________

def plotProcFieldAttachGS(simOutput, 
                          procList,
                          labelList,
                          suffixFigName,
                          AOG, 
                          field, 
                          LOL, 
                          species,
                          xLabel,
                          yLabel,
                          order,
                          extendDirection,
                          plotter,
                          plotterArgs,
                          extendX,
                          extendY,
                          nbrXTicks,
                          nbrYTicks,
                          nbrCTicks,
                          xTicksDecimals,
                          yTicksDecimals,
                          cTicksDecimals,
                          cmapName,
                          scaleGS,
                          extendDirectionGS,
                          nLevelsGS,
                          options,
                          directionGS,
                          extensionsList,
                          EPSILON,
                          printIO): 

    (data, mini, maxi)       = extractProcessedData(simOutput, procList, AOG, field, LOL, species, 'NoThreshold', True, printIO)
    (GS, miniGS, maxiGS)     = extractGrayScales(simOutput, procList, AOG, field, LOL, species, scaleGS, printIO)
    (xmin, xmax, ymin, ymax) = field.axExtend2d()
    (xLabel,yLabel,cLabel)   = field.labels2d(xLabel, yLabel, False)

    figure     = plt.figure()
    plt.clf()

    (gs, axes, gsAxes) = makeAxesGridAttachGrayScale(plt, 
                                                     len(procList), 
                                                     order, 
                                                     extendDirection, 
                                                     extendDirectionGS)

    for (proc, label, ax, gsAx) in zip(procList, labelList, axes, gsAxes):
        plotMatrix(ax, 
                   data[proc][:,:],
                   plotter=plotter,
                   xmin=xmin,
                   xmax=xmax,
                   ymin=ymin,
                   ymax=ymax,
                   cmapName=cmapName,
                   vmin=mini,
                   vmax=maxi,
                   **plotterArgs)

        adaptAxesExtent(ax,
                        xmin,
                        xmax,
                        ymin,
                        ymax, 
                        extendX, 
                        extendY, 
                        nbrXTicks, 
                        nbrYTicks,
                        xTicksDecimals,
                        yTicksDecimals,
                        EPSILON)

        addTitleLabelsGrid(ax,
                           title=label,
                           xLabel=xLabel,
                           yLabel=yLabel,
                           grid=False)

        
        plotGrayScale(gsAx,
                      GS[proc],
                      mini,
                      maxi,
                      maxiGS,
                      nLevelsGS,
                      cmapName,
                      options,
                      nbrCTicks,
                      cTicksDecimals,
                      directionGS,
                      EPSILON)
        
    gs.tight_layout(figure)
    figName = simOutput.fieldAttachGrayScaleFigDir(AOG, field, LOL, species) + species + '_' + suffixFigName
    saveFig(plt, figName, extensionsList)
    plt.close()

#__________________________________________________
