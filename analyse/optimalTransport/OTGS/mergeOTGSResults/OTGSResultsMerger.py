#_____________________
# OTGSResultsMerger.py
#_____________________

from itertools                                       import product

from mergeOTGSResults                                import mergeOTGSResultsForField
from ....utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ....utils.analyse.io.navigate                   import *

#__________________________________________________

class OTGSResultsMerger:

    def __init__(self, config):
        self.config    = config
        self.simOutput = buildSimulationsOutput(config)

    #_________________________

    def run(self, **kwargs):
        try:
            AOG            = kwargs['AOG']
            GOR            = kwargs['GOR']
            species        = kwargs['species']
            try:
                field      = kwargs['field']
            except:
                field      = None
            try:
                LOL        = kwargs['LOL']
            except:
                LOL        = None
            try:
                TS         = kwargs['TS']
            except:
                TS         = None
            try:
                configName = kwargs['configName']
            except:
                configName = None

            self.mergeOTGSResultsForSpecies(AOG, GOR, species, field, LOL, TS, configName)
        except:
            self.mergeOTGSResultsForAllSpecies()

    #_________________________

    def mergeOTGSResultsForSpecies(self, AOG, GOR, species, field=None, LOL=None, TS=None, configName=None):

        (fieldList, LOLList, TSList) = self.simOutput.fieldLOLTSList(AOG, field, LOL, TS)
        if configName is None:
            configNameList = self.config.OTGS_configurationNames
        else:
            configNameList = [configName]

        for (field, LOL, TS, configName) in product(fieldList, LOLList, TSList, configNameList):
            mergeOTGSResultsForField(self.simOutput,
                                     configName,
                                     AOG,
                                     species,
                                     field,
                                     LOL,
                                     TS,
                                     self.config.printIO)

    #_________________________

    def mergeOTGSResultsForAllSpecies(self):

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.mergeOTGSResultsForSpecies(AOG, GOR, species)

#__________________________________________________
