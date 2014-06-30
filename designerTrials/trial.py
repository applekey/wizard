# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trial.ui'
#
# Created: Fri Jun 27 14:27:32 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from banner import banner


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

    def firstButtonClicked(self):
       print 'here'
        
    def secondButtonClicked(self):
        mainWindowSize = self.size
        
        buttonSize = self.pushButton_2.geometry()

        newX = 0.13*mainWindowSize.width()
        width = mainWindowSize.width() - newX;
        resizeButton = QtCore.QRect(newX, buttonSize.y(), width, buttonSize.height())

        self.pushButton_2.setGeometry(resizeButton)
    

    def thirdButtonClicked(self):
        pass
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        
        self.height = 600
        self.width = 800


        MainWindow.resize(self.width, self.height)
        self.size = QtCore.QRect(0, 0, self.width, self.height)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))


        pushButton33 = QtGui.QPushButton(self.centralwidget)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 190, 800, 161))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        
        self.mytest = banner(MainWindow)
        self.mytest.configure(3,['abc','edg','fdfd'],['#2980b9','#e67e22','#95a5a6'])



        button2Width = self.width*0.12
        button2Position = self.width - button2Width
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(button2Position, 190, button2Width, 161))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
        #self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        #self.pushButton_3.setGeometry(QtCore.QRect(470, 190, 131, 161))
        #self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.firstButtonClicked)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.secondButtonClicked)
        #QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.thirdButtonClicked)
        
       
        
        QtCore.QMetaObject.connectSlotsByName(self.centralwidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        
        fontDatabase = QtGui.QFontDatabase()
        font = fontDatabase.addApplicationFont("OpenSans-Bold.ttf")
  
        self.pushButton.setText(_translate("MainWindow", "    Scanning \n    Adjusting ", None))
        
        #abc = fontDatabase.families()
        #for a in abc:
        #    print a

        
        self.pushButton.setStyleSheet("Text-align:left;border: none;background:rgb(200,100,150);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(self.width, self.width))
        abc = self.pushButton.setFont(QtGui.QFont("Open Sans", 15))
        
        palette = QtGui.QPalette()

        palette.setColor(QtGui.QPalette.ButtonText,QtCore.Qt.white)
        self.pushButton.setPalette(palette)

       


        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        #self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

