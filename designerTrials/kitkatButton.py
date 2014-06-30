from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QPainter
from PyQt4.QtCore import QRectF


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

class kitKatButton( QtGui.QPushButton):
    def hello():
        print 'hello'
    def paintEvent(self,QPaintEvent):
        QtGui.QPushButton.paintEvent(self,QPaintEvent)
        painter = QPainter(self)
        startAngle = 90 * 16;
        spanAngle = 180 * 16;
        height = self.size().height()
        painter.drawPie(QRectF(0.0, 0.0, 80.0, height),startAngle,spanAngle)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        painter.drawPixmap(100, 0.0, icon.pixmap(200, 200));





