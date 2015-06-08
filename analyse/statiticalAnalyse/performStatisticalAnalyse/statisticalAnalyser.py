#_______________________
# statisticalAnalyser.py
#_______________________

from itertools                                      import product

from performStatisticalAnalyse                      import analyseFieldSpecies
from ...utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ...utils.analyse.io.navigate                   import *

#__________________________________________________

class StatisticalAnalyser:

    def __init__(self, config):
        self.config    = config
        self.simOutput = buildSimulationsOutput(config)

    #_________________________

    def run(self, **kwargs):
        try:
            AOG       = kwargs['AOG']
            species   = kwargs['species']
            field     = None
            LOL       = None
            if kwargs.has_key('field'):
                field = kwargs['field']
            if kwargs.has_key('LOL'):
                LOL   = kwargs['LOL']
            self.analyseFieldsForSpecies(AOG, species, field, LOL)
        except:
            self.analyseFieldsForAllSpecies()

    #_________________________

    def analyseFieldsForAllSpecies(self):
        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.analyseFieldsForSpecies(AOG, species)

    #_________________________

    def analyseFieldsForSpecies(self, AOG, species, field=None, LOL=None):
        
        (fieldList, LOLList) = self.simOutput.fieldLOLList(AOG, field, LOL)
        for (field, LOL) in product(fieldList, LOLList):
            analyseFieldSpecies(self.simOutput,
                                AOG,
                                field,
                                LOL,
                                species,
                                self.config.statisticalAnalyse_nLevelsAlpha,
                                self.config.statisticalAnalyse_chooseScaling,
                                self.config.printIO)

#__________________________________________________
