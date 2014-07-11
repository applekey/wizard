from PyQt4 import QtCore, QtGui
from awsomeNavigation import awsomeNavigation


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
    def __init__(self,position):
        
        super( awsomeDialog, self ).__init__()
        
        self.parent = self
        self.setupUi()
        self.parent.setGeometry(QtCore.QRect(position.x(), position.y(), 200, 200))
        
        self.parent.setObjectName(_fromUtf8("widget"))
        
        self.resizeEvent  = self.onResize
       
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

    def mousePressEvent(self,mouseEvent):
        self.oldPosition = mouseEvent.globalPos()

    def mouseMoveEvent(self,mouseEvent):
        delta = mouseEvent.globalPos()- self.oldPosition
        self.move(self.pos().x()+delta.x(),self.pos().y()+delta.y())
        self.oldPosition = mouseEvent.globalPos()


    def onResize(self,event):
        width= event.size().width()
        height= event.size().height()
        newSize = QtCore.QRect(0,0,width,height)
        self.verticalLayout.setGeometry(newSize)

    def setupUi(self):
        self.verticalLayout = QtGui.QVBoxLayout(self.parent)
        self.verticalLayout.setContentsMargins(10, -1, 10, 10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.parent)
        self.horizontalLayout_2.setContentsMargins(10, 5, 10, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.parent)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.pushButton = QtGui.QPushButton(self.parent)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtGui.QScrollArea(self.parent)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        #self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 419, 386))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi()
    

    def retranslateUi(self):
      
        self.label.setText(_translate("Dialog", "TextLabel", None))
        self.pushButton.setText(_translate("Dialog", "PushButton", None))