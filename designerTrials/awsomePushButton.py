from PyQt4 import QtCore, QtGui
from componentConfirguration  import *

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

class awsomePushButton( QtGui.QPushButton):
    def onResize(self,event):
        width= event.size().width()
        height= event.size().height()
        newSize = QtCore.QRect(0,0,width,height)
        self.setIconSize(QtCore.QSize(30,25))   
    
    def __init__(self, parentForm,iconStatePics):
        super( awsomePushButton, self ).__init__(parentForm)
        self.iconStatePics = iconStatePics
        self.setStyleSheet("background: transparent;")
        self.setMinimumSize(QtCore.QSize(50, 50))
        self.setIconSize(self.size())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(self.iconStatePics[0])), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.resizeEvent  = self.onResize
        self.setMouseTracking(True)
       

    def mouseMoveEvent(self, event):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(self.iconStatePics[1])), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
    def leaveEvent(self, event):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(self.iconStatePics[0])), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)


