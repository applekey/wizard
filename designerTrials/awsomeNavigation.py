# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'awsomeNavigation.ui'
#
# Created: Sun Jul 06 18:19:50 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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
        self.verticalLayout.setGeometry(newSize)
        self.whateveruwant.setGeometry(newSize)
       
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName(_fromUtf8("MainWindow"))
        
        self.height = 800
        self.width = 800

        self.MainWindow.resize(self.width, self.height)
        self.size = QtCore.QRect(0, 0, self.width, self.height)
        
        ## the main screen and the naviagation bar lives on the verticle layout
        self.verticalLayout = QtGui.QVBoxLayout(self.MainWindow)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        ## this is where the main screen will live
        self.whateveruwant = layoutWidget(self.MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.whateveruwant.sizePolicy().hasHeightForWidth())
        self.whateveruwant.setSizePolicy(sizePolicy)
        
        self.verticalLayout.addWidget(self.whateveruwant)
        
        ### this is where the naviagation bars will live
        #self.horizontalLayout = QtGui.QHBoxLayout()
        #self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        #self.pushButton = QtGui.QPushButton(MainWindow)
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        #self.pushButton.setSizePolicy(sizePolicy)
        #self.pushButton.setObjectName(_fromUtf8("pushButton"))
        #self.horizontalLayout.addWidget(self.pushButton)
        #spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        #self.horizontalLayout.addItem(spacerItem)
       
        #self.pushButton_2 = QtGui.QPushButton(MainWindow)
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        #self.pushButton_2.setSizePolicy(sizePolicy)
        #self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        #self.horizontalLayout.addWidget(self.pushButton_2)
        #self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        #self.pushButton.setText(_translate("Form", "PushButton", None))
        #self.pushButton_2.setText(_translate("Form", "PushButton", None))
        Form.resizeEvent  = self.onResize

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

   

