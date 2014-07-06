# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allFunctionality.ui'
#
# Created: Fri Jun 20 13:11:44 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

#import hidden Api from meshmixer

import mmapi
from mmRemote import *;

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
    def setupUi(self, WizardPage):
        self.setWindowFlags (QtCore.Qt.FramelessWindowHint)
        WizardPage.setObjectName(_fromUtf8("WizardPage"))
        WizardPage.resize(934, 869)
        WizardPage.setWindowFlags (QtCore.Qt.FramelessWindowHint)
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
        self.label_7.setGeometry(QtCore.QRect(30, 410, 121, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(WizardPage)
        self.label_8.setGeometry(QtCore.QRect(30, 510, 121, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(WizardPage)
        self.label_9.setGeometry(QtCore.QRect(30, 550, 121, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(WizardPage)
        self.label_10.setGeometry(QtCore.QRect(30, 610, 121, 31))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(WizardPage)
        self.label_11.setGeometry(QtCore.QRect(40, 780, 121, 31))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.ImportScan = QtGui.QPushButton(WizardPage)
        self.ImportScan.setGeometry(QtCore.QRect(220, 50, 75, 23))
        self.ImportScan.setObjectName(_fromUtf8("ImportScan"))
        self.SelectAll = QtGui.QPushButton(WizardPage)
        self.SelectAll.setGeometry(QtCore.QRect(220, 90, 75, 31))
        self.SelectAll.setObjectName(_fromUtf8("SelectAll"))
        self.RemeshModel = QtGui.QPushButton(WizardPage)
        self.RemeshModel.setGeometry(QtCore.QRect(220, 140, 75, 31))
        self.RemeshModel.setObjectName(_fromUtf8("RemeshModel"))
        self.EnableWireframeMode = QtGui.QPushButton(WizardPage)
        self.EnableWireframeMode.setGeometry(QtCore.QRect(220, 180, 131, 31))
        self.EnableWireframeMode.setObjectName(_fromUtf8("EnableWireframeMode"))
        self.DeformSmoothEnable = QtGui.QPushButton(WizardPage)
        self.DeformSmoothEnable.setGeometry(QtCore.QRect(220, 220, 75, 31))
        self.DeformSmoothEnable.setObjectName(_fromUtf8("DeformSmoothEnable"))
        self.RoughtSelection = QtGui.QPushButton(WizardPage)
        self.RoughtSelection.setGeometry(QtCore.QRect(220, 270, 75, 31))
        self.RoughtSelection.setObjectName(_fromUtf8("RoughtSelection"))
        self.EditOffset = QtGui.QPushButton(WizardPage)
        self.EditOffset.setGeometry(QtCore.QRect(220, 410, 75, 31))
        self.EditOffset.setObjectName(_fromUtf8("EditOffset"))
        self.SmoothBoundary = QtGui.QPushButton(WizardPage)
        self.SmoothBoundary.setGeometry(QtCore.QRect(220, 510, 75, 31))
        self.SmoothBoundary.setObjectName(_fromUtf8("SmoothBoundary"))
        self.Discard = QtGui.QPushButton(WizardPage)
        self.Discard.setGeometry(QtCore.QRect(220, 550, 75, 31))
        self.Discard.setObjectName(_fromUtf8("Discard"))
        self.SecondaryRemeshing = QtGui.QPushButton(WizardPage)
        self.SecondaryRemeshing.setGeometry(QtCore.QRect(220, 610, 75, 31))
        self.SecondaryRemeshing.setObjectName(_fromUtf8("SecondaryRemeshing"))
        self.HideLeg = QtGui.QPushButton(WizardPage)
        self.HideLeg.setGeometry(QtCore.QRect(230, 780, 75, 31))
        self.HideLeg.setObjectName(_fromUtf8("HideLeg"))
        self.label_12 = QtGui.QLabel(WizardPage)
        self.label_12.setGeometry(QtCore.QRect(550, 90, 181, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.groupBox = QtGui.QGroupBox(WizardPage)
        self.groupBox.setGeometry(QtCore.QRect(500, 50, 311, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.RemeshSlider = QtGui.QSlider(self.groupBox)
        self.RemeshSlider.setGeometry(QtCore.QRect(30, 30, 211, 91))
        self.RemeshSlider.setMinimum(0)
        self.RemeshSlider.setMaximum(100)
        self.RemeshSlider.setPageStep(10)
        self.RemeshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.RemeshSlider.setInvertedAppearance(False)
        self.RemeshSlider.setObjectName(_fromUtf8("RemeshSlider"))
        self.groupBox_2 = QtGui.QGroupBox(WizardPage)
        self.groupBox_2.setGeometry(QtCore.QRect(500, 220, 311, 161))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.DeformSmooth_scaleValue = QtGui.QSlider(self.groupBox_2)
        self.DeformSmooth_scaleValue.setGeometry(QtCore.QRect(40, 120, 160, 22))
        self.DeformSmooth_scaleValue.setMinimum(5)
        self.DeformSmooth_scaleValue.setMaximum(30)
        self.DeformSmooth_scaleValue.setOrientation(QtCore.Qt.Horizontal)
        self.DeformSmooth_scaleValue.setObjectName(_fromUtf8("DeformSmooth_scaleValue"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(40, 20, 181, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.DeformSmooth_smoothValue = QtGui.QSlider(self.groupBox_2)
        self.DeformSmooth_smoothValue.setGeometry(QtCore.QRect(40, 50, 160, 22))
        self.DeformSmooth_smoothValue.setMinimum(0)
        self.DeformSmooth_smoothValue.setMaximum(100)
        self.DeformSmooth_smoothValue.setSingleStep(1)
        self.DeformSmooth_smoothValue.setPageStep(10)
        self.DeformSmooth_smoothValue.setOrientation(QtCore.Qt.Horizontal)
        self.DeformSmooth_smoothValue.setObjectName(_fromUtf8("DeformSmooth_smoothValue"))
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(40, 90, 181, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.InvertSelection = QtGui.QPushButton(WizardPage)
        self.InvertSelection.setGeometry(QtCore.QRect(240, 300, 75, 31))
        self.InvertSelection.setObjectName(_fromUtf8("InvertSelection"))
        self.groupBox_3 = QtGui.QGroupBox(WizardPage)
        self.groupBox_3.setGeometry(QtCore.QRect(490, 410, 311, 101))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.offset_distance = QtGui.QSlider(self.groupBox_3)
        self.offset_distance.setGeometry(QtCore.QRect(20, 60, 160, 22))
        self.offset_distance.setMinimum(5)
        self.offset_distance.setMaximum(30)
        self.offset_distance.setOrientation(QtCore.Qt.Horizontal)
        self.offset_distance.setObjectName(_fromUtf8("offset_distance"))
        self.label_16 = QtGui.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(20, 30, 181, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.groupBox_4 = QtGui.QGroupBox(WizardPage)
        self.groupBox_4.setGeometry(QtCore.QRect(480, 560, 311, 101))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.SmoothBoundary_distance = QtGui.QSlider(self.groupBox_4)
        self.SmoothBoundary_distance.setGeometry(QtCore.QRect(20, 60, 160, 22))
        self.SmoothBoundary_distance.setMinimum(0)
        self.SmoothBoundary_distance.setMaximum(100)
        self.SmoothBoundary_distance.setOrientation(QtCore.Qt.Horizontal)
        self.SmoothBoundary_distance.setObjectName(_fromUtf8("SmoothBoundary_distance"))
        self.label_17 = QtGui.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(20, 30, 181, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_15 = QtGui.QLabel(WizardPage)
        self.label_15.setGeometry(QtCore.QRect(30, 680, 121, 31))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.SecondaryOffset = QtGui.QPushButton(WizardPage)
        self.SecondaryOffset.setGeometry(QtCore.QRect(220, 680, 75, 31))
        self.SecondaryOffset.setObjectName(_fromUtf8("SecondaryOffset"))
        self.groupBox_5 = QtGui.QGroupBox(WizardPage)
        self.groupBox_5.setGeometry(QtCore.QRect(480, 710, 311, 101))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.SecondaryOffset_distance = QtGui.QSlider(self.groupBox_5)
        self.SecondaryOffset_distance.setGeometry(QtCore.QRect(20, 60, 160, 22))
        self.SecondaryOffset_distance.setMinimum(5)
        self.SecondaryOffset_distance.setMaximum(30)
        self.SecondaryOffset_distance.setOrientation(QtCore.Qt.Horizontal)
        self.SecondaryOffset_distance.setObjectName(_fromUtf8("SecondaryOffset_distance"))
        self.label_18 = QtGui.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(20, 30, 181, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))

        self.retranslateUi(WizardPage)
        QtCore.QObject.connect(self.ImportScan, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.importFigure)
        QtCore.QObject.connect(self.SelectAll, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.selectAll)
        QtCore.QObject.connect(self.RemeshModel, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.remesh)
        QtCore.QObject.connect(self.EnableWireframeMode, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.wireframe)
        QtCore.QObject.connect(self.DeformSmoothEnable, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.deformsmooth)
        QtCore.QObject.connect(self.RoughtSelection, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.roughtselectionforsocket)
        
        QtCore.QObject.connect(self.SmoothBoundary, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.ModifySmoothBoundary)
        QtCore.QObject.connect(self.Discard, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.editDiscard)
        QtCore.QObject.connect(self.SecondaryRemeshing, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.remeshsecondtime)
        QtCore.QObject.connect(self.SecondaryOffset, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.editoffset)
        QtCore.QObject.connect(self.HideLeg, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.selectleghide)

        QtCore.QObject.connect(self.RemeshSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), WizardPage.remeshValueChanged)
        QtCore.QObject.connect(self.DeformSmooth_smoothValue, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), WizardPage.deformSmooth_smoothValueChanged)
        QtCore.QObject.connect(self.offset_distance, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), WizardPage.offset_distanceValueChanged)
        QtCore.QObject.connect(self.SmoothBoundary_distance, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), WizardPage.smoothBoundary_distanceValueChanged)
        QtCore.QObject.connect(self.SecondaryOffset_distance, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), WizardPage.offsetSecond_distanceValueChanged)
        QtCore.QObject.connect(self.DeformSmooth_scaleValue, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), WizardPage.deformSmooth_scaleValueChanged)

        QtCore.QObject.connect(self.InvertSelection, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.invertSelection)
        QtCore.QObject.connect(self.EditOffset, QtCore.SIGNAL(_fromUtf8("clicked()")), WizardPage.editoffset)
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
        self.ImportScan.setText(_translate("WizardPage", "import", None))
        self.SelectAll.setText(_translate("WizardPage", "select all", None))
        self.RemeshModel.setText(_translate("WizardPage", "remesh", None))
        self.EnableWireframeMode.setText(_translate("WizardPage", "wireframe mode", None))
        self.DeformSmoothEnable.setText(_translate("WizardPage", "PushButton", None))
        self.RoughtSelection.setText(_translate("WizardPage", "PushButton", None))
        self.EditOffset.setText(_translate("WizardPage", "offset", None))
        self.SmoothBoundary.setText(_translate("WizardPage", "PushButton", None))
        self.Discard.setText(_translate("WizardPage", "PushButton", None))
        self.SecondaryRemeshing.setText(_translate("WizardPage", "PushButton", None))
        self.HideLeg.setText(_translate("WizardPage", "PushButton", None))
        self.label_12.setText(_translate("WizardPage", "remesh value", None))
        self.groupBox.setTitle(_translate("WizardPage", "Remesh", None))
        self.groupBox_2.setTitle(_translate("WizardPage", "Deform smooth", None))
        self.label_13.setText(_translate("WizardPage", "smooth value", None))
        self.label_14.setText(_translate("WizardPage", "scale value", None))
        self.InvertSelection.setText(_translate("WizardPage", "invert", None))
        self.groupBox_3.setTitle(_translate("WizardPage", "offset", None))
        self.label_16.setText(_translate("WizardPage", "distance", None))
        self.groupBox_4.setTitle(_translate("WizardPage", "smooth boundary", None))
        self.label_17.setText(_translate("WizardPage", "distance", None))
        self.label_15.setText(_translate("WizardPage", "eddit offset", None))
        self.SecondaryOffset.setText(_translate("WizardPage", "PushButton", None))
        self.groupBox_5.setTitle(_translate("WizardPage", "offset", None))
        self.label_18.setText(_translate("WizardPage", "distance", None))
## do not touch the code down here

    @staticmethod
    def SingleInstanceApiCommander(operation, modifier, modifierValue):
        remote = mmRemote()
        remote.connect()
        cmd = mmapi.StoredCommands()
        #some commands don't follow the scheme

        if operation is "selectAll":
             cmd.AppendSelectCommand_All()
        else:
            cmd.AppendBeginToolCommand(operation)
        
        if modifierValue is not None:
            cmd.AppendToolParameterCommand(modifier,modifierValue)

        #cmd.AppendCompleteToolCommand("accept")
        remote.runCommand(cmd);
        remote.shutdown();

    @staticmethod
    def importFigure():
       pass

    @staticmethod
    def selectAll(): 
      Ui_WizardPage.SingleInstanceApiCommander("selectAll",None,None)

    @staticmethod
    def wireframe():
        print 'here'

    @staticmethod
    def remesh():
       Ui_WizardPage.SingleInstanceApiCommander("remesh","smooth",0.325)

    @staticmethod
    def deformsmooth():
       Ui_WizardPage.SingleInstanceApiCommander("smooth","scale",0.7)
     
    @staticmethod
    def roughtselectionforsocket():
        print 'here'
    
    @staticmethod
    def invertSelection():
        print 'here'

    @staticmethod
    def editoffset():
        Ui_WizardPage.SingleInstanceApiCommander("offset","distance",0.7)

    @staticmethod
    def ModifySmoothBoundary():
        Ui_WizardPage.SingleInstanceApiCommander("smoothboundary","smoothness",25.0)

    @staticmethod
    def editDiscard():
        Ui_WizardPage.SingleInstanceApiCommander("discard",None,None)

    @staticmethod
    def remeshsecondtime():
        Ui_WizardPage.SingleInstanceApiCommander("remesh","smooth",13)

    @staticmethod
    def selectleghide():
        print 'here'

    ## value changed events

    @staticmethod
    def remeshValueChanged(value):
       Ui_WizardPage.SingleInstanceApiCommander("remesh","smooth",value/float(100))

    @staticmethod
    def deformSmooth_smoothValueChanged(value):
        Ui_WizardPage.SingleInstanceApiCommander("smooth","scale",value/float(100))

    @staticmethod
    def offset_distanceValueChanged(value):
        print 'here'

    @staticmethod
    def smoothBoundary_distanceValueChanged(value):
        print 'here'

    @staticmethod
    def offsetSecond_distanceValueChanged(value):
        print 'here'

    @staticmethod
    def deformSmooth_scaleValueChanged(value):
        print 'here'
    





    def __init__( self, parent ):
        super(Ui_WizardPage, self).__init__(parent)
        #intilize mesh mixer remote
    

        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WizardPage = QtGui.QWizardPage()
    ui = Ui_WizardPage()
    ui.setupUi(WizardPage)
    WizardPage.show()
    sys.exit(app.exec_())

