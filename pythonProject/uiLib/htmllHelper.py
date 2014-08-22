import sys,os
from PyQt4.QtCore import QObject, pyqtSlot
from PyQt4.QtGui import QApplication, QApplication, QCursor
from PyQt4.QtWebKit import QWebView
from PyQt4.QtWebKit import *
from extensionController import *
import threading
from commonFunctions import *

from PyQt4 import QtCore, QtGui

from Tkinter import *
import tkFileDialog
from urllib import urlopen
from basePage import *

import htmlConfiguration
from MeshWrapper import *

class cd:
    def dosmth(self):
        QApplication.setOverrideCursor(QCursor(QtCore.Qt.WaitCursor))
        MeshWrapper.deformsmooth(value)
        QApplication.restoreOverrideCursor()

class htmlHelper(QtGui.QWidget,basePage):

    def pageChangeEvent(self):
         self.frame.evaluateJavaScript('''
    try {
        onPageSwitch()
    }
    catch(err) {
        
    }

''')

    def onResize(self,event):
        width= event.size().width()
        height= event.size().height()
        newSize = QtCore.QRect(0,0,width,height)
        self.verticalLayout.setGeometry(newSize)
    def __init__(self, parent,navigationController):
        super(htmlHelper, self).__init__(parent)
        self.navigationController = navigationController
    def getText(self,location):
        isFile = os.path.isfile(location)
        if(isFile):
            with open(location, 'r') as f:
                webpage = f.read().decode('utf-8')

            return webpage
        else:
            print 'cant find page'
            print location
            return ""
    def setHtml(self,htmlPage):  
        print 'abs path is' + htmlPage
        htmlPage = resource_path(htmlPage)
        baseUrl = QtCore.QUrl.fromLocalFile(htmlPage)
        htmlText = self.getText(htmlPage)

        self.webView = QWebView()
        self.frame = self.webView.page().mainFrame()
        self.webView.setHtml(htmlText,baseUrl)
      

        self.webView.settings().setAttribute(QWebSettings.PluginsEnabled, True)
        self.frame.addToJavaScriptWindowObject('htmlHelper', self)
       
       
        self.setupUi()

    def setupUi(self):
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.addWidget(self.webView)
   
    def callcDynamic(self,string):
        pass

    @pyqtSlot('QString')
    def extensionFunction(self,value):
        print value
        self.callcDynamic(value)

    @pyqtSlot()
    def interact(self): 
        pass
        local=locals()  
        sh = Shell(local)
        sh.interact( )
    
    @pyqtSlot(int)
    def switchPage(self,value): 
        self.navigationController.changePage(value)
    
    @pyqtSlot()
    def selectAll(self): 
       MeshWrapper.selectAll()
    
    @pyqtSlot()
    def importScan(self):   
        root = Tk()
        root.withdraw()
        fileName= str(tkFileDialog.askopenfilename(parent=root))
        if fileName is not '':
            MeshWrapper.importFigure(fileName);

    ##sliders
    @pyqtSlot(float)
    def remesh(self,value):  
        MeshWrapper.remesh(value)
    
    @pyqtSlot()
    def discard(self):  
        MeshWrapper.editDiscard()
    
    @pyqtSlot(float)
    def smoothDeform(self,value):   
        
        ef = cd()
        tasks = [ef.dosmth]
        for task in tasks:
            t = threading.Thread(target=task, args=())
            t.start()
  
    @pyqtSlot(float)
    def scaleDeform(self,value):  

        MeshWrapper.deformsmooth(value)

    @pyqtSlot(float)
    def offset(self,value):      
        MeshWrapper.editoffset(value)
 
 
