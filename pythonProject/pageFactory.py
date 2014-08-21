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
from htmllHelper import *
from commonFunctions  import *

import json

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

class pageFactory():
    def __init__(self,parentWidget):
        self.parentWidget = parentWidget
        
        self.__mainKey = "pageSetup"
        self.__sectionKey = "section"
        self.__pageRootKey = "pageRoot"
    def getPageData(self,dataLocation):

        if not os.path.isfile(resource_path(dataLocation)):
            print dataLocation + "missing json file"
         
        print dataLocation
        json_data=open(resource_path(dataLocation)).read()
        pageConfiguration = json.loads(json_data)

        self.pageRoot = pageConfiguration[self.__pageRootKey]
        return pageConfiguration[self.__mainKey]

    def createPages(self,sections):
      
        self.pagesToAdd = []
        pageSections = sections[self.__sectionKey]
        for y in range(0,len(pageSections)):
            entry= dict(pageSections[y])
            for keys,values in entry.items():
                if str(keys) == "page":
                    page = htmlHelper(self.parentWidget)
                    page.setHtml(self.pageRoot+"\\"+values)
                    self.pagesToAdd.append(page)


        ### create and modify the widgets here
        #controlWidget = demoPage
        #self.page1Widget = layoutWidget(self.parentWidget,controlWidget)
        #self.page1Widget.setText("1")
        #self.page1Widget.setVideoSource(resource_path("imageFiles\\video\\abc.mov"))


        #self.endPage = demoEndPage(self.parentWidget)

        ### add all the widgets to pages to add
        #self.pagesToAdd.append( self.page1Widget);
        #self.pagesToAdd.append( self.endPage);
         


        return self.pagesToAdd