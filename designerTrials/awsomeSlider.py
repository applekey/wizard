# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'awsomeSlider.ui'
#
# Created: Sun Jul 06 23:50:37 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class awsomeSlider(QtGui.QFrame):
    def onResize(self,event):
        width= event.size().width()
        height= event.size().height()
        newSize = QtCore.QRect(0,0,width,height)
        self.verticalLayout.setGeometry(newSize)
        #self.but.setGeometry(newSize)
    
    def sizeHint(self):
        pass
    
    def __init__(self,parent):
         super(awsomeSlider, self).__init__( parent)
         self.parent = parent
         self.resizeEvent  = self.onResize
         self.setupUi()
         

    def setupUi(self):
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        
        self.verticalLayout.addWidget(self.label_3)
        
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        self.horizontalSlider = QtGui.QSlider(self)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.label = QtGui.QLabel(self.parent)
        self.label.setText("abcd")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.parent)
        self.label_2.setText("fdsaf")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
      
        
        
       




