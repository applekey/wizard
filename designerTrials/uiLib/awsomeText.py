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


class awsomeText(QtGui.QFrame):
    def __init__(self, parentForm):
        super( awsomeText, self ).__init__()
        self.__setupUi(self)
        self.setStyleSheet("background:"+navBarBackgroundColor)
    
    def setText(self,bottom,Top):
        self.OuterLabel.setText(Top)
        self.innerLabel.setText(bottom)

    def __setupUi(self, parentForm):    
        # main verticle layout where everthing lives
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
           
        # the outter label that the verticle layout lives in 
        self.OuterLabel = QtGui.QLabel(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OuterLabel.sizePolicy().hasHeightForWidth())
        self.OuterLabel.setSizePolicy(sizePolicy)
        self.OuterLabel.setObjectName(_fromUtf8("OuterLabel"))
        self.verticalLayout.addWidget(self.OuterLabel)
            
            
        # this is the space between the label and the main text, control window
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
            
        # i added a grid layout for the bottom, all controls will live in this grid
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.innerLabel = QtGui.QLabel(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.innerLabel.sizePolicy().hasHeightForWidth())
            
        # i added just some text for now
        self.innerLabel.setSizePolicy(sizePolicy)
        self.innerLabel.setObjectName(_fromUtf8("innerLabel"))
        self.gridLayout.addWidget(self.innerLabel, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.OuterLabel.setText(_translate("Form", "OuterLabdel", None))
        self.innerLabel.setText(_translate("Form", "InnerText", None))