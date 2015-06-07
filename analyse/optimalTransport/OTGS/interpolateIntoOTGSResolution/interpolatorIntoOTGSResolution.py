#__________________________________
# interpolatorIntoOTGSResolution.py
#__________________________________

from itertools                                       import product

from interpolateIntoOTGSResolution                   import interpolateAOGFieldsGSIntoOTGSResolution
from ....utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ....utils.analyse.io.navigate                   import *

#__________________________________________________

class InterpolatorIntoOT2DResolution:

    def __init__(self, config):
        self.config    = config
        self.simOutput = buildSimulationsOutput(config)

    #_________________________

    def run(self, **kwargs):
        if not self.config.OTGS_interpolateIntoOTGSResolution:
            return

        try:
            AOG     = kwargs['AOG']
            GOR     = kwargs['GOR']
            species = kwargs['species']
            self.interpolateIntoOTGSResolutionForSpecies(AOG, GOR, species)
        except:
            self.interpolateIntoOTGSResolutionForAllSpecies()

    #_________________________

    def interpolateIntoOTGSResolutionForSpecies(self, AOG, GOR, species):

        interpolateAOGFieldsGSIntoOTGSResolution(self.simOutput,
                                                 AOG,
                                                 species,
                                                 self.config.OTGS_resolution,
                                                 self.config.printIO)

    #_________________________
    
    def interpolateIntoOTGSResolutionForAllSpecies(self):

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.interpolateIntoOTGSResolutionForSpecies(AOG, GOR, species)

#__________________________________________________
