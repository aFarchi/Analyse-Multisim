#_______________________
# defaultTransparency.py
#_______________________

#__________________________________________________

def defaultTransparency(t):
    return t

#__________________________________________________

def fastVanishingTransparency(t):
    if t < 0.6:
        return 0.0
    else:
        return 1. + ( 1.0 / 0.4 ) * ( t - 1.0 )

#__________________________________________________

def customTransparency(t):
    return min(max(t, 0.25), 0.8)

#__________________________________________________

