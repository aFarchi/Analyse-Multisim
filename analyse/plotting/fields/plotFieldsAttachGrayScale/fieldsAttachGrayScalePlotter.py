#________________________________
# fieldsAttachGrayScalePlotter.py
#________________________________

from itertools                                      import product

from ....utils.analyse.simulation.simulationsOutput import buildSimulationsOutput
from ....utils.analyse.io.navigate                  import *
from plotFieldsAttachGrayScale                      import plotProcFieldAttachGS

#__________________________________________________

class FieldsAttachGrayScalePlotter:

    def __init__(self, config):
        self.config    = config
        self.simOutput = buildSimulationsOutput(config)

    def plot(self, **kwargs):
        if self.config.plotFieldsAttachGrayScale:
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
             suffixFigNameList) = self.simOutput.makeProcLabelSuffixListList(AOO=self.config.plotFieldsAttachGrayScale_AOO,
                                                                             addSimLabel=self.config.plotFieldsAttachGrayScale_simLabels)

            for (procList, labelList, suffixFigName) in zip(procListList, labelListList, suffixFigNameList):

                plotProcFieldAttachGS(self.simOutput,
                                      procList,
                                      labelList,
                                      suffixFigName,
                                      AOG,
                                      field,
                                      LOL,
                                      species,
                                      self.config.plotFieldsAttachGrayScale_xLabel,
                                      self.config.plotFieldsAttachGrayScale_yLabel,
                                      self.config.plotFieldsAttachGrayScale_order,
                                      self.config.plotFieldsAttachGrayScale_extendDirection,
                                      self.config.plotFieldsAttachGrayScale_plotter,
                                      self.config.plotFieldsAttachGrayScale_plotterArgs,
                                      self.config.plotFieldsAttachGrayScale_extendX,
                                      self.config.plotFieldsAttachGrayScale_extendY,
                                      self.config.plotFieldsAttachGrayScale_nbrXTicks,
                                      self.config.plotFieldsAttachGrayScale_nbrYTicks,
                                      self.config.plotFieldsAttachGrayScale_nbrCTicks,
                                      self.config.plotFieldsAttachGrayScale_xTicksDecimals,
                                      self.config.plotFieldsAttachGrayScale_yTicksDecimals,
                                      self.config.plotFieldsAttachGrayScale_cTicksDecimals,
                                      self.config.plotFieldsAttachGrayScale_cmapName,
                                      self.config.plotFieldsAttachGrayScale_scaleGS,
                                      self.config.plotFieldsAttachGrayScale_extendDirectionGS,
                                      self.config.preprocessRawData_nLevelsGrayScale,
                                      self.config.plotFieldsAttachGrayScale_options,
                                      self.config.plotFieldsAttachGrayScale_directionGS,
                                      self.config.plotFieldsAttachGrayScale_extensions,
                                      self.config.EPSILON,
                                      self.config.printIO)

#__________________________________________________

