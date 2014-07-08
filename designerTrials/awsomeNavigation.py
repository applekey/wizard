# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'awsomeNavigation.ui'
#
# Created: Sun Jul 06 18:19:50 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from layoutWidget import layoutWidget
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

class awsomeNavigation(QtGui.QWidget):
    def __init__(self, parentForm):
        super( awsomeNavigation, self ).__init__(parentForm)
        self.parent = parentForm
        self.pages =[]
        self.resize(parentForm.size())
        self.size = QtCore.QRect(0, 0, self.width(), self.height())

        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
    
    def addPages(self,pages):
        self.pages =pages

    def renderPages(self):
        self.setupUi(self)

    def onResize(self,event):
        width= event.size().width()
        height= event.size().height()
        newSize = QtCore.QRect(0,0,width,height)
        self.layoutWidget.setGeometry(newSize)
        self.verticalLayout.setGeometry(newSize)
    
    def returnParent(self):
        return self.layoutWidget

    def setupUi(self,parent):

        ## the main screen and the naviagation bar lives on the verticle layout
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        ## this is where the main screen will live
        self.activePage = self.pages[0]
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.activePage.sizePolicy().hasHeightForWidth())
        self.activePage.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.activePage)
        
        ## this is where the naviagation bars will live
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        self.backButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout.addWidget(self.backButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
       
        self.fowardButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fowardButton.sizePolicy().hasHeightForWidth())
        self.fowardButton.setSizePolicy(sizePolicy)
        self.fowardButton.setObjectName(_fromUtf8("fowardButton"))
        self.horizontalLayout.addWidget(self.fowardButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        
        self.backButton.setText(_translate("Form", "back", None))
        self.fowardButton.setText(_translate("Form", "foward", None))
        self.resizeEvent  = self.onResize
     

        

   

