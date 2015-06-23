#____________
# plotting.py
#____________

import numpy as np

from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib              import gridspec
from ..io.files              import fileNameSuffix
from positions               import timeTextPBarRect
from positions               import positionsTimeTxtPbar
from plot                    import plot

#____________________________________________________________

def plottingOptions():
    options = np.array(['b-', 'g-', 'r-', 'm-', 'y-', 'c-', 'k-',
                        'b--','g--','r--','m--','y--','c--','k--',
                        'b:', 'g:', 'r:', 'm:', 'y:', 'c:', 'k:',
                        'b-.','g-.','r-.','m-.','y-.','c-.','k-.'])
    n       = len(options)
    return (options, n)

#____________________________________________________________

def plottingOptionsMultiSim():
    options = np.array([['b-', 'g-', 'r-', 'm-', 'y-', 'c-', 'k-'],
                        ['b--','g--','r--','m--','y--','c--','k--'],
                        ['b:', 'g:', 'r:', 'm:', 'y:', 'c:', 'k:' ],
                        ['b-.','g-.','r-.','m-.','y-.','c-.','k-.']])

    (m, n) = options.shape
    return (options, m, n)

#____________________________________________________________

def tryAddCustomLegend(ax, makeRoom):
    if makeRoom:
        divider = make_axes_locatable(ax)
        lax     = divider.append_axes('right', '10%',frameon=False)
        lax.set_yticks([])
        lax.set_xticks([])

    try:
        ax.legend(fontsize='xx-small', loc='center right', bbox_to_anchor=(1.13, 0.5), fancybox=True, framealpha=0.40)
    except:
        ax.legend(fontsize='xx-small', loc='center right', bbox_to_anchor=(1.13, 0.5), fancybox=True)

#____________________________________________________________

def makeGrid(nbrOfItems, extendDirection):
    nColumns = int(np.floor(np.sqrt(nbrOfItems)))
    nLines   = nColumns

    while nColumns*nLines < nbrOfItems:
        if extendDirection == 'vertical':
            nLines += 1
        elif extendDirection == 'horizontal':
            nColumns += 1
        else:
            nLines += 1
            nColumns += 1

    return (nLines, nColumns)

#____________________________________________________________

def addAxGS(plt, gs, index, modulo):
    nc = int(np.mod(index, modulo))
    nl = int((index-nc)/modulo)
    return plt.subplot(gs[nl,nc])

#____________________________________________________________

def makeAxesGrid(plt, rect, nbrOfItems, order, extendDirection):
    (nLines, nColumns) = makeGrid(nbrOfItems, extendDirection)
    gs                 = gridspec.GridSpec(nLines, nColumns)
    gs.update(left=rect[0], bottom=rect[1], right=rect[2], top=rect[3])

    figure             = plt.figure(figsize=(4*nColumns+1, 4*nLines+1))
    axes               = []

    if order == 'horizontalFirst':
        modulo = nColumns
    elif order == 'verticalFirst':
        modulo = nLines

    for j in xrange(nbrOfItems):
        axes.append(addAxGS(plt, gs, j, modulo))

    return (figure, gs, axes)

#____________________________________________________________

def makeAxesGridAttachGrayScale(plt, nbrOfItems, order, extendDirection, extendDirectionGS):
    axes               = []
    (nLines, nColumns) = makeGrid(nbrOfItems, extendDirection)
    gsAxes             = []

    if extendDirectionGS == 'horizontal':
        figure         = plt.figure(figsize=(8*nColumns+1, 4*nLines+1))
    else:
        figure         = plt.figure(figsize=(4*nColumns+1, 8*nLines+1))
           
    if order == 'horizontalFirst':
        modulo = nColumns
    elif order == 'verticalFirst':
        modulo = nLines

    if extendDirectionGS == 'horizontal':
        gs = gridspec.GridSpec(nLines, 2*nColumns)

        for j in xrange(nbrOfItems):
            nc = int(np.mod(j, modulo))
            nl = int((j-nc)/modulo)
            axes.append(plt.subplot(gs[nl,2*nc]))
            gsAxes.append(plt.subplot(gs[nl,2*nc+1]))
        return (figure, gs, axes, gsAxes)

    else:
        gs = gridspec.GridSpec(2*nLines, nColumns)

        for j in xrange(nbrOfItems):
            nc = int(np.mod(j, modulo))
            nl = int((j-nc)/modulo)
            axes.append(plt.subplot(gs[2*nl,nc]))
            gsAxes.append(plt.subplot(gs[2*nl+1,nc]))
        return (figure, gs, axes, gsAxes)
            
    #elif attachGS == 'one':
    #    (nLines, nColumns) = makeGrid(nbrOfItems+1, extendDirection)
    #    gs                 = gridspec.GridSpec(nLines, nColumns)
    #
    #    for j in xrange(nbrOfItems):
    #        axes.append(addAxGS(plt, gs, j, modulo))
    #    gsAx = addAxGS(plt, gs, nbrOfItems, modulo)
    #    return (gs, axes, gsAx)

