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
        self.oTModulePath            = '/Users/Alban/Desktop/Optimal-Transport/'
        self.oT2DLauncher            = self.oTModulePath + 'launchSimulation2D.py'
        #self.oT2DLauncherPlotting    = self.oTModulePath + 'plotSimulation2D.py'

        #_________________________

        self.defaultFilesLauncherPath = self.modulePath + 'utils/launchers/'
        self.defaultPythonLauncher    = self.defaultFilesLauncherPath + 'defaultLauncher.py'
        self.defaultBashLauncher      = self.defaultFilesLauncherPath + 'defaultLauncher.sh'
        self.defaultNodesFile         = self.defaultFilesLauncherPath + 'defaultNodes.dat'

        #_________________________

        self.defaultFilesOTConfigPath = self.modulePath + 'utils/oTConfig/'
        self.defaultConfigOT2D        = self.defaultFilesOTConfigPath + 'defaultOT2D.cfg'

#__________________________________________________
