# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created: Thu Jul 03 11:03:16 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

#import in the custom banner and the custom player
from componentConfirguration import *
from banner import banner
from awsomePlayer import awsomePlayer
from awsomeText import awsomeText
from awsomeSlider import awsomeSlider
 
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

class layoutWidget(QtGui.QFrame):
    def __init__(self, parentForm,controlWidget):
        super( layoutWidget, self ).__init__(parentForm)
        self.specifiedLayout = 0
        self.controlWidget = controlWidget
        ## the default layout 0 is the one with the banner, the video player and finally the text
        # layout 1 is the first selection screen with the text boxes
        self.setupUi(parentForm)

    def setGeometry(self, qrect):
        #self.centralwidget.setGeometry(qrect)
        self.__resizeGeometry(qrect)
        super(layoutWidget,self).setGeometry(qrect)
            
    def __resizeGeometry(self,qsize):
        self.verticalLayout.setGeometry(qsize)

    def sepecifySpecificLayout(layout):
        self.layout = layout

    def setText(self,text):
        #self.textFrame.setText(text,text)
        pass

    def setupUi(self,parentForm):
      
        # this is the verticle layout that all the visual elementss on 
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setMargin(0)
        #self.verticalLayout.setContentsMargins(11, 0, 11, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        # this is for the banner
        
        
        #------------------------ this is the spacer item inbetween the banner and the video player
        #spacerItem = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        #self.verticalLayout.addItem(spacerItem)
        
        # this is the video player layout
        self.videoPlayer = awsomePlayer(self)

        self.videoPlayer.setStyleSheet("background:"+videoPlayerBackgroundColor)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoPlayer.sizePolicy().hasHeightForWidth())
        
        self.videoPlayer.setSizePolicy(sizePolicy)
        self.videoPlayer.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.videoPlayer)
        
        # ------------------------this is the second spacer
        #spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        #self.verticalLayout.addItem(spacerItem1)
        

        # this is the final dialog box
        self.textFrame = self.controlWidget(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textFrame.sizePolicy().hasHeightForWidth())
        self.textFrame.setSizePolicy(sizePolicy)
        self.textFrame.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.textFrame)
      
        self.retranslateUi()

    def retranslateUi(self):
        pass



