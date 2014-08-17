# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'awsomeNavigation.ui'
#
# Created: Sun Jul 06 18:19:50 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from layoutWidget import layoutWidget
from banner import banner
from navigationConfiguration import *
from awsomePushButton import awsomePushButton

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
        self.currentPage = 0
        self.parent = parentForm
        self.pages =[]
        self.resize(parentForm.size())
        self.size = QtCore.QRect(0, 0, self.width(), self.height())
        self.setStyleSheet("background:"+navBarBackgroundColor)

        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        
    
    def addPages(self,pages):
        self.pages =pages

    def nextClicked(self):
        if self.currentPage is len(self.pages)-1:
            return
        else:
            self.currentPage = self.currentPage+1
            self.changePage(self.currentPage)

    def prevClicked(self):
        if self.currentPage is 0:
            return
        else:
            self.currentPage = self.currentPage-1
            self.changePage(self.currentPage)


    def changePage(self,pageNumber):
        for pageIndex in range(len(self.pages)):
            if pageIndex is pageNumber:
                self.pages[pageIndex].show()
                self.verticalLayout.removeWidget(self.activePage)
                self.verticalLayout.removeWidget(self.sizeGrip)
                self.verticalLayout.removeItem(self.horizontalLayout)
                self.activePage.hide()
                self.activePage = self.pages[pageIndex]
                self.verticalLayout.addWidget(self.activePage)
                self.verticalLayout.addLayout(self.horizontalLayout)
                self.verticalLayout.addWidget(self.sizeGrip,0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)
                self.currentPage = pageNumber
                ## check banner state
                if pageIndex is 0:
                    self.backButton.setIconsPack([navigationBackStandardTheme1,navigationBackHoverTheme1]);
                    self.fowardButton.setIconsPack([navigationFowardStandardTheme1,navigationFowardHoverTheme1]);
                    self.banner.modifyTabGeometry(0)
                elif pageIndex is 1:
                    self.backButton.setIconsPack([navigationBackStandardTheme2,navigationBackHoverTheme2]);
                    self.fowardButton.setIconsPack([navigationFowardStandardTheme2,navigationFowardHoverTheme2]);
                    self.banner.modifyTabGeometry(1)
                elif pageIndex is 2:
                    self.backButton.setIconsPack([navigationBackStandardTheme3,navigationBackHoverTheme3]);
                    self.fowardButton.setIconsPack([navigationFowardStandardTheme3,navigationFowardHoverTheme3]);
                    self.banner.modifyTabGeometry(2)
                else:
                    pass

                
                
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
    
    def bannerTriggered(self,number):
        if self.currentPage is number:
            return
        self.changePage(number)

    def setupUi(self,parent):
        ## the main screen and the naviagation bar lives on the verticle layout
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        ## banner stuff
        self.banner = banner(self)
        self.banner.setStyleSheet("background:"+"#9b59b6")

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.banner.sizePolicy().hasHeightForWidth())
        
        self.banner.setSizePolicy(sizePolicy)
        #self.banner.setMinimumSize(QtCore.QSize(200, 100))
        self.banner.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.banner)
        
        ## hide all the active pages
        for pageIndex in range(len(self.pages)):
            self.pages[pageIndex].hide()
            self.activePagePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
            self.activePagePolicy.setHorizontalStretch(0)
            self.activePagePolicy.setVerticalStretch(0)
            self.activePagePolicy.setHeightForWidth(self.pages[pageIndex].sizePolicy().hasHeightForWidth())
            self.pages[pageIndex].setSizePolicy(self.activePagePolicy)

        ## this is where the main screen will live
        self.activePage = self.pages[0]
        self.activePage.show()
        

        self.verticalLayout.addWidget(self.activePage)
        
        ## this is where the naviagation bars will live
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        #self.horizontalLayout.setContentsMargins(30, 15, 30, 15)
        
        self.backButton = awsomePushButton(self.layoutWidget,[navigationBackStandardTheme1,navigationBackHoverTheme1])
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout.addWidget(self.backButton)
        
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
       
        self.fowardButton = awsomePushButton(self.layoutWidget,[navigationFowardStandardTheme1,navigationFowardHoverTheme1])
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fowardButton.sizePolicy().hasHeightForWidth())
        self.fowardButton.setSizePolicy(sizePolicy)
        self.fowardButton.setObjectName(_fromUtf8("fowardButton"))
        self.horizontalLayout.addWidget(self.fowardButton)
        self.verticalLayout.addLayout(self.horizontalLayout)


        self.resizeEvent  = self.onResize

        #link for click signal
        QtCore.QObject.connect(self.fowardButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.nextClicked)
        QtCore.QObject.connect(self.backButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.prevClicked)
        self.banner.bannerTriggered.connect(self.bannerTriggered)

        self.sizeGrip = QtGui.QSizeGrip(self.layoutWidget)
        self.verticalLayout.addWidget( self.sizeGrip, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight);

     

        

   

