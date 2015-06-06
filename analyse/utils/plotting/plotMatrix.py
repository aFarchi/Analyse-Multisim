#______________
# plotMatrix.py
#______________

import numpy      as np
import matplotlib as mpl

from matplotlib              import gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
from cmap                    import colormap
from positions               import colorBarRect
from plotting                import adaptAxesExtent

#__________________________________________________

def plotMatrix(ax, matrix, plotter, xmin=0.0, xmax=1.0, ymin=0.0, ymax=1.0, cmapName='jet', **kwargs):
    kwargs = fillKwargs(plotter, xmin, xmax, ymin, ymax, cmapName, **kwargs)

    if plotter == 'imshow':
        return ax.imshow(matrix, **kwargs)

    elif plotter == 'contour':
        return ax.contour(matrix, **kwargs)

    elif plotter == 'contourf':
        return ax.contourf(matrix, **kwargs)

#__________________________________________________

def fillKwargs(plotter, xmin, xmax, ymin, ymax, cmapName, **kwargs):
    cmap   = colormap(cmapName)
    if kwargs.has_key('vmin') and kwargs.has_key('vmax'):
        norm = mpl.colors.Normalize(vmin=kwargs['vmin'], vmax=kwargs['vmax'], clip=False)
        kwargs['norm'] = norm

    kwargs['cmap'] = cmap

    if not kwargs.has_key('origin'):
        kwargs['origin'] = 'lower'
    if not kwargs.has_key('extent'):
        kwargs['extent'] = [xmin, xmax, ymin, ymax]

    if plotter == 'imshow':
        if not kwargs.has_key('interpolation'):
            kwargs['interpolation'] = 'nearest'
    elif plotter == 'contour':
        if not kwargs.has_key('colors'):
            kwargs['colors'] = 'k'
        if not kwargs.has_key('linestyles'):
            kwargs['linestyles'] = 'solid'

    return kwargs

#__________________________________________________

def addColorBar(plt, timeTextPBar, cmapName, mini, maxi, nbrTicks, ticksDecimals, label):
    rect = colorBarRect(timeTextPBar)
    gsCB = gridspec.GridSpec(1, 1, left=rect[0], bottom=rect[1], right=rect[2], top=rect[3])
    cax  = plt.subplot(gsCB[0, 0], frameon=False)
    cbar = plotColorBar(cax, cmapName, mini, maxi, nbrTicks, ticksDecimals, '')
    cbar.set_label(label, labelpad=-80)
    return (cax, cbar)

#__________________________________________________

def plotColorBar(cax, cmapName, mini, maxi, nbrTicks, ticksDecimals, label, orientation='vertical'):
    cmap  = colormap(cmapName)
    norm  = mpl.colors.Normalize(vmin=mini, vmax=maxi, clip=False)

    if nbrTicks < 2:
        ticks = None
    else:
        ticks = np.linspace(mini, maxi, nbrTicks).round(decimals=ticksDecimals).tolist()

    return mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, ticks=ticks, label=label, orientation=orientation)

#__________________________________________________

def plotGrayScale(ax, GS, mini, maxi, maxiGS, nLevels, cmapName, options, 
                  nbrGSTicks, nbrCTicks, GSTicksDecimals, cTicksDecimals, direction, EPSILON):

    levels = np.linspace(mini, maxi, nLevels)
    plotColorBar(ax, cmapName, mini, maxi, nbrCTicks, cTicksDecimals, None, orientation='vertical')

    for TS in GS:
        if direction == 'vertical':
            args = [GS[TS]/maxiGS, levels]
        else:
            args = [levels, GS[TS]/maxiGS]
        args.append(options[TS])
        ax.plot(*args)

    '''
    if direction == 'vertical':
        ymin = mini
        ymax = maxi
        xmin = 0.0
        xmax = maxiGS

        nbrXTicks      = nbrGSTicks
        nbrYTicks      = nbrCTicks
        xTicksDecimals = GSTicksDecimals
        yTicksDecimals = cTicksDecimals

        (matrixColorBar, X) = np.meshgrid(levels, [0,1], indexing='ij')
        
    else:
        xmin = mini
        xmax = maxi
        ymin = 0.0
        ymax = maxiGS

        nbrXTicks      = nbrCTicks
        nbrYTicks      = nbrGSTicks

        xTicksDecimals = cTicksDecimals        
        yTicksDecimals = GSTicksDecimals

        (X, matrixColorBar) = np.meshgrid([0,1], levels, indexing='ij')


    adaptAxesExtent(ax,
                    xmin,
                    xmax,
                    ymin,
                    ymax,
                    0.0,
                    0.0,
                    nbrXTicks,
                    nbrYTicks,
                    xTicksDecimals,
                    yTicksDecimals,
                    EPSILON)
    '''

    #plotMatrix(ax, matrixColorBar, 'imshow', xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, cmapName=cmapName, 
    #           vmin=mini, vmax=maxi, interpolation='bilinear')
    #return (xmin, xmax, ymin, ymax)

#__________________________________________________

