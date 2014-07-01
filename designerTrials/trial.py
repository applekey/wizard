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

  
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        
        self.height = 600
        self.width = 800


        MainWindow.resize(self.width, self.height)
        self.size = QtCore.QRect(0, 0, self.width, self.height)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #self.custom = kitKatButton(MainWindow)
        #self.custom.setGeometry(200,0,400,100)
        #self.custom.setText('abc')
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.custom.setIcon(icon)
        
      

        #self.mytest = banner(MainWindow)
        #self.mytest.configure(3,['abc','edg','fdfd'],['#2980b9','#e67e22','#95a5a6'])
       
        self.player = awsomePlayer(MainWindow)
        self.player.setSource("C:\\abc.mov")

   

   


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

