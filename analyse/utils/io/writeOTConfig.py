#__________________
# writeLaunchers.py
#__________________

from read                import readLinesNoFilter
from readDefaultFiles    import readDefaultConfigOT2D
from readDefaultFiles    import readDefaultConfigPlotOT2D
from write               import writeLinesFillingWithArgs

#__________________________________________________

def writeDefaultConfigOT2D(fileName, args):
    writeLinesFillingWithArgs(readDefaultConfigOT2D(), fileName, args)

#__________________________________________________

def writeDefaultPlottingConfigOT2D(fileName, args, plottingParametersFile):
    writeLinesFillingWithArgs(readDefaultConfigPlotOT2D(), fileName, args)
    lines = readLinesNoFilter(plottingParametersFile)
    try:
        f     = open(fileName, 'a')
        for line in lines:
            f.write(line)
        f.close()
    except:
        print('Could not write file : '+fileName)

#__________________________________________________
