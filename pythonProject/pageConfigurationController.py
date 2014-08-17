import json

jsonFile = "C:\\Users\\applekey2\\Documents\\wizard\\pythonProject\\pageConfiguration.json"

class pageConfigurationController:
    __mainKey = "pageSetup"
    __sectionKey = "section"

   
    def loadPages(self,pageConfigurationLocation):
        json_data=open(pageConfigurationLocation).read()
        pageConfiguration = json.loads(json_data)
        abc = pageConfiguration[self.__mainKey]
        
        ef = len(abc[0])
        for x in range(0,len(pageConfiguration[self.__mainKey])):
            sections = pageConfiguration[self.__mainKey][x][self.__sectionKey]
            for y in range(0,len(sections)):
              print sections[y]
          
        


abc = pageConfigurationController()
data = abc.loadPages(jsonFile)
abc = 3

