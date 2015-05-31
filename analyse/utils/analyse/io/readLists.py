#_____________
# readLists.py
#_____________

import numpy as np

from ...io.files           import fileNameSuffix 
from ...io.files           import fileNameSuffixOfShifts
from ...io.read            import readLines

#__________________________________________________

def readFileLabels(fileName):
    return readLines(fileName, removeBlancks=False) 

#__________________________________________________    
                                                
def readFileLevels(fileName):
    lines  = readLines(fileName)
    levels = np.zeros(len(lines))
    for i in xrange(len(lines)):
        levels[i] = float(lines[i])
    return levels

#__________________________________________________

def readFileMinValues(fileName):
    lines = readLines(fileName)
    minVal = {}
    for line in lines:
        l = line.split(':')
        minVal[l[0]] = float(l[1])
    return minVal

#__________________________________________________

def readFileProcesses(fileName, prefixProcName=None, suffixProcName=None):
    lines      = readLines(fileName)
    parameters = lines.pop(0).split('\t')

    for i in xrange(len(parameters)):
        if parameters[i] == 'BCS':
            BCS_num = i
        elif parameters[i] == 'BCSunder':
            BCSunder_num = i
        elif parameters[i] == 'ICS':
            ICS_num = i
        elif parameters[i] == 'ICSunder':
            ICSunder_num = i
        elif parameters[i] == 'DRY_DEP':
            DRY_DEP_num = i
        elif parameters[i] == 'RESOLUTION':
            RESOLUTION_num = i
        elif parameters[i] == 'SOURCE':
            SOURCE_num = i
        elif parameters[i] == 'PSD_SOURCE':
            PSD_SOURCE_num = i
        elif parameters[i] == 'METEO':
            METEO_num = i
        elif parameters[i] == 'KZ':
            KZ_num = i
        elif parameters[i] == 'RAIN':
            RAIN_num = i
        elif parameters[i] == 'DX':
            DX_num = i
        elif parameters[i] == 'DY':
            DY_num = i
        elif parameters[i] == 'DZ':
            DZ_num = i
        elif parameters[i] == 'DT':
            DT_num = i
            
    names = []
    for line in lines:
        parameters = line.split('\t')
        BCS        = parameters[BCS_num]
        BCSunder   = parameters[BCSunder_num]
        ICS        = parameters[ICS_num]
        ICSunder   = parameters[ICSunder_num]
        DryDep     = parameters[DRY_DEP_num]
        Reso       = parameters[RESOLUTION_num]
        Source     = parameters[SOURCE_num]
        PSD_Source = parameters[PSD_SOURCE_num]
        Met        = parameters[METEO_num]
        Kz         = parameters[KZ_num]
        Rain       = parameters[RAIN_num]
        dx         = parameters[DX_num]
        dy         = parameters[DY_num]
        dz         = parameters[DZ_num]
        dt         = parameters[DT_num]

        suffix     = fileNameSuffixOfShifts(dx,dy,dz,dt)
        names.append( Reso   + '-' +
                      Source + '_' + PSD_Source + '-' +
                      Met    + '-' +
                      Kz     + '-' +
                      Rain   + '-' +
                      DryDep + '-' +
                      ICS    + '-' + ICSunder   + '-' +
                      BCS    + '-' + BCSunder   + '-' +
                      suffix )

    if prefixProcName:
        result = []
        for name in names:
            result.append(prefixProcName + name)
        names = result

    if suffixProcName:
        result = []
        for name in names:
            result.append(name + suffixProcName)
        names = result

    return names

#__________________________________________________
