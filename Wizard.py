from PyQt4 import QtCore,QtGui
from PyQt4.phonon import Phonon
# import ui pages
# for now just import the main page with all the buttons
from allFunctionality import Ui_WizardPage

# create the main window class

class ApplicationWindow(QtGui.QMainWindow):
    

    def __init__( self, parent = None ):
        super(ApplicationWindow, self).__init__(parent)
        self.setWindowTitle('Main Window')
        self.wizard = None
        self.a = None
        self.b = None

    #def nextCalled(self,id):
    #    self.a.calluser()

    def exportMovies( self ):
        """ Launches the export movies wizard. """
        screen = QtGui.QDesktopWidget().screenGeometry()

        self.wizard = QtGui.QWizard(self)
        width = screen.width()
        height = screen.height()
        self.wizard.setWizardStyle(QtGui.QWizard.ModernStyle)
        #self.wizard.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.wizard.resize(width/2.0 ,height-200)
        xPos = self.wizard.x()
        yPos = self.wizard.y()
        self.wizard.move(0,0)

        self.a = Ui_WizardPage(self.wizard)
        self.wizard.addPage(self.a)
        #self.wizard.currentIdChanged.connect(self.nextCalled)
        self.wizard.exec_()
        #wizard.setWindowFlags(QtCore.Qt.FramelessWindowHint )

if ( __name__ == '__main__' ):
    # create the application if necessary
    app = None
    if ( not QtGui.QApplication.instance() ):
        app = QtGui.QApplication([])
    
    window = ApplicationWindow()
    #window.show()
    window.exportMovies()
    
    # execute the application if we've created it
    if ( app ):
        app.exec_()

