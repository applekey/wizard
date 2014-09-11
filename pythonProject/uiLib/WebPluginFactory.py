import sys
from PyQt4.QtCore import QSize, Qt
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

from awsomePlayer import *



class WebPluginFactory(QWebPluginFactory):

    def __init__(self, parent = None):
        self.parent = parent
        QWebPluginFactory.__init__(self, parent)
        
    def create(self, mimeType, url, names, values):
        if mimeType == "x-pyqt/widget":
            player = awsomePlayer(self.parent)
            for x in range(0,len(names)):
                 if names[x] == 'src':
                    player.setSource(values[x])
                    player.lower()
            return player
    
    def plugins(self):
        plugin = QWebPluginFactory.Plugin()
        plugin.name = "PyQt Widget"
        plugin.description = "An example Web plugin written with PyQt."
        mimeType = QWebPluginFactory.MimeType()
        mimeType.name = "x-pyqt/widget"
        mimeType.description = "PyQt widget"
        mimeType.fileExtensions = []
        plugin.mimeTypes = [mimeType]
        print "plugins"
        return [plugin]