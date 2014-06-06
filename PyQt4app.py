from PyQt4 import QtGui
from PyQt4.phonon import Phonon
from wiz import Ui_WizardPage

# create the main window class

class ApplicationWindow(QtGui.QMainWindow):
    def __init__( self, parent = None ):
        super(ApplicationWindow, self).__init__(parent)
        self.setWindowTitle('Main Window')

    def exportMovies( self ):
        """ Launches the export movies wizard. """
        wizard = QtGui.QWizard(self)
        wizard.addPage(Ui_WizardPage(wizard))
        wizard.exec_()

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

