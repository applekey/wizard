#
# Created: Sun Jul 06 18:19:50 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

import sys,os

from PyQt4 import QtCore, QtGui
from layoutWidget import layoutWidget
from patientInfoPage import patientInfo
from awsomeSlider import awsomeSlider
from demoPage import demoPage
from demoEndPage import demoEndPage
from allControl import *

import json

jsonFile = "C:\\Users\\applekey2\\Documents\\wizard\\pythonProject\\pageConfiguration.json"


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

class pageFactory():
    def __init__(self,parentWidget):
        self.parentWidget = parentWidget
        self.pagesToAdd = []
        self.__mainKey = "pageSetup"
        self.__sectionKey = "section"
        self.__pageRootKey = "pageRoot"

    def createWidgets(self):
        json_data=open(jsonFile).read()
        pageConfiguration = json.loads(json_data)

        pageRoot = pageConfiguration[self.__pageRootKey]

        for x in range(0,len(pageConfiguration[self.__mainKey])):
            sections = pageConfiguration[self.__mainKey][x][self.__sectionKey]
            for y in range(0,len(sections)):
                entry= dict(sections[y])
                for keys,values in entry.items():
                    if str(keys) == "page":
                        page = HTMLHelper(self.parentWidget)
                        page.setHtml(pageRoot+"\\"+values)
                        self.pagesToAdd.append(page)






        fileLocation = "C:\\Users\\applekey2\\Documents\\wizard\\htmlControls\\controls.html"
      
        self.introPage =HTMLHelper(self.parentWidget)
        self.introPage.setHtml(fileLocation)

        ## create and modify the widgets here
        controlWidget = demoPage
        self.page1Widget = layoutWidget(self.parentWidget,controlWidget)
        self.page1Widget.setText("1")
        self.page1Widget.setVideoSource(resource_path("imageFiles\\video\\abc.mov"))


        self.endPage = demoEndPage(self.parentWidget)

        ## add all the widgets to pages to add
        self.pagesToAdd.append( self.introPage);
        self.pagesToAdd.append( self.page1Widget);
        self.pagesToAdd.append( self.endPage);
         


        return self.pagesToAdd