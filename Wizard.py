from PyQt4 import QtCore,QtGui
from PyQt4.phonon import Phonon
# import ui pages
# for now just import the main page with all the buttons
#from allFunctionality import Ui_WizardPage

# import all pages
from pageOne import pageOne
from allFunctionality import *

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

# create the main window class

class Ui_MainWindow(object):
    def onResize(self,event):
        width= self.MainWindow.size().width()
        height= self.MainWindow.size().height()
        newSize = QtCore.QRect(0,0,width,height)
        self.widget.setGeometry(newSize)
        
        #self.player.setGeometry(newSize)
    
    def setupUi(self, MainWindow):
       
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName(_fromUtf8("MainWindow"))
        
        self.height = 800
        self.width = 800


        self.MainWindow.resize(self.width, self.height)
        self.size = QtCore.QRect(0, 0, self.width, self.height)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.wizard = QtGui.QWizard(MainWindow)
        self.wizard.addPage(Ui_WizardPage(self.wizard))
        self.wizard.resize(200/2.0 ,500-200)
        self.wizard.show()
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow(flags=QtCore.Qt.FramelessWindowHint)
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())












#class ApplicationWindow(QtGui.QMainWindow):
    

#    def __init__( self, parent = None ):
#        super(ApplicationWindow, self).__init__(flags=QtCore.Qt.FramelessWindowHint)
#        self.setWindowTitle('Main Window')
#        self.wizard = None
#        #self.initilize(parent)
#        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#        self.label = QtGui.QLabel(self)
#        self.label.setGeometry(QtCore.QRect(30, 50, 121, 31))
        

#    #def nextCalled(self,id):
#    #    self.a.calluser()

#    def initilize( self,parent ):
#        # set the screen size
#        screen = QtGui.QDesktopWidget().screenGeometry()
#        self.wizard = QtGui.QWizard(parent)
#        width = screen.width()
#        height = screen.height()
#        self.wizard.setWizardStyle(QtGui.QWizard.ModernStyle)
#        #self.wizard.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#        self.wizard.resize(width/2.0 ,height-200)
#        xPos = self.wizard.x()
#        yPos = self.wizard.y()
#        self.wizard.move(0,0)
        
#        self.setUpPages()

       
#        #self.wizard.currentIdChanged.connect(self.nextCalled)
#        self.wizard.exec_()
#        #wizard.setWindowFlags(QtCore.Qt.FramelessWindowHint )
#    def setUpPages(self):
#        self.wizard.addPage(Ui_WizardPage(self.wizard))

#if ( __name__ == '__main__' ):
#    import sys
#    app = QtGui.QApplication(sys.argv)
  
#    ui = ApplicationWindow()
#    sys.exit(app.exec_())

