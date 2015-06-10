#_____________
# buildTmap.py
#_____________

import numpy as np
from scipy.interpolate import interp1d

#__________________________________________________

def makeInterpolatorPP(X, Y, copy=True):
    if copy:
        return makeInterpolatorPP(X.copy(), Y.copy(), copy=False)

    XPP       = np.zeros(X.size+2)
    XPP[1:-1] = X[:]
    XPP[0]    = X[0] - 1.0
    XPP[-1]   = X[-1] + 1.0

    YPP       = np.zeros(Y.size+2)
    YPP[1:-1] = Y[:]
    YPP[0]    = Y[0]
    YPP[-1]   = Y[-1]

    return interp1d(XPP, YPP, copy=False, bounds_error=False, fill_value=0.0)

#__________________________________________________

def buildTmap(Tarray, error):
    N             = Tarray.size

    # Filters T to make it stricly growing
    TFiltered     = np.minimum(1.0, Tarray)
    TFiltered[0]  = 0.0
    TFiltered[-1] = 1.0

    DT            = TFiltered[1:] - TFiltered[:-1]
    meanDT        = DT.mean()
    minDT         = meanDT * error
    DT            = np.maximum(minDT, DT)

    TFiltered[1:] = DT.cumsum()

    # Interpolates Tmap and its inverse
    X             = np.linspace(0.0, 1.0, N)
    Tmap          = makeInterpolatorPP(X, TFiltered, copy=True)
    inverseTmap   = makeInterpolatorPP(TFiltered, X, copy=False)

    return (Tmap, inverseTmap)

#__________________________________________________
