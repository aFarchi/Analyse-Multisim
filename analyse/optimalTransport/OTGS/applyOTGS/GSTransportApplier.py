#______________________
# GSTransportApplier.py
#______________________

from itertools                                       import product

from applyGSTransport                                import applyGSTransportForField
from ....utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ....utils.analyse.io.navigate                   import *

#__________________________________________________

class GSTransportApplier:

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
                TS         = kwargs['TS']
            except:
                TS         = None
            try:
                configName = kwargs['configName']
            except:
                configName = None

            self.applyGSTransportForSpecies(AOG, species, field, LOL, TS, configName)
        except:
            self.applyGSTransportForAllSpecies()

    #_________________________

    def applyGSTransportForSpecies(self, AOG, species, field=None, LOL=None, TS=None, configName=None):
        (fieldList, LOLList, TSList) = self.simOutput.fieldLOLTSList(AOG, field, LOL, TS)
        if configName is None:
            configNameList = self.config.OTGS_configurationNames
        else:
            configNameList = [configName]

        for (field, LOL, TS, configName) in product(fieldList, LOLList, TSList, configNameList):
            applyGSTransportForField(self.simOutput,
                                     configName,
                                     AOG,
                                     species,
                                     field,
                                     LOL,
                                     TS,
                                     self.config.OTGS_applyOTGS_Error,
                                     self.config.printIO)

    #_________________________

    def applyGSTransportForAllSpecies(self):
        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.applyGSTransportForSpecies(AOG, species)

#__________________________________________________
