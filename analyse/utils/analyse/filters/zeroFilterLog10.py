#___________________
# zeroFilterLog10.py
#___________________

import numpy as np

#__________________________________________________

def zeroFilterLog10(rawData, minValue, lol):
    data = np.maximum(rawData, minValue)
    if lol == 'log':
        data = np.log10(data) - np.log10(minValue)
    return data

#__________________________________________________

def zeroFilterLog10Coarsed(rawData, minValue, lol, coarseFactor):
    data = np.maximum(rawData, coarseFactor*minValue)
    if lol == 'log':
        data = np.log10(data) - np.log10(minValue)
    return data

#__________________________________________________
