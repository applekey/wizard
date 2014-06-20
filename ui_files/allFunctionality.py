# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allFunctionality.ui'
#
# Created: Fri Jun 20 14:24:41 2014
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
        WizardPage.resize(920, 620)
        self.label = QtGui.QLabel(WizardPage)
        self.label.setGeometry(QtCore.QRect(30, 50, 121, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(WizardPage)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 121, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(WizardPage)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 121, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(WizardPage)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 121, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(WizardPage)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 121, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(WizardPage)
        self.label_6.setGeometry(QtCore.QRect(30, 270, 121, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(WizardPage)
        self.label_7.setGeometry(QtCore.QRect(30, 310, 121, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(WizardPage)
        self.label_8.setGeometry(QtCore.QRect(30, 350, 121, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(WizardPage)
        self.label_9.setGeometry(QtCore.QRect(30, 390, 121, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(WizardPage)
        self.label_10.setGeometry(QtCore.QRect(30, 420, 121, 31))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(WizardPage)
        self.label_11.setGeometry(QtCore.QRect(30, 450, 121, 31))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.pushButton = QtGui.QPushButton(WizardPage)
        self.pushButton.setGeometry(QtCore.QRect(220, 50, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(WizardPage)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 90, 75, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(WizardPage)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 140, 75, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(WizardPage)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 180, 131, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(WizardPage)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 220, 75, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(WizardPage)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 270, 75, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(WizardPage)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 310, 75, 31))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(WizardPage)
        self.pushButton_8.setGeometry(QtCore.QRect(220, 350, 75, 31))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(WizardPage)
        self.pushButton_9.setGeometry(QtCore.QRect(220, 390, 75, 31))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(WizardPage)
        self.pushButton_10.setGeometry(QtCore.QRect(220, 420, 75, 31))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(WizardPage)
        self.pushButton_11.setGeometry(QtCore.QRect(220, 450, 75, 31))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.horizontalSlider = QtGui.QSlider(WizardPage)
        self.horizontalSlider.setGeometry(QtCore.QRect(550, 120, 160, 22))
        self.horizontalSlider.setMinimum(5)
        self.horizontalSlider.setMaximum(30)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.label_12 = QtGui.QLabel(WizardPage)
        self.label_12.setGeometry(QtCore.QRect(550, 90, 181, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))

        self.retranslateUi(WizardPage)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.import)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.selectAll)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.remesh)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.wireframe)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.deformsmooth)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.roughtselectionforsocket)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.editoffset)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), WizardPage.remeshValueChanged)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(_translate("WizardPage", "WizardPage", None))
        self.label.setText(_translate("WizardPage", "1. bring in scan", None))
        self.label_2.setText(_translate("WizardPage", "2. select all", None))
        self.label_3.setText(_translate("WizardPage", "3. remesh", None))
        self.label_4.setText(_translate("WizardPage", "4. turn on wireframe, use lower resolution", None))
        self.label_5.setText(_translate("WizardPage", "5. deform smooth", None))
        self.label_6.setText(_translate("WizardPage", "6. rought slection for socket modeling", None))
        self.label_7.setText(_translate("WizardPage", "7. edit offset", None))
        self.label_8.setText(_translate("WizardPage", "8. modify, smooth boundary", None))
        self.label_9.setText(_translate("WizardPage", "9. edit discard", None))
        self.label_10.setText(_translate("WizardPage", "10. remesh, select mm", None))
        self.label_11.setText(_translate("WizardPage", "11. select the leg, hide it", None))
        self.pushButton.setText(_translate("WizardPage", "import", None))
        self.pushButton_2.setText(_translate("WizardPage", "select all", None))
        self.pushButton_3.setText(_translate("WizardPage", "remesh", None))
        self.pushButton_4.setText(_translate("WizardPage", "wireframe mode", None))
        self.pushButton_5.setText(_translate("WizardPage", "PushButton", None))
        self.pushButton_6.setText(_translate("WizardPage", "PushButton", None))
        self.pushButton_7.setText(_translate("WizardPage", "offset", None))
        self.pushButton_8.setText(_translate("WizardPage", "PushButton", None))
        self.pushButton_9.setText(_translate("WizardPage", "PushButton", None))
        self.pushButton_10.setText(_translate("WizardPage", "PushButton", None))
        self.pushButton_11.setText(_translate("WizardPage", "PushButton", None))
        self.label_12.setText(_translate("WizardPage", "remesh value", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WizardPage = QtGui.QWizardPage()
    ui = Ui_WizardPage()
    ui.setupUi(WizardPage)
    WizardPage.show()
    sys.exit(app.exec_())

