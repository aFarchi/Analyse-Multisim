#________________________
# plotForwardTransport.py
#________________________

from matplotlib import pyplot as plt

from ....utils.analyse.io.extractProcessedData import extractProcessedDataForwardTransport
from ....utils.plotting.plotting               import makeAxesApplyGSTransport
from ....utils.plotting.plotMatrix             import plotMatrix
from ....utils.plotting.plotting               import adaptAxesExtent
from ....utils.plotting.plotting               import addTitleLabelsGrid
from ....utils.plotting.plotMatrix             import plotGrayScale
from ....utils.plotting.saveFig                import saveFig

#__________________________________________________

def plotForwardTransport(simOutput, 
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

    (data0, data1, mini, maxi)  = extractProcessedDataForwardTransport(simOutput, configName, p0, p1, AOG, field, LOL, species, TS, printIO)

    grayScales                  = {} 
    grayScales['Tm1od0']        = field.computeGrayScale(data0, mini, maxi, nLevelsGS, threshold=(TS=='Threshold'))
    grayScales['d1']            = field.computeGrayScale(data1, mini, maxi, nLevelsGS, threshold=(TS=='Threshold'))

    maxiGS                      = max(grayScales['Tm1od0'].max(), grayScales['d1'].max())

    options                     = {}
    options['Tm1od0']           = optionInit
    options['d1']               = optionFinal
 
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
                       title='$T^{-1}\circ d_0$',
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
                       title='$d_1$',
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
    figName = simOutput.plotApplyGSTransportP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS) + 'forwardTransport'
    saveFig(plt, figName, extensionsList)
    plt.close()

#__________________________________________________
