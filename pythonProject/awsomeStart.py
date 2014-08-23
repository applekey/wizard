# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'awsomeNavigation.ui'
#
# Created: Sun Jul 06 18:19:50 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

import sys
import atexit
## append all project paths
sys.path.append( 'componentConfiguration' )
sys.path.append( 'contentPage' )
sys.path.append( 'uiLib' )
sys.path.append( 'imageFiles' )
sys.path.append( 'settingSaver' )
sys.path.append( 'extensionController' )
sys.path.append( 'meshController' )
sys.path.append( 'meshController/implementation' )
sys.path.append( 'meshController/pythonApi' )


from PyQt4 import QtCore, QtGui
from pageFactory import pageFactory
from awsomeNavigation import awsomeNavigation
from extensionController import *
from MeshWrapper import *

from resourceFile import *
from PyQt4 import QtSvg,QtXml

import inspect

#from resourceFile import *


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

class Ui_MainWindow(QtGui.QMainWindow):

    def __init__(self):
        self.oldPosition = QtCore.QPoint(0,0)
        super( Ui_MainWindow, self ).__init__()
        self.setupUi()
        self.centerOnScreen()

    def centerOnScreen (self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.setGeometry(10,30,resolution.width()/2.8, resolution.height()*0.9)

    #def mousePressEvent(self,mouseEvent):
    #    self.oldPosition = mouseEvent.globalPos()
    #    print mouseEvent.pos()

    #def mouseMoveEvent(self,mouseEvent):
    #    delta = mouseEvent.globalPos()- self.oldPosition
    #    self.move(self.pos().x()+delta.x(),self.pos().y()+delta.y())
    #    self.oldPosition = mouseEvent.globalPos()

    def onResize(self,event):
        width= event.size().width()
        height= event.size().height()
        newSize = QtCore.QRect(0,0,width,height)
        self.awsomeNavigation.setGeometry(newSize)
    
    def appendPageTupple(self,pages,sectionIndex):
        newPageList = []
        for x in range(0,len(pages)): 
            newPageList.append((sectionIndex,pages[x]))
        return newPageList

    def setupUi(self):
        ### get all extensions
       
       
        extensions = extensionController.getExtensions('extensions')
     
         
        self.awsomeNavigation = awsomeNavigation(self)
        self.pageFactory = pageFactory(self.awsomeNavigation.returnParent())
        
        jsonFile = "htmlPages//pageConfiguration.json"
        sections= self.pageFactory.getPageData(jsonFile)
        for x in range(0,len(sections)):
              self.awsomeNavigation.addSection("abc")
              pagesData = sections[x]
              pages = self.pageFactory.createPages(pagesData,self.awsomeNavigation,extensions)
              pages = self.appendPageTupple(pages,x)
              self.awsomeNavigation.addPages(pages)
             
       
     
        self.awsomeNavigation.renderPages()
        
        
        self.resizeEvent  = self.onResize
        height = 800
        width = 800
        newSize = QtCore.QSize(width,height)
        self.resize(newSize)
 

       


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    MainWindow.show()
    sys.exit(app.exec_())

   

