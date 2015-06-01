#________
# read.py
#________

import numpy as np

from files import extensionOfFile

#__________________________________________________

def arrayFromFile(fileName):
    if fileName is None or fileName == '':
        return None

    ext = extensionOfFile(fileName)

    try:
        if ext == 'npy':
            return np.load(fileName)
        else:
            return np.fromfile(fileName)
    except:
        return None

#__________________________________________________

def readLines(fileName, strip=True, removeBlancks=True, commentChar='#', includeEmptyLines=False):
    lines         = readLinesNoFilter(fileName)
    filteredLines = []

    for line in lines:
        l = line.replace('\n','')
        if strip:
            l = l.strip()
        if removeBlancks:
            l = l.replace(' ','')
        if commentChar:
            l = l.split(commentChar)[0]
        if l == '' and includeEmptyLines:
            filteredLines.append(l)
        if not l == '':
            filteredLines.append(l)

    return filteredLines

#__________________________________________________

def readLinesNoFilter(fileName):
    try:
        f = open(fileName, 'r')
        l = f.readlines()
        f.close()
        return l
    except:
        print('Could not read file : '+fileName)
        return []

#__________________________________________________
