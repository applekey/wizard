## -*- coding: utf-8 -*-

## Form implementation generated from reading ui file 'trial.ui'
##
## Created: Fri Jun 27 14:27:32 2014
##      by: PyQt4 UI code generator 4.11
##
## WARNING! All changes made in this file will be lost!

#from PyQt4 import QtCore, QtGui
#from banner import banner
#from kitkatButton import kitKatButton
#from awsomePlayer import awsomePlayer
#from layoutWidget import layoutWidget
#from awsomeSlider import awsomeSlider


#try:
#    _fromUtf8 = QtCore.QString.fromUtf8
#except AttributeError:
#    def _fromUtf8(s):
#        return s

#try:
#    _encoding = QtGui.QApplication.UnicodeUTF8
#    def _translate(context, text, disambig):
#        return QtGui.QApplication.translate(context, text, disambig, _encoding)
#except AttributeError:
#    def _translate(context, text, disambig):
#        return QtGui.QApplication.translate(context, text, disambig)

#class Ui_MainWindow(object):
#    def onResize(self,event):
#        width= self.MainWindow.size().width()
#        height= self.MainWindow.size().height()
#        newSize = QtCore.QRect(0,0,width,height)
#        self.centralwidget.setGeometry(newSize)
#        #self.player.setGeometry(newSize)
    
#    def setupUi(self, MainWindow):
       
#        self.MainWindow = MainWindow
#        self.MainWindow.setObjectName(_fromUtf8("MainWindow"))
        
#        self.height = 800
#        self.width = 800

#        self.MainWindow.resize(self.width, self.height)
#        self.size = QtCore.QRect(0, 0, self.width, self.height)

#        self.centralwidget = QtGui.QWidget(self.MainWindow)
#        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
#        self.centralwidget.setGeometry(self.size)
       

#        #self.custom = kitKatButton(MainWindow)
#        #self.custom.setGeometry(200,0,400,100)
#        #self.custom.setText('abc')
#        #icon = QtGui.QIcon()
#        #icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#        #self.custom.setIcon(icon)
#        #self.mytest = banner(self.centralwidget)
       
#        #self.player = awsomePlayer(self.centralwidget)
#        #self.player.setSource("C:\\abc.mov")
#        #self.player.setGeometry(self.size)

#        self.slider = awsomeSlider(self.centralwidget)

#        #self.widget = layoutWidget(self.centralwidget)
#        #newSize = QtCore.QRect(0,0,self.width,self.height)
#        #self.widget.setGeometry(newSize)
#        #self.widget.hide()
#        self.MainWindow.resizeEvent  = self.onResize


#if __name__ == "__main__":
#    import sys
#    app = QtGui.QApplication(sys.argv)
#    MainWindow = QtGui.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())


from PyQt4 import QtCore, QtGui


