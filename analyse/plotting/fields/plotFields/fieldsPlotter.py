#_________________
# fieldsPlotter.py
#_________________

from itertools                                      import product

from ....utils.analyse.simulation.simulationsOutput import buildSimulationsOutput
from ....utils.analyse.io.navigate                  import *
from plotField                                      import plotProcField

#__________________________________________________

class FieldsPlotter:

    def __init__(self, config):
        self.config    = config
        self.simOutput = buildSimulationsOutput(config)

    def plot(self, **kwargs):
        if self.config.plotFields:
            try:
                AOG       = kwargs['AOG']
                species   = kwargs['species']
                field     = None
                LOL       = None
                if kwargs.has_key('field'):
                    field = kwargs['field']
                if kwargs.has_key('LOL'):
                    LOL   = kwargs['LOL']
                self.plotAOGFields(AOG, species, field, LOL)
            except:
                self.plotFieldsForAllSpecies()

    def plotFieldsForAllSpecies(self):
        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.plotAOGFields(AOG, species)

    def plotAOGFields(self, AOG, species, field=None, LOL=None):

        (fieldList, LOLList) = self.simOutput.fieldLOLList(AOG, field, LOL)

        for (field, LOL) in product(fieldList, LOLList):

            (procListList, 
             labelListList, 
             suffixFigNameList) = self.simOutput.makeProcLabelSuffixListList(AOO=self.config.plotFields_AOO,
                                                                             addSimLabel=self.config.plotFields_simLabels)

            for (procList, labelList, suffixFigName) in zip(procListList, labelListList, suffixFigNameList):

                plotProcField(self.simOutput,
                              procList,
                              labelList,
                              suffixFigName,
                              self.config.plotFields_applyGlobalScaling,
                              AOG,
                              field,
                              LOL,
                              species,
                              self.config.plotFields_xLabel,
                              self.config.plotFields_yLabel,
                              self.config.plotFields_cLabel,
                              self.config.plotFields_order,
                              self.config.plotFields_extendDirection,
                              self.config.plotFields_plotter,
                              self.config.plotFields_plotterArgs,
                              self.config.plotFields_extendX,
                              self.config.plotFields_extendY,
                              self.config.plotFields_nbrXTicks,
                              self.config.plotFields_nbrYTicks,
                              self.config.plotFields_nbrCTicks,
                              self.config.plotFields_xTicksDecimals,
                              self.config.plotFields_yTicksDecimals,
                              self.config.plotFields_cTicksDecimals,
                              self.config.plotFields_colorBar,
                              self.config.plotFields_cmapName,
                              self.config.plotFields_extensions,
                              self.config.EPSILON,
                              self.config.printIO)

#__________________________________________________

