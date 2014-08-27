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
from WebPluginFactory import *

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
    def warnEvent(self):
        self.frame.evaluateJavaScript('''
        try {
            onWarnEvent()
        }
        catch(err) {
        
        }
        ''')
   

    def onResize(self,event):
        width= event.size().width()
        height= event.size().height()
        newSize = QtCore.QRect(0,0,width,height)
        self.verticalLayout.setGeometry(newSize)
    def __init__(self, parent,navigationController,extensionMethods):
        super(htmlHelper, self).__init__(parent)
        self.navigationController = navigationController
        self.extensionMethods = extensionMethods
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

        QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)
        factory = WebPluginFactory(self)
        
       

        print 'abs path is' + htmlPage
        htmlPage = resource_path(htmlPage)
        baseUrl = QtCore.QUrl.fromLocalFile(htmlPage)
        htmlText = self.getText(htmlPage)

        self.webView = QWebView()
        self.frame = self.webView.page().mainFrame()

        self.webView.settings().setAttribute(QWebSettings.PluginsEnabled, True)
        self.webView.page().setPluginFactory(factory)
        self.webView.setHtml(htmlText,baseUrl)
        self.frame.addToJavaScriptWindowObject('htmlHelper', self)
       
       
        self.setupUi()

    def setupUi(self):
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.addWidget(self.webView)
   
    def callDynamic(self,functionCall):
        try:
           index = functionCall.index('(')
           functionName = functionCall[0:index]
           for method in self.extensionMethods:
               if hasattr(method, functionName):
                   eval('method.'+functionCall)
        except:
            warnEvent()

#---------------------------------------------------------------------------------------------------------------------
    @pyqtSlot()
    def cancel(self):
        if MeshWrapper.cancel() is not True:
            self.warnEvent()
    @pyqtSlot()
    def complete(self):
        if MeshWrapper.complete() is not True:
            self.warnEvent()
    @pyqtSlot('QString')
    def extensionFunction(self,value):
        print value
        self.callDynamic(str(value))
     
    @pyqtSlot()
    def smoothBoundary(self):
        if MeshWrapper.smoothBoundary() is not True:
            self.warnEvent()  

    @pyqtSlot()
    def createFaceGroup(self):
        if MeshWrapper.createFaceGroup() is not True:
            self.warnEvent()  
    
    @pyqtSlot()
    def align(self):
        if MeshWrapper.align() is not True:
            self.warnEvent()  

    @pyqtSlot()
    def inspector(self):
        if MeshWrapper.inspector() is not True:
            self.warnEvent()  

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
        if MeshWrapper.selectAll() is not True:
            self.warnEvent()
       
    
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
        if MeshWrapper.remesh(value) is not True:
            self.warnEvent()
    
    @pyqtSlot()
    def discard(self):  
        if MeshWrapper.editDiscard() is not True:
             self.warnEvent()

    @pyqtSlot(float)
    def smoothDeform(self,value):   
        #self.warnEvent()
        if MeshWrapper.deformsmooth(value) is not True:
            self.warnEvent()
   
       
        #task = {lambda x: MeshWrapper.deformsmooth(x)}
       
        #t = threading.Thread(target=task, args=([value]))
        #t.start()
        #t.join()
        #self.warnEventEnd()
  
    @pyqtSlot(float)
    def scaleDeform(self,value):  

        if MeshWrapper.deformsmooth(value) is not True:
             self.warnEvent()

    @pyqtSlot(float)
    def offset(self,value):      
        if MeshWrapper.editoffset(value) is not True:
            self.warnEvent()
 
 
