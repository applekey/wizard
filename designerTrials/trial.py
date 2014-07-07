# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trial.ui'
#
# Created: Fri Jun 27 14:27:32 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from banner import banner
from kitkatButton import kitKatButton
from awsomePlayer import awsomePlayer
from layoutWidget import layoutWidget


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

class Ui_MainWindow(object):
    def onResize(self,event):
        width= self.MainWindow.size().width()
        height= self.MainWindow.size().height()
        newSize = QtCore.QRect(0,0,width,height)
        self.centralwidget.setGeometry(newSize)
        #self.player.setGeometry(newSize)
    
    def setupUi(self, MainWindow):
       
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName(_fromUtf8("MainWindow"))
        
        self.height = 800
        self.width = 800


        self.MainWindow.resize(self.width, self.height)
        self.size = QtCore.QRect(0, 0, self.width, self.height)

        self.centralwidget = QtGui.QWidget(self.MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.centralwidget.setGeometry(self.size)
       

        #self.custom = kitKatButton(MainWindow)
        #self.custom.setGeometry(200,0,400,100)
        #self.custom.setText('abc')
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.custom.setIcon(icon)
        #self.mytest = banner(self.centralwidget)
       
        self.player = awsomePlayer(self.centralwidget)
        self.player.setSource("C:\\abc.mov")
        self.player.setGeometry(self.size)

        #self.widget = layoutWidget(self.centralwidget)
        #newSize = QtCore.QRect(0,0,self.width,self.height)
        #self.widget.setGeometry(newSize)
        #self.widget.hide()
        self.MainWindow.resizeEvent  = self.onResize


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

