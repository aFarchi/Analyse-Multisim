#___________________
# zeroFilterLog10.py
#___________________

import numpy as np

#__________________________________________________

def minValueFiltered():
    return ( - 1.0 )

#__________________________________________________

def halfMinValueFiltered():
    return ( - 0.5 )

#__________________________________________________

def zeroFilterLog10(rawData, minValue, LOL):

    if LOL == 'lin':
        return ( minValueFiltered() * ( rawData <= minValue ) +
                 rawData            * ( rawData >  minValue ) )
    
    elif LOL == 'log':
        data = np.log10(np.maximum(rawData, 0.1 * minValue)) - np.log10(minValue)

        return ( minValueFiltered() * ( data <= 0.0 ) +
                 data               * ( data >  0.0 ) )
    
#__________________________________________________
