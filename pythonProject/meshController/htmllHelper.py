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
        self.isInitialized=False
        self.meshWrapper = MeshWrapper()

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
    def show(self):
         
         if not self.isInitialized:
             self.lazyLoad()
             self.isInitialized=True
         super(htmlHelper, self).show()

    def lazyLoad(self):

        QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)
        factory = WebPluginFactory(self)

        self.webView = QWebView(self)
        self.frame = self.webView.page().mainFrame()

        self.webView.settings().setAttribute(QWebSettings.PluginsEnabled, True)
        self.webView.page().setPluginFactory(factory)
        self.webView.setHtml(self.htmlText,self.baseUrl)
        
        
        self.frame.addToJavaScriptWindowObject('htmlHelper', self)
       
       
        self.setupUi()
    
    def setHtml(self,htmlPage):  
        self.htmlPage = resource_path(htmlPage)
        self.baseUrl = QtCore.QUrl.fromLocalFile(self.htmlPage)
        htmlText = self.getText(self.htmlPage)
        self.htmlText =htmlText
       

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
                   if eval('method.'+functionCall) is not True:
                       self.warnEvent()
        except:
            self.warnEvent()

#---------------------------------------------------------------------------------------------------------------------

    @pyqtSlot()
    def selectNewPart(self):
        objects = MeshWrapper.selectNewPart() 
            
    @pyqtSlot()
    def loadLatest(self):
        if MeshWrapper.loadLatest() is not True:
            self.warnEvent()

    @pyqtSlot()
    def saveLatest(self):
        if MeshWrapper.saveLatest() is not True:
            self.warnEvent()

    @pyqtSlot()
    def seperate(self):
        if MeshWrapper.seperate() is not True:
            self.warnEvent()


    @pyqtSlot()
    def expandToConnected(self):
        if MeshWrapper.expandToConnected() is not True:
            self.warnEvent()

    @pyqtSlot()
    def invert(self):
        if MeshWrapper.invertSelection() is not True:
            self.warnEvent()

    @pyqtSlot()
    def planecut(self):
        if MeshWrapper.planecut() is not True:
            self.warnEvent()

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
    def inspectorAutoRepair(self):
        if MeshWrapper.repairAll() is not True:
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
        fileName= str(tkFileDialog.askopenfilename(parent=root,filetypes=[("3d Files","*.ply;*.obj")]))
        if fileName is not '':
            state =  MeshWrapper.importFigure(fileName) 
            if state is not True:
                self.warnEvent()

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
        if MeshWrapper.deformsmooth(value) is not True:
            self.warnEvent()
  
    @pyqtSlot(float)
    def scaleDeform(self,value):  

        if MeshWrapper.deformsmooth(value) is not True:
             self.warnEvent()

    @pyqtSlot(float)
    def offset(self,value):      
        if MeshWrapper.editoffset(value) is not True:
            self.warnEvent()
 
 
