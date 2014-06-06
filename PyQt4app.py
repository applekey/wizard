from PyQt4 import QtGui
from PyQt4.phonon import Phonon
from wiz import Ui_WizardPage

# create the wizard classes

class MoviesPage(QtGui.QWizardPage):
    def __init__( self, parent ):
        super(MoviesPage, self).__init__(parent)
        self.setTitle('Movies')
        self.setSubTitle('Setup movie specific data')
        

class FramesPage(QtGui.QWizardPage):
    def __init__( self, parent ):
        super(FramesPage, self).__init__(parent)
        self.setTitle('Frames')
        self.setSubTitle('Setup frame specific data')

class RenderSettingsPage(QtGui.QWizardPage):
    def __init__( self, parent ):
        super(RenderSettingsPage, self).__init__(parent)
        self.setTitle('Render Settings')
        self.setSubTitle('Setup common render settings for all types')

#-------------------------------------------------------
# create the dialog class

class OptionsDialog(QtGui.QDialog):
    def __init__( self, parent ):
        super(OptionsDialog, self).__init__(parent)
        self.setWindowTitle('Options')

#-------------------------------------------------------
# create the main window class

class ApplicationWindow(QtGui.QMainWindow):
    def __init__( self, parent = None ):
        super(ApplicationWindow, self).__init__(parent)
        self.setWindowTitle('Main Window')

    def exportMovies( self ):
        """ Launches the export movies wizard. """
        wizard = QtGui.QWizard(self)
        wizard.addPage(Ui_WizardPage(wizard))
        wizard.addPage(MoviesPage(wizard))
        wizard.addPage(RenderSettingsPage(wizard))
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

