# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoPage.ui'
#
# Created: Sat Jul 12 20:07:19 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from awsomeSlider import awsomeSlider
from componentConfirguration import *
from PyQt4.QtWebKit import QWebView
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

class demoPage(QtGui.QWidget):
    def onResize(self,event):
        width= event.size().width()
        height= event.size().height()
        newSize = QtCore.QRect(0,0,width,height)
        self.verticalLayout.setGeometry(newSize)

    def __init__(self, parent):
        self.parent = parent
        super(demoPage, self).__init__(parent)
        self.setupUi()
        self.resizeEvent  = self.onResize

    def setupUi(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.All, QtGui.QPalette.Text, brush)
        palette.setBrush(QtGui.QPalette.All, QtGui.QPalette.WindowText, brush)

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setContentsMargins(0,30,0,0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self)
        
       
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self)
       
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setPalette(palette)
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        #self.plainTextEdit = QtGui.QPlainTextEdit(self)
        font = QtGui.QFont()

        font.setPointSize(15)
        #self.plainTextEdit.setFont(font)
        self.webview = QWebView(self)
        self.webview.settings().setUserStyleSheetUrl(QtCore.QUrl(''))
        self.webview.setHtml('''
<!DOCTYPE html>
<html lang="en">
  <style>
  body {
   background:#A8ACAF !important;
}

.circle
{
width:50px;
height:50px;
border-radius:25px;
font-size:50px;
color:#A8ACAF;
line-height:50px;
text-align:center;
background:#ffffff
}

#headerContainer
{
  margin-top:10px;
  margin-left:5px;
}

#headerFont
{
  font-size:30px;
}

#paragraphSection
{
  margin-top:40px;
  margin-left:20px;
  font-size:22px;
  font-family:times;
}
  </style>
  <head>
    <meta charset="utf-8">
    <title>
    </title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"
    rel="stylesheet">
    <link href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css"
    rel="stylesheet">
  </head>
  
  <body id="body">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js">
    </script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js">
    </script>
    <div id="headerContainer" class="row">
      <div class="col-md-1">
        <div class="circle">
          1
        </div>
      </div>
      <div id="headerFont" class="col-md-7">
        Adjusting
      </div>
    </div>
    <div id="paragraphSection" class="row">
      <p>
        Turn on the computer, connect the Scanner to the USB and Power (if needed)
        and make sure everything is working. Use any Skanect-compatible 3D scanner.
      </p>
    </div>
  </body>

</html>
''')
        self.verticalLayout.addWidget(self.webview)
    



        ##self.plainTextEdit.setPalette(palette)
        #self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        #self.plainTextEdit.setStyleSheet(scrollBarStyle)
        #self.plainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        #self.plainTextEdit.setReadOnly(True)


        #self.verticalLayout.addWidget(self.plainTextEdit)
        #self.horizontalLayout_2 = QtGui.QHBoxLayout()
        #self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        #spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        #self.horizontalLayout_2.addItem(spacerItem1)
        
        
        
        
        #self.pushButton = awsomeSlider(self)
        #self.horizontalLayout_2.addWidget(self.pushButton)
        #self.verticalLayout.addLayout(self.horizontalLayout_2)
       

        self.retranslateUi()
     

    def retranslateUi(self):
      
        self.label_2.setText(_translate("MainWindow", "4", None))
        self.label.setText(_translate("MainWindow", "Preparing", None))
      
