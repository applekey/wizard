import sys
from PyQt4.QtCore import QObject, pyqtSlot
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebView
import tkFileDialog

import os
sys.path.append( 'meshController' )
from MeshWrapper import *

 
html = """
<html>
<body>
   <button id="myInputType1" type="button">Import Model</button>
   <button id="remeshButton" type="button">remesh</button>
<script>
document.getElementById("myInputType1").onclick = function(){
   htmlHelper.importClick();
};
document.getElementById("remeshButton").onclick = function(){
   htmlHelper.remesh();
};

</script>


</body>
</html>
"""
 
class HTMLHelper(QObject):
    def __init__(self, parent=None):
        super(HTMLHelper, self).__init__(parent)
    
    @pyqtSlot()
    def importClick(self):   
        fileName= str(tkFileDialog.askopenfilename())
        MeshWrapper.importFigure(fileName);
    
    @pyqtSlot()
    def remesh(self):   
        MeshWrapper.remesh()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QWebView()
    frame = view.page().mainFrame()
    helper = HTMLHelper()
    view.setHtml(html)
    frame.addToJavaScriptWindowObject('htmlHelper', helper)
   
    view.show()
    app.exec_()