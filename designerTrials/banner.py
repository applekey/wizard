# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Sun Jun 29 22:55:56 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from constants import *

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


class banner(QtGui.QWidget):
    def __init__(self, parentForm):
        super( banner, self ).__init__()
        ## create our own widget, the resizing and such will be done one this
        self.centralwidget = QtGui.QWidget(parentForm)
        self.formWidth =  parentForm.size().width()
        ## specify some min, max boundaries, I am not allowing this to shrink in height
        ## and become smaller than a certain number
        self.tabNumber = 3
        self.tabText = ['abc','edg','hgi']
        
        self.__setupUi(self.centralwidget)
       
        
        
       
    
    #configure the number of tabs, and also the text in each tab
    def configure(numberOfTabs,tabTextArray):
        self.tabNumber = numberOfTabs
        self.tabText = tabTextArray

    def setGeometry(self, int1, int2, int3, int4):
        self.centralwidget.setGeometry(int1, int2, int3, int4)
    
    def setGeometry(self, qrect):
        self.centralwidget.setGeometry(qrect)
    
    def __setupUi(self, parentForm):   
        # get the parent form's size
      
        self.centralwidget.setGeometry(0, 0, self.formWidth, bannerHeightPixels)

        self.ribbonButtons = []
        
        currentDrawPosition = 0
        secondaryButtonWidths =  (self.formWidth - self.formWidth*firstButtonWidthPercentage)/float(self.tabNumber-1)
        
        for i in range(self.tabNumber):
            if i is 0:
                currentButtonWidth = self.formWidth*firstButtonWidthPercentage
            else:
                currentButtonWidth = secondaryButtonWidths
            
            newButton = QtGui.QPushButton(self.centralwidget)
            newButton.setGeometry(currentDrawPosition,0,currentButtonWidth,bannerHeightPixels)
            
            #style and look
            newButton.setStyleSheet("Text-align:left;border: none;background:rgb(200,100,150);")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            #icon
            newButton.setIcon(icon)
            newButton.setIconSize(QtCore.QSize(iconWidth, bannerHeightPixels))

            self.ribbonButtons.append(newButton)

            currentDrawPosition += currentButtonWidth


           

        
        QtCore.QMetaObject.connectSlotsByName(parentForm)

  



