#_________________________
# plotSimulationsFields.py
#_________________________

from matplotlib import pyplot as plt

from itertools                                       import product
from ....utils.analyse.processRawData.extractRawData import extractFieldAllIterations
from ....utils.plotting.plotting                     import makeAxesGrid
from ....utils.plotting.plotMatrix                   import plotMatrix
from ....utils.plotting.plotting                     import adaptAxesExtent
from ....utils.plotting.plotting                     import addTitleLabelsGrid
from ....utils.plotting.plotMatrix                   import addColorBar
from ....utils.plotting.plotting                     import addTimeTextPBar
from ....utils.plotting.saveFig                      import saveFig
from ....utils.plotting.positions                    import figureRect
from ....utils.io.files                              import fileNameSuffix

#__________________________________________________

def plotProcField(rawData, 
                  simOutput, 

                  procList,
                  labelList,
                  suffixFigName,

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
                  timeTextPBar,
                  extensionsList,
                  EPSILON): 

    (data, mini, maxi, tmax) = extractFieldAllIterations(rawData, procList, field, LOL)

    xmin  = field.axMini(0)
    ymin  = field.axMini(1)
    xmax  = field.axMaxi(0)
    ymax  = field.axMaxi(1)

    if xLabel:
        xLabel = field.labels[0]
    else:
        xLabel = ''

    if yLabel:
        yLabel = field.labels[1]
    else:
        yLabel = ''

    if cLabel:
        cLabel = field.name
    else:
        cLabel = ''

    for t in xrange(tmax):
        
        figure     = plt.figure()
        plt.clf()

        (gs, axes) = makeAxesGrid(plt,
                                  len(procList),
                                  order=order,
                                  extendDirection=extendDirection)

        for (proc, label, ax) in zip(procList, labelList, axes):
            plotMatrix(ax, 
                       data[proc][t,:,:],
                       plotter=plotter,
                       xmin=xmin,
                       xmax=xmax,
                       ymin=ymin,
                       ymax=ymax,
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

        gs.tight_layout(figure, rect=figureRect(colorBar, timeTextPBar))

        if colorBar:
            addColorBar(plt, 
                        timeTextPBar,
                        cmapName, 
                        mini,
                        maxi,
                        nbrCTicks,
                        cticksDecimals,
                        cLabel)

        if timeTextPBar:
            addTimeTextPBar(plt,
                            t,
                            tmax)

        figName = simOutput.simOutputFieldFigDir(AOG, field, LOL, species) + species + '_' + suffixFigName + '_' + fileNameSuffix(t, tmax)
        saveFig(plt, figName, extensionsList)
        plt.close()

#__________________________________________________
