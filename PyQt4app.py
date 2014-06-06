from PyQt4 import QtCore,QtGui
from PyQt4.phonon import Phonon
from wiz import Ui_WizardPage

# create the main window class

class ApplicationWindow(QtGui.QMainWindow):
    wizard = None
    a = None
    b = None

    def __init__( self, parent = None ):
        super(ApplicationWindow, self).__init__(parent)
        self.setWindowTitle('Main Window')
    def nextCalled(self,id):
        self.a.calluser()
    def exportMovies( self ):
        """ Launches the export movies wizard. """
       
        self.wizard = QtGui.QWizard(self)
        self.a = Ui_WizardPage(self.wizard)
        self.b = Ui_WizardPage(self.wizard)
        self.wizard.addPage(self.a)
        self.wizard.addPage(self.b)
        self.wizard.currentIdChanged.connect(self.nextCalled)
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

