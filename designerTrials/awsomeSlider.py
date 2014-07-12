# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'awsomeSlider.ui'
#
# Created: Sun Jul 06 23:50:37 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from componentConfirguration import *

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
    
    def sizeHint(self):
        return QtCore.QSize(300,80) 
    
    def __init__(self,parent):
         super(awsomeSlider, self).__init__( parent)
         self.parent = parent
         self.resizeEvent  = self.onResize
         self.setupUi()
    
    def setLabelText(controlName, unitName):
        self.label_3.setText(controlName)
        self.label_2.setText(unitName);
    
    def sliderValueChanged(self,intValue):
        self.label.setText(str(intValue))

    def setupUi(self):
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setText("Degree")
        
        self.verticalLayout.addWidget(self.label_3)
        
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        self.horizontalSlider = QtGui.QSlider(self)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalSlider.setStyleSheet(qSliderStyle)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL('valueChanged(int)'), self.sliderValueChanged)
        
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.label = QtGui.QLabel(self.parent)
        self.label.setText(str(self.horizontalSlider.value()))
        self.label.setStyleSheet(awsomeSliderNumberDisplayStyle)

        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.parent)
        self.label_2.setText("cm")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
      
        
        
       




