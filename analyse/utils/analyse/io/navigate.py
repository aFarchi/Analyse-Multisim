#____________
# navigate.py
#____________

#__________________________________________________

def LinOrLog():
    return ['lin', 'log']

#__________________________________________________

def AirOrGround():
    return ['air/', 'ground/']

#__________________________________________________

def GazOrRadios():
    return ['gaz', 'radios']

#__________________________________________________

def DryOrWet(AOG):
    if 'air' in AOG:
        return ['']
    elif 'ground' in AOG:
        return ['dry/','wet/']
    else:
        return []

#__________________________________________________

def InCloudOrBelowCould(AOG, GOR):
    IOB                 = {}
    if 'air' in AOG:
        IOB['']         = ['']
    elif 'ground' in AOG:
        IOB['dry/']     = ['']
        if 'gaz' in GOR:
            IOB['wet/'] = ['']
        elif 'radios' in GOR:
            IOB['wet/'] = ['InCloud/', 'BelowCloud/']
    else:
        IOB['']         = ['']

    return IOB

#__________________________________________________
