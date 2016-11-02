#________________
# defineFields.py
#________________

from air.airColumn                   import AirColumn
from air.airGroundLevel              import AirGroundLevel
from ground.totalDeposition          import TotalDeposition

#__________________________________________________

def defineAirFields(simOutput):
    airColumn      = AirColumn(simOutput)
    airGroundLevel = AirGroundLevel(simOutput)
    return [airColumn, airGroundLevel]

#__________________________________________________

def defineGroundFields(simOutput):
    totalDep = TotalDeposition(simOutput)
    return [totalDep]

#__________________________________________________

def defineFields(simOutput):
    fieldList            = {}
    fieldList['air/']    = [] # defineAirFields(simOutput)
    fieldList['ground/'] = defineGroundFields(simOutput)
    return fieldList

#__________________________________________________
