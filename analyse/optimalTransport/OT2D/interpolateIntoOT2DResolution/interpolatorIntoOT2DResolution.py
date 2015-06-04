#__________________________________
# interpolatorIntoOT2DResolution.py
#__________________________________

from itertools                                       import product

from interpolateIntoOT2DResolution                   import interpolateAOGFieldsIntoOT2DResolution
from ....utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ....utils.analyse.io.navigate                   import *

#__________________________________________________

class InterpolatorIntoOT2DResolution:

    def __init__(self, config):
        self.config    = config
        self.simOutput = buildSimulationsOutput(config)

    #_________________________

    def run(self, **kwargs):
        if not self.config.OT2D_interpolateIntoOT2DResolution:
            return

        try:
            AOG     = kwargs['AOG']
            GOR     = kwargs['GOR']
            species = kwargs['species']
            self.interpolateIntoOT2DResolutionForSpecies(AOG, GOR, species)
        except:
            self.interpolateIntoOT2DResolutionForAllSpecies()

    #_________________________

    def interpolateIntoOT2DResolutionForSpecies(self, AOG, GOR, species):

        interpolateAOGFieldsIntoOT2DResolution(self.simOutput,
                                             AOG,
                                             species,
                                             self.config.OT2D_shape,
                                             self.config.printIO)

    #_________________________
    
    def interpolateIntoOT2DResolutionForAllSpecies(self):

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.interpolateIntoOT2DResolutionForSpecies(AOG, GOR, species)

#__________________________________________________
