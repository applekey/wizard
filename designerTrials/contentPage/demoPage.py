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
        self.plainTextEdit = QtGui.QPlainTextEdit(self)
        font = QtGui.QFont()

        font.setPointSize(15)
        self.plainTextEdit.setFont(font)
        #self.plainTextEdit.setPalette(palette)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit.setStyleSheet(scrollBarStyle)
        self.plainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEdit.setReadOnly(True)


        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        
        
        
        
        self.pushButton = awsomeSlider(self)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
       

        self.retranslateUi()
     

    def retranslateUi(self):
      
        self.label_2.setText(_translate("MainWindow", "4", None))
        self.label.setText(_translate("MainWindow", "Preparing", None))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "M-185 is a state trunkline highway in the U.S. state of Michigan that circles Mackinac Island, a popular tourist destination on the Lake Huron side of the Straits of Mackinac, along the island\'s shoreline. A narrow paved road of 8.004 miles (12.881 km), it offers scenic views of the straits that divide the Upper and the Lower peninsulas of Michigan and Lakes Huron and Michigan. It has no connection to any other Michigan state trunkline highways—as it is on an island—and is accessible only by passenger ferry. The City of Mackinac Island, which shares jurisdiction over the island with the Mackinac Island State Park Commission (MISPC), calls the highway Main Street within the built-up area on the island\'s southeast quadrant, and Lake Shore Road elsewhere. M-185 passes by several important sites within Mackinac Island State Park, including Fort Mackinac, Arch Rock, British Landing, and Devil\'s Kitchen. Lake Shore Road carries the highway next to the Lake Huron shoreline, running between the water\'s edge and woodlands outside of the downtown area.\n"
"\n"
"According to the Michigan Department of Transportation (MDOT), M-185 is \"the only state highway in the nation where motor vehicles are banned\".[3] Traffic on it is by foot, on horse, by horse-drawn vehicle, or by bicycle. Restrictions on automobiles date back to the 1890s, and since the ban, only a few vehicles have been permitted on the island other than the city\'s emergency vehicles. The highway was built during the first decade of the 20th century by the state and designated as a state highway in 1933. The highway was paved in the 1950s, and portions were rebuilt to deal with shoreline erosion in the 1980s. Until 2005, it was the only state highway without any automobile accidents.\n"
"\n"
"The monarchy of the Kingdom of England began with Alfred the Great and ended with Queen Anne, who became Queen of Great Britain when England merged with Scotland to form a union in 1707. For monarchs after Queen Anne, see List of British monarchs.\n"
"\n"
"Arguments are made for a few different kings deemed to control enough of the ancient kingdoms of the Anglo-Saxons to be deemed the first King of England. For example Offa, king of Mercia, and Egbert, king of Wessex, are sometimes described as kings of England by popular writers, but not by all historians. In the late eighth century Offa achieved a dominance over southern England which did not survive his death in 796. In 829 Egbert conquered Mercia, but he soon lost control of it. By the late ninth century Wessex was the dominant Anglo-Saxon kingdom. Its king, Alfred the Great, was overlord of western Mercia and used the title King of the Angles and Saxons (and starts the list below), but he never ruled eastern and northern England, which was then the Danelaw. His son Edward the Elder conquered the eastern Danelaw, but Edward\'s son Æthelstan became the first king to rule the whole of England when he conquered Northumbria in 927, and he is regarded by some modern historians as the first king of England.[1][2]\n"
"\n"
"The Principality of Wales was incorporated into the Kingdom of England under the Statute of Rhuddlan in 1284, and in 1301 King Edward I invested his eldest son, the future King Edward II, as Prince of Wales. Since that time, with the exception of King Edward III, the eldest sons of all English monarchs have borne this title. After the death of Queen Elizabeth I without issue, in 1603, the crowns of England and Scotland were joined in personal union under King James VI of Scotland, who became James I of England. By royal proclamation, James titled himself \"King of Great Britain\", but no such kingdom was created until 1707, when England underwent legislative union with Scotland to form the new Kingdom of Great Britain, during the reign of Queen Anne.[3]", None))
       

