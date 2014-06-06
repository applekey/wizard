import json
import time

configFileName = 'config.txt'

class config:
    __height = 0
    isValidConfig = false
    ## writting to config file options
    def saveCurrentConfig(filePath):
        __height = height
        fileName = filePath +"_" + time.strftime("%d/%m/%Y")
        f = open(fileName, 'w')
        ##file.write()  file.write("hello world in the new file\n")


    ## reading from config file options
    def __assignConfig(words):
        if words[0]== 'height':
            try:
                __height = words[1]
            except ValueError:
                print 'height error'

    def loadConfig(self):
        fine = open(configFileName,'r')
        for line in file:
            words = line.split()
            __assignConfig(words)