from PyQt4 import QtCore,QtGui
from PyQt4.phonon import Phonon
# import ui pages
# for now just import the main page with all the buttons
#from allFunctionality import Ui_WizardPage

# import all pages
from pageOne import pageOne
from allFunctionality import *

# create the main window class

class ApplicationWindow(QtGui.QMainWindow):
    

    def __init__( self, parent = None ):
        super(ApplicationWindow, self).__init__(parent)
        self.setWindowTitle('Main Window')
        self.wizard = None
        self.initilize(parent)
        

    #def nextCalled(self,id):
    #    self.a.calluser()

    def initilize( self,parent ):
        # set the screen size
        screen = QtGui.QDesktopWidget().screenGeometry()
        self.wizard = QtGui.QWizard(parent)
        width = screen.width()
        height = screen.height()
        self.wizard.setWizardStyle(QtGui.QWizard.ModernStyle)
        #self.wizard.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.wizard.resize(width/2.0 ,height-200)
        xPos = self.wizard.x()
        yPos = self.wizard.y()
        self.wizard.move(0,0)
        
        self.setUpPages()

       
        #self.wizard.currentIdChanged.connect(self.nextCalled)
        self.wizard.exec_()
        #wizard.setWindowFlags(QtCore.Qt.FramelessWindowHint )
    def setUpPages(self):
        self.wizard.addPage(Ui_WizardPage(self.wizard))

if ( __name__ == '__main__' ):
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow(flags=QtCore.Qt.FramelessWindowHint)
    ui = ApplicationWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

