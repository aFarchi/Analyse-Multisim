#_________________
# writeOTConfig.py
#_________________

from readDefaultFiles    import readDefaultConfigOT2D
from readDefaultFiles    import readDefaultConfigPlotOT2D
from write               import writeLinesFillingWithArgs
from write               import appendFileToFile

#__________________________________________________

def writeDefaultConfigOT2D(fileName, args, algorithmParametersFile):
    writeLinesFillingWithArgs(readDefaultConfigOT2D(), fileName, args)
    appendFileToFile(algorithmParametersFile, fileName)

#__________________________________________________

def writeDefaultPlottingConfigOT2D(fileName, args, plottingParametersFile):
    writeLinesFillingWithArgs(readDefaultConfigPlotOT2D(), fileName, args)
    appendFileToFile(plottingParametersFile, fileName)

#__________________________________________________

def writeDefaultPlottingConfigOT2DAllConfig(fileName, args, outputDirList, labelList, plottingParametersFile):
    try:
        f = open(fileName, 'w')
        for line in lines:
            if '$outputDir$' in line:
                for outputDir in outputDirList:
                    f.write(line.replace('$outputDir$', outputDir))
            elif '$label$' in line:
                for label in labelList:
                    f.write(line.replace('$label$', label))
            else:
                for arg in args:
                    line = line.replace(arg, args[arg])
                f.write(line)
            f.close()
    except:
        print('Could not write file : '+fileName)

    appendFileToFile(plottingParametersFile, fileName)

#__________________________________________________
