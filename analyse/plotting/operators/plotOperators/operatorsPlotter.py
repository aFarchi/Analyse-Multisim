#____________________
# operatorsPlotter.py
#____________________

from itertools                                      import product

from ....utils.analyse.simulation.simulationsOutput import buildSimulationsOutput
from ....utils.analyse.io.navigate                  import *
from plotOperator                                   import plotL2WassersteinOTGS
from plotOperator                                   import plotL2WassersteinOT2D
from plotOperator                                   import plotStatisticalOperators

#__________________________________________________

class OperatorsPlotter:

    def __init__(self, config):
        self.config    = config
        self.simOutput = buildSimulationsOutput(config)

    def plot(self, **kwargs):
        try:
            AOG       = kwargs['AOG']
            species   = kwargs['species']
            field     = None
            LOL       = None
            if kwargs.has_key('field'):
                field = kwargs['field']
            if kwargs.has_key('LOL'):
                LOL   = kwargs['LOL']
            self.plotAOGOperators(AOG, species, field, LOL)
        except:
            self.plotOperatorsForAllSpecies()

    def plotOperatorsForAllSpecies(self):
        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.plotAOGOperators(AOG, species)

    def plotAOGOperators(self, AOG, species, field=None, LOL=None):

        (fieldList, LOLList, TSList) = self.simOutput.fieldLOLTSList(AOG, field, LOL, None)
        OTGSConfigNameList           = self.config.OTGS_configurationNames
        OT2DConfigNameList           = self.config.OT2D_configurationNames

        for (field, LOL) in product(fieldList, LOLList):
            plotStatisticalOperators(self.simOutput,
                                     AOG,
                                     field,
                                     LOL,
                                     species,
                                     self.config.preprocessRawData_nLevelsFM,
                                     self.config.statisticalAnalyse_nLevelsAlpha,
                                     self.config.plotOperators_cmapName,
                                     self.config.plotOperators_extensions)

        for (field, LOL, TS, configName) in product(fieldList, LOLList, TSList, OTGSConfigNameList):    
            plotL2WassersteinOTGS(self.simOutput,
                                  configName,
                                  AOG,
                                  field,
                                  LOL,
                                  species,
                                  TS,
                                  self.config.plotOperators_cmapName,
                                  self.config.plotOperators_extensions)

        for (field, LOL, configName) in product(fieldList, LOLList, OT2DConfigNameList):
            plotL2WassersteinOT2D(self.simOutput,
                                  configName,
                                  AOG,
                                  field,
                                  LOL,
                                  species,
                                  self.config.plotOperators_cmapName,
                                  self.config.plotOperators_extensions)
            
#__________________________________________________

