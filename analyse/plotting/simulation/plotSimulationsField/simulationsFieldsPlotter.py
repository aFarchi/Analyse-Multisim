#____________________________
# simulationsFieldsPlotter.py
#____________________________

from itertools                                       import product

from ....utils.analyse.processRawData.extractRawData import extractRawDataMultiProc
from ....utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ....utils.analyse.io.navigate                   import *
from plotSimulationsFields                           import plotProcField

#__________________________________________________

class SimulationsFieldPlotter:

    def __init__(self, plotSimOutputConfig):
        self.config    = plotSimOutputConfig
        self.simOutput = buildSimulationsOutput(plotSimOutputConfig)

    def plot(self, **kwargs):
        if self.config.plotSimulationsField:
            try:
                AOG       = kwargs['AOG']
                GOR       = kwargs['GOR']
                species   = kwargs['species']
                field     = None
                LOL       = None
                if kwargs.has_key('field'):
                    field = kwargs['field']
                if kwargs.has_key('LOL'):
                    LOL   = kwargs['LOL']
                self.plotAOGFields(AOG, GOR, species, field, LOL)
            except:
                self.plotFieldsForAllSpecies()

    def plotFieldsForAllSpecies(self):
        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.plotAOGFields(AOG, GOR, species)

    def plotAOGFields(self, AOG, GOR, species, field=None, LOL=None):

        rawData = extractRawDataMultiProc(self.simOutput, AOG, GOR, species, self.config.printIO)

        if field is None:
            fieldList = self.simOutput.fieldList[AOG]
        else:
            fieldList = []
            for f in self.simOutput.fieldList[AOG]:
                if field == f.name:
                    fieldList.append(f)
                    break

        if LOL is None:
            LOLList   = LinOrLog()
        else:
            LOLList   = [LOL]

        cmapName      = 'jet'
        if self.config.plotSimulationsField_colorBar:
            cmapName  = self.config.plotSimulationsField_cmapName

        for (field, LOL) in product(fieldList, LOLList):

            if self.config.plotSimulationsField_AOO == 'all':
                procListList      = [self.simOutput.procList]
                labelListList     = [self.simOutput.labelList]
                suffixFigNameList = ['allsim']

            elif self.config.plotSimulationsField_AOO == 'one':
                procListList      = []
                labelListList     = []
                suffixFigNameList = []

                for (proc, label) in zip(self.simOutput.procList, self.simOutput.labelList):
                    procListList.append([proc])
                    labelListList.append([label])
                    suffixFigNameList.append([label])

            for (procList, labelList, suffixFigName) in zip(procListList, labelListList, suffixFigNameList):

                plotProcField(rawData,
                              self.simOutput,
                              procList,
                              labelList,
                              suffixFigName,
                              AOG,
                              field,
                              LOL,
                              species,
                              self.config.plotSimulationsField_xLabel,
                              self.config.plotSimulationsField_yLabel,
                              self.config.plotSimulationsField_cLabel,
                              self.config.plotSimulationsField_order,
                              self.config.plotSimulationsField_extendDirection,
                              self.config.plotSimulationsField_plotter,
                              self.config.plotSimulationsField_plotterArgs,
                              self.config.plotSimulationsField_extendX,
                              self.config.plotSimulationsField_extendY,
                              self.config.plotSimulationsField_nbrXTicks,
                              self.config.plotSimulationsField_nbrYTicks,
                              self.config.plotSimulationsField_nbrCTicks,
                              self.config.plotSimulationsField_xTicksDecimals,
                              self.config.plotSimulationsField_yTicksDecimals,
                              self.config.plotSimulationsField_cTicksDecimals,
                              self.config.plotSimulationsField_colorBar,
                              cmapName,
                              self.config.plotSimulationsField_timeTextPBar,
                              self.config.extensions,
                              self.config.EPSILON)

#__________________________________________________

