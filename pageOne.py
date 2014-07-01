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

class pageOne(QtGui.QWizardPage):

        
    def setupUi(self, WizardPage):
        vbox = QtGui.QVBoxLayout()
        areaInput = QtGui.QInputDialog.getText(self, "Copy Area", "New Area Name:", 0)
        vbox.addWidget(areaInput);
        
        self.btn = QtGui.QPushButton('Dialog', self)
    
    def __init__( self, parent ):
        super(pageOne, self).__init__(parent)
       
        self.setupUi(self)


