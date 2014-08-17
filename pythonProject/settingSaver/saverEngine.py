class Singleton(object):
  _instance = None
  def __new__(class_, *args, **kwargs):
    if not isinstance(class_._instance, class_):
        class_._instance = object.__new__(class_, *args, **kwargs)
    return class_._instance

class demoPage():

    def __init__(self):
        self.sectionName = sectionName
        self.properties = []

    def addProperty(self,group,propertyName,propertyValue):
        self.properties.append((group,propertyName,propertyValue))

    def printToList(self,saveLocation):
        saveFile = open(saveLocation,'w')
        for property in self.properties:
            saveFile.write(property[0]+""+property[1]+""+property[2]+"")
