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

    def sizeHint(self):
        return QtCore.QSize(300,80)

    def __init__(self, parentForm):
        super( banner, self ).__init__()

        ## specify some min, max boundaries, I am not allowing this to shrink in height
        ## and become smaller than a certain number
        self.tabNumber = 3
        self.tabText = ['abc','edg','hgi']
        self.activecolorArray = ['#1ABC9C','#F1C40F','#E74C3B']
        self.inactivecolorArray = ['#A8ACAF','#99A3A3','#879191']
        self.__setupUi(self)
        self.currentTabExpanded = 0
        self.resizeEvent = self.__resizeGeometry
       
    #configure the number of tabs, and also the text in each tab
    def configure(self,numberOfTabs,tabTextArray,colorArray):
        #self.tabNumber = numberOfTabs
        #self.tabText = tabTextArray
        #self.colorArray = colorArray
        # there is a bug here, the tabs will not change, fix later
        pass

    def __resizeGeometry(self,event):
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
        width = self.size().width()
        secondaryButtonWidths =  (width - width*firstButtonWidthPercentage)/float(self.tabNumber-1)
        self.currentTabExpanded = tabToExpand
        currentDrawPosition = 0
        for i in range(self.tabNumber):
    
            if i is 0:
                styleSheetText = "text-align:left;border: none;"
            else:
                 
                 radiuxPx =  self.size().height() *bannerCurvaturePercentage
         
                 styleSheetText = "border-radius:"+ str(radiuxPx)+"px;"+"Text-align:left;border: none;"
            

            if i is tabToExpand:
                currentButtonWidth = self.size().width()*firstButtonWidthPercentage
                styleSheetText = styleSheetText+ "background:"+self.activecolorArray[i]+";"
            else:
                currentButtonWidth = secondaryButtonWidths
                styleSheetText = styleSheetText+ "background:"+self.inactivecolorArray[i]+";"
            self.ribbonButtons[i].setGeometry(currentDrawPosition,0,currentButtonWidth+200,self.size().height())
            self.ribbonButtons[i].setStyleSheet(styleSheetText)
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
            if i is 0:
                styleSheetText = "Text-align:left;border: none;background:"+self.activecolorArray[i]+";"
            else:
                 radiuxPx =  self.size().height() *bannerCurvaturePercentage
                 styleSheetText = "border-radius:"+ str(radiuxPx)+"px;"+"Text-align:left;border: none;background:"+self.inactivecolorArray[i]+";"
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


  



         