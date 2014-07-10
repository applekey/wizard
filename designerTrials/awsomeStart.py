# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'awsomeNavigation.ui'
#
# Created: Sun Jul 06 18:19:50 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from awsomeNavigation import awsomeNavigation
from pageFactory import pageFactory

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
        super( Ui_MainWindow, self ).__init__()
        self.setupUi()

    def mousePressEvent(self,mouseEvent):
        self.oldPosition = mouseEvent.globalPos()

    def mouseMoveEvent(self,mouseEvent):
        delta = mouseEvent.globalPos()- self.oldPosition
        self.move(self.pos().x()+delta.x(),self.pos().y()+delta.y())
        self.oldPosition = mouseEvent.globalPos()

    def onResize(self,event):
        width= event.size().width()
        height= event.size().height()
        newSize = QtCore.QRect(0,0,width,height)
        self.awsomeNavigation.setGeometry(newSize)
 
    def setupUi(self):
        self.awsomeNavigation = awsomeNavigation(self)
        self.pageFactory = pageFactory(self.awsomeNavigation.returnParent())
        pages= self.pageFactory.createWidgets()
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

   

