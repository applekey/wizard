# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Sun Jun 29 22:55:56 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from kitkatButton import *
from componentConfirguration import *
from PyQt4.QtCore import QObject, pyqtSignal

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
    ## define the signal
    bannerTriggered = QtCore.pyqtSignal(int,name='bannerTriggered')

    def sizeHint(self):
        return QtCore.QSize(300,80)

    def __init__(self, parentForm):
        
       
        super( banner, self ).__init__(parentForm)
      
        ## specify some min, max boundaries, I am not allowing this to shrink in height
        ## and become smaller than a certain number
        self.tabNumber = 3
        self.tabText = bannerText
        self.activecolorArray = activeColors
        self.inactivecolorArray = inactiveColors
        self.currentTabExpanded = 0
        self.__setupUi(self)
        
        self.resizeEvent = self.__resizeGeometry
       
    #configure the number of tabs, and also the text in each tab
    def configure(self,text,activeColorArray,inactiveColorArray,):
        self.activecolorArray
        # there is a bug here, the tabs will not change, fix later
        pass

    def __resizeGeometry(self,event):
        self.modifyTabGeometry(self.currentTabExpanded)
        for button in self.ribbonButtons:
            button.setIconSize(QtCore.QSize(bannerIconWidth,self.size().height()))
            button.setIconPosition(QtCore.QPoint(bannerIconWidth/2,9))
    
    def buttonClicked(self):
        button = self.sender()
        
        buttonNumber = int( button.objectName())
        self.bannerTriggered.emit(buttonNumber)
        # handle firstButton
        if buttonNumber is self.currentTabExpanded:
            pass #ignore for now
        else:
            self.modifyTabGeometry(buttonNumber)
        
    def modifyTabGeometry(self,tabToExpand):
        if tabToExpand is self.currentTabExpanded:
            pass

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
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path(activeIcons[i])), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ribbonButtons[i].setIcon(icon)
            else:
                currentButtonWidth = secondaryButtonWidths
                styleSheetText = styleSheetText+ "background:"+self.inactivecolorArray[i]+";"
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path(inactiveIcons[i])), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ribbonButtons[i].setIcon(icon)

            self.ribbonButtons[i].setGeometry(currentDrawPosition,0,currentButtonWidth+200,self.size().height())
            self.ribbonButtons[i].setStyleSheet(styleSheetText)
            currentDrawPosition += currentButtonWidth
        
    def __setupUi(self, parentForm):   
        #create the font
        fontDatabase = QtGui.QFontDatabase()
        font = fontDatabase.addApplicationFont(fontFile)
        #text color
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.All, QtGui.QPalette.WindowText, brush)
      


        #self.pushButton.setPalette(palette)

        self.ribbonButtons = []
        # create the buttons
        for i in range(self.tabNumber):
            newButton = kitKatButton(self)
            newButton.setObjectName(str(i))

            #style and look
            if i is 0:
                styleSheetText = "Text-align:left;border: none;background:"+self.activecolorArray[i]+";"
            else:
                 radiuxPx =  self.size().height() *bannerCurvaturePercentage
                 styleSheetText = "border-radius:"+ str(radiuxPx)+"px;"+"Text-align:left;border: none;background:"+self.inactivecolorArray[i]+";"
            newButton.setStyleSheet(styleSheetText)
            #icon
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(resource_path(inactiveIcons[i])), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            newButton.setIcon(icon)
            newButton.setIconSize(QtCore.QSize(bannerIconWidth, self.size().height()))
         

            #newButton.setIconPosition(QtCore.QPoint(50,self.calculateBannerHeight(self.size().width())/float(10)))
            #text
            paddedText = '   '+self.tabText[i]
            newButton.setText(paddedText)
            newButton.setFont(QtGui.QFont(fontName, fontSize))
            newButton.setTextPosition(QtCore.QPoint(100,50))
            newButton.setPalette(palette)
            #link for click signal
            QtCore.QObject.connect(newButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClicked)

            self.ribbonButtons.append(newButton)
        self.modifyTabGeometry(0)
        
      


  



         