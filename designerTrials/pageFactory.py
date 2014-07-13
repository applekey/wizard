#
# Created: Sun Jul 06 18:19:50 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!
import sys
sys.path.append( 'contentPage' )


from PyQt4 import QtCore, QtGui
from layoutWidget import layoutWidget
from patientInfoPage import patientInfo
from awsomeSlider import awsomeSlider
from demoPage import demoPage
from demoEndPage import demoEndPage


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
        controlWidget = demoPage
        self.page1Widget = layoutWidget(self.parentWidget,controlWidget)
        self.page1Widget.setText("1")
        self.page1Widget.setVideoSource("abc.mov")


        self.endPage = demoEndPage(self.parentWidget)

        ## add all the widgets to pages to add
        self.pagesToAdd.append( self.introPage);
        self.pagesToAdd.append( self.page1Widget);
        self.pagesToAdd.append( self.endPage);
   
        return self.pagesToAdd