#_____________
# positions.py
#_____________

#__________________________________________________

def positionsTimeTxtPbar():
    xTxt       = 0.0
    yTxt       = 0.0

    xPbarStart = 0.2
    xPbarEnd   = 0.8
    yPbar      = 0.0

    return (xTxt, yTxt, xPbarStart, xPbarEnd, yPbar)

#__________________________________________________

def figureRect(colorBar, timeTextPBar):
    xStart     = 0.0
    if colorBar:
        xEnd   = 0.85
    else:
        xEnd   = 1.0
    if timeTextPBar:
        yStart = 0.12
    else:
        yStart = 0.0
    yEnd       = 1.0

    return [xStart, yStart, xEnd, yEnd]

#__________________________________________________

def colorBarRect(timeTextPBar):
    xStart     = 0.87
    xEnd       = 0.93

    if timeTextPBar:
        yStart = 0.12
    else:
        yStart = 0.07
    yEnd       = 0.93

    return [xStart, yStart, xEnd, yEnd]

#__________________________________________________

def timeTextPBarRect():
    xStart = 0.07
    xEnd   = 0.93
    yStart = 0.04
    yEnd   = 0.10

    return [xStart, yStart, xEnd, yEnd]

#__________________________________________________
