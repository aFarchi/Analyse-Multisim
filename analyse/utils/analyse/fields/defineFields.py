#________________
# defineFields.py
#________________

from ..io.readLists                  import catchMinValuesFromFile
from ..io.readLists                  import catchLevelsFromFile
from ..timeSelection.defaultTSelect  import makeSelectXtimesNt

from air.airColumn                   import AirColumn
from air.airGroundLevel              import AirGroundLevel
from ground.totalDeposition          import TotalDeposition

#__________________________________________________

def defineFieldsFromFiles(outputDir, sessionName, xTSelect=None):
    minValues  = catchMinValuesFromFile(outputDir, sessionName)
    levels     = catchLevelsFromFile(outputDir, sessionName)
    if xTSelect is None:
        funTSelect = None
    else:
        funTSelect = makeSelectXtimesNt(xTSelect)
    return defineFields(minValues, funTSelect, levels)

#__________________________________________________

def defineAirFields(minValues=None, funTSelect=None, levels=None):
    airColumn      = AirColumn(minValues, funTSelect, levels)
    airGroundLevel = AirGroundLevel(minValues, funTSelect)
    return [ airColumn , airGroundLevel ]

#__________________________________________________

def defineGroundFields(minValues=None, funTSelect=None):
    totalDep = TotalDeposition(minValues, funTSelect)
    return [totalDep]

#__________________________________________________

def defineFields(minValues=None, funTSelect=None, levels=None):
    fieldList            = {}
    fieldList['air/']    = defineAirFields(minValues, funTSelect, levels)
    fieldList['ground/'] = defineGroundFields(minValues, funTSelect)
    return fieldList

#__________________________________________________
