import sys,os
from PyQt4.QtCore import QObject, pyqtSlot
from PyQt4.QtGui import QApplication, QApplication, QCursor
from PyQt4.QtWebKit import QWebView
from PyQt4.QtWebKit import *
from extensionController import *
import threading

from PyQt4 import QtCore, QtGui

from Tkinter import *
import tkFileDialog
from urllib import urlopen

import htmlConfiguration
sys.path.append( 'meshController' )
from MeshWrapper import *

class cd:
    def dosmth(self):
        QApplication.setOverrideCursor(QCursor(QtCore.Qt.WaitCursor))
        MeshWrapper.deformsmooth(value)
        QApplication.restoreOverrideCursor()

class htmlHelper(QtGui.QWidget):
    def onResize(self,event):
        width= event.size().width()
        height= event.size().height()
        newSize = QtCore.QRect(0,0,width,height)
        self.verticalLayout.setGeometry(newSize)
    def __init__(self, parent):
        super(htmlHelper, self).__init__(parent)
    def getText(self,location):
        isFile = os.path.isfile(location)
        if(isFile):
            with open(location, 'r') as f:
                webpage = f.read().decode('utf-8')

            return webpage
        else:
            return ""
    def setHtml(self,htmlPage):  
        htmlText = self.getText(htmlPage)
        baseUrl = QtCore.QUrl.fromLocalFile(htmlPage)
        
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
    @pyqtSlot()
    def interact(self): 
        local=locals()  
        sh = Shell(local)
        sh.interact( )
    
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
    def offsetA(self,value):   
        
        MeshWrapper.editoffset(value)
 
 
