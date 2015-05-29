#________
# cast.py
#________

#__________________________________________________

def castString(toType, s):
    if toType == 'str':
        return s
    elif toType == 'float':
        try:
            return float(s)
        except:
            print('Could not cast '+s+' into float...')
            print('Replacing by 0.0')
            return 0.0
    elif toType == 'int':
        try:
            return int(s)
        except:
            print('Could not cast '+s+' into int...')
            print('Replacing by 0')
            return 0
    elif toType == 'bool':
        return ( s == 'True' )

#__________________________________________________
