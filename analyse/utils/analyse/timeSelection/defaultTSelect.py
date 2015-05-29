#__________________
# defaultTSelect.py
#__________________

#__________________________________________________

def selectLastT(Nt):
    return Nt-1

#__________________________________________________

def selectFirstT(Nt):
    return 0

#__________________________________________________

def makeSelectXtimesNt(x):
    def selectXtimesNt(Nt):
        return min(int(Nt*x), Nt-1)
    return selectXtimesNt

#__________________________________________________
