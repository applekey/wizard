# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Sun Jun 29 22:55:56 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from constants import *
from kitkatButton import *

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


class banner(QtGui.QFrame):

    def calculateBannerHeight(self,width):
        #return bannerHeightAbsolute
        #return bannerHeightPixelsPercentage *self.bannerWidth
        return self.size().height()
    def __init__(self, parentForm):
        super( banner, self ).__init__()
        self.bannerWidth =  self.size().width()
        self.bannerHeight = self.calculateBannerHeight(self.bannerWidth)
        ## specify some min, max boundaries, I am not allowing this to shrink in height
        ## and become smaller than a certain number
        self.tabNumber = 3
        self.tabText = ['abc','edg','hgi']
        self.colorArray = ['#2980b9','#e67e22','#95a5a6']
        self.__setupUi(self)
        self.currentTabExpanded = 0
        self.resizeEvent = self.__resizeGeometry
       
    #configure the number of tabs, and also the text in each tab
    def configure(self,numberOfTabs,tabTextArray,colorArray):
        self.tabNumber = numberOfTabs
        self.tabText = tabTextArray
        self.colorArray = colorArray
        # there is a bug here, the tabs will not change, fix later

    def __resizeGeometry(self,event):
        self.bannerWidth =  self.size().width()
        self.modifyTabGeometry(self.currentTabExpanded)
    
    def buttonClicked(self):
        button = self.sender()
        
        buttonNumber = int( button.objectName())
        # handle firstButton
        if buttonNumber is self.currentTabExpanded:
            pass #ignore for now
        else:
            self.modifyTabGeometry(buttonNumber)
        
    def modifyTabGeometry(self,tabToExpand):
        secondaryButtonWidths =  (self.bannerWidth - self.bannerWidth*firstButtonWidthPercentage)/float(self.tabNumber-1)
        self.currentTabExpanded = tabToExpand
        currentDrawPosition = 0
        for i in range(self.tabNumber):
            currentColor = self.colorArray[i]
            if i is 0:
                styleSheetText = "Text-align:left;border: none;background:"+currentColor+";"
            else:
                 print self.bannerHeight
                 radiuxPx =  self.bannerHeight *bannerCurvaturePercentage
                 styleSheetText = "border-radius:"+ str(radiuxPx)+"px;"+"Text-align:left;border: none;background:"+currentColor+";"
            self.ribbonButtons[i].setStyleSheet(styleSheetText)

            if i is tabToExpand:
                currentButtonWidth = self.bannerWidth*firstButtonWidthPercentage
            else:
                currentButtonWidth = secondaryButtonWidths
            self.ribbonButtons[i].setGeometry(currentDrawPosition,0,currentButtonWidth+200,self.bannerHeight)
            
            currentDrawPosition += currentButtonWidth
        
    def __setupUi(self, parentForm):   
        #create the font
        fontDatabase = QtGui.QFontDatabase()
        font = fontDatabase.addApplicationFont(fontFile)
        #text color
        #palette = QtGui.QPalette()
        #palette.setColor("#e74c3c")
        #self.pushButton.setPalette(palette)

        self.ribbonButtons = []
        # create the buttons
        for i in range(self.tabNumber):
            newButton = kitKatButton(parentForm)
            newButton.setObjectName(str(i))

            #style and look
            currentColor = self.colorArray[i]
            if i is 0:
                styleSheetText = "Text-align:left;border: none;background:"+currentColor+";"
            else:
                 radiuxPx =  self.bannerHeight *bannerCurvaturePercentage
                 styleSheetText = "border-radius:"+ str(radiuxPx)+"px;"+"Text-align:left;border: none;background:"+currentColor+";"
            newButton.setStyleSheet(styleSheetText)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            
            #icon
            newButton.setIcon(icon)
            #newButton.setIconSize(QtCore.QSize(iconWidth, self.bannerHeight))
            #newButton.setIconPosition(QtCore.QPoint(50,self.calculateBannerHeight(self.size().width())/float(10)))
            #text
            paddedText = '   '+self.tabText[i]
            newButton.setText(paddedText)
            newButton.setFont(QtGui.QFont(fontName, fontSize))

            #link for click signal
            QtCore.QObject.connect(newButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClicked)

            self.ribbonButtons.append(newButton)
        self.modifyTabGeometry(1)
        
        QtCore.QMetaObject.connectSlotsByName(parentForm)


  



         