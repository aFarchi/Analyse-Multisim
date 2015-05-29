#________________________
# defaultConfiguration.py
#________________________

from ..io.read      import readLines
from ..types.cast   import castString
from ..types.string import catListOfString

#__________________________________________________

class DefaultConfiguration(object):

    def __init__(self, configFile=None):
        self.defaultAttributes()
        self.initListsAndDicts()
        self.fromfile(configFile)
        self.checkAttributes()

    #_________________________

    def __repr__(self):
        return 'DefaultConfiguration class'
        
    #_________________________

    def replaceByDefaultValue(self, attr):
        self.__setattr__(attr, self.defaultValues[attr])
        if self.printWarning[attr]:
            print('No valid element found for '+attr)
            print('Replaced by default value : ')
            print(self.defaultValues[attr])

    #_________________________

    def checkAttribute(self, attr):
        if self.attributeType[attr] == 'dict':
            if self.__getattribute__(attr) == {}:
                self.replaceByDefaultValue(attr)
        elif self.attributeType[attr] == 'list':
            if self.__getattribute__(attr) == []:
                self.replaceByDefaultValue(attr)
        else:
            if not self.__dict__.has_key(attr):
                self.replaceByDefaultValue(attr)
    
    #_________________________

    def checkAttributes(self):
        for attr in self.attributes:
            if self.isSubAttribute[attr] == []:
                self.checkAttribute(attr)

        for attr in self.attributes:
            if len(self.isSubAttribute[attr]) > 0:
                parentAttributesCompatible = True
                for (parentAttr, parentValue) in self.isSubAttribute[attr]:
                    if not self.__getattribute__(parentAttr) == parentValue:
                        parentAttributesCompatible = False
                        break
                if parentAttributesCompatible:
                    self.checkAttribute(attr)

    #_________________________

    def fromfile(self, fileName):
        lines = readLines(fileName, strip=True, removeBlancks=True, commentChar='#', includeEmptyLines=False)

        for line in lines:
            try:
                members   = line.split('=')
                attrName  = members.pop(0)
                attrValue = catListOfString(members)

                if not attrValue == '' and attrName in self.attributes:
                    
                    if self.attributeType[attrName] == 'dict':
                        members = attrValue.split(':')
                        key     = members.pop(0)
                        if '&None&' in catListOfString(members):
                            value = None
                        else:
                            value = castString(members.pop(0), catListOfString(members))
                        self.__getattribute__(attrName)[key] = value

                    elif self.attributeType[attrName] == 'list':
                        members = attrValue.split(':')
                        self.__getattribute__(attrName).append(castString(members.pop(0), catListOfString(members)))

                    else:
                        self.__setattr__(attrName, castString(self.attributeType[attrName], attrValue))
            except:
                print('Could not read line :'+line)

    #_________________________

    def initListsAndDicts(self):
        for attr in self.attributes:
            if self.attributeType[attr] == 'list':                
                self.__setattr__(attr, [])
            elif self.attributeType[attr] == 'dict':
                self.__setattr__(attr, {})

    #_________________________

    def defaultAttributes(self):
        self.attributes     = []
        self.defaultValues  = {}
        self.isSubAttribute = {}
        self.attributeType  = {}
        self.printWarning   = {}

    #_________________________

    def addAttribute(self, attrName, defaultVal=None, isSubAttr=[], attrType='str', printWarning=True):
        self.attributes.append(attrName)
        self.defaultValues[attrName]  = defaultVal
        self.isSubAttribute[attrName] = isSubAttr
        self.attributeType[attrName]  = attrType
        self.printWarning[attrName]   = printWarning

#__________________________________________________
