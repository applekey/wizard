# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page2.ui'
#
# Created: Tue Jul 01 13:30:33 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName(_fromUtf8("WizardPage"))
        WizardPage.resize(807, 904)
        self.widget = QtGui.QWidget(WizardPage)
        self.widget.setGeometry(QtCore.QRect(40, 50, 711, 381))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.widget)
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.verticalLayout.addWidget(self.videoPlayer)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.seekSlider = phonon.Phonon.SeekSlider(self.widget)
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.horizontalLayout.addWidget(self.seekSlider)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.widget)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.horizontalLayout.addWidget(self.volumeSlider)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(_translate("WizardPage", "WizardPage", None))
        self.pushButton.setText(_translate("WizardPage", "start/stop", None))
        self.pushButton_2.setText(_translate("WizardPage", "fullscreeen?", None))

from PyQt4 import phonon

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WizardPage = QtGui.QWizardPage()
    ui = Ui_WizardPage()
    ui.setupUi(WizardPage)
    WizardPage.show()
    sys.exit(app.exec_())

