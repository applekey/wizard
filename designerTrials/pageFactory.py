#
# Created: Sun Jul 06 18:19:50 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from layoutWidget import layoutWidget
from patientInfoPage import patientInfo


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

class pageFactory():
    def __init__(self,parentWidget):
        self.parentWidget = parentWidget
        self.pagesToAdd = []

    def createWidgets(self):
        self.introPage =patientInfo(self.parentWidget) 

        ## create and modify the widgets here
        self.page1Widget = layoutWidget(self.parentWidget)
        self.page1Widget.setText("1")
        self.page2Widget = layoutWidget(self.parentWidget)
        self.page2Widget.setText("2")
        self.page3Widget = layoutWidget(self.parentWidget)
        self.page3Widget.setText("3")
        self.page4Widget = layoutWidget(self.parentWidget)
        self.page4Widget.setText("4")
        ## add all the widgets to pages to add
        self.pagesToAdd.append( self.introPage);
        self.pagesToAdd.append( self.page1Widget);
        self.pagesToAdd.append( self.page2Widget);
        self.pagesToAdd.append( self.page3Widget);
        self.pagesToAdd.append( self.page4Widget);
        return self.pagesToAdd