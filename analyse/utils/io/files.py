#_________
# files.py
#_________

import numpy as np

#__________________________________________________

def extensionOfFile(fileName):
    if not '.' in fileName:
        return None
    else:
        l = fileName.split('.')
        return l[len(l)-1]

#__________________________________________________

def fileNameSuffix(i,iMaxP1):
    nDigit = np.ceil(np.log10(iMaxP1))
    s      = str(int(i))
    while len(s) < nDigit:
        s  = '0' + s
    return s

#__________________________________________________

def fileNameSuffixOfShifts(dx, dy, dz, dt):
    return ( 'shift_' +
             dx + '_' +
             dy + '_' +
             dz + '_' +
             dt )

#__________________________________________________

