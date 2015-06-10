#______________
# plotField.py
#______________

from matplotlib import pyplot as plt

from itertools                                 import product

from ....utils.analyse.io.extractProcessedData import extractProcessedData
from ....utils.plotting.plotting               import makeAxesGrid
from ....utils.plotting.plotMatrix             import plotMatrix
from ....utils.plotting.plotting               import adaptAxesExtent
from ....utils.plotting.plotting               import addTitleLabelsGrid
from ....utils.plotting.plotMatrix             import addColorBar
from ....utils.plotting.plotting               import addTimeTextPBar
from ....utils.plotting.saveFig                import saveFig
from ....utils.plotting.positions              import figureRect

#__________________________________________________

def plotProcField(simOutput, 
                  procList,
                  labelList,
                  suffixFigName,
                  applyGlobalScaling,
                  AOG, 
                  field, 
                  LOL, 
                  species,
                  xLabel,
                  yLabel,
                  cLabel,
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
                  cticksDecimals,
                  colorBar,
                  cmapName,
                  extensionsList,
                  EPSILON,
                  printIO): 

    (data, mini, maxi)       = extractProcessedData(simOutput, procList, AOG, field, LOL, species, 'NoThreshold', applyGlobalScaling, printIO)
    (xmin, xmax, ymin, ymax) = field.axExtend2d()
    (xLabel, yLabel, cLabel) = field.labels2d(xLabel, yLabel, cLabel)

    figure     = plt.figure()
    plt.clf()

    (gs, axes) = makeAxesGrid(plt,
                              len(procList),
                              order=order,
                              extendDirection=extendDirection)

    for (proc, label, ax) in zip(procList, labelList, axes):
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

    gs.tight_layout(figure, rect=figureRect(colorBar, False))

    if colorBar:
        addColorBar(plt, 
                    False,
                    cmapName, 
                    mini,
                    maxi,
                    nbrCTicks,
                    cticksDecimals,
                    cLabel)

    figName = simOutput.fieldFigDir(AOG, field, LOL, species) + species + '_' + suffixFigName
    saveFig(plt, figName, extensionsList)
    plt.close()

#__________________________________________________
