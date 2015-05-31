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
        self.otModulePath            = '/Users/Alban/Desktop/Optimal-Transport/'

        #_________________________

        self.defaultFilesLauncherPath = self.modulePath + 'utils/launchers/'
        self.defaultPythonLauncher    = self.defaultFilesLauncherPath + 'defaultLauncher.py'
        self.defaultBashLauncher      = self.defaultFilesLauncherPath + 'defaultLauncher.sh'
        self.defaultNodesFile         = self.defaultFilesLauncherPath + 'defaultNodes.dat'

#__________________________________________________
