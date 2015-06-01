#______________
# modulePath.py
#______________

#__________________________________________________

class ModulePath:

    def __init__(self):

        self.moduleUpperPath         = '/Users/Alban/Desktop/Analyse-Multisim/'
        self.modulePath              = self.moduleUpperPath + 'analyse/'
        self.moduleLauncher          = self.moduleUpperPath + 'launcher.py'
        self.moduleLauncherPlotting  = self.moduleUpperPath + 'launcherPlotting.py'
        self.moduleLauncherAnimating = self.moduleUpperPath + 'launcherAnimating.py'
        self.OTModulePath            = '/Users/Alban/Desktop/Optimal-Transport/'
        self.OT2DLauncher            = self.OTModulePath + 'launchSimulation2D.py'
        self.OT2DLauncherPlotting    = self.OTModulePath + 'plotSimulation2D.py'

        #_________________________

        self.defaultFilesLauncherPath = self.modulePath + 'utils/launchers/'
        self.defaultPythonLauncher    = self.defaultFilesLauncherPath + 'defaultLauncher.py'
        self.defaultBashLauncher      = self.defaultFilesLauncherPath + 'defaultLauncher.sh'
        self.defaultNodesFile         = self.defaultFilesLauncherPath + 'defaultNodes.dat'

        #_________________________

        self.defaultFilesOTConfigPath = self.modulePath + 'utils/OTConfig/'
        self.defaultConfigOT2D        = self.defaultFilesOTConfigPath + 'defaultOT2D.cfg'
        self.defaultConfigPlotOT2D    = self.defaultFilesOTConfigPath + 'defaultPlotOT2D.cfg'

#__________________________________________________
