# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Sun Jun 29 22:55:56 2014
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


class banner(QtGui.QWidget):
    def __init__(self, parentForm):
        super( banner, self ).__init__()
        self.centralwidget = QtGui.QWidget(parentForm)
        self.__setupUi(self.centralwidget)
        ## create our own widget, the resizing and such will be done one this
        
        ## specify some min, max boundaries, I am not allowing this to shrink in height
        ## and become smaller than a certain number

    def setGeometry(self, int1, int2, int3, int4):
        self.centralwidget.setGeometry(int1, int2, int3, int4)
    
    def setGeometry(self, qrect):
        self.centralwidget.setGeometry(qrect)
    
    def __setupUi(self, Form):
        
        self.centralwidget.setGeometry(QtCore.QRect(300, 0, 500, 300))
        
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(110, 140, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 70, 291, 101))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.checkBox_2 = QtGui.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(100, 110, 70, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(250, 130, 70, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.checkBox.setText(_translate("Form", "CheckBox", None))
        self.pushButton.setText(_translate("Form", "PushButton", None))
        self.checkBox_2.setText(_translate("Form", "CheckBox", None))
        self.checkBox_3.setText(_translate("Form", "CheckBox", None))



