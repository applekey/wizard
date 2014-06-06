# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizardpage.ui'
#
# Created: Wed Jun 04 13:38:36 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import phonon
from PyQt4.phonon import Phonon
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

class Ui_WizardPage(QtGui.QWizardPage):
    
    def calluser(self):
        self.videoPlayer.play()
        
    def setupUi(self, WizardPage):
        WizardPage.setObjectName(_fromUtf8("WizardPage"))
        WizardPage.resize(814, 665)
        self.radioButton = QtGui.QRadioButton(WizardPage)
        self.radioButton.setGeometry(QtCore.QRect(170, 280, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.toolButton = QtGui.QToolButton(WizardPage)
        self.toolButton.setGeometry(QtCore.QRect(200, 240, 25, 19))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.commandLinkButton = QtGui.QCommandLinkButton(WizardPage)
        self.commandLinkButton.setGeometry(QtCore.QRect(140, 430, 188, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.button = QtGui.QPushButton('Button', self)
        self.name='me'
        self.button.clicked.connect(self.calluser)

        self.videoPlayer = phonon.Phonon.VideoPlayer(WizardPage)
        self.videoPlayer.setGeometry(QtCore.QRect(270, 280, 300, 200))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        media = Phonon.MediaSource('C:\\video.3gp')
        vp = self.videoPlayer
        vp.load(media)
        vp.show()
        #vp.play()
        

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(_translate("WizardPage", "WizardPage", None))
        self.radioButton.setText(_translate("WizardPage", "RadioButton", None))
        self.toolButton.setText(_translate("WizardPage", "...", None))
        self.commandLinkButton.setText(_translate("WizardPage", "CommandLinkButton", None))
    def __init__( self, parent ):
        super(Ui_WizardPage, self).__init__(parent)
       
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WizardPage = QtGui.QWizardPage()
    ui = Ui_WizardPage()
    ui.setupUi(WizardPage)
    WizardPage.show()
    sys.exit(app.exec_())

