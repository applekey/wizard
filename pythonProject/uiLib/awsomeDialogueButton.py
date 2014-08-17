from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from awsomeDialog import *


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

class awsomeDialogButton(QtGui.QToolButton):
    def __init__(self, *args):
        super(awsomeDialogButton, self).__init__(*args)
        self.mousePressEvent = self.getPos

    def getPos(self , event):
        pos = QtGui.QCursor().pos()
        self.dosmth(pos)
    def modalClosed(self,event):
        self.window().setDisabled(False)
    def dosmth(self,point):
        self.modal = awsomeDialog(point)
        self.window().setDisabled(True)
        self.modal.show()
        self.modal.closeEvent = self.modalClosed
      
        
        