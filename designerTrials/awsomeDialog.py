from PyQt4 import QtCore, QtGui
from awsomeNavigation import awsomeNavigation
from pageFactory import pageFactory

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

class awsomeDialog(QtGui.QDialog):
       def __init__(self):
        self.oldPosition = QtCore.QPoint(0,0)
        super( moreInfoDialog, self ).__init__()
        self.setupUi()