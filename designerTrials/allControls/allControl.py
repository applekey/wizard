import sys,os
from PyQt4.QtCore import QObject, pyqtSlot
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebView

from PyQt4 import QtCore, QtGui

from Tkinter import *
import tkFileDialog
from urllib import urlopen

import htmlConfiguration

sys.path.append( 'meshController' )
from MeshWrapper import *

class HTMLHelper(QtGui.QWidget):
    def onResize(self,event):
        width= event.size().width()
        height= event.size().height()
        newSize = QtCore.QRect(0,0,width,height)
        self.verticalLayout.setGeometry(newSize)
    def __init__(self, parent=None):
        super(HTMLHelper, self).__init__(parent)
    
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
        self.webView = QWebView()
        self.frame = self.webView.page().mainFrame()
        self.webView.setHtml(htmlText)
        self.frame.addToJavaScriptWindowObject('htmlHelper', self)
        self.setupUi()

    def setupUi(self):
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.addWidget(self.webView)
    @pyqtSlot()
    def importClick(self):   
        root = Tk()
        root.withdraw()
        fileName= str(tkFileDialog.askopenfilename(parent=root))
        if fileName is not '':
            MeshWrapper.importFigure(fileName);
    @pyqtSlot()
    def remesh(self):   
        MeshWrapper.remesh()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileLocation = "C:\\Users\\applekey2\\Documents\\wizard\\htmlControls\\controls.html"

    with open(fileLocation, 'r') as f:
        webpage = f.read().decode('utf-8')
  
    helper = HTMLHelper()
    helper.setHtml(webpage)
    
   
    
    app.exec_()