#____________________________________________________________

def addTitleLabelsGrid(ax, title, xLabel, yLabel, grid):
    if bool(title):
        ax.set_title(title)
    if bool(xLabel):
        ax.set_xlabel(xLabel)
    if bool(yLabel):
        ax.set_ylabel(yLabel)
    if grid:
        ax.grid()

#____________________________________________________________

def trySetScale(ax, xScale, yScale):
    if xScale is not None:
        try:
            ax.set_xscale(xScale)
        except:
            pass

    if yScale is not None:
        try:
            ax.set_yscale(yScale)
        except:
            pass

#____________________________________________________________

def addTimeTextPBar(plt, t, tMaxP1):
    rect     = timeTextPBarRect()
    gsTTPB   = gridspec.GridSpec(1, 1, left=rect[0], bottom=rect[1], right=rect[2], top=rect[3])
    ax       = plt.subplot(gsTTPB[0, 0], frameon=False)
    return (ax, plotTimeTextPBar(ax, t, tMaxP1))

#____________________________________________________________

def plotTimeTextPBar(ax, t, tMaxP1):
    (xTxt, yTxt, xPbarStart, xPbarEnd, yPbar) = positionsTimeTxtPbar()
    ret = [ax.text(xTxt, yTxt, fileNameSuffix(t, tMaxP1)+' / '+str(tMaxP1-1))]

    if t < tMaxP1-1:
        lineBkgPbar, = plot(ax, [yPbar,yPbar], [xPbarStart+float(t)/(tMaxP1-1)*(xPbarEnd-xPbarStart),xPbarEnd], 'k-', linewidth=5)
        ret.append(lineBkgPbar)

    if t > 0:
        linePbar,    = plot(ax, [yPbar,yPbar], [xPbarStart,xPbarStart+float(t)/(tMaxP1-1)*(xPbarEnd-xPbarStart)], 'g-', linewidth=5)
        ret.append(linePbar)

    adaptAxesExtent(ax, 0.0, 1.0, -0.5, 0.5, 0.0, 0.0, 0, 0, 1, 1, 0.0)
    return ret

#____________________________________________________________

def adaptAxesExtent(ax, xmin, xmax, ymin, ymax, extendX, extendY, nbrXTicks, nbrYTicks, xTicksDecimals, yTicksDecimals, EPSILON):    
    xExtend = max(xmax - xmin, EPSILON)
    yExtend = max(ymax - ymin, EPSILON)

    ax.set_xlim(xmin-xExtend*extendX, xmax+xExtend*extendX)
    ax.set_ylim(ymin-yExtend*extendY, ymax+yExtend*extendY)

    xTicks = np.linspace(xmin, xmax, nbrXTicks).round(decimals=xTicksDecimals).tolist()
    yTicks = np.linspace(ymin, ymax, nbrYTicks).round(decimals=yTicksDecimals).tolist()

    ax.set_xticks(xTicks)
    ax.set_yticks(yTicks)

#____________________________________________________________

def makeAxesApplyGSTransport(plt, orientation):

    gs = gridspec.GridSpec(2, 2)

    if orientation == 'horizontal':
        ax1  = plt.subplot(gs[0, 0])
        ax2  = plt.subplot(gs[0, 1])
        axGS = plt.subplot(gs[1, :])

    elif orientation == 'vertical':
        ax1  = plt.subplot(gs[0, 0])
        ax2  = plt.subplot(gs[1, 0])
        axGS = plt.subplot(gs[:, 1])
    
    return (gs, ax1, ax2, axGS)

#____________________________________________________________
