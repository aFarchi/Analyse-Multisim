#_____________
# buildTmap.py
#_____________

import numpy as np
from scipy.interpolate import interp1d

#__________________________________________________

def buildTmap(Tarray, error):
    N             = Tarray.size

    # Filters T to make it stricly growing
    TFiltered     = np.minimum(1.0, Tarray)
    TFiltered[0]  = 0.0
    DT            = TFiltered[1:] - TFiltered[:N-1]
    DT            = np.maximum(error/N, DT)

    TFiltered[1:] = DT.cumsum()

    TFiltered    /= TFiltered[N-1]

    # Extends X and T arrays to avoid boundary errors
    XTmap         = np.zeros(N+2)
    TTmap         = np.zeros(N+2)

    XTmap[0]      = - 1.0
    XTmap[1:N+1]  = np.linspace(0.0, 1.0, N)
    XTmap[N+1]    = 2.0

    TTmap[0]      = 0.0
    TTmap[1:N+1]  = TFiltered[:]
    TTmap[N+1]    = 1.0

    # Interpolates Tmap
    Tmap          = interp1d(XTmap, TTmap)

    XTmap[0]      = 0.0
    XTmap[N+1]    = 1.0
    TTmap[0]      = - 1.0
    TTmap[N+1]    = 2.0

    # Interpolates inverse Tmap
    inverseTmap   = interp1d(TTmap, XTmap, copy=False)

    return (Tmap, inverseTmap)

#__________________________________________________
