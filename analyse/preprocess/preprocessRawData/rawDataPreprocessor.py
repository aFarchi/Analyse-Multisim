#_______________________
# rawDataPreprocessor.py
#_______________________

from itertools                                      import product

from preprocessRawData                              import computeAOGFields
from preprocessRawData                              import computeFMScalingMakeGSAOGFields
from preprocessRawDataBigMemory                     import computeAOGFieldsBigMemory
from preprocessRawDataBigMemory                     import computeFMScalingMakeGSAOGFieldsBigMemory

from ...utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ...utils.analyse.processRawData.extractRawData import extractRawDataMultiProc
from ...utils.analyse.io.navigate                   import *

#__________________________________________________

class RawDataPreprocessor:

    def __init__(self, config):
        self.config    = config
        self.simOutput = buildSimulationsOutput(config)

    #_________________________

    def run(self, **kwargs):
        if self.config.preprocessRawData:
            try:
                AOG       = kwargs['AOG']
                GOR       = kwargs['GOR']
                species   = kwargs['species']
                self.preprocessRawDataForSpecies(AOG, GOR, species)
            except:
                self.preprocessRawDataForAllSpecies()

    #_________________________

    def preprocessRawDataForSpecies(self, AOG, GOR, species):

        if self.config.preprocessRawData_bigMemory:
            rawData = extractRawDataMultiProc(self.simOutput, 
                                              AOG,
                                              GOR,
                                              species,
                                              self.config.printIO)

            computeAOGFieldsBigMemory(rawData,
                                      self.simOutput,
                                      AOG,
                                      species,
                                      self.config.printIO)

            computeFMScalingMakeGSAOGFieldsBigMemory(rawData,
                                                     self.simOutput,
                                                     AOG,
                                                     species,
                                                     self.config.preprocessRawData_nLevelsGrayScale,
                                                     self.config.printIO)

        else:
            computeAOGFields(self.simOutput,
                             AOG,
                             GOR,
                             species,
                             self.config.printIO)

            computeFMScalingMakeGSAOGFields(self.simOutput,
                                            AOG,
                                            GOR,
                                            species,
                                            self.config.preprocessRawData_nLevelsGrayScale,
                                            self.config.printIO)

    #_________________________
    
    def preprocessRawDataForAllSpecies(self):

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.preprocessRawDataForSpecies(AOG, GOR, species)

#__________________________________________________
