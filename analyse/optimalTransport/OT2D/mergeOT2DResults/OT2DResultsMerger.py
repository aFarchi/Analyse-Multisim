#_____________________
# OT2DResultsMerger.py
#_____________________

from itertools                                       import product

from mergeOT2DResults                                import mergeOT2DResultsForField
from ....utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ....utils.analyse.io.navigate                   import *

#__________________________________________________

class OT2DResultsMerger:

    def __init__(self, config):
        self.config    = config
        self.simOutput = buildSimulationsOutput(config)

    #_________________________

    def run(self, **kwargs):
        try:
            AOG            = kwargs['AOG']
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
                configName = kwargs['configName']
            except:
                configName = None

            self.mergeOT2DResultsForSpecies(AOG, species, field, LOL, configName)
        except:
            self.mergeOT2DResultsForAllSpecies()

    #_________________________

    def mergeOT2DResultsForSpecies(self, AOG, species, field=None, LOL=None, configName=None):

        (fieldList, LOLList) = self.simOutput.fieldLOLList(AOG, field, LOL)
        if configName is None:
            configNameList = self.config.OT2D_configurationNames
        else:
            configNameList = [configName]

        for (field, LOL, configName) in product(fieldList, LOLList, configNameList):
            mergeOT2DResultsForField(self.simOutput,
                                     configName,
                                     AOG,
                                     species,
                                     field,
                                     LOL,
                                     self.config.printIO)

    #_________________________

    def mergeOT2DResultsForAllSpecies(self):

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.mergeOT2DResultsForSpecies(AOG, species)

#__________________________________________________
