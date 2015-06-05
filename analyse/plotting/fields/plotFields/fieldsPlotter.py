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
        if self.config.plotFields_colorBar:
            cmapName  = self.config.plotFields_cmapName

        for (field, LOL) in product(fieldList, LOLList):

            if self.config.plotFields_AOO == 'all':
                procListList      = [self.simOutput.procList]
                labelListList     = [self.simOutput.labelList]
                suffixFigNameList = ['allsim']

            elif self.config.plotFields_AOO == 'one':
                procListList      = []
                labelListList     = []
                suffixFigNameList = []

                for (proc, label) in zip(self.simOutput.procList, self.simOutput.labelList):
                    procListList.append([proc])
                    labelListList.append([label])
                    suffixFigNameList.append([label])

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
                              cmapName,
                              self.config.plotFields_extensions,
                              self.config.EPSILON,
                              self.config.printIO)

#__________________________________________________

