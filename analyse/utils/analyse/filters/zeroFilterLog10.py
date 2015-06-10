#___________________
# zeroFilterLog10.py
#___________________

import numpy as np

#__________________________________________________

def zeroFilterLog10(rawData, minValue, LOL, TS):

    if TS == 'Threshold':
        minValueFiltered = -1.0
    else:
        minValueFiltered = minValue

    if LOL == 'lin':
        return ( minValueFiltered * ( rawData <= minValue ) +
                 rawData          * ( rawData >  minValue ) )
    
    elif LOL == 'log':
        data = np.log10(np.maximum(rawData, 0.1 * minValue)) - np.log10(minValue)

        return ( minValueFiltered * ( data <= 0.0 ) +
                 data             * ( data >  0.0 ) )
    
#__________________________________________________
