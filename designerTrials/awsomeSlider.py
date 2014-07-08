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
    def geometryChanged(self):
        pass
    def sizeHint(self):
        return QtCore.QSize(400,800)
    def __init__(self,parent):
         super(awsomeSlider, self).__init__( parent)
         self.setupUi()
    def setupUi(self):
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setGeometry(self.geometry())
        self.controlKnob = QtGui.QPushButton(self)
        self.controlKnob.setGeometry(self.geometry())
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.awsomeSlider.sizePolicy().hasHeightForWidth())
        self.controlKnob.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.controlKnob)
        
        
       




