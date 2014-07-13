from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QPainter
from PyQt4.QtCore import QRectF,QPoint,QSize


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
    def mousePressEvent(self,mouseEvent):
        self.oldPosition = mouseEvent.globalPos()
        super(kitKatButton,self).mousePressEvent(mouseEvent)

    def mouseMoveEvent(self,mouseEvent):
        delta = mouseEvent.globalPos()- self.oldPosition
        self.window().move(self.window().pos().x()+delta.x(),self.window().pos().y()+delta.y())
        self.oldPosition = mouseEvent.globalPos()


    def __init__(self, *args):
        self.oldPosition = QtCore.QPoint(0,0)
        self.text = ""
        self.textPosition = QPoint( 30, 10 );
        self.icon = None
        self.basicStyle = 'border: none'
        self.addedStyle = self.basicStyle
        self.iconPosition = QPoint( 0, 0 );
        return super(kitKatButton, self).__init__(*args)
    
    def changeText(self,text):
        self.text = text
        self.repaint()
    
    def setText(self,text):
        self.changeText(text)

    def setTextPosition(self,point):
        self.textPosition =point
        self.repaint()
   
    def setIcon(self,icon):
        self.icon = icon
    
    def setIconPosition(self,point):
        self.iconPosition = point

    def setStyleSheet(self, style):
        self.addedStyle = style+self.basicStyle
        super(kitKatButton, self).setStyleSheet( self.addedStyle)
        self.repaint()

    def paintEvent(self,QPaintEvent):
        QtGui.QPushButton.paintEvent(self,QPaintEvent)
        # set the style sheet
        #super(kitKatButton, self).setStyleSheet( self.addedStyle)
        
        painter = QPainter(self)
        if self.icon is not None:
             painter.drawPixmap(self.iconPosition.x(), self.iconPosition.y(), self.icon.pixmap(self.iconSize().width(), self.iconSize().height()))

        painter.drawText( self.textPosition, self.text );




