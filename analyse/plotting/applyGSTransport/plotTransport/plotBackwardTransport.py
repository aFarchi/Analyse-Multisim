#_________________________
# plotBackwardTransport.py
#_________________________

from matplotlib import pyplot as plt

from ....utils.analyse.io.extractProcessedData import extractProcessedDataBackwardTransport
from ....utils.plotting.plotting               import makeAxesApplyGSTransport
from ....utils.plotting.plotMatrix             import plotMatrix
from ....utils.plotting.plotting               import adaptAxesExtent
from ....utils.plotting.plotting               import addTitleLabelsGrid
from ....utils.plotting.plotMatrix             import plotGrayScale
from ....utils.plotting.saveFig                import saveFig

#__________________________________________________

def plotBackwardTransport(simOutput, 
                          configName, 
                          p0, 
                          p1, 
                          AOG, 
                          field, 
                          LOL,
                          species,
                          TS,
                          nLevelsGS,
                          optionInit,
                          optionFinal,
                          xLabel,
                          yLabel,
                          directionGS,
                          cmapName,
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
                          extensionsList,
                          printIO,
                          EPSILON):

    (data0, data1, mini, maxi)  = extractProcessedDataBackwardTransport(simOutput, configName, p0, p1, AOG, field, LOL, species, TS, printIO)

    grayScales                  = {} 
    grayScales['d0']            = field.computeGrayScale(data0, mini, maxi, nLevelsGS, threshold=(TS=='Threshold'))
    grayScales['Tod1']          = field.computeGrayScale(data1, mini, maxi, nLevelsGS, threshold=(TS=='Threshold'))

    maxiGS                      = max(grayScales['d0'].max(), grayScales['Tod1'].max())

    options                     = {}
    options['d0']               = optionInit
    options['Tod1']             = optionFinal
 
    (xmin, xmax, ymin, ymax)    = field.axExtend2d()
    (xLabel, yLabel, cLabel)    = field.labels2d(xLabel, yLabel, False)

    figure                      = plt.figure()
    plt.clf()

    (gs, axInit, axFinal, axGS) = makeAxesApplyGSTransport(plt, directionGS)

    plotMatrix(axInit,
               data0,
               plotter=plotter,
               xmin=xmin,
               xmax=xmax,
               ymin=ymin,
               ymax=ymax,
               cmapName=cmapName,
               vmin=mini,
               vmax=maxi,
               **plotterArgs)

    adaptAxesExtent(axInit,
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

    addTitleLabelsGrid(axInit,
                       title='$d_0$',
                       xLabel=xLabel,
                       yLabel=yLabel,
                       grid=False)

    plotMatrix(axFinal,
               data1,
               plotter=plotter,
               xmin=xmin,
               xmax=xmax,
               ymin=ymin,
               ymax=ymax,
               cmapName=cmapName,
               vmin=mini,
               vmax=maxi,
               **plotterArgs)

    adaptAxesExtent(axFinal,
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

    addTitleLabelsGrid(axFinal,
                       title='$T\circ d_1$',
                       xLabel=xLabel,
                       yLabel=yLabel,
                       grid=False)

    plotGrayScale(axGS,
                  grayScales,
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
    figName = simOutput.plotApplyGSTransportP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS) + 'backwardTransport'
    saveFig(plt, figName, extensionsList)
    plt.close()

#__________________________________________________
