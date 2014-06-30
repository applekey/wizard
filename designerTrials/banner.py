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
        self.colorArray = ['#2980b9','#e67e22','#95a5a6']
        self.__setupUi(self.centralwidget)
        self.currentTabExpanded = 0
       
    #configure the number of tabs, and also the text in each tab
    def configure(self,numberOfTabs,tabTextArray,colorArray):
        self.tabNumber = numberOfTabs
        self.tabText = tabTextArray
        self.colorArray = colorArray

    def setGeometry(self, int1, int2, int3, int4):
        self.centralwidget.setGeometry(int1, int2, int3, int4)
    
    def setGeometry(self, qrect):
        self.centralwidget.setGeometry(qrect)
    
    def buttonClicked(self):
        button = self.sender()
        
        buttonNumber = int( button.objectName())
        # handle firstButton
        if buttonNumber is self.currentTabExpanded:
            pass #ignore for now
        else:
            self.modifyTabGeometry(buttonNumber+1)
        
    def modifyTabGeometry(self,tabToExpand):
        secondaryButtonWidths =  (self.formWidth - self.formWidth*firstButtonWidthPercentage)/float(self.tabNumber-1)
        self.currentTabExpanded = tabToExpand-1
        currentDrawPosition = 0
        for i in range(self.tabNumber):
            if i is tabToExpand-1:
                currentButtonWidth = self.formWidth*firstButtonWidthPercentage
            else:
                currentButtonWidth = secondaryButtonWidths
            self.ribbonButtons[i].setGeometry(currentDrawPosition,0,currentButtonWidth,bannerHeightPixels)
            
            currentDrawPosition += currentButtonWidth
            
      
    def __setupUi(self, parentForm):   
        # get the parent form's size
      
        self.centralwidget.setGeometry(0, 0, self.formWidth, bannerHeightPixels)

        self.ribbonButtons = []
        # create the buttons
        for i in range(self.tabNumber):
            newButton = QtGui.QPushButton(self.centralwidget)
            newButton.setObjectName(str(i))
            #style and look
            currentColor = self.colorArray[i]
           
            newButton.setStyleSheet("Text-align:left;border: none;background:"+currentColor+";")

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            #icon
            newButton.setIcon(icon)
            newButton.setIconSize(QtCore.QSize(iconWidth, bannerHeightPixels))
            #text
            paddedText = '   '+self.tabText[i]
            newButton.setText(paddedText)

            #link for click signal
            QtCore.QObject.connect(newButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClicked)

            self.ribbonButtons.append(newButton)
        self.modifyTabGeometry(1)
        
        QtCore.QMetaObject.connectSlotsByName(parentForm)

  