class SlidersGroup(QtGui.QGroupBox):

    valueChanged = QtCore.pyqtSignal(int)

    def __init__(self, orientation, title, parent=None):
        super(SlidersGroup, self).__init__(title, parent)

        self.slider = QtGui.QSlider(orientation)
        self.slider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.slider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.setSingleStep(1)

        self.scrollBar = QtGui.QScrollBar(orientation)
        self.scrollBar.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.dial = QtGui.QDial()
        self.dial.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.slider.valueChanged.connect(self.scrollBar.setValue)
        self.scrollBar.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        self.dial.valueChanged.connect(self.valueChanged)

        if orientation == QtCore.Qt.Horizontal:
            direction = QtGui.QBoxLayout.TopToBottom
        else:
            direction = QtGui.QBoxLayout.LeftToRight

        slidersLayout = QtGui.QBoxLayout(direction)
        slidersLayout.addWidget(self.slider)
        slidersLayout.addWidget(self.scrollBar)
        slidersLayout.addWidget(self.dial)
        self.setLayout(slidersLayout)    

    def setValue(self, value):    
        self.slider.setValue(value)    

    def setMinimum(self, value):    
        self.slider.setMinimum(value)
        self.scrollBar.setMinimum(value)
        self.dial.setMinimum(value)    

    def setMaximum(self, value):    
        self.slider.setMaximum(value)
        self.scrollBar.setMaximum(value)
        self.dial.setMaximum(value)    

    def invertAppearance(self, invert):
        self.slider.setInvertedAppearance(invert)
        self.scrollBar.setInvertedAppearance(invert)
        self.dial.setInvertedAppearance(invert)    

    def invertKeyBindings(self, invert):
        self.slider.setInvertedControls(invert)
        self.scrollBar.setInvertedControls(invert)
        self.dial.setInvertedControls(invert)


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.horizontalSliders = SlidersGroup(QtCore.Qt.Horizontal,
                "Horizontal")
        self.verticalSliders = SlidersGroup(QtCore.Qt.Vertical, "Vertical")

        self.stackedWidget = QtGui.QStackedWidget()
        self.stackedWidget.addWidget(self.horizontalSliders)
        self.stackedWidget.addWidget(self.verticalSliders)

        self.createControls("Controls")

        self.horizontalSliders.valueChanged.connect(self.verticalSliders.setValue)
        self.verticalSliders.valueChanged.connect(self.valueSpinBox.setValue)
        self.valueSpinBox.valueChanged.connect(self.horizontalSliders.setValue)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.controlsGroup)
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)

        self.minimumSpinBox.setValue(0)
        self.maximumSpinBox.setValue(20)
        self.valueSpinBox.setValue(5)

        self.setWindowTitle("Sliders")

    def createControls(self, title):
        self.controlsGroup = QtGui.QGroupBox(title)

        minimumLabel = QtGui.QLabel("Minimum value:")
        maximumLabel = QtGui.QLabel("Maximum value:")
        valueLabel = QtGui.QLabel("Current value:")

        invertedAppearance = QtGui.QCheckBox("Inverted appearance")
        invertedKeyBindings = QtGui.QCheckBox("Inverted key bindings")

        self.minimumSpinBox = QtGui.QSpinBox()
        self.minimumSpinBox.setRange(-100, 100)
        self.minimumSpinBox.setSingleStep(1)

        self.maximumSpinBox = QtGui.QSpinBox()
        self.maximumSpinBox.setRange(-100, 100)
        self.maximumSpinBox.setSingleStep(1)

        self.valueSpinBox = QtGui.QSpinBox()
        self.valueSpinBox.setRange(-100, 100)
        self.valueSpinBox.setSingleStep(1)

        orientationCombo = QtGui.QComboBox()
        orientationCombo.addItem("Horizontal slider-like widgets")
        orientationCombo.addItem("Vertical slider-like widgets")

        orientationCombo.activated.connect(self.stackedWidget.setCurrentIndex)
        self.minimumSpinBox.valueChanged.connect(self.horizontalSliders.setMinimum)
        self.minimumSpinBox.valueChanged.connect(self.verticalSliders.setMinimum)
        self.maximumSpinBox.valueChanged.connect(self.horizontalSliders.setMaximum)
        self.maximumSpinBox.valueChanged.connect(self.verticalSliders.setMaximum)
        invertedAppearance.toggled.connect(self.horizontalSliders.invertAppearance)
        invertedAppearance.toggled.connect(self.verticalSliders.invertAppearance)
        invertedKeyBindings.toggled.connect(self.horizontalSliders.invertKeyBindings)
        invertedKeyBindings.toggled.connect(self.verticalSliders.invertKeyBindings)

        controlsLayout = QtGui.QGridLayout()
        controlsLayout.addWidget(minimumLabel, 0, 0)
        controlsLayout.addWidget(maximumLabel, 1, 0)
        controlsLayout.addWidget(valueLabel, 2, 0)
        controlsLayout.addWidget(self.minimumSpinBox, 0, 1)
        controlsLayout.addWidget(self.maximumSpinBox, 1, 1)
        controlsLayout.addWidget(self.valueSpinBox, 2, 1)
        controlsLayout.addWidget(invertedAppearance, 0, 2)
        controlsLayout.addWidget(invertedKeyBindings, 1, 2)
        controlsLayout.addWidget(orientationCombo, 3, 0, 1, 3)
        self.controlsGroup.setLayout(controlsLayout)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